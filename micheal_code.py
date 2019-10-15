
from __future__ import division
import numpy as np
import scipy.io as sio
from scipy.stats import truncnorm
import warnings
import random
np.random.seed(0)
# Simulate diffusion models
def simuldiffn200(N=100,Alpha=1,Vet=.2,Rmr=.2,Nu=1,Zeta=None,rangeVet=0,rangeRmr=0,rangeZeta=0,Eta=.3,Varsigma=1):

    if Zeta is None:
        Zeta = .5*Alpha

    if (Nu < -5) or (Nu > 5):
        Nu = np.sign(Nu)*5
        warnings.warn('Nu is not in the range [-5 5], bounding drift rate to %.1f...' % (Nu))

    if (Eta > 3):
        warning.warn('Standard deviation of drift rate is out of bounds, bounding drift rate to 3')
        eta = 3

    if (Eta == 0):
        Eta = 1e-16

    #Initialize output vectors
    result = np.zeros(N)
    T = np.zeros(N)
    XX = np.zeros(N)
    N200 = np.zeros(N)

    #Called sigma in 2001 paper
    D = np.power(Varsigma,2)/2

    #Program specifications
    eps = 2.220446049250313e-16 #precision from 1.0 to next double-precision number
    delta=eps

    for n in range(0,N):
        r1 = np.random.normal()
        mu = Nu + r1*Eta
        zz = Zeta - rangeZeta/2 + rangeZeta*np.random.uniform()
        finish = 0
        totaltime = 0
        startpos = 0
        Aupper = Alpha - zz
        Alower = -zz
        radius = np.min(np.array([np.abs(Aupper), np.abs(Alower)]))
        while (finish==0):
            lambda_ = 0.25*np.power(mu,2)/D + 0.25*D*np.power(np.pi,2)/np.power(radius,2)
            # eq. formula (13) in 2001 paper with D = sigma^2/2 and radius = Alpha/2
            F = D*np.pi/(radius*mu)
            F = np.power(F,2)/(1 + np.power(F,2) )
            # formula p447 in 2001 paper
            prob = np.exp(radius*mu/D)
            prob = prob/(1 + prob)
            dir_ = 2*(np.random.uniform() < prob) - 1
            l = -1
            s2 = 0
            while (s2>l):
                s2=np.random.uniform()
                s1=np.random.uniform()
                tnew=0
                told=0
                uu=0
                while (np.abs(tnew-told)>eps) or (uu==0):
                    told=tnew
                    uu=uu+1
                    tnew = told + (2*uu+1) * np.power(-1,uu) * np.power(s1,(F*np.power(2*uu+1,2)));
                    # infinite sum in formula (16) in BRMIC,2001
                l = 1 + np.power(s1,(-F)) * tnew;
            # rest of formula (16)
            t = np.abs(np.log(s1))/lambda_;
            # is the negative of t* in (14) in BRMIC,2001
            totaltime=totaltime+t
            dir_=startpos+dir_*radius
            vetime = Vet - rangeVet/2 + rangeVet*np.random.uniform()
            rmrt = Rmr - rangeRmr/2 + rangeRmr*np.random.uniform()
            if ( (dir_ + delta) > Aupper):
                T[n]=vetime+totaltime+rmrt
                XX[n]=1
                N200[n]=vetime
                finish=1
            elif ( (dir_-delta) < Alower ):
                T[n]=vetime+totaltime+rmrt
                XX[n]=-1
                N200[n]=vetime
                finish=1
            else:
                startpos=dir_
                radius=np.min(np.abs([Aupper, Alower]-startpos))

    result = T*XX
    return result
