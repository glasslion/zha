Agglomerative Clustering

2017-05-05
Agglomerative Clustering
注:
Agglomerative clustering 代表了一类算法， 它们在开始时把每个点都当做一个独立的 cluster， 然后不断合并两个最接近的的的的 cluster 直到满足了某种停止条件。 scikit-learn 里实现的停止条件是 聚类的个数。
有几种可选的 linkage 参数，用来衡量到底怎样的两个 cluster 才算是最接近的:
- ward: 这是默认的选项。它会挑选两个合并后，方差增加最小的聚类。 这经常导致的得到的聚类都是差不多大小的。
- average: 合并后所有点平均距离是最小的两个聚类
- complete(maximum): 合并后，所有点的最大距离最小的两个聚类

如果聚类成员的数量分布不均匀的话（比如有一个聚类的成员特别多时），average 或 complete 可能更合适。

Agglomerative clustering 不能用来预测新的数据。 因此 AgglomerativeClustering 类也没有 predict 方法， 使用 `fit_predict` 方法代替之。

SciPy 提供了另一种实现

The SciPy clustering algorithms have a slightly different interface to the scikit-learn clustering algorithms
We can then feed this linkage array into the scipy dendrogram function to plot the dendrogram

DBSCAN

2017-05-05
DBSCAN
注:

它不需要用户预先知道聚类对数量。

它能捕捉形状比较复杂的聚类， 它还能识别出那些不属于任何聚类的点。

DBSCAN 比 agglomerative clustering 和 k-means 要慢一些， 但仍然能用于大型数据集。

Points that are within a dense region are called core samples (or core points)
Core samples that are closer to each other than the distance eps are put into the same cluster by DBSCAN.
If there are at least min_samples many data points within a distance of eps to a given data point, that data point is classified as a core sample.
However, a boundary point might be neighbor to core samples of more than one cluster.
The parameter eps is somewhat more important, as it determines what it means for points to be “close

Comparing and Evaluating Clustering Algorithms

2017-05-10
Comparing and Evaluating Clustering Algorithm
注: the most important ones being the adjusted rand index (ARI) and normalized mutual information (NMI),
A common mistake when evaluating clustering in this way is to use accuracy_score instead of adjusted_rand_score,
When applying clustering algorithms, there is usually no ground truth to which to compare the results. If we knew the right clustering of the data, we could use this information to build a supervised model like a classifier. Therefore, using metrics like ARI and NMI usually only helps in developing algorithms, not in assessing success in an application.
ke the silhouette coefficient. However, these often don’t work well in practice. The silhouette score computes the compactness of a cluster, where higher is better, with a perfect score of 1. While compact clusters are good, compactness doesn’t allow for complex shapes.
The only way to know whether the clustering corresponds to anything we are interested in is to analyze the clusters manually.

Summary and Outlook

2017-05-10
Summary and Outlook
注: Each of the algorithms has somewhat different strengths.
k-means allows for a characterization of the clusters using the cluster means. It can also be viewed as a decomposition method, where each data point is represented by its cluster center.
DBSCAN allows for the detection of “noise points” that are not assigned any cluster, and it can help automatically determine the number of clusters
it allow for complex cluster shapes,
DBSCAN sometimes produces clusters of very differing size, which can be a strength or a weakness
Agglomerative clustering can provide a whole hierarchy of possible partitions of the data, which can be easily inspected via dendrograms.
Often it is hard to quantify the usefulness of an unsupervised algorithm, though this shouldn’t deter you from using them to gather insights from your data.

One-Hot-Encoding (Dummy Variables)

2017-05-17
One-Hot-Encoding (Dummy Variables)
注: By far the most common way to represent categorical variables is using the one-hot-encoding or one-out-of-N encoding, also known as dummy variables.
The idea behind dummy variables is to replace a categorical variable with one or more new features that can have the values 0 and 1.
. In statistics, it is common to encode a categorical feature with k different possible values into k–1 features (the last one is represented as all zeros)
There are two ways to convert your data to a one-hot encoding of categorical variables, using either pandas or scikit-learn.
A good way to check the contents of a column is using the value_counts function of a pandas Series to show us what the unique values are and how often they appear:
The get_dummies function automatically transforms all columns that have object type (like strings) or are categorical
Including the output variable, or some derived property of the output variable, into the feature  representation is a very common mistake in building supervised machine learning models.
Be careful: column indexing in pandas includes the end of the range

