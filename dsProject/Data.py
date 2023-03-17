from pickle import FALSE
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Read datasource#
data = pd.read_csv('C:/Users/giova/projectsPythonDatascience/dsProject/files/vehicles.csv', sep=',', low_memory=False, dtype='unicode')

# Clear properties not essential for analytics#
data.drop('barrelsA08', axis=1, inplace=True)
data.drop('charge120', axis=1, inplace=True)
data.drop('charge240', axis=1, inplace=True)
data.drop('city08U', axis=1, inplace=True)
data.drop('cityA08', axis=1, inplace=True)
data.drop('cityA08U', axis=1, inplace=True)
data.drop('cityCD', axis=1, inplace=True)
data.drop('cityE', axis=1, inplace=True)
data.drop('cityUF', axis=1, inplace=True)
data.drop('co2', axis=1, inplace=True)
data.drop('co2A', axis=1, inplace=True)
data.drop('co2TailpipeAGpm', axis=1, inplace=True)
data.drop('comb08U', axis=1, inplace=True)
data.drop('combA08', axis=1, inplace=True)
data.drop('combA08U', axis=1, inplace=True)
data.drop('combE', axis=1, inplace=True)
data.drop('combinedCD', axis=1, inplace=True)
data.drop('combinedUF', axis=1, inplace=True)
data.drop('engId', axis=1, inplace=True)
data.drop('eng_dscr', axis=1, inplace=True)
data.drop('feScore', axis=1, inplace=True)
data.drop('fuelCostA08', axis=1, inplace=True)
data.drop('fuelType1', axis=1, inplace=True)
data.drop('ghgScore', axis=1, inplace=True)
data.drop('ghgScoreA', axis=1, inplace=True)
data.drop('highway08U', axis=1, inplace=True)
data.drop('highwayA08', axis=1, inplace=True)
data.drop('highwayA08U', axis=1, inplace=True)
data.drop('highwayCD', axis=1, inplace=True)
data.drop('highwayE', axis=1, inplace=True)
data.drop('highwayUF', axis=1, inplace=True)
data.drop('hlv', axis=1, inplace=True)
data.drop('hpv', axis=1, inplace=True)
data.drop('id', axis=1, inplace=True)
data.drop('lv2', axis=1, inplace=True)
data.drop('lv4', axis=1, inplace=True)
data.drop('mpgData', axis=1, inplace=True)
data.drop('phevBlended', axis=1, inplace=True)
data.drop('pv2', axis=1, inplace=True)
data.drop('pv4', axis=1, inplace=True)
data.drop('range', axis=1, inplace=True)
data.drop('rangeCity', axis=1, inplace=True)
data.drop('rangeCityA', axis=1, inplace=True)
data.drop('rangeHwy', axis=1, inplace=True)
data.drop('rangeHwyA', axis=1, inplace=True)
data.drop('UCity', axis=1, inplace=True)
data.drop('UCityA', axis=1, inplace=True)
data.drop('UHighway', axis=1, inplace=True)
data.drop('UHighwayA', axis=1, inplace=True)
data.drop('guzzler', axis=1, inplace=True)
data.drop('trans_dscr', axis=1, inplace=True)
data.drop('tCharger', axis=1, inplace=True)
data.drop('sCharger', axis=1, inplace=True)
data.drop('atvType', axis=1, inplace=True)
data.drop('fuelType2', axis=1, inplace=True)
data.drop('rangeA', axis=1, inplace=True)
data.drop('evMotor', axis=1, inplace=True)
data.drop('mfrCode', axis=1, inplace=True)
data.drop('c240Dscr', axis=1, inplace=True)
data.drop('charge240b', axis=1, inplace=True)
data.drop('c240bDscr', axis=1, inplace=True)
data.drop('createdOn', axis=1, inplace=True)
data.drop('modifiedOn', axis=1, inplace=True)
data.drop('startStop', axis=1, inplace=True)
data.drop('phevCity', axis=1, inplace=True)
data.drop('phevHwy', axis=1, inplace=True)
data.drop('phevComb', axis=1, inplace=True)

# Verify and clear null or empty values#
data.isnull().sum()
data = data[~data.cylinders.isnull()].copy()
data = data[~data.displ.isnull()].copy()
data = data[~data.trany.isnull()].copy()
ValueDrive = '4-Wheel or All-Wheel Drive'
data.drive.fillna(ValueDrive, inplace=True)
data.isnull().sum()

# Create database file in format csv with data filtered#
df = pd.DataFrame(data)
df.to_csv('C:/Users/giova/projectsPythonDatascience/dsProject/filesclearDatabase/vehicles_filtered.csv')

#ANALYSIS EXPLORATORY

# Some Categorical Unordered Uni variate Analysis, graphs comments#

# data.fuelType.value_counts(normalize=True)#
# data.fuelType.value_counts(normalize=True).plot.barh()#
# plt.show()#

# data.make.value_counts(normalize=True)#
# data.make.value_counts(normalize=True).plot.barh()#
# plt.show()#

# data.model.value_counts(normalize=True)#
# data.model.value_counts(normalize=True).plot.barh()#
# plt.show()#

# plt.scatter(data.fuelType, data.trany, label="stars", color="green", marker=".", s=30)#
# plt.xlabel('x - make')#
# plt.ylabel('y - model')#
# plt.show()#

# data.fuelType.value_counts(normalize=True)#
# data.fuelType.value_counts(normalize=True).plot.pie()#
# plt.show()#


#%%
