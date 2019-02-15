import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
import matplotlib.pyplot as plt

df = pd.read_excel('Produccion del día.xlsx')
X = np.array([i+1 for i in range(df.shape[0])])
y = np.cumsum(df[df.columns[1]])

poly = PolynomialFeatures(degree=2)
X_ = poly.transform(X)