Numbers Can Encode Categoricals

2017-05-19
Numbers Can Encode Categoricals
注: The get_dummies function in pandas treats all numbers as continuous and will not create dummy variables for them. To get around this, you can either use scikit-learn’s OneHotEncoder
The OneHotEncoder does the same encoding as pandas.get_dummies, though it currently only works on categorical variables that are intege

Binning, Discretization, Linear Models, and Trees

2017-05-19
Binning, Discretization, Linear Models, and Trees
注: One way to make linear models more powerful on continuous data is to use binning (also known as discretization) of the feature to split it up into multiple features,
Binning features generally has no beneficial effect for tree-based models
If there are good reasons to use a linear model for a particular dataset—say, because it is very large and high-dimensional, but some features have nonlinear relations with the output—binning can be a great way to increase modeling power.

Interactions and Polynomials

2017-05-23
Interactions and Polynomials
注: Another way to enrich a feature representation, particularly for linear models, is adding interaction features and polynomial features of the original data.
This kind of feature engineering is often used in statistical modeling, but it’s also common in many practical machine learning applications.
For a given feature x, we might want to consider x ** 2, x ** 3, x ** 4, and so on. This is implemented in PolynomialFeatures in the preprocessing module:
When using a more complex model like a random forest, Adding interactions and polynomials actually decreases performance slightly

Univariate Nonlinear Transformations

2017-05-23
Univariate Nonlinear Transformations
注: There are other transformations that often prove useful for transforming certain features: in particular, applying mathematical functions like log, exp, or sin.
linear models and neural networks are very tied to the scale and distribution of each feature, and if there is a nonlinear relation between the feature and the target, that becomes hard to model—particularly in regression
The functions log and exp can help by adjusting the relative scales in the data
The sin and cos functions can come in handy when dealing with data that encodes periodic patterns.
Most models work best when each feature (and in regression also the target) is loosely Gaussian distributedUsing transformations like log and exp is a hacky but simple and efficient way to achieve this.
usually only a subset of the features should be transformed, or sometimes each feature needs to be transformed in a different way
Sometimes it is also a good idea to transform the target variable y in regression.
for less complex models like linear models and naive Bayes models.
Tree-based models, on the other hand, are often able to discover important interactions themselves, and don’t require transforming the data explicitly most of the time.
Other models, like SVMs, nearest neighbors, and neural networks, might sometimes benefit from using binning, interactions, or polynomials, but the implications there are usually much less clear than in the case of linear models.

Automatic Feature Selection
2017-05-31
Automatic Feature Selection
注: Univariate Statistics
univariate, meaning that they only consider each feature individually. Consequently, a feature will be discarded if it is only informative when combined with another feature.
the features that are related with the highest confidence are selected
In the case of classification, this is also known as analysis of variance (ANOVA)
Univariate tests are often very fast to compute, and don’t require building a model.
To use univariate feature selection in scikit-learn, you need to choose a test, usually either f_classif (the default) for classification or f_regression for regression
SelectKBest, which selects a fixed number k of features, and SelectPercentile, which selects a fixed percentage of features
All methods for discarding parameters use a threshold to discard all features with too high a p-value (which means they are unlikely to be related to the target).
We can find out which features have been selected using the get_support method, which returns a Boolean mask of the selected features
Univariate feature selection can still be very helpful, though, if there is such a large number of features that building a model on them is infeasible, or if you suspect that many features are completely uninformative.
Model-Based Feature Selection
Model-based feature selection uses a supervised machine learning model to judge the importance of each feature
The supervised model that is used for feature selection doesn’t need to be the same model that is used for the final supervised modeling.
Decision trees and decision tree–based models provide a feature_importances_ attribute, which directly encodes the importance of each feature.
Linear models have coefficients, which can also be used to capture feature importances by considering the absolute values.
linear models with L1 penalty learn sparse coefficients, which only use a small subset of features. This can be viewed as a form of feature selection
In contrast to univariate selection, model-based selection considers all features at once, and so can capture interactions
To use model-based feature selection, we need to use the SelectFromModel transformer
Iterative Feature Selection
In iterative feature selection, a series of models are built, with varying numbers of features.
There are two basic methods: starting with no features and adding features one by one until some stopping criterion is reached, or starting with all features and removing features one by one until some stopping criterion is reached.
these methods are much more computationally expensive
recursive feature elimination (RFE)
If you are unsure when selecting what to use as input to your machine learning algorithms, automatic feature selection can be quite helpful. It is also great for reducing the amount of features needed—for example, to speed up prediction or to allow for more interpretable models
In most real-world cases, applying feature selection is unlikely to provide large gains in performance.

