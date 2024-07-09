## General Functions for Nerve Analysis 
# Cassady S. Olson 

import os
import sys
import imagej
import numpy as np
import matplotlib.pyplot as plt

ij = imagej.init(['sc.fiji:fiji', 'org.morphonets:SNT'], mode = "headless")

from scyjava import jimport 
PointInImage = jimport('sc.fiji.snt.util.PointInImage')
Tree = jimport('sc.fiji.snt.Tree')
TreeStatistics = jimport('sc.fiji.snt.analysis.TreeStatistics')

def getFiles(filePath):
    dir = os.listdir(filePath)
    if '.DS_Store' in dir:
        dir.remove('.DS_Store')
        
    return dir
    
def rootTip(fileNames, filePath, plot):
    numFiles = len(fileNames)
    root = np.zeros([numFiles,3])
    avgTip = np.zeros([numFiles,3])
    maxTip = np.zeros([numFiles,3])
    nerves = []
    allPts = []
    for file in range(numFiles): 
        #load tree 
        thisFile = filePath + fileNames[file]
        tree = Tree(thisFile)

       #Get root
        thisRoot = tree.getRoot()
        root_list = []
        root_list.append([thisRoot.x, thisRoot.y, thisRoot.z])
        root_list = np.asarray(root_list)
        root[file,:] = root_list

        # Get Tip
        tree_stats = TreeStatistics(tree)
        tips = tree_stats.getTips()
    
        # Get x,y,z coordinates from PointInImage objects.
        tips_iterator = tips.iterator()
        tips_list = []
        while tips_iterator.hasNext():
            t = tips_iterator.next()
            tips_list.append([t.x, t.y, t.z])
        tips_list = np.asarray(tips_list)

       
        maxTip[file, :] = tips_list.max(axis = 0)
        
        
        points = tree.getNodes()
        # Get x,y,z coordinates from PointInImage objects.
        points_iterator = points.iterator()
        points_list = []
        while points_iterator.hasNext():
            p = points_iterator.next()
            points_list.append([p.x, p.y, p.z])
        points_list = np.asarray(points_list)
        # Average tip = center of all points
        avgTip[file,:] = np.mean(points_list, axis = 0).squeeze()
        

        allPts.append(points_list)
        if plot == 'y':
            rootTip = np.stack((root[file,:],avgTip[file,:]))
            fig, ax = plt.subplots() 
            ax.scatter(points_list[:,0], points_list[:,1])
            ax.scatter(root[file, 0], root[file, 1])
            ax.scatter(tips_list[:,0], tips_list[:,1])
            ax.scatter(avgTip[file, 0], avgTip[file, 1])
            ax.plot(rootTip[:,0], rootTip[:,1], 'm')
            ax.set_title(fileNames[file])
        
        

    return root, avgTip

def translateNerves(root, avgTip):
    moveRoot = np.zeros([len(root), 3])    
    moveRoot[:, 0] = root[:,0]
    moveRoot[:,1] = root[:,1]
    newRoot = root-moveRoot
    
    newAvgTip = avgTip - moveRoot
    absNewAvgTip = np.absolute(newAvgTip[:,0])    
    newAvgTip[:,0] = absNewAvgTip
    newAvgTip[:,1] = -1*newAvgTip[:,1]
    

    return newRoot, newAvgTip

def mag2d(x): 
    if x.ndim > 1:
        mag = np.sqrt(x[:,0]**2 + x[:,1]**2)
    else:
        mag = np.sqrt(x[0]**2 + x[1]**2)
    return mag
    
def dot3D(x, y):
    dot = x[0]*y[0] + x[1]*y[1] + x[2]*y[2]
    return dot 
    
def unitVector(avgTip, magAvgTip):
    normAvgTip = np.zeros([len(avgTip), 3])
    if magAvgTip == []:
        magAvgTip = mag2d(avgTip[:,0:2])
    for x in range(len(avgTip)):
        normAvgTip[x,0:2] = avgTip[x,0:2]/magAvgTip[x]
    if np.size(avgTip, 1) == 3:
        normAvgTip[:,2] = avgTip[:,2]
    return normAvgTip
    
def unitVector1(avgTip, magAvgTip):
    normAvgTip = np.zeros([len(avgTip), 3])
    if magAvgTip == []:
        magAvgTip = mag2d(avgTip[:,0:2])
    for x in range(len(avgTip)):
        normAvgTip[x,0:2] = avgTip[x,0:2]/magAvgTip
    if np.size(avgTip, 1) == 3:
        normAvgTip[:,2] = avgTip[:,2]
    return normAvgTip
    
def cent_pnt(pnts):
    """Return the centre of a point array"""
    pnts = np.asarray(pnts)
    return np.average(pnts, axis=0).squeeze()

def translate(pnts, cent=None):
    """Translate the points about the origin
    :Requires:
    :--------
    :  pnts - 2D sequence of point coordinates (N, 2)
    :  cent - a list, tuple, ndarray of xc, yc
    :
    :Returns:
    :-------
    :  p_trans - input points translated about the origin
    :
    :-------
    """
    pnts = np.asarray(pnts)
    if cent is None:
        p_trans = pnts - cent_pnt(pnts)
    else:
        p_trans = pnts - np.asarray(cent)
    return p_trans