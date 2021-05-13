"""
Total ASEAN countries population for the years 2005 to 2014
"""
# importing the required libraries
import csv
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt


def total_asean_population():
    """
    Total ASEAN countries population for the years 2005 to 2014
    """
    with open('datasets/population_estimates_csv.csv', 'r') as file:
        population_data = list(csv.DictReader(file, delimiter=','))
        file.close()

    with open('datasets/asean_countries.csv', 'r') as file:
        asean_list = [row['Asean countries'] for row in csv.DictReader(file)]
        file.close()

    years = [
             "2005", "2006", "2007",
             "2008", "2009", "2010",
             "2011", "2012", "2013", "2014"
            ]
    population = defaultdict(list)

    for row in population_data:
        if row['Region'] in asean_list and row['Year'] in years:
            population[row['Region']].append(int(float(row['Population'])))

    x_tick = np.arange(len(asean_list))
    width = 0.075  # the width of the bars

    figure, array_of_axes = plt.subplots()
    array_of_axes.bar(x_tick - 0.3, population['Brunei Darussalam'],
                      width, label='Brunei')
    array_of_axes.bar(x_tick - 0.225, population['Cambodia'],
                      width, label='Cambodia')
    array_of_axes.bar(x_tick - 0.15, population['Indonesia'],
                      width, label='Indonesia')
    array_of_axes.bar(x_tick - 0.075,
                      population["Lao People's Democratic Republic"],
                      width, label='Loas')
    array_of_axes.bar(x_tick, population['Malaysia'],
                      width, label='Malaysia')
    array_of_axes.bar(x_tick + 0.075, population['Myanmar'],
                      width, label='Myanmar')
    array_of_axes.bar(x_tick + 0.15, population['Philippines'],
                      width, label='Philippines')
    array_of_axes.bar(x_tick + 0.225, population['Singapore'],
                      width, label='Singapore')
    array_of_axes.bar(x_tick + 0.3, population['Thailand'],
                      width, label='Thailand')
    array_of_axes.bar(x_tick + 0.375, population['Viet Nam'],
                      width, label='Vietnam')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    array_of_axes.set_xlabel('Years')
    array_of_axes.set_ylabel('Population')
    array_of_axes.set_title('ASEAN countries population')
    array_of_axes.set_xticks(x_tick)
    array_of_axes.set_xticklabels(years)
    array_of_axes.legend()
    figure.tight_layout()
    # Displaying the bar plot
    plt.show()


if __name__ == '__main__':
    total_asean_population()
