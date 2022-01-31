# -*- coding: utf-8 -*-
"""
Main file to create my own package...

Created on Mon Jan 31 15:57:00 2022

@author: MauritsOever
https://github.com/MauritsOever
"""

# start this file with creating a class
# so this package is only able to do some basic financially related stuff...
# https://realpython.com/python3-object-oriented-programming/

# dependencies right now:


class maupy:
    
    def Yahoo(self, list_of_ticks, startdate, enddate):
        '''
        Parameters
        ----------
        list_of_ticks : list of strings, tickers
        startdate     : string
        enddate       : string

        Returns
        -------
        dataframe of stock returns and prices based on tickers and date

        '''
        print(list_of_ticks, startdate, enddate)
        
        return 'test again'
    
    def OLS(self, vY, mX):
        """
        Parameters
        ----------
        vY : vector, dependent variable
        mX : 

        Returns
        -------
        None.

        """    
        vbeta = 3 
        return vbeta
    
    

#%% testing the code below...

test = maupy()
vbeta = test.OLS('dkf', 'df')
test.Yahoo('list', 'string1', 'string2')



