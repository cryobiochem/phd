# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Input raw data
data = pd.read_csv('PCA.csv', index_col=0)

# Standardize the data
scaler = StandardScaler()
data_std = scaler.fit_transform(data)

# Perform PCA
pca = PCA(n_components=6)
principal_components: object = pca.fit_transform(data_std)
explained_variance_ratio = pca.explained_variance_ratio_
pcnumber = ['PC1', 'PC2', 'PC3', 'PC4','PC5', 'PC6']

# Create a dataframe to store the results
results = pd.DataFrame(data=principal_components, columns=pcnumber)
results['Sample'] = data.index
print(explained_variance_ratio) #prints the variance for each PCx



# Visualize the results
plt.figure(figsize=(8, 6))
plt.scatter(results['PC1'], results['PC2'])
plt.xlabel('PC1 ({:.2f}%)'.format(explained_variance_ratio[0]*100))
plt.ylabel('PC2 ({:.2f}%)'.format(explained_variance_ratio[1]*100))
plt.title('PCA of Sofia Samples')
for i, sample in enumerate(results['Sample']):
    plt.annotate(sample, (results['PC1'][i], results['PC2'][i]))
plt.show()

# Create a scree plot
plt.figure(figsize=(8, 6))
plt.plot(np.arange(1, len(explained_variance_ratio)+1), explained_variance_ratio, 'o-')
plt.xlabel('Number of Principal Components')
plt.ylabel('Explained Variance Ratio')
plt.title('Scree Plot')
plt.show()

# Loading plot
loadings = pd.DataFrame(pca.components_.T, columns=pcnumber, index=data.columns)
plt.figure(figsize=(8, 6))
plt.scatter(loadings['PC1'], loadings['PC2'])
plt.xlabel('PC1 Loading')
plt.ylabel('PC2 Loading')
plt.title('Loading Plot')
for i, feature in enumerate(loadings.index):
    plt.annotate(feature, (loadings['PC1'][i], loadings['PC2'][i]))
plt.show()

# Cluster the samples
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3)
kmeans.fit(principal_components)
results['Cluster'] = kmeans.predict(principal_components)

# Get centroids
centroids = pd.DataFrame(kmeans.cluster_centers_, columns=pcnumber)
centroids['Cluster'] = ['Cluster {}'.format(i+1) for i in range(len(centroids))]

# Plot the results
fig, ax = plt.subplots(figsize=(8, 6))
colors = ['#40A599', '#C9505E', '#000000'] # list of colors for each cluster
for i, cluster in enumerate(set(results['Cluster'])):
    mask = results['Cluster'] == cluster
    ax.scatter(results.loc[mask, 'PC1'], results.loc[mask, 'PC2'], c=colors[i], label=cluster, alpha=.75)
    centroid = centroids.loc[centroids['Cluster'] == cluster]
    ax.scatter(centroid['PC1'], centroid['PC2'], c='black', s=100, marker='x', facecolors='black')
for i, sample in enumerate(results['Sample']):
    plt.annotate(sample, (results['PC1'][i], results['PC2'][i]), size=8)
ax.legend()

# Add dashed lines where x=0 and y=0
ax.axhline(y=0, linestyle='dotted', lw=1, color='grey')
ax.axvline(x=0, linestyle='dotted', lw=1, color='grey')

# Add loading vectors
loadings = pd.DataFrame(pca.components_.T, columns=pcnumber, index=data.columns)
for i, feature in enumerate(loadings.index):
    plt.arrow(0, 0, loadings['PC1'][i]*2, loadings['PC2'][i]*2, color='r', alpha=.5, linewidth=2, head_width=.02, head_length=.02)
    plt.text(loadings['PC1'][i]*2, loadings['PC2'][i]*2, feature, color='r', alpha=.7)

# Set axis labels and title
plt.xlabel('PC1 ({:.2f}%)'.format(explained_variance_ratio[0]*100))
plt.ylabel('PC2 ({:.2f}%)'.format(explained_variance_ratio[1]*100))
#plt.title('PCA Biplot with Clusters and Centroids')
ax.legend().remove()

# Show the plot
plt.style.use('fivethirtyeight')
plt.savefig('biplot.tif', dpi=600, format='tif')
plt.show()


