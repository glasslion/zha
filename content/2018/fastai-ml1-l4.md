#Title: 随机森林模型调优
Author: Leonardo Zhou
Category: 机器学习
Date: 2018-06-01
# Slug: post/fastai-ml1-lesson4
#save_as: post/fastai-ml1-lesson4/index.html

## 重要的超参数

1. set_rf_samples()
每个tree 使用的数据集的大小

1m

20k 假设树是平衡的， 则树的的高度是 log2(20k), 有 20k 个 leaf

越小的 sample size, 越不容易过拟合， 但准确率也更低

更快

注: 当 rf_samples size 和 样本总大小相差很大时， oob score 会很耗时。 这和 fastai 的 subsampling 的实现有关，scikit-learn 本身不支持 subsampling, Jeremry 用了一种比较hacky 的方式实现的。

2. `min_samples_leaf`
默认值为 1。 更稳定， generalize。避免过拟合。
常用的取值 1,3,5,10, 25, 100 ...


3. `max_features`
 在使用 `set_rf_samples()` 时， 每颗树的训练子集(行) 在训练开始前就被划分好了。不同于，是在每次分割树时才做出的。 `max_features` 对树的多样性很关键。决策树的划分是一种贪心策略，即局部最优策略。容易忽略有关联的feature。如下图所示，由于树的*同质化*严重， max_features=None 的随机森林(绿线) ， 增加树的数量，很快就对降低错误率不起作用了。
![Alt text](./1528279567256.png)

常用的取值有 None, 0.5, sqrt log2

如果你已经知道哪些feature,以及 feature 之间的关联关系， 你几乎总是能够构造出一个和你的随机森林表现相当的逻辑回归模型。 然而在现实中， 我们几乎不可能完全搞清楚这些关系。 这正是基于树的模型的优势所在。


feature engerning 之后， validation score 变得更差了？
可能原因1： 过拟合了。 看 oob, 如果因为 sample size 远小于 ， 导致 oob 计算太慢， 则可以再划分出第二个验证集(随机取样)。 如果这个分数也变差了， 那就能确定是过拟合了。但是随机森林通常很难会出现严重过拟合。
另一种可能是， validation set 不是random sample, 比如时间序列。

## One-Hot Encoding
One Hot Encoding 在使用逻辑回归或神经网络等模型时，是一项非常重要的数据预处理步骤。
| ID | Category |
|----|----------|
| 1  | cat      |
| 2  | dog      |
| 3  | bird     |
| 4  | horse    |
| 5  | cat      |


| ID | Category | Category Num |
|----|----------|--------------|
| 1  | cat      | 1            |
| 2  | dog      | 2            |
| 3  | bird     | 3            |
| 4  | horse    | 4            |
| 5  | cat      | 1            |


| ID | Category | is_cat | is_dog | is_bird | is_horse |
|----|----------|--------|--------|---------|----------|
| 1  | cat      | 1      | 0      | 0       | 0        |
| 2  | dog      | 0      | 1      | 0       | 0        |
| 3  | bird     | 0      | 0      | 1       | 0        |
| 4  | horse    | 0      | 0      | 0       | 1        |
| 5  | cat      | 1      | 0      | 0       | 0        |


但理论上随机森林.
对于,是否还有必要保留，之前问题。
这一点也应实际使用的模型而已。，通常对于随机森林来说，是建议保留的。

尽管理论上， 随机森林，尽管表面上看来，只是多了一次划分， 影像不大。但每次划分后的数据却减半
less rich(数据更少！), less effective.
OneHot Encoding 后是否还保留原始的feature？ 随机森林建议保留， 逻辑回归不保留
OneHot encoding 之后的 feature importance 也很重要

## 去除冗余特征
我们还可以通过尝试，
那么什么样的特征算是冗余、重复的呢？ 一种更准确的描述是那些相关性很高的的特征。

统计学里，有很多指标可以用来衡量两个变量的相关性， 其中最常用的是 coefficient of determination(决定系数), 记为 **R<sup>2</sup>**, R-squared。

![Alt text](1528804428226.png)
![Alt text](1528804447702.png)

$SS_\text{tot}=\sum_i (y_i-\bar{y})^2,$


对于随机森林而言， 它并不关心模型的线性关系， 而关心顺序。 .因此 Rank-Order Correlation 显然更加合适。


只有对于简单线性回归而言，决定系数(R<sup>2</sup>)为样本相关系数(R)的平方。

Spearman's Rank-Order Correlation


Hierarchical clustering
Correlation matrix
树状图 Dendrogram

![Alt text](1528805202458.png)


阅读材料:
[可汗学院 R-squared or coefficient of determination](https://www.khanacademy.org/math/ap-statistics/bivariate-data-ap/assessing-fit-least-squares-regression/v/r-squared-or-coefficient-of-determination)

