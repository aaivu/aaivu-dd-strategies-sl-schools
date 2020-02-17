#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 12:57:44 2018

@author: wolfpack
"""
import pandas as pd
from scipy.cluster import hierarchy as hc
import matplotlib.pyplot as plt

mean_all = pd.read_csv('marks_mean.csv')
mean_all = mean_all.drop("Unnamed: 0",axis=1)

#correlation matrices
corr_mat_pearson = mean_all.corr(method='pearson')
corr_mat_spearman = mean_all.corr(method='spearman')
corr_mat_kendall = mean_all.corr(method='kendall')

#corr_condensed = hc.distance.squareform(corr_mat_pearson) # convert to condensed
z = hc.linkage(corr_mat_pearson, method='average',metric='cosine')
dendrogram = hc.dendrogram(z, labels=(corr_mat_pearson.columns), orientation='right')
plt.xlabel('cosine distance')
plt.ylabel('subjects')
plt.title('Hierachical Cluster Dendogram for pearson correaltion matix with cosine distance & average cluster method (PCA)')
plt.show()

z = hc.linkage(corr_mat_pearson, method='weighted',metric='cosine')
dendrogram = hc.dendrogram(z, labels=(corr_mat_pearson.columns), orientation='right')
plt.xlabel('cosine distance')
plt.ylabel('subjects')
plt.title('Hierachical Cluster Dendogram for pearson correaltion matix with cosine distance & weighted cluster method(PCA)')
plt.show()

z = hc.linkage(corr_mat_spearman, method='average',metric='cosine')
dendrogram = hc.dendrogram(z, labels=(corr_mat_spearman.columns), orientation='right')
plt.xlabel('cosine distance')
plt.ylabel('subjects')
plt.title('Hierachical Cluster Dendogram for spearman correaltion matix with cosine distance & average cluster method(PCA)')
plt.show()

z = hc.linkage(corr_mat_spearman, method='weighted',metric='cosine')
dendrogram = hc.dendrogram(z, labels=(corr_mat_spearman.columns), orientation='right')
plt.xlabel('cosine distance')
plt.ylabel('subjects')
plt.title('Hierachical Cluster Dendogram for spearman correaltion matix with cosine distance & weighted cluster method(PCA)')
plt.show()

z = hc.linkage(corr_mat_kendall, method='average',metric='cosine')
dendrogram = hc.dendrogram(z, labels=(corr_mat_kendall.columns), orientation='right')
plt.xlabel('cosine distance')
plt.ylabel('subjects')
plt.title('Hierachical Cluster Dendogram for kendall correaltion matix with cosine distance & average cluster method(PCA)')
plt.show()

z = hc.linkage(corr_mat_kendall, method='weighted',metric='cosine')
dendrogram = hc.dendrogram(z, labels=(corr_mat_kendall.columns), orientation='right')
plt.xlabel('cosine distance')
plt.ylabel('subjects')
plt.title('Hierachical Cluster Dendogram for kendall correaltion matix with cosine distance & weighted cluster method(PCA)')
plt.show()
