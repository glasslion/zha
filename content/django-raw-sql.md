Title: 闲话 Django Raw SQL
Author: Leonardo Zhou
Category: Django
Date: 2014-09-17 21:33:00
Slug: post/django-raw-sql
save_as: post/django-raw-sql/index.html


在 Web 开发中，是否使用和怎样使用 ORM 一直是比较容易引起争议的话题。 在 Django 社区里， 相关的讨论也有很多。 一方面， Django 自带的 ORM 十分简明易学， 处理起简单的查询来得心应手， 相比与 Raw SQL，代码的可读性好很多。另一方面， 面对较为复杂的查询，受限于其表达能力，Django ORM 写起来就有点力不从心了。 即使最终能用 ORM 语句搞定， 代码的可读性可能还不及 Raw SQL， 也比较容易出现性能问题。

Raw SQL or not raw SQL， that is the question。

题外话：
尽管，本文的主旨是想探讨下 Django 里 raw SQL 的应用。但笔者仍然强烈建议在使用 raw SQL 之前， 应尽量尝试一些常规的 ORM 手段。`select_related()` 和 `prefetch_related()` 往往可以大幅减少 SQL 查询的数量。一些性能问题往往可通过 cache 缓解。 [django-debug-toolbar](https://github.com/django-debug-toolbar/django-debug-toolbar/) 和 [django-devserver](https://github.com/dcramer/django-devserver) 对找出存在性能问题的 ORM 查询很有帮助。 Django 官方文档中的 这篇 [Database access optimization](https://docs.djangoproject.com/en/dev/topics/db/optimization/) 也是份不错的参考资料。


## Manager.raw

Django 的官方文档 [Performing raw SQL queries](https://docs.djangoproject.com/en/dev/topics/db/sql/) 主要推荐使用 `Manager.raw(raw_query, params=None, translations=None)`  来执行 raw SQL。 而且 `Manager.raw` 这个API 并不是单纯执行 SQL 语句那么简单， 它还提供了不少很有用的功能。

`Manager.raw`  依然能抵御 SQL 注入攻击。对于接受参数的 SQL 语句，我们不应该手动去填充 SQL 字符串， 而是应该在 SQL 语句里加上 `%s`, `%(key)s`之类的占位符， 然后把实际的值传给 `params` 参数：
```python
lname = 'Doe'
# Wrong:
Person.objects.raw('SELECT * FROM myapp_person WHERE last_name = %s' % lname)

# Right：
Person.objects.raw('SELECT * FROM myapp_person WHERE last_name = %s', [lname])
```
通过 `Manager.raw` ， 我们还可以给 Model 加上原来数据库表结构里不存在的字段：
```python
people = Person.objects.raw('SELECT *, age(birth_date) AS age FROM myapp_person')
for p in people:
    print("%s is %s." % (p.first_name, p.age))
```

raw SQL 可以只包含 Model 的部分字段。 当访问那些 raw SQL 没有覆盖到的字段时，Django 会自动触发一条新的 SQL， 去查询对应字段的值：
```
for p in Person.objects.raw('SELECT id, first_name FROM myapp_person'):
    print(p.first_name, # This will be retrieved by the original query
        p.last_name) # This will be retrieved on demand
```

`Manager.raw` 虽然很强大， 然而它返回的是一个 `RawQuerySet` 。 不同与于正常的 `QuerySet`  ， 我们不能在 `RawQuerySet` 上执行 `filter` 和 `order_by` 等常见操作。 `RawQuerySet` 仍然然支持 Python 的 index 和 slice 操作(`query_set[0]`, `query_set[0:5]`)，但不像`QuerySet` 是在 数据库层面通过 `LIMIT` 语句完成， `RawQuerySet` 是将数据集全部取出后，在 Python 代码里做的 index 和 slice, 其实现比较低效。

这些缺陷导致了 raw SQL 很难在不同场合复用。 所以，总体上 `Manager.raw` 给我的感觉是： 食之无味，弃之可惜。

## Model ↔ 视图

实际上， Django Models 不仅可以映射成数据库里的 Table， 也可以映射成View(视图)。

以 MySQL 官方样例数据库 [Sakila](http://dev.mysql.com/doc/sakila/en/index.html) 里的 `sales_by_film_category`  视图为例：

```sql
# View sales_by_film_category
CREATE VIEW sales_by_film_category AS
SELECT c.name AS category,
    sum(p.amount) AS total_sales
   FROM payment p
     JOIN rental r ON p.rental_id = r.rental_id
     JOIN inventory i ON r.inventory_id = i.inventory_id
     JOIN film f ON i.film_id = f.film_id
     JOIN film_category fc ON f.film_id = fc.film_id
     JOIN category c ON fc.category_id = c.category_id
  GROUP BY c.name
  ORDER BY sum(p.amount) DESC;
```

注： Sakila 数据库里各表的结构和关系可以参考这篇[文档](http://dev.mysql.com/doc/sakila/en/sakila-structure.html)，本文限于篇幅，就不详细解释了。

这样一个数据库视图， 通过 Django `inspectdb`  command 解析后，就可以得到如下的 Django  Model :
```python
class SalesByFilmCategory(Model):
    category = models.IntegerField(primary_key=True)
    total_sales = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sales_by_film_category'
```

这个 Model 除了是只读（不可写）之外，相比于一般的 Model 并无二致。
由于 Manager 返回的是普通的 `QuerySet`,  我们可以链式地调用 `filter`， `order_by` 等操作。

e.g:
```python
SalesByFilmCategory.objects.filter(category__in=xxx).filter(total_sales__gt==xxxxx).order_by('total_sales')
```

相比于 View(此处是指MVC 里的View，而非 DB 的View) 和 Template， Model 往往更加容易和第三方应用进行集成。譬如， 通过 django admin 的 ModelAdmin，我们只需几行代码就可以给上面的 的视图加上一个漂亮的查询报表界面（尽管是只读的）。类似的，通过 [Django REST framework](http://www.django-rest-framework.org/) 的 `ListModelMixin`， `RetrieveModelMixin`, 给 视图加上一个只读的 REST API 也非常简单。 Django 社区会推崇 "Fat Models, Helper Modules, Thin Views, Stupid Templates." 的设计理念的道理正在于此。

我们还可以通过自定义 Model 的 Manager， Meta Class 来进一步定制 ORM，以达到在多个地方重用同一个 Model (View) 的目的。


## MATERIALIZED VIEWS
对 View 的查询， 从本质上来说和一般的表查询并没有什么不同， 因此也不会有性能上的提升。很多情况下，正是因为ORM 生成的查询过于复杂，缓慢， 我们才会转投 raw SQL。 尽管 raw SQL 给予了我们在最大程度上优化 SQL 查询自由， 但有时候优化效果还是不能尽如人意。 如果对于查询结果的实时性要求不高的话，将耗时查询的结果 cache 住， 会是更合理的解决方案。

Django 自带的 [Cache 框架](https://docs.djangoproject.com/en/dev/topics/cache/) 设计十分优秀, 扩展性也很好，这里不再赘述。 其实， 除了传统的 cache 技术外，在数据库层面也是有文章可做的。
 PostgreSQL 9.3 添加了对 materialised views 的支持。Materialised View 是一种特殊的视图。不同与一般的视图， Materialised View 会将第一次查询所得到结果会被缓存到磁盘。再次查询时， Materialised View 将直接返回缓存后的数据， 速度自然会很快。

到目前为止，PostgreSQL 的materialised views 还无法像 Oracle 那样做到自动更新 (`auto-refreshed`)。所以要通过 cron 或 celery 之类的工具 去定时刷新 (`REFRESH MATERIALIZED VIEW name` )。传统的 cache 解决方案( memcached, redis) 支持对每个 key 设定不同的 timeout，相比之下， materialised views 在这方面不够灵活， 我们无法对 行(Row) 级数据更新。但 materialised views 也有自己的一些优势： 

-  Materialised Views 被配置好后， 对最终用户而言， 他们就是普通的 Django Model， 不需要在代码里对 cache 是否存在/是否需要更新做额外的处理。
-  memcached/redis 比较适合用来缓存单个 Model 对象， 但对于包含多个对象的 QuerySet， 其处理能力就比较弱了， 无法实现 Django Model.filter 之类的操作。 当应用程序代码里有多处使用到相似的 QuerySet， 每个QuerySet有所不同，但彼此又存在一定的交集时， cache 就无法得到有效利用。而 Materialised Views 就可以把这些 QuerySet 的合集缓存起来，每个 View 就是一个普通的 Django Model。各个 QuerySet 就只是在 Model 上调用不同的 filtet 方法而已。 PostgreSQL 支持在 Materialised Views 上建立索引， 查询速度也不会成为瓶颈。


 
