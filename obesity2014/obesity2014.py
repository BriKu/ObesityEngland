import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data source: 
# https://www.data.gov.uk/dataset/a7fb45df-7566-488b-80d8-a5dd5e52ff32/statistics-on-obesity-physical-activity-and-diet-england
data = pd.ExcelFile("obes-phys-acti-diet-eng-2014-tab.xls")
print(data.sheet_names)

#Read 2nd section, by age
data_age = data.parse('7.2', skiprows=4, skipfooter=14)

#Rename Unnamed to Year
data_age.rename(columns={'Unnamed: 0': 'Year'}, inplace=True)

#Drop empties and reset index
data_age.dropna(inplace=True)
data_age.set_index('Year',inplace=True)

print(data_age)

#Plot
#data_age.plot()
#plt.show()

#Plotting everything causes total to override everything
#Drop the total column and plot
data_age_minus_total = data_age.drop('Total', axis=1)
data_age_minus_total.plot()
plt.show()

plt.close()
#Plot children vs adults
data_age['Under 16'].plot(label="Under 16")
data_age['35-44'].plot(label="35-44")
plt.legend(loc="upper right")
plt.show()

#Extrapolate graph to predict future for children
kids_values = data_age['Under 16'].values
x_axis = range(len(kids_values))
poly_degree = 4      #swith to 3 to compare
curve_fit = np.polyfit(x_axis,kids_values,poly_degree)
poly_interp = np.poly1d(curve_fit)
poly_fit_values = []

for i in range(len(x_axis)):
    poly_fit_values.append(poly_interp(i))

plt.close()
plt.plot(x_axis, poly_fit_values, "-r", label = "Fitted")
plt.plot(x_axis, kids_values, "-b", label = "Orig")

plt.legend(loc="upper right")
plt.show()

plt.close()

#plt.plot(x_axis, poly_fit_values, "-r", label = "Fitted")
plt.plot(x_axis, kids_values, "-b", label = "Orig")

x_axis2 = range(15)

poly_fit_values = []
for i in range(len(x_axis2)):
    poly_fit_values.append(poly_interp(i))

plt.plot(x_axis2, poly_fit_values, "-g", label = "Prediction")
plt.legend(loc="upper right")
plt.show()