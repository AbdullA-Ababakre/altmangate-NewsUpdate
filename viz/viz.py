# 11.18.2023 AGI A.I. Hacker Mansion House Altmangate A.I. Project CoLab Notebook Link
# https://colab.research.google.com/drive/11VO2tKK0afXM4rC--P86OEWXhXr0fOMM?usp=sharing#scrollTo=gvBSrs-8xB18


# https://datascientyst.com/get-list-of-n-different-colors-names-python-pandas/
import plotly.express as px
from sklearn.decomposition import PCA
from random import randint

pca = PCA()
components = pca.fit_transform(ebd)

labels = {
    str(i): f"Principal Component Axis # {i+1} ({var:.1f}%)"
    for i, var in enumerate(pca.explained_variance_ratio_ * 100)
}

fig = px.scatter_matrix(
    components,
    labels=labels,
    dimensions=range(2),
    color=[('Element #%06X' % randint(0, 0xFFFFFF)) for  i in range(len(vectors))]
)
fig.update_traces(diagonal_visible=False)
fig.show()





# visualization

#import pprint
#pprint.PrettyPrinter(indent=4).pprint(embeddings)

# 1. Dimensionality Reduction: Apply dimensionality reduction techniques like PCA (Principal Component Analysis) or t-SNE (t-Distributed Stochastic Neighbor Embedding) to reduce the high-dimensional embeddings to a 2D or 3D space for visualization.

# Example using PCA for dimensionality reduction
from sklearn.decomposition import PCA

# Assuming embeddings is your data
ebd = [embeddings[k] for k in embeddings.keys()]
pca = PCA(n_components=2)  # Reduce to 2 dimensions
embeddings_2d = pca.fit_transform(ebd)

# 2. Visualization with Matplotlib or Seaborn: Once you have reduced dimensions, plot the data using scatter plots or other visualization techniques.

import matplotlib.pyplot as plt

plt.scatter(embeddings_2d[:, 0], embeddings_2d[:, 1])
plt.title('Visualization of Embeddings')
plt.xlabel('Component 1')
plt.ylabel('Component 2')
plt.show()

# 3. You can also use Seaborn for more advanced visualization options.
import seaborn as sns

sns.scatterplot(x=embeddings_2d[:, 0], y=embeddings_2d[:, 1])