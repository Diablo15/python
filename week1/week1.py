# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#           NAME: week1.py
#         AUTHOR: Stratis Gavves
#  LAST MODIFIED: 18/03/10
#    DESCRIPTION: TODO
#
#------------------------------------------------------------------------------
import numpy as np
import urllib
import os
import sys
import math
import scipy.signal as sgn

def extractColorHistogram( im ):
    # PRE [DO NOT TOUCH]
    histo = []
    
    # WRITE YOUR CODE HERE
    im_r = im[:, :, 0].flatten()
    histo_r = np.bincount(im_r,None,256)
    im_g = im[:, :, 1].flatten()
    histo_g = np.bincount(im_g,None,256)
    im_b = im[:, :, 2].flatten()
    histo_b = np.bincount(im_b,None,256)
    
    # RETURN [DO NOT TOUCH]
    histo = np.concatenate([histo_r, histo_g, histo_b])
    return histo

def computeVectorDistance( vec1, vec2, dist_type ):
    # PRE [DO NOT TOUCH]
    dist = []
    
    # WRITE YOUR CODE HERE
    if dist_type == 'euclidean' or dist_type == 'l2':
        dist = np.linalg.norm(vec1 - vec2)
    elif dist_type == 'intersect' or dist_type == 'l1':
        dist = sum(np.minimum(vec1, vec2))
    elif dist_type == 'chi2':
        dist = sum(((vec1 - vec2) **2) / (vec1+vec2))
    elif dist_type == 'hellinger':
        dist = sum(np.sqrt((vec1*vec2)))
                        
    # RETURN [DO NOT TOUCH]
    return dist
    
def computeImageDistances( images ):
    # PRE [DO NOT TOUCH]
    imdists = []
    
    # WRITE YOUR CODE HERE
    for i in range(0, 60):
        imdists.append([])
        for j in range(0, 60):
            imdists[i].append(extractColorHistogram.histo(images))
    
    # RETURN [DO NOT TOUCH]
    return imdists
    
def rankImages( imdists, query_id ):
    # PRE [DO NOT TOUCH]
    ranking = []

    # WRITE YOUR CODE HERE
    ranking = np.argsort(imdists[query_id])
    
    # RETURN [DO NOT TOUCH]
    return ranking

def get_gaussian_filter(sigma):
    # PRE [DO NOT TOUCH]
    sigma = float(sigma)
    G = []
    
    # WRITE YOUR CODE HERE FOR DEFINING THE HALF SIZE OF THE FILTER
    # half_size = ...
    #
    x = np.arange(-half_size, half_size + 1)        

    # WRITE YOUR CODE HERE
    # G
                        
    # RETURN [DO NOT TOUCH]
    G = G / sum(G) # It is important to normalize with the total sum of G
    return G
    
def get_gaussian_der_filter(sigma, order):
    # PRE [DO NOT TOUCH]
    sigma = float(sigma)
    dG = []
    
    # WRITE YOUR CODE HERE
    # half_size = ...
    #
    x = np.arange(-half_size, half_size + 1)
    
    # if order == 1:
        # WRITE YOUR CODE HERE
        # dG = ...
    # elif order == 2:
        # WRITE YOUR CODE HERE
        # dG = ...

    # RETURN [DO NOT TOUCH]
    return dG

def gradmag(im_dr, im_dc):
    # PRE [DO NOT TOUCH]
    im_dmag = []

    # WRITE YOUR CODE HERE
    # im_dmag = ...
    #

    # RETURN [DO NOT TOUCH]
    return im_dmag    

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# [ALREADY IMPLEMENTED. DO NOT TOUCH]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def apply_filter(im, myfilter, dim):
    H, W = im.shape
    if dim == 'col':
        im_filt = sgn.convolve(im.flatten(), myfilter, 'same')
        im_filt = np.reshape(im_filt, [H, W])
    elif dim == 'row':
        im_filt = sgn.convolve(im.T.flatten(), myfilter, 'same')
        im_filt = np.reshape(im_filt, [W, H]).T
    
    return im_filt

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# [ALREADY IMPLEMENTED. DO NOT TOUCH]    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def apply_gaussian_conv(im, G):
    im_gfilt = apply_filter(im, G, 'col')
    im_gfilt = apply_filter(im_gfilt, G, 'row')
    
    return im_gfilt


        
        
    
