from mlxtend.data import loadlocal_mnist
X, Y = loadlocal_mnist(
images_path='../data/mnist/t10k-images.idx3-ubyte',
labels_path='../data/mnist/t10k-labels.idx1-ubyte')
print(X.shape)
print(Y.shape)
print(X[0])
print(X[0].reshape(28,28))
print(Y[0])
