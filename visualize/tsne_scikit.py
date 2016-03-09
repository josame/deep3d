import sys
import numpy as np
import pylab as Plot
from sklearn.manifold import TSNE
print "Run Y = tsne.tsne(X, no_dims, perplexity) to perform t-SNE on your dataset."
print "Running example on 3D dataset"
X = np.loadtxt("X.txt");
labels = np.loadtxt("Y.txt");
model = TSNE(n_components=2, random_state=0, perplexity=float(sys.argv[1]), early_exaggeration=float(sys.argv[2]), learning_rate=float(sys.argv[3]))
np.set_printoptions(suppress=False)
Y=model.fit_transform(X)
Plot.scatter(Y[:,0], Y[:,1], 20, labels);
Plot.show();
'''
ipython tsne_scikit.py 30 22.0 200.0
'''
