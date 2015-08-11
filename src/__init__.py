"""

GeePee module - general Gaussian process regression/fitting module. This is forked from my earlier GaussianProcesses and Infer modules that was developed for Gibson et al. (2012) and later work. Please cite this paper if making use of this code. This fork is to enable the GP object to be more easily passed to other optimisation/inference codes, and to simplify the application to simple problems. This code is designed to be as fast as possible without rewriting any basic linear algebra routines, and as flexible as possible, enabling extension to externally defined kernels, and combining multiple GPs into a single posterior (e.g. for multiple light curve fitting).

Neale Gibson
ngibson@eso.org
nealegibby@gmail.com

"""

from Optimiser import *

from InferGP import GP
#from InferMGP import MGP

from GPUtils import *
import GPRegression as GPR
import GPCovarianceMatrix as GPC
from GPKernelFunctions import *
from GPPeriodicKernelFunctions import *
from GPToeplitz import *
