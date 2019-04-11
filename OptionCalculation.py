#!/usr/bin/env python
# coding=UTF-8
'''
@Description: COMP7405 Assignment 3
@Author: CJJ && HXZ
@LastEditors: Cai Jiajun
@Date: 2019-04-02 17:12:19
@LastEditTime: 2019-04-11 16:28:38
'''

import numpy as np
import math
import scipy.stats as si

class OptionCalculation(object):

    def __init__(self):
        '''
        Generate the test cases
        '''
        # @list,tThe first THREE Asian options are put options, the last THREE are call options 
        self.Asian = self._init_Asian_testcases()

        # @list, the first SIX Asian options are put options, the last THREE are call options 
        self.Basket = self._init_Basket_testcases()
        
        # risk-free rate
        self.r = 0.05

        # maturity 
        self.T = 3

        # current asset value
        self.S0 = 100.0

        pass
    
    def _init_Asian_testcases(self):
        
        sigma = [0.3, 0.3, 0.4, 0.3, 0.3, 0.4]
        K = [100.0]*6
        n = [50, 100, 50, 50, 100, 50]
        Type = ['Put']*3 + ['Call']*3

        return [{'sigma':p1, 'K': p2, 'n': p3, 'Type': p4} for (p1, p2, p3, p4) in zip(sigma, K, n, Type)]
        
    def _init_Basket_testcases(self):

        S1 = [100.0]*12
        S2 = [100.0]*12
        K = list(map(float, [100]*3+[80, 120]+[100]*4+[80, 120, 100]))
        sigma1 = [.3]*2 + [.1] + [.3]*2 + [.5] + [.3]*2 + [.1] + [.3]*2 + [.5]
        sigma2 = [.3]*5 + [.5] + [.3]*5 + [.5]
        rho = [.5] + [.9] + [.5]*5 + [.9] + [.5]*4
        Type = ['Put']*6 + ['Call']*6

        return [{'S1':p1, 'S2': p2, 'K': p3, 'sigma1': p4, 'sigma2': p5, 'rho': p6, 'Type': p7} \
                for (p1, p2, p3, p4, p5, p6, p7) in zip(S1, S2, K, sigma1, sigma2, rho, Type)]
    
    def BSFormulas(self, other_para)-> float:

        S = other_para['S']
        K = other_para['K']
        ttm = other_para['t']
        r = other_para['r']
        sigma = other_para['vol']
        Type = other_para['type']

        d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2)
               * (ttm)) / (sigma * np.sqrt(ttm))
        d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2)
            * (ttm)) / (sigma * np.sqrt(ttm))

        if Type == "Call":
            result = (S * si.norm.cdf(d1, 0.0, 1.0) - K *
                    np.exp(-r * (ttm)) * si.norm.cdf(d2, 0.0, 1.0))
            return result
        if Type == "Put":
            result = (K * np.exp(-r * (ttm)) * si.norm.cdf(-d2,
                    0.0, 1.0) - S * si.norm.cdf(-d1, 0.0, 1.0))
            return result
        return -1
        
    def ImpVol(self, other_para = None)-> float:
        
        S = other_para['S']
        K = other_para['K']
        T = other_para['t']
        value = other_para['value']
        r = other_para['r']
        q = other_para['q']
        Type = other_para['type']

        sigmahat = np.sqrt(2*np.abs((np.log(S/K)+(r-q)*(T))/ T)) 
        tolerance = 0.00000001
        xnew  = sigmahat
        increment = 1
        n = 1
        nmax = 100

        while (abs(increment) > tolerance) & (n < nmax):
            d1 = (np.log(S / K) + (r - q + 0.5 * xnew ** 2) * T) / (xnew * np.sqrt(T))
            d2 = (np.log(S / K) + (r - q - 0.5 * xnew ** 2) * T) / (xnew * np.sqrt(T))
            if Type == "Call":
                fx = S * np.exp(-q * T) * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0) - value
            if Type == "Put":
                fx = K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) - S * np.exp(-q * T) * si.norm.cdf(-d1, 0.0, 1.0) -  value
            vega = 1 / np.sqrt(2 * np.pi) * S * np.exp(-q * T) * np.exp(-(d1 ** 2) * 0.5) * np.sqrt(T)
            increment = fx/vega
            xnew = xnew - increment
            n += 1

        return abs(xnew)

    def ClosedFormFormulas(self, other_para = None)-> float:
        """Calculate the Asian option value using closed-form formulas

        Args:
            self: you can get the testcases from self.Asian
            other_para: if you want to test you functions using other samples, please input a dictionary with the same format as \
                the element of @self.Asian (i.e. {'sigma':p1, 'K': p2, 'n': p3, 'Type': p4})
        Returns:
            A float number with the value of Asian option
        """

        #TODO(Big Huang): 请开始你的表演
        K = other_para['K']
        T = other_para['T']
        S0 = other_para['S']
        r = other_para['r']
        sigma = other_para['sigma']
        Type = other_para['type']
        n = other_para['n']
        
        sigma_hat = sigma * np.sqrt((n + 1) * (2 * n + 1)/(6 * n ** 2))
        u_hat = (r - 0.5 * sigma ** 2) * (n + 1) / (2 * n) + 0.5 * sigma_hat ** 2
        
        d1 = (np.log(S0 / K) + (u_hat + 0.5 * sigma_hat ** 2) * T ) / (sigma_hat * np.sqrt(T))
        d2 = d1 - sigma_hat * np.sqrt(T)
        
        if Type == "Call":
            option_value = np.exp(-r * T) * (S0 * np.exp(u_hat * T) * si.norm.cdf(d1, 0.0, 1.0) - K * si.norm.cdf(d2, 0.0, 1.0) )
            return option_value
            
        if Type == "Put":
            option_value = np.exp(-r * T) * (K * si.norm.cdf(-d2, 0.0, 1.0) - S0 * np.exp(u_hat * T) * si.norm.cdf(-d1, 0.0, 1.0))
            return option_value
        
        return -1

    def ClosedFormForBasketOption(self, other_para =None)->float:
        
        K = other_para['K']
        T = other_para['t']
        S_0 = other_para['S']
        r = other_para['r']
        sigma = other_para['sigma']
        
        Rho_input = other_para['rho']
        Type = other_para['type']
        n = 2
        sigma_hat_1 = 0
        B_1 = 1
        Rho = np.zeros(shape=(n,n))
        #Rho_input的输入为相关系数，如果是3个以上的Rho = [0.3, 0.4, 0.5] 则分别为第一个期权与第二个期权，第一个期权和第三个期权，第二个和第三个的相关系数，以此类推
        #生成Rho矩阵
        for i in range(n):
            for j in range(i,n):
                if i == j:
                    Rho[i][j] = 1.0
                else:
                    Rho[i][j] = Rho_input[i + j - 1]
                    Rho[j][i] = Rho[i][j]  
        #参数
        for i in range(n):
            for j in range(n):
                sigma_hat_1 += sigma[i] * sigma[j] * Rho[i][j]
            B_1 *= S_0[i]
        sigma_hat = np.sqrt(sigma_hat_1) / n   
        u_hat = r - 0.5 * np.sum(np.multiply(sigma,sigma)) / n + 0.5 * sigma_hat ** 2
        B_0 = B_1 ** (1 / n)
        
        d1 = (np.log(B_0/ K) + (u_hat + 0.5 * sigma_hat ** 2) * T ) / (sigma_hat * np.sqrt(T))
        d2 = d1 - sigma_hat * np.sqrt(T)
        
        if Type == "Call":
            option_value = np.exp(-r * T) * (B_0 * np.exp(u_hat * T) * si.norm.cdf(d1, 0.0, 1.0) - K * si.norm.cdf(d2, 0.0, 1.0) )
            return option_value
            
        if Type == "Put":
            option_value = np.exp(-r * T) * (K * si.norm.cdf(-d2, 0.0, 1.0) - B_0 * np.exp(u_hat * T) * si.norm.cdf(-d1, 0.0, 1.0))
            return option_value
        return -1   
        
    def MonteCarloAsianOption(self, other_para = None)-> float:
        """Calculate the Asian option value using Monte Carlo method

        Args:
            self: you can get the testcases from self.Asian
            other_para: if you want to test you functions using other samples, please input a dictionary with the same format as \
                the element of @self.Asian (i.e. {'sigma':p1, 'K': p2, 'n': p3, 'Type': p4})
        Returns:
            A float number with the value of Asian option
        """

        #TODO(Big Huang): 请开始你的表演

        S0 = other_para['S']
        K = other_para['K']
        T = other_para['T']
        r = other_para['r']
        sigma = other_para['sigma']
        M = other_para['n']
        I = other_para['I']
        Type = other_para['type']
        c_v = other_para['c_v']

        
        dt = T / M
        drift = np.exp((r - 0.5 * sigma ** 2) * dt) 
        arith_Payoff = []    
        geo_Payoff = []
        np.random.seed(10)
        
        for i in range(I):
            growth_factor = drift * np.exp(sigma * np.sqrt(dt) * np.random.randn())
            path = []    
            for t in range(M):
                if t == 0:
                    path.append(S0 * growth_factor)
                else:
                    growth_factor = drift * np.exp(sigma * np.sqrt(dt) * np.random.randn())
                    S_t = path[t-1] * growth_factor
                    path.append(S_t)
                    
            arith_Mean = np.mean(path)
            geo_Mean = np.exp(np.sum(np.log(path)) / M)
            
            if Type == 'Call':
                arith_Payoff.append(np.exp(- r * T) * max(arith_Mean - K, 0))
                geo_Payoff.append(np.exp(- r * T) * max(geo_Mean - K, 0))
            elif Type == 'Put':
                arith_Payoff.append(np.exp(- r * T) * max(K - arith_Mean, 0))
                geo_Payoff.append(np.exp(- r * T) * max(K - geo_Mean, 0))
            
        Pmean = np.mean(arith_Payoff)
        Gmean = np.mean(geo_Payoff)
        Pstd = np.std(arith_Payoff)
        confmc = [Pmean - 1.96 * Pstd / np.sqrt(M),Pmean + 1.96 * Pstd / np.sqrt(M)]
        result_for_Standard_MC = {'Price':Pmean,'95% Confidence Interval':confmc}
        print(result_for_Standard_MC)
        if c_v == 'False':
            return result_for_Standard_MC
        elif c_v == 'True':
            #MC with Control Variate
            covXY = np.mean(np.multiply(arith_Payoff, geo_Payoff)) - Pmean * Gmean
            theta = covXY / np.var(geo_Payoff)
            
            geo_payoff_1 = []
            para ={
                'K': K,
                'T': T,
                'S': S0,
                'r': r,
                'sigma': sigma,
                'type': Type,
                'n': M

            }
            geo = self.ClosedFormFormulas(para)
            for item in geo_Payoff:
                geo_payoff_1.append(geo - item)
            z = arith_Payoff + np.multiply(theta,geo_payoff_1)
            z_mean = np.mean(z)
            z_std = np.std(z)
            confcv = [z_mean - 1.96 * z_std / np.sqrt(M),z_mean + 1.96 * z_std / np.sqrt(M)]
            result_with_Control_Variate = {'Price':z_mean,'95% Confidence Interval':confcv}
            print(result_with_Control_Variate)
            return result_with_Control_Variate
            
        return -1

    def MonteCarloBasketOption(self, other_para = None)-> float:
        """Calculate the Basket option value using Monte Carlo method

        Args:
            self: you can get the testcases from @self.Basket
            other_para: if you want to test you functions using other samples, please input a dictionary with the same format as \
                the element of @self.Asian (i.e. {'S1':p1, 'S2': p2, 'K': p3, 'sigma1': p4, 'sigma2': p5, 'rho': p6, 'Type': p7})
        Returns:
            A float number with the value of Basket option
        """

        #TODO(Big Huang): 请开始你的表演

        S0 = other_para['S']
        K = other_para['K']
        T = other_para['T']
        r = other_para['r']
        sigma = other_para['sigma']
        #M = other_para['M']
        M = 50
        Type = other_para['type']
        Rho_input = other_para['rho']
        c_v = other_para['c_v']
        I = other_para['I']

        dt = T / M
        drift = {}
        for i in range(2):
            drift[i] = np.exp((r - 0.5 * sigma[i] ** 2) * dt) 
        arith_Payoff = []
        geo_Payoff = []
        growth_factor = {}
        arith_Mean_1 = {}
        geo_Mean_1 = {}
        path_1 = {} 
        
        np.random.seed(10)
        z_1 = np.random.randn()
        np.random.seed(5)
        z_2 = np.random.randn()

        for i in range(I): 
            
            #calculate the initial growth factor
            if i == 0:
                growth_factor[0] = drift[0] * np.exp(sigma[0] * np.sqrt(dt) * z_1)
                growth_factor[1] = drift[1] * np.exp(sigma[1] * np.sqrt(dt) * (Rho_input[0] * z_1 + np.sqrt(1 - Rho_input[0]** 2) * z_2))

            #calculate the growth factor
            else:
                z = np.random.randn()
                growth_factor[0] = drift[0] * np.exp(sigma[0] * np.sqrt(dt) * z)
                growth_factor[1] = drift[1] * np.exp(sigma[1] * np.sqrt(dt) * (Rho_input[0] * z + np.sqrt(1 - Rho_input[0]** 2) * np.random.randn()))
            
            path_1 = {} 
            for j in range(2):
                path_1[j] = []
                path_1[j].append(S0[j] * growth_factor[j])  
            #calculate the full path 
            for t in range(1, M): 
                #calculate the two standard normal distribution with Rho_input
                z = np.random.randn()
                growth_factor[0] = drift[0] * np.exp(sigma[0] * np.sqrt(dt) * z)
                growth_factor[1] = drift[1] * np.exp(sigma[1] * np.sqrt(dt) * (Rho_input[0] * z + np.sqrt(1 - (Rho_input[0])** 2) * np.random.randn()))
                #calculate the full path path_1
                for j in range(2):   
                    S_t = path_1[j][t-1] * growth_factor[j]
                    path_1[j].append(S_t)
        
            for j in range(2):
                arith_Mean_1[j] = np.mean(path_1[j])
                geo_Mean_1[j] = np.exp(np.sum(np.log(path_1[j])) / M)
            
            sum_1 = 0
            sum_2 = 0
            if Type == 'Call':
                for j in range(2):
                    sum_1 +=  np.exp(- r * T) * (arith_Mean_1[j] - K)
                    sum_2 +=  np.exp(- r * T) * (geo_Mean_1[j] - K)
                arith_Payoff.append(np.exp(- r * T) * max(sum_1, 0))
                geo_Payoff.append(np.exp(- r * T) * max(sum_2, 0))
            elif Type == 'Put':
                for j in range(2):
                    sum_1 +=  np.exp(- r * T) * (K - arith_Mean_1[j])
                    sum_2 +=  np.exp(- r * T) * (K - geo_Mean_1[j])
                arith_Payoff.append(np.exp(- r * T) * max(K - arith_Mean_1[j], 0))
                geo_Payoff.append(np.exp(- r * T) * max(K - geo_Mean_1[j], 0))
        
        Pmean = np.mean(arith_Payoff)
        Gmean = np.mean(geo_Payoff)
        Pstd = np.std(arith_Payoff)
        
        confmc = [Pmean - 1.96 * Pstd / np.sqrt(M),Pmean + 1.96 * Pstd / np.sqrt(M)]
        result_for_standrad_MC = {'Arith_Price':Pmean,'Geo_Price':Gmean,'95% Confidence Interval':confmc}
        print(result_for_standrad_MC)
        if c_v == 'False':
            return result_for_standrad_MC
        elif c_v == 'True':        
            #control Variate
            covXY = np.mean(np.multiply(arith_Payoff, geo_Payoff)) - Pmean * Gmean
            theta = covXY / np.var(geo_Payoff)

            para = {
                'K': K,
                't': T,
                'S': S0,
                'r': r,
                'sigma': sigma,
                'n': 2,
                'rho': Rho_input,
                'type': Type
            }
            
            geo = self.ClosedFormForBasketOption(other_para=para)
            
            geo_payoff_1 = []
            for item in geo_Payoff:
                geo_payoff_1.append(geo - item)

            z = arith_Payoff + np.multiply(theta,geo_payoff_1)
            z_mean = np.mean(z)
            z_std = np.std(z)
            confcv = [z_mean - 1.96 * z_std / np.sqrt(M),z_mean + 1.96 * z_std / np.sqrt(M)]
            result_for_control_variate = {'Arith_Price':z_mean,'95% Confidence Interval':confcv}
            print(result_for_control_variate)
            return result_for_control_variate
        return -1

    
    def BinomialTreeAmericanOption(self, other_para = None)-> float:

        S = other_para['S']
        vol = other_para['vol']
        r = other_para['r']
        T = other_para['T']
        K = other_para['K']
        N = other_para['N']
        Type = other_para['type']

        dt = T/N
        u = math.exp(vol*math.sqrt(dt))
        d = 1/u
        
        p = (math.exp(r*dt)-d)/(u-d)
        DF = math.exp(-r*dt)

        initial_asset = [S*(u**i *(d**(N-i))) for i in range(N+1)]

        if Type == 'Call':

            initial_asset = [max(0,s-K) for s in initial_asset]
            for i in range(N,0,-1):
                # in the i-round
                new_asset = []

                for j in range(i-1,-1,-1):

                    cur_S = S*(u**(j))*(d**(i-1-j))
                    op = max(cur_S-K,DF*(p*initial_asset[j+1]+(1-p)*initial_asset[j]))
                    new_asset.append(op)
                
                initial_asset = new_asset[::-1]
            return initial_asset[0]
            
        elif Type == 'Put':
            initial_asset = [max(0,K-s) for s in initial_asset]
            for i in range(N,0,-1):
                # in the i-round
                new_asset = []

                for j in range(i-1,-1,-1):

                    cur_S = S*(u**(j))*(d**(i-1-j))
                    op = max(K-cur_S,DF*(p*initial_asset[j+1]+(1-p)*initial_asset[j]))
                    new_asset.append(op)
                
                initial_asset = new_asset[::-1]
            return initial_asset[0]
        

if __name__ == "__main__":

    ## example code
    OC = OptionCalculation()
    para = {
        'S':100.0,
        'vol': 0.3,
        'r': 0.05,
        'T': 3,
        'K': 100.0,
        'N': 50,
        'type': 'Put'
    }
    value = OC.BinomialTreeAmericanOption(other_para=para)
    print("the option value is %f" %value)
    pass