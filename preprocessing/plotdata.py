import pylab as pl
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA

#pylab is part of matplotlib (in matplotlib.pylab) and tries to give you a MatLab like environment.

# import iris data with four features
iris = datasets.load_iris()
X = iris.data[:, :2]  # all row, 2 cloumn # [:,:] mean all row and cloumn(sample,featrue)
Y = iris.target

x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5

pl.figure(2, figsize=(8, 6)) #top level container for all plot elements
pl.clf() #clear the entire current fig

# Plot the training points
pl.scatter(X[:, 0], X[:, 1], c=Y, cmap=pl.cm.Paired)
pl.xlabel('Sepal length')
pl.ylabel('Sepal width')

pl.xlim(x_min, x_max)
pl.ylim(y_min, y_max)
pl.xticks(())
pl.yticks(())

# To getter a better understanding of interaction of the dimensions
# plot the first three PCA dimensions
fig = pl.figure(1, figsize=(8, 6))
ax = Axes3D(fig, elev=-150, azim=110)
X_reduced = PCA(n_components=3).fit_transform(iris.data)
ax.scatter(X_reduced[:, 0], X_reduced[:, 1], X_reduced[:, 2], c=Y,
           cmap=pl.cm.Paired)
ax.set_title("First three PCA directions")
ax.set_xlabel("1st eigenvector")
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel("2nd eigenvector")
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel("3rd eigenvector")
ax.w_zaxis.set_ticklabels([])

pl.show()
