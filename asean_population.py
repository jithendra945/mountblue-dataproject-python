"""
ASEAN countries population for the year 2014
"""
# importing the required libraries
import csv
import matplotlib.pyplot as plt

country = []
population = []


def addlabels(x_value, y_value):
    """
    Adding labels on top of bar plot
    """
    for j in range(len(x_value)):
        plt.text(j, y_value[j], y_value[j], ha="center")


with open('datasets/population_estimates_csv.csv', 'r') as population_estimate:
    population_data = list(csv.reader(population_estimate, delimiter=','))
    region_index = population_data[0].index('Region')
    year_index = population_data[0].index('Year')
    population_index = population_data[0].index('Population')
    with open('datasets/asean_countries.csv', 'r') as asean_countries:
        asean_data = list(csv.reader(asean_countries, delimiter='\n'))
        asean_list = []
        for i in range(1, len(asean_data)):
            asean_list.append(asean_data[i][0])
        for row in population_data:
            if row[year_index] == "2014":
                if row[region_index] in asean_list:
                    country.append(row[region_index])
                    population.append(int(float(row[population_index])))
        asean_countries.close()
    population_estimate.close()

# changing names to shorter one's
COUNTRY_LENGTH = len(country)
for c_value in range(COUNTRY_LENGTH):
    if country[c_value] == "Brunei Darussalam":
        country[c_value] = "Brunei"
    elif country[c_value] == "Lao People's Democratic Republic":
        country[c_value] = "Laos"

# Passing the parameters to the bar function,
# this is the main function which creates the bar plot
plt.bar(country, population)
addlabels(country, population)
plt.title('ASEAN countries population for the year 2014')
plt.xlabel('Countries')
plt.ylabel('Population')
plt.xticks(rotation=25)

# Displaying the bar plot
plt.show()
