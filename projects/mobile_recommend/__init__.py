import mglearn
mglearn.plots.plot_ridge_n_samples()
from sklearn.model_selection import learning_curve, KFold
from sklearn.linear_model import ElasticNet
en_model = ElasticNet()
from sklearn.datasets import make_blobs
