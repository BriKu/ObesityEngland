import pandas as pd
import matplotlib.pyplot as plt

# Data source: 
# https://www.data.gov.uk/dataset/a7fb45df-7566-488b-80d8-a5dd5e52ff32/statistics-on-obesity-physical-activity-and-diet-england
data = pd.ExcelFile("obes-phys-acti-diet-eng-2016-tab.xlsx")
print(data.sheet_names)

#Read 1st section, by gender
data_gender = data.parse('Table 1', skiprows=3,skipfooter=14)

#Read 2nd section, by age
data_age = data.parse('Table 2', skiprows=3, skipfooter=14)

#Drop empties and reset index
data_gender.drop('Unnamed: 1', axis = 1, inplace = True)
data_gender.dropna(inplace=True)
data_gender.set_index('Year',inplace=True)

data_age.drop('Unnamed: 1', axis = 1, inplace = True)
data_age.dropna(inplace=True)
data_age.set_index('Year',inplace=True)

#Drop Unknown columns
data_gender.drop('Unknown', axis = 1, inplace = True)
data_age.drop('Unknown', axis = 1, inplace = True)

#Sort so that the most recent year is last
data_gender = data_gender.sort_index(ascending=True)
data_age = data_age.sort_index(ascending=True)

#Print tables
print(data_gender)
print(data_age)

#Plot without Total
data_gender_minus_total = data_gender.drop('All persons', axis = 1)
data_gender_minus_total.plot()
plt.show()
plt.close()

data_age_minus_total = data_age.drop('All ages', axis = 1)
data_age_minus_total.plot()
plt.show()
plt.close()

#Plot Adult vs Children
data_age['Under 16'].plot(label="Under 16")
data_age['35 to 44'].plot(label="35-44")
plt.legend(loc="upper right")
plt.show()
plt.close()

#Pi Chart by gender 2014/15
data_gender_2014_15 = data_gender_minus_total.iloc[-1]
print(data_gender_2014_15)
plt.pie(data_gender_2014_15, labels=data_gender_minus_total.columns)
plt.title("Male vs Female Obesity in 2014/15")
plt.show()

#Pi Chart by ages 2014/15
data_age_2014_15 = data_age_minus_total.iloc[-1]
print(data_age_2014_15)
plt.pie(data_age_2014_15, labels=data_age_minus_total.columns)
plt.title("Obesity in 2014/15 by Age")
plt.show()