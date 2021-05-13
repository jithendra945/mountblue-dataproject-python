"""
Total SAARC population vs year
"""
# importing the required libraries
import csv
from collections import defaultdict
import matplotlib.pyplot as plt


def addlabels(length, population):
    """
    for Adding labels on top of bar plot
    """
    for value in range(length):
        plt.text(value, population[value], population[value], ha="center")


def total_saarc_population():
    """
    Total SAARC population vs year
    """
    with open('datasets/population_estimates_csv.csv', 'r') as file:
        population_data = list(csv.DictReader(file, delimiter=','))
        file.close()

    with open('datasets/saarc_countries.csv', 'r') as file:
        saarc_list = [row['saarc countries'] for row in csv.DictReader(file)]
        file.close()

    years = [
             "2005", "2006", "2007", "2008",
             "2009", "2010", "2011", "2012",
             "2013", "2014", "2015"
            ]
    saarc = defaultdict(int)

    for row in population_data:
        if row['Region'] in saarc_list:
            if row['Year'] in years:
                saarc[row['Year']] += int(float(row['Population']))

    year = list(saarc.keys())
    population = list(saarc.values())

    # Passing the parameters to the bar function,
    # this is the main function which creates the bar plot
    plt.bar(year, population)
    addlabels(len(year), population)
    plt.title('Total SAARC population vs year')
    plt.xlabel('Years')
    plt.ylabel('Population')
    plt.xticks(rotation=25)

    # Displaying the bar plot
    plt.show()


if __name__ == '__main__':
    total_saarc_population()
