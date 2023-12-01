# Principal Component Analysis

This is the Python script for for performing Principal Component Analysis (PCA) in a multidimensional dataset with one outcome variable, particularly tailored for cryopreservation applications.
This script was written by Bruno M. Guerreiro (https://scholar.google.com/citations?user=nbyAZasAAAAJ&hl=en&oi=ao) to this specific application during the PhD thesis (2020-2024).

If used, please reference the following research paper: https://www.biorxiv.org/content/10.1101/2023.10.13.562212v1

How to use:

1. Install Anaconda Navigator
2. Install PyCharm inside the Anaconda environment
3. Open the anaconda prompt and install the following libraries: numpy, pandas, matplotlib, scikit-learn - using the conda install command.
4. Prepare the CSV file as PCA.csv, with the first column as outcome variable, and all subsequent columns as predictor variables. Avoid null values, use the same order of magnitude for data. Place PCA.csv in the same directory as pca.py.
5. In pca.py, change the number of principal components you desire in lines 16-19, in the function and the callable list. The number of components cannot be larger than the number of variables.
6. Run pca.py in PyCharm with Ctrl+Shift+F10. Graphics will be exported to the same directory of pca.csv and pca.py.

Questions? bm.guerreiro@campus.fct.unl.pt