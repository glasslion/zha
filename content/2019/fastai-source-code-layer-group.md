Title: fast.ai 源码浅析 - LayerGroups
Author: Leonardo Zhou
Category: 机器学习
Date: 2019-05-18
Slug: post/fastai-source-code-layer-group
save_as: post/fastai-source-code-layer-group/index.html
Tags: fastai pytorch

fastai 在使用预训练模型进行迁移学习(Transfer Learning)时， 有一项:很酷的特性: 你可以给模型的 不同 layer 设置不同的 learning rate (Discriminative Learning Rates).

然而一些模型 如 ResNet 有很多层， 要给每一层都设置一个不同的 lr, 既麻烦也没有必要。其解决方法在 **Practical Deep Learning for Coders, v3** 课上， Jeremy 已经简略地提到过了。 fastai 会把 model 划分成若干个 layer groups, 给每个 group 设置一个不同的 learning rate。

其具体实现是怎样的?  不同结构的模型又是怎么划分 layer groupn 的? 对于新模型我们又应该怎样去设置 layer groups？ 要解答这些问题， 就需要我们自己来阅读源码了。

在通过 `cnn_learner()` 等方式创建 learner 时， 会调用 `learn.split()` 来对 model layers 分组:

**fastai/vision/learner.py**
```python
def cnn_learner(data:DataBunch, base_arch:Callable...):
    ...
    model = create_cnn_model(...)
    learn = Learner(data, model, **kwargs)
    learn.split(split_on or meta['split'])
```

`learn.split()` 会把分组结果存放在 learner 的 `layer_groups` 属性里:

**fastai/basic_train.py**
```python
def split(self, split_on:SplitFuncOrIdxList)->None:
    "Split the model at `split_on`."
    if isinstance(split_on,Callable):
        split_on = split_on(self.model)
    self.layer_groups = split_model(self.model, split_on)
    return self
```

一个 model 的 layer 分组方案， 其实是由 `split_on` 参数决定的。这个 `split_on` 参数可以在调用 `cnn_learner` 创建 learner 时手动传入， 缺省使用 模型 `meta` 配置里的 的 `split`参数。


fastai.vision 指定了以下几种 split_on 函数:
**fastai/vision/learner.py**
```python
# By default split models between first and second layer
def _default_split(m: nn.Module):
    return (m[1],)

# Split a resnet style model
def _resnet_split(m: nn.Module):
    return (m[0][6], m[1])

# Split squeezenet model on maxpool layers
def _squeezenet_split(m: nn.Module):
    return (m[0][0][5], m[0][0][8], m[1])

def _densenet_split(m: nn.Module):
    return (m[0][0][7], m[1])

def _vgg_split(m: nn.Module):
    return (m[0][0][22], m[1])

def _alexnet_split(m: nn.Module):
    return (m[0][0][6], m[1])

_default_meta = {'cut': None, 'split': _default_split}
_resnet_meta = {'cut': -2, 'split': _resnet_split}
_squeezenet_meta = {'cut': -1, 'split': _squeezenet_split}
_densenet_meta = {'cut': -1, 'split': _densenet_split}
_vgg_meta = {'cut': -1, 'split': _vgg_split}
_alexnet_meta = {'cut': -1, 'split': _alexnet_split}
```

然而光看这段代码， 我们任然会一头雾水，`m[0][0][6]` ,  `m[1]`  这些 magic number 到底是怎样来的。

我们以 alenxnet 为例, 在深入看下这块的实现:

`fastai.vision.models` 下大部分模型是直接使用的 `torchvision` 的实现, 其中 AlexNet 的实现代码如下:

**torchvision/models/alexnet.py**
```python
class AlexNet(nn.Module):
    def __init__(self, num_classes=1000):
        super(AlexNet, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=11, stride=4, padding=2),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
            nn.Conv2d(64, 192, kernel_size=5, padding=2),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
            nn.Conv2d(192, 384, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(384, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(256, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
        )
        self.avgpool = nn.AdaptiveAvgPool2d((6, 6))
        self.classifier = nn.Sequential(
            nn.Dropout(),
            nn.Linear(256 * 6 * 6, 4096),
            nn.ReLU(inplace=True),
            nn.Dropout(),
            nn.Linear(4096, 4096),
            nn.ReLU(inplace=True),
            nn.Linear(4096, num_classes),
        )

    def forward(self, x):
        x = self.features(x)
        x = self.avgpool(x)
        x = x.view(x.size(0), 256 * 6 * 6)
        x = self.classifier(x)
        return x
```

