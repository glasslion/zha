Title: Django 无法在QuerySet中select_related()一个GenericForeignKey的解决方法
Date: 2013-08-16 16:20:00
Author: Leonardo Zhou
Category: Python
Slug: post/58406919860/django
Save_as: post/58406919860/django/index.html
Tags: django
Summary: 手动对 related field 做一次独立的SQL查询，在内存中缓存 related field，从而把 N+M 条 SQL 简化成 2 条 SQL

在Django开发中， 用 `select_related()` 把 item 的 `ForeignKey` 在同一条SQL中通过 join table 一起取出是很常见的做法。但 `select_related` 是不支持 `GenericForeignKey` （主要用于 ContentType）的。


自Django 1.4开始， Django 提供了 `prefetch_related` 这个方法来解决这个问题。 除了 `GenericForeignKey`. ，`prefetch_related` 还可以作用在 `ManyToManyField` 和 'many-to-one' 的 ForeignKey 这些 `select_related()` 不支持的 field. `prefetch_related` 的原理是对related field 做一次独立的 query, 将 related field 缓存在内存中，今后去取 queryset 中各个 item 的 related field 时，就直接从缓存中找，而不是每次都做一次 db query. 对 `prefetch_related` 更详细的解释可以参考[官方文档][]。

对 Django 版本低于1.4的项目， 可以参考这篇博客 [Django patterns, part 4: forwards generic relations][] 给出的解决方法. 其思路和 prefetch\_related 几乎是一样的，都是缓存 related field 。把 N+M 条SQL （N 是 queryset中item的数量，M是的 related\_field 的 Model 的 item
数量） 简化 成2 条 SQL。


下面是我基于Daniel Roseman 的博客，在Justin Israel的 [gist][]基础上改良的脚本，虽然只支持 content\_type 的 `GenericForeignKey` ，但经过简单的修改， 可以很容易支持其他类型的field.

    :::python
    '''
    Cache the generic relation field of all the objects 
    in the queryset, using larger bulk queries ahead of time.
     
    Improved from original by Daniel Roseman:
    http://blog.roseman.org.uk/2010/02/22/django-patterns-part-4-forwards-generic-relations/

    and

    justinfx's gist cache_generics.py :
    https://gist.github.com/justinfx/3095246#file-cache_generics-py

    Supports customized object_id_field and GenericForeignKey name.

    '''

    from operator import attrgetter
    from django.contrib.contenttypes.models import ContentType
     
    def cache_generic_content_types(queryset, object_id_field='object_id', content_type_fk='content_object'):
        """
        Django does not support select_related on generic foreign key. Thus some
        ORM actions may trigger N+M querys(N is item number of the queryset and
        M is the item number of the content type). This function will cache content
        and reduce N+M querys to 2 querys.

        object_id_field: see https://docs.djangoproject.com/en/1.3/ref/contrib/contenttypes/#django.contrib.contenttypes.generic.GenericRelation
        content_type_fk: the name of GenericForeignKey which linked to content type
        """
        get_object_id = attrgetter(object_id_field)
        generics = {}
        for item in queryset:
            if get_object_id(item) is not None:
                generics.setdefault(item.content_type_id, set()).add(get_object_id(item))
     
        content_types = ContentType.objects.in_bulk(generics.keys())
     
        relations = {}
        for ct, fk_list in generics.iteritems():
            ct_model = content_types[ct].model_class()
            relations[ct] = ct_model.objects.in_bulk(list(fk_list))
     
        for item in queryset:
            try:
                cached_val = relations[item.content_type_id][get_object_id(item)]
            except KeyError:
                cached_val = None
            setattr(item, '_%s_cache' % content_type_fk, cached_val)
        return queryset

view [gist: generic_relations.py][]


  [官方文档]: docs.djangoproject.com/en/dev/ref/models/querysets/#prefetch-related
  [Django patterns, part 4: forwards generic relations]: http://blog.roseman.org.uk/2010/02/22/django-patterns-part-4-forwards-generic-relations/
  [gist]: https://gist.github.com/justinfx/3095246#file-cache_generics-py
  [gist: generic_relations.py]: https://gist.github.com/glasslion/6247958#file-generic_relations-py
