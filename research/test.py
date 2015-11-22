# -*- coding: utf-8 -*-
import numpy as np
from numpy import diag
import numpy.random as rand
from numpy.linalg import norm, inv
import seaborn

import models
from util import gnp
from viz import plotNetwork


rand.seed(1233)
N = 128
max_rounds = 1000
s = rand.rand(N)
A = gnp(N, 0.04, rand_weights=True)
B = diag(rand.rand(N)) * 0.5
#models.deGroot(A, s, max_rounds, plot=True)
#op = models.friedkinJohnsen(A, s, max_rounds, plot=True)
#models.meetFriend(A, s, max_rounds, plot=True)
#models.hk(s, 0.07, max_rounds, eps=1e-8, plot=True)
models.hk_local(A, s, 0.07, max_rounds, eps=1e-8, plot=True, save=True)
#models.ga(A, B, s, max_rounds, plot=True, save=True)
#plotNetwork(A, op[-1,:])