import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

df = pd.read_csv("./data/db-composition_classes.csv",)
df = df.dropna()
print(df.head())
print("Shape of the Dataset: {}".format(df.shape))

# 2 is the default number of components in TSNE
model = TSNE(learning_rate=100, random_state=42)
transformed = model.fit_transform(df.drop("Outcome", axis=1))

# visualizing the first 2 columns of TSNE reduced dataset
xs = transformed[:, 0]
ys = transformed[:, 1]
plt.scatter(xs, ys, alpha=0.5)
plt.show()

# new dataset with TSNE Dataset and Output column of the original dataset
tsne_df = pd.DataFrame({'TSNE1': transformed[:, 0], 'TSNE2': transformed[:, 1], 'Outcome': df['Outcome']})
print(tsne_df.head())

# Visualizing the columns of TSNE Model with the Outcome column mapping
grid = sns.FacetGrid(tsne_df, hue="Outcome")
grid.map(plt.scatter, "TSNE1", "TSNE2", alpha=0.5).add_legend()
plt.show()