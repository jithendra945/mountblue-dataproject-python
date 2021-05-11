"""
Indian population over years
"""
# importing the required libraries
import csv
import matplotlib.pyplot as plt

year = []
population = []


def addlabels(x_value, y_value):
    """
    Adding labels on top of bar plot
    """
    for j in range(len(x_value)):
        plt.text(j, y_value[j], y_value[j], ha="center")


with open('datasets/population_estimates_csv.csv', 'r') as file:
    my_list = list(csv.reader(file, delimiter=','))
    region_index = my_list[0].index('Region')
    year_index = my_list[0].index('Year')
    population_index = my_list[0].index('Population')
    for row in my_list:
        if row[region_index] == "India":
            year.append(row[year_index])
            population.append(int(float(row[population_index])))
    file.close()

# Passing the parameters to the bar function,
# this is the main function which creates the bar plot
# taking the last 10 years of data
plt.bar(year[-10:], population[-10:])
addlabels(year[-10:], population[-10:])
plt.title('Indian population over years')
plt.xlabel('Years')
plt.ylabel('Population')
plt.xticks(rotation=25)

# Displaying the bar plot
plt.show()
