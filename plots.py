import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import plotly.express as px 
import numpy as np
from plotly.offline import init_notebook_mode, iplot
from plotly.tools import FigureFactory as FF

import pandas as pd 
import numpy as np
import adjustText as aT

def dataindia():


    df_cases=pd.read_csv('https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv')
    df_deaths=pd.read_csv('https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_deaths_global.csv&filename=time_series_covid19_deaths_global.csv')


    # In[3]:


    df_cases=df_cases[df_cases['Country/Region']=='India']
    df_deaths=df_deaths[df_deaths['Country/Region']=='India']
    df_cases=df_cases.drop(columns=['Province/State', 'Lat','Long'])
    df_deaths=df_deaths.drop(columns=['Province/State', 'Lat','Long'])
    df_cases.iloc[0]


    # In[4]:


    cases_list=df_cases.iloc[0, :].tolist()
    del cases_list[0]
    deaths_list=df_deaths.iloc[0, :].tolist()
    del deaths_list[0]
    Dates=list(df_cases.columns.values)
    del Dates[0]
    return deaths_list,cases_list,Dates