可以看出 `torchvision` 的视线里把 AlexNet Model 所有 layers 划分为了 3个  `nn.Sequential` 串:
- features
- avgpool
- classifier

注: AlexNet 作为一种顺序模型， 只用一串 `nn.Sequential` 块 就可以实现了。 而`torchvision` 为了代码组织更加清晰和易用， 才按照 layer 的功能划分了 3串

打印出来的模型结构如下:
```
AlexNet(
  (features): Sequential(
    (0): Conv2d(3, 64, kernel_size=(11, 11), stride=(4, 4), padding=(2, 2))
    (1): ReLU(inplace)
    (2): MaxPool2d(kernel_size=3, stride=2, padding=0, dilation=1, ceil_mode=False)
    ...
    (5): MaxPool2d(kernel_size=3, stride=2, padding=0, dilation=1, ceil_mode=False)
    (6): Conv2d(192, 384, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    ...
    (10): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (11): ReLU(inplace)
    (12): MaxPool2d(kernel_size=3, stride=2, padding=0, dilation=1, ceil_mode=False)
  )
  (avgpool): AdaptiveAvgPool2d(output_size=(6, 6))
  (classifier): Sequential(
    (0): Dropout(p=0.5)
    (1): Linear(in_features=9216, out_features=4096, bias=True)
    ...
    (6): Linear(in_features=4096, out_features=1000, bias=True)
  )
)
```
这里的`模型并不是我们最终使用的模型， 它的结构是针对 ImageNet 数据集设计的， 解决的是 1000个类别图片的分类问题， 因此我们还会对它进行改造:

`cnn_learner()` 通过调用 `create_cnn_model()` 来创建 实际使用的模型:

**fastai/vision/learner.py**
```python
def create_cnn_model(base_arch, nc, cut, 。。。):
    "Create custom convnet architecture"
    body = create_body(base_arch, pretrained, cut)
	...
    head = create_head(...)
    return nn.Sequential(body, head)
```
 可见 fastai 创建出来的模型是由 body 和 head 两块拼接而成:
 - body 是在预训练模型(e.g. AlexNet) 上 丢弃若干层网络得到的
 `create_body()` 具体会丢弃哪些层， 是由 model 的 `meta['cut']` 参数决定的。
在上文的 代码里， 我们可以看到 ` _alexnet_meta['cut']` 的值为 -1. 这意味着丢弃 AlexNet 的最后一串 layer， 即前文提到的 `classifier` Sequential.

 - head 的结构只和我们的数据有多少类别有关， 和body 用的是alexnet, 还是 vgg 或 resnet 没有关系。 其具体结构， 下文会讲。

最终的模型结构课简化如下:
```
(
    (body): (
	    (features)
	    (avgpool)
    )
    (head)
)
```

现在 再回过头看 alexnet 的 `split_on` 函数就比较好理解了:
```python
def _alexnet_split(m: nn.Module):
    return (m[0][0][6], m[1])
```

`m[0]` 为 `body`,  `m[0][0]` 即 `features`， `m[1]` 即 `head`

`(m[0][0][6], m[1])` 意味着  features 的 前6层 划为第一个 layer group, 第7层到 head 划分为第而个 layer group， head 作为第三个 layer group。

由于 head 层是我们自己添加的， 是预训练模型里不存在的, 它的 learning rate 显然应该和预训练模型不同， 这也是所有的 `split_on` 函数都包含 `m[1]` 这一项的原因。

至于 AlexNet 为什么选择在 `m[0][0][6]` 处切一下， vgg 在 `m[0][0][22]`切一下， resnet 在 `m[0][6]` 切一下， 经过分析这些模型的结构，可发现这些切割垫都是卷积层中间的位置。
