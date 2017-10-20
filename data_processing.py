# Import numpy here

"""

Some utility funcitons: ignore this part, its just to visualize some data

#
#
#
#
#
#
#

"""

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

def display_iris(X, y):
    no_samples, no_features = X.shape
    feature_names = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Flower Type"]
    space_before = 30
    column_space = len(max(feature_names, key=lambda x: len(x)))
    body = ""
    body += " " * space_before
    for feature in feature_names:
        body += " | "
        body += feature
        body += " " * (column_space - len(feature))
    body += " |\n"
    for _ in range(space_before + len(feature_names) * column_space + (len(feature_names) + 1) * 3):
        body += "-"
    body += "\n"
    for i in range(no_samples):
        flower_no = "Flower number {0} at index {1}".format(i + 1, i)
        body += flower_no
        body += " " * (space_before - len(flower_no))
        for j in range(4):
            body += " | "
            current_cell = str(X[i, j])
            body += current_cell
            body += " " * (column_space - len(current_cell))
        body += " | "
        if y[i] == 0:
            current = "Setosa"
        elif y[i] == 1:
            current = "Versicolour"
        else:
            current = "Virginica"
        body += current
        body += " " * (column_space - len(current))
        body += " |\n"
    print(body)


def plot_scatter(x1, x2, labels):
    plt.figure(figsize=(10,6))
    plt.scatter(x=x1, y=x2, c=labels, cmap=plt.cm.gist_rainbow)
    plt.show()


def plot_centroids(x1, x2, centroids1, centroids2):
    labels = np.zeros(x1.shape)
    labels_centroids = np.ones(centroids1.shape) * 100
    
    x1 = np.concatenate((x1, centroids1))
    x2 = np.concatenate((x2, centroids2))
    labels = np.concatenate((labels, labels_centroids))
    plt.figure(figsize=(10,6))
    plt.scatter(x=x1, y=x2, c=labels, cmap=plt.cm.bwr)
    plt.show()


def plot_kmeans(x1, x2, centroids1, centroids2, labels):
    non_centroid_labels = np.zeros(x1.shape)
    centroid_labels = np.ones(centroids1.shape)

    x1_centroids = np.concatenate((x1, centroids1))
    x2_centroids = np.concatenate((x2, centroids2))
    centroid_labels = np.concatenate((non_centroid_labels, centroid_labels))
    
    plt.figure(figsize=(20,6))
    plt.subplot(121)
    plt.scatter(x=x1, y=x2, c=labels, cmap=plt.cm.gist_rainbow)
    plt.subplot(122)
    plt.scatter(x=x1_centroids, y=x2_centroids, c=centroid_labels, cmap=plt.cm.bwr)
    plt.show()




#
#
# Start coding here!







"""
Let's play with some data

The dataset we are going to look at is the Iris dataset:

* Every row represents a different flower.
* Every column represents a different **feature** for that flower

The features (columns) reprsent the Sepal Length, Sepal Width, Petal Length and Petal Width for each flower. 

Each flower is one of three different types: Setosa, Versicolour, and Virginica.

"""

# Loading and displaying the data...
iris = load_iris()
X = iris.data
y = iris.target

#display_iris(X, y)





"""
What if we don't know the type for every flower?

Let's try _clustering_ the data.

Clustering is a method of grouping data points in different groups, called clusters

Data points in the same clusters are similar to one another
"""

"""
 Algorithm: K-means clustering

1. Find a measure of "similarity" for points (rows) in the data (e.g. distance between each row) 

2. Choose how many clusters do you want to divide the data in, e. g. _n_

3. Select _n_ random points from the data, we'll call these cluster _centroids_

4. Repeat the following steps many times:
    a. For each point (row) in the data, assign/label it with the _centroid_ it is closest to; 
        Each point will be labeled to the _centroid_ it is closest to
    b. For each _centroid_: take all points assigned to it in step a and find the mean of these points; 
        This new point will be the new _centroid_

5. At the end, the points assigned to each _centroid_ will belong to a different cluster.
"""

# 1. Find a measure of "similarity" between data points





# 2. Choose how many clusters you want to divide the data in





# 3. Select n random points from the data





# 4. Repeat the following:
# a. Label each point to a centroid






# b. Find new centroids from mean of labeled points









# Put it all together


