Title: 为什么你不应该使用 Django ModelForm 的 Meta.exclude 属性
Author: Leonardo Zhou
Category: Django

Django. **ModelForm.Meta.exclude**

Daniel Greenfeld 在 《Two Scoops of Django》这本书里， 就已经指出过 **ModelForm.Meta.exclude** 这方面的问题。 不过当时 Daniel 是从 Web 安全 的角度考虑的，如果一个 Model 在后续的改动中加上了一个普通用户不应该有权限编辑的字段， 那些使用了 **exclude** 的 Form 都会默认包含这个字段。提权漏洞。

这也印证了《 The Zen of Python 》里的那句话: **Explicit is better than implicit**。



