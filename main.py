import sys
from teritorial_units import *


def menu():
    print('''What would you like to do:
   (1) List statistics
   (2) Display 3 cities with longest names
   (3) Display county's name with the largest number of communities
   (4) Display locations, that belong to more than one category
   (5) Advanced search
   (0) Exit program''')

def options(option):

    Malopolska = Voivodeship.VOIVODESHIPS[0]

    if option == '1':
        display_statistics = Display(['Małopolska'], Malopolska.statistics('MAŁOPOLSKIE'))
        print(display_statistics.get_table('2'))

    elif option == '2':
        display_longest_names = Display(['Trzy powiaty z najdłuższą nazwą: '], Malopolska.longest_names('MAŁOPOLSKIE'))
        print(display_longest_names.get_table('3'))

    elif option == '3':
        display_county_name = Display(['Powiat z największą ilością gmin: '], [Malopolska.county_largest_number_communities('MAŁOPOLSKIE')])
        print(display_county_name.get_table('3'))

    elif option == '4':
        display_locations_many_categories = Display(['Lokacje należące do więcej niż jednej kategorii: '],
                                                    Malopolska.locations_belonging_to_more_categories('MAŁOPOLSKIE'))

        print(display_locations_many_categories.get_table('3'))

    elif option == '5':
        searched_location = input('Please provide name of the location you look for or part of the name: ')

        search_results = Malopolska.advanced_search(searched_location)

        if search_results:

            founded_location = []
            for location in search_results:
                founded_location += location

            display_location_advanced_search = Display(['LOCATION', 'TYPE'], founded_location)
            print(display_location_advanced_search.get_table('1'))

        else:
            print('There is no such location.')

    elif option == '0':
        sys.exit()

    else:
        print('There is no such option.')

def main():
    Voivodeship.loading_data_from_file('malopolska.csv')

    Malopolska = Voivodeship.VOIVODESHIPS[0]

    while True:
        menu()
        option = input('Choose your option: ')
        options(option)


if __name__ == '__main__':
    main()