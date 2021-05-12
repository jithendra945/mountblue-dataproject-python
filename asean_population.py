"""
ASEAN countries population for the year 2014
"""
# importing the required libraries
import csv
import matplotlib.pyplot as plt


def addlabels(length, population):
    """
    for Adding labels on top of bar plot
    """
    for value in range(length):
        plt.text(value, population[value], population[value], ha="center")


def asean_population():
    """
    Plotting bar for asean countries for the year 2014
    """
    with open('datasets/population_estimates_csv.csv', 'r') as file:
        population_data = list(csv.DictReader(file, delimiter=','))
        file.close()

    with open('datasets/asean_countries.csv', 'r') as file:
        asean_list = [row['Asean countries'] for row in csv.DictReader(file)]
        file.close()

    population = []
    for row in population_data:
        if row['Year'] == "2014" and row['Region'] in asean_list:
            population.append(int(float(row['Population'])))

    # changing names to shorter one's
    # countries_length = len(asean_list)
    for key, value in enumerate(asean_list):
        if value == "Brunei Darussalam":
            asean_list[key] = "Brunei"
        elif value == "Lao People's Democratic Republic":
            asean_list[key] = "Laos"

    # Passing the parameters to the bar function,
    # this is the main function which creates the bar plot
    plt.bar(asean_list, population)
    addlabels(len(asean_list), population)
    plt.title('ASEAN countries population for the year 2014')
    plt.xlabel('Countries')
    plt.ylabel('Population')
    plt.xticks(rotation=25)

    # Displaying the bar plot
    plt.show()


if __name__ == '__main__':
    asean_population()
