import sys
from teritorial_units import Voivodeship, Count, Community
from display import Display


def menu():
    '''Function that prints out menu of the program.'''

    print('''What would you like to do:
   (1) List statistics
   (2) Display 3 cities with longest names
   (3) Display county's name with the largest number of communities
   (4) Display locations, that belong to more than one category
   (5) Advanced search
   (0) Exit program''')


def options(option,choosen_voivodeship):
    '''Function that collects input and based on that input appropriate method from Voivodship class is initiated,
    instance of Display class is created and appropriate method from display class is initiated by the instance of this
    class..'''

    if option == '1':
        display_statistics = Display([choosen_voivodeship.voivodeship_name],
                                     choosen_voivodeship.statistics(choosen_voivodeship.voivodeship_name))
        print(display_statistics.get_table('2'))
        print('\n\n')

    elif option == '2':
        display_longest_names = Display(['Three counties with largest name: '],
                                        choosen_voivodeship.longest_names(choosen_voivodeship.voivodeship_name))

        print(display_longest_names.get_table('3'))
        print('\n\n')


    elif option == '3':
        display_county_name = Display(['County with largest number of communities: '],
                                      [choosen_voivodeship.county_largest_number_communities
                                       (choosen_voivodeship.voivodeship_name)])

        print(display_county_name.get_table('3'))
        print('\n\n')

    elif option == '4':
        display_locations_many_categories = Display(['Locations belonging to more than one category: '],
                                                    choosen_voivodeship.locations_belonging_to_more_categories
                                                    (choosen_voivodeship.voivodeship_name))

        print(display_locations_many_categories.get_table('3'))
        print('\n\n')

    elif option == '5':
        searched_location = input('Please provide name of the location you look for or part of the name: ')

        search_results = choosen_voivodeship.advanced_search(searched_location.title())

        if search_results:  # checking whether program contain data of such location

            founded_location = []
            for location in search_results:
                founded_location += location

            display_location_advanced_search = Display(['LOCATION', 'TYPE'], founded_location)
            print(display_location_advanced_search.get_table('1'))
            print('\n\n')

        else:
            print('There is no such location.')
            print('\n\n')

    elif option == '0':
        sys.exit()

    else:
        print('There is no such option.')
        print('\n\n')


def start_menu(choosen_voivodeship):
    '''Function that creates instance of Voivodeship class, initiates
    menu function and option functions, collects user input in term of choosen option.'''

    while True:
        menu()
        print('\n')
        option = input('Choose your option: ')
        options(option, choosen_voivodeship)


def main():
    '''Function that enables selection of Voivodeship.'''
    Voivodeship.loading_data_from_file('malopolska.csv')

    available_voivodships = ['Małopolskie']

    while True:
        user_choice = input('Please choose Voivodeship from Poland: ')

        if user_choice not in available_voivodships:
            print('Sorry we do not have data pertaining to this voivodeship. Please try again.')

        else:
            for voivodeship in range(len(Voivodeship.VOIVODESHIPS)):
                if Voivodeship.VOIVODESHIPS[voivodeship].voivodeship_name == user_choice.upper():
                    choosen_voivodeship = Voivodeship.VOIVODESHIPS[voivodeship]

                    print('\n')
                    start_menu(choosen_voivodeship)
                    break


if __name__ == '__main__':
    main()