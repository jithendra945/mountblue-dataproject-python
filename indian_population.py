"""
Indian population over years
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


def indian_population():
    """
    Bar Plot of 'population of India' vs. years.
    """
    with open('datasets/population_estimates_csv.csv', 'r') as file:
        csv_list = list(csv.DictReader(file, delimiter=','))
        file.close()

    india = defaultdict(int)

    for row in csv_list:
        if row['Region'] == "India":
            india[row['Year']] = int(float(row['Population']))

    # taking the recent 10 years of data
    years = 10

    # passing the parameters to the bar function,
    # this is the main function which creates the bar plot
    plt.bar(list(india.keys())[-years:], list(india.values())[-years:])
    addlabels(years, list(india.values())[-years:])
    plt.title('Indian population over years')
    plt.xlabel('Years')
    plt.ylabel('Population')
    plt.xticks(rotation=25)

    # Displaying the bar plot
    plt.show()


if __name__ == '__main__':
    indian_population()
