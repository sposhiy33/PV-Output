# Geographic Optimization of PV Units in the Contiguous USA

The goal of this project is to model the energy generation of PV Units across the contiguous USA by taking into account meteorlogical and economic factors. 

First a meterological model will be built that takes into account the following variables: Irridiance (energy of solar radiation in one square meter), Temperature, Humidity, and Wind Speed. Using a existing PV generation data, a machine-learning based multiple regression model will be trained to predict PV generation when given the sufficient data.

Next an economical model will be produced that calculates the cost (in $) of installing PV units at a certain location. This model takes into account the location's proximity to the electrical grid and the capacity of the eletrical grid to support new generation sites.

In order to run the model, the follwing packages must be installed IN THE SAME ENVIRONMENT: \n
(1) [Numpy](https://numpy.org/) \n 
(2) [Pandas](https://pandas.pydata.org/) \n 
(3) [GeoPandas](https://geopandas.org/en/stable/) \n 
(4) [MatPlotLib](https://matplotlib.org/) \n
(5) [SciKit-Learn](https://scikit-learn.org/stable/) \n
(6) [Shapely](https://pypi.org/project/Shapely/) \n 
(7) [Seaborn](https://seaborn.pydata.org/) \n