Utilizing Expert Knowledge

2017-05-31
Utilizing Expert Knowledge
注: Often, domain experts can help in identifying useful features that are much more informative than the initial representation of the data
Adding a feature does not force a machine learning algorithm to use it,doesn’t hurt.

Cross-Validation
2017-06-06
Cross-Validation
注: The most commonly used version of cross-validation is k-fold cross-validationCross-validation is implemented in scikit-learn using the cross_val_score function from the model_selection module. By default, cross_val_score performs three-fold cross-validation, returning three accuracy values. We can change the number of folds used by changing the cv parameteA common way to summarize the cross-validation accuracy is to compute the meanBenefits of Cross-Validation避免 train_test_split 随机分隔数据集导致的不确定性。provides some information about how sensitive our model is to the selection of the training datasetuse our data more effectivelyThe main disadvantage of cross-validation is increased computational coststratified k-fold cross-validationwe split the data such that the proportions between classes are the same in each fold as they are in the whole datasetIt is usually a good idea to use stratified k-fold cross-validation instead of k-fold cross-validation to evaluate a classifier,For regression, scikit-learn uses the standard k-fold cross-validation by defaultscikit-learn allows for much finer control over what happens during the splitting of the data by providing a cross-validation splitter as the cv parameterFor most use cases, the defaults of k-fold cross-validation for regression and stratified k-fold for classification work wellshuffle the data instead of stratifying the folds,by setting the shuffle parameter of KFold to True.If we shuffle the data, we also need to fix the random_state to get a reproducible shuffling. Otherwise, each run of cross_val_score would yield a different resultLeave-one-out cross-validationYou can think of leave-one-out cross-validation as k-fold cross-validation where each fold is a single sampleThis can be very time consuming, particularly for large datasets, but sometimes provides better estimates on small datasetsShuffle-split cross-validationIn shuffle-split cross-validation, each split samples train_size many points for the training set and test_size many (disjoint) point for the test set. This splitting is repeated n_iter timesallows for control over the number of iterations independently of the training and test sizesIt also allows for using only part of the data in each iterationSubsampling the data in this way can be useful for experimenting with large datasets.Cross-validation with groupsuse GroupKFold, which takes an groups array that indicates groups in the data that should not be split when creating the training and test sets, and should not be confused with the class label.common in medical applications,speech recognition

Grid Search
2017-06-12
Grid Search
注: Fitting the GridSearchCV object not only searches for the best parameters, but also automatically fits a new model on the whole training dataset with the parameters that yielded the best cross-validation performance.
The parameters that were found are scored in the best_params_ attribute
You can access the model with the best parameters trained on the whole training set using the best_estimator_ attribute
It is often helpful to visualize the results of cross-validation, to understand how the model generalization depends on the parameters we are searchin
The results of a grid search can be found in the cv_results_ attribute
best visualized as a heat map (
if no change in accuracy is visible over the different parameter settings, it could also be that a parameter is just not important at all. It is usually good to try very extreme values first, to see if there are any changes in the accuracy as a result of changing a parameter.
GridSearchCV uses stratified k-fold cross-validation by default for classification, and k-fold cross-validation for regression.
However, you can also pass any cross-validation splitter,In particular, to get only a single split into a training and a validation set, you can use ShuffleSplit or StratifiedShuffleSplit with n_iter=1. This might be helpful for very large datasets, or very slow models.
Nested cross-validation
Implementing nested cross-validation in scikit-learn is straightforward. We call cross_val_score with an instance of GridSearchCV as the model
scores = cross_val_score(GridSearchCV(SVC(), param_grid, cv=5),
                         iris.data, iris.target, cv=5)
Parallelizing cross-validation and grid search
While running a grid search over many parameters and on large datasets can be computationally challenging, it is also embarrassingly parallel.
You can make use of multiple cores in GridSearchCV and cross_val_score by setting the n_jobs parameter
scikit-learn does not allow nesting of parallel operations.
you should monitor your memory usage when building large models in parallel
IPython parallel framework
spark-sklearn package

Keep the End Goal in Mind

2017-06-12
Evaluation Metrics and Scoring