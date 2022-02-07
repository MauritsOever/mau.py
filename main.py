# -*- coding: utf-8 -*-
"""
Main file to create my own package...

Created on Mon Jan 31 15:57:00 2022

@author: MauritsOever
https://github.com/MauritsOever

liskov substitution principle
child parent classes - python inheritance
only need to import packages once in a class
docker
google cloud
container - virtual machine
getters and setters
data engineering
"""

# start this file with creating a class
# so this package is only able to do some basic financially related stuff...
# https://realpython.com/python3-object-oriented-programming/

# dependencies right now:
# pandas 0.25.1
# numpy 1.16.5
# yfinance 0.1.63

    
def Yahoo(list_of_ticks, startdate, enddate, retsorclose = 'rets'):
    '''
    Parameters
    ----------
    list_of_ticks : list of strings, tickers
    startdate     : string, format is yyyy-mm-dd
    enddate       : string, format is yyyy-mm-dd
    retsorclose   : string, 'rets' for returns and 'close' for adjusted closing prices
    Returns
    -------
    dataframe of stock returns or prices based on tickers and date

    '''
    import yfinance as yf
    import pandas as pd
    import numpy as np
    
    dfclose = pd.DataFrame(yf.download(list_of_ticks, start=startdate, end=enddate))['Adj Close']
    dfrets  = np.log(dfclose) - np.log(dfclose.shift(1))
    
    if retsorclose == 'rets':
        return dfrets
    else:
        return dfclose
        
class OLS:
    def __init__(self, vY, mX, const = 'yes'):
        import numpy as np
        self.variable_names = list(mX.columns)
        self.Y = np.array(vY)
        if const == 'yes':
            self.const = 'yes'
            self.X = np.ones((len(mX), len(mX.columns)+1))
            self.X[:, 1:] = mX
        else:
            self.const = 'no'
            self.X = np.array(mX)
            
    def fit(self):
        """
        Parameters
        ----------
        vY      : vector, dependent variable
        mX      : df of exogenous variables
        const   : 'yes' for the inclusion of a constant, literally anything else for no constant

        Returns
        -------
        vector of betas

        """   
        import numpy as np
        self.vbeta = np.linalg.inv(self.X.T@self.X)@self.X.T@self.Y
        
        # include some standard errors sometime maybe
        # standarderrors = 
        return self.vbeta
    
    def predict(self):
        """
        takes no argument, but needs self.vbeta to be defined, so you need to fit the model first
        
        Returns
        -------
        Array of predicted Y values.

        """
        self.pred_y = self.X@self.vbeta
        
        return self.pred_y
    
    
    def standard_errors(self):
        """
        takes no argument, but needs self.vbeta to be defined, so you need to fit the model first

        Returns
        -------
        vector of standard errors

        """
        import numpy as np
        self.errors = self.Y - self.predict()
        self.dSigmaHat = (1/len(self.errors))*np.sum(self.errors**2)
        self.SE_OLS = np.sqrt(np.diag(self.dSigmaHat * np.linalg.inv(self.X.T@self.X)))
        
        return self.SE_OLS
    
    def desc(self):
        """
        Takes no argument, this function gives all OLS related output.
        Includes beta estimates, standard errors, significance and top ten funny shrek moments (you won't believe number 1!)

        Returns
        -------
        None.

        todo:
            - make table and put in ests, s.e.'s and tstats
            - R squared, n of obs, 
        """
        import numpy as np
        import pandas as pd
        
        try:
            table = np.array([self.vbeta, 
                              self.SE_OLS, 
                              self.vbeta/self.SE_OLS])
        except: 
            self.fit()
            self.predict()
            self.standard_errors()
            table = np.array([self.vbeta, self.SE_OLS, self.vbeta/self.SE_OLS])

        table = pd.DataFrame(table)
        
        if self.const == 'yes':
            list_of_cols = ['const']
        else:
            list_of_cols = []
        
        list_of_cols = list_of_cols + self.variable_names
        table.columns = list_of_cols
        table.index = ['ests', 's.e.', 'tstat']
        
        #R_squared = 
        print(table)
        
        
        return table
        
        

#%% testing the code below...



list_of_ticks = ['AAPL', 'MSFT', 'TSLA']
startdate = "2017-03-21"
enddate = "2020-03-21"


test = Yahoo(list_of_ticks, startdate, enddate, 'close')

vY = test.iloc[1:,0]
mX = test.iloc[1:,1:]

#model = OLS(vY, mX, 'yes')
model = OLS(vY, mX, 'yes')
model.fit()
model.standard_errors()
table_test = model.desc()


