<!--Title: Python Docstring 格式小考
Author: Leonardo Zhou
Category: Python
Date: 2015-08-15 22:39:00
Slug: post/python-docstring-formats
save_as: post/python-docstring-formats/index.html
Tags: sphinx-->

```python
def send_message(sender, recipient, message_body, priority=1):

    Send a message to a recipient

    :param str sender: The person sending the message
    :param str recipient: The recipient of the message
    :param str message_body: The body of the message
    :param priority: The priority of the message, can be a number 1-5
    :type priority: integer or None
    :return: the message id
    :rtype: int
    :raises ValueError: if the message_body exceeds 160 characters
    :raises TypeError: if the message_body is not a basestring
```

## NumPy/SciPy Style
```python
def send_message(sender, recipient, message_body, priority=1):

    Send a message to a recipient

    Parameters
    ----------
    sender : str
        The person sending the message
    recipient : str
        The recipient of the message
    message_body : str
        The body of the message
    priority : integer, 1
        The priority of the message, can be a number 1-5

    Returns
    -------
    int
        the message id

    Raises
    ------
    ValueError
        If the message_body exceeds 160 characters
    TypeError
        If the message_body is not a basestrings
```

## Google Style
```python
def send_message(sender, recipient, message_body, priority=1):

    Send a message to a recipient

    Args:
    sender (str) : The person sending the message
    recipient (str): The recipient of the message
    message_body (str) : The body of the message
    priority (integer, 1) : The priority of the message, can be a number 1-5

    Returns:
        int: the message id


    Raises:
    ValueError: If the message_body exceeds 160 characters
    TypeError: If the message_body is not a basestrings
```
## 参考资料


- [PEP 0257 -- Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
- [PEP 0287 -- reStructuredText Docstring Format](https://www.python.org/dev/peps/pep-0287/)
- [Point to alternative formats for docstrings #4](https://github.com/amontalenti/elements-of-python-style/pull/4)
- [A Guide to NumPy/SciPy Documentation](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt)
- [Google Python Style Guide #Comments](http://google.github.io/styleguide/pyguide.html#Comments)
- [sphinx.ext.napoleon – Support for NumPy and Google style docstrings](http://www.sphinx-doc.org/en/stable/ext/napoleon.html)
