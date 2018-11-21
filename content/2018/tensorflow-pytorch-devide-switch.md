Title: Tensorflow 和 PyTorch 如何快速切换使用的 CPU/GPU 设备
Author: Leonardo Zhou
Category: 机器学习
Date: 2018-10-07
Slug: post/tensorflow-pytorch-devide-switch
save_as: post/tensorflow-pytorch-devide-switch/index.html


在做机器学习时， 常遇到这样的场景: 模型有时要跑在 CPU 上，有时要跑在 GPU 上， 有时又要跑在 某块指定的 GPU 上。

对于开源项目， 我们更是无法确定用户要使用怎样的设备， 要是换个设备， 就要大改代码， 就很糟糕了。

本文就简要介绍下 Tensorflow 和 PyTorch 这两个最常用的深度学习框架下， 怎样来最便捷地切换使用的设备。

## Tensorflow
在 Tensorflow 里的实现很简单， 我们把相应的代码放到一个 `tf.device` 块里就行了。

```python
with tf.device('/cpu:0'):
    a = tf.constant([1.0, 2.0, 3.0,], shape=[2, 3])
    b = tf.constant([1.0, 2.0, 3.0,], shape=[3, 2])
    c.append(tf.matmul(a, b))
```

也可以指定一个 session 所能使用的设备:

```python
config = tf.ConfigProto()
config.gpu_options.visible_device_list= '1' # GPU 的序号
config.device_count={'GPU': 1}) # 1： 只用 GPU, 0: 只用CPU
session = tf.Session(config=config, ...)
```


如果想把设备和代码完全分离， 我们还可以通过设置`CUDA_VISIBLE_DEVICES`环境变量来实现:

```bash
CUDA_VISIBLE_DEVICES="0,2,3" python model.py # 使用 GPU 0, 2,3
CUDA_VISIBLE_DEVICES="" python model.py # 使用 CPU
```

以上 3 种实现方式的作用范围， 由小而大。 with block 只会影响其代码块， 而 环境变量会影响整个程序。

## PyTorch
在 PyTorch 的早期版本里， 官方没有提供一个切换设备的方法， 各种第三方实现也比较 ugly。
PyTorch 创建的 tensor 默认是 跑在CPU 上的, 我们如果要创建一个 在 GPU 上运行的 tensor 需要调用 `.cuda()` 方法。  e.g.  `torch.rand(3,3).cuda()`。

因此在早期 PyTorch 代码里， 常用下面的模式， 去做兼容：

```python
x = x.new_ones(5, 3, dtype=torch.float)
y = torch.rand(5, 3)
if use_cuda:
    x = x.cuda()
    y = y.cuda()
```


直到 2018年4月底， PyTorch 0.4.0 发布后， PyTorch 才有了一种更优雅的写法:  使用`to()` 方法。
`to()` 可接受一个 `device` 参数，而不像 `.cuda()` 是写死了的。

```python
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
...
x = x.to(device)
model = MyModule(...).to(device)
```

一言以蔽之， 将以前 Pytorch 代码里 `.cuda()` 替换成 `.to(device)` 就行了。

这种写法相比于 Tensorflow 仍略欠优雅, 但根据 github issue 里的反馈， 官方也不打算在这方面再做优化了。 PyTorch 官方文档里也已经基本改成 `.to(device)` 这种写法。 大家可以撸起袖子改代码啦！