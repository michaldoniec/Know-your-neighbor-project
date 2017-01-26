class Voivodeship:
    '''Class containing data pertaining to Voivodeships (names, numbers), its counts (names, numbers, types)
    and its communities (names, numbers, types).'''

    VOIVODESHIPS = []  # all Voivodeships

    def __init__(self,voivodeship_number, voivodeship_name):
        '''Creating instance of Voivodeship class containing list of counts belonging to the given
        Voivodeship's instance.'''

        self.voivodeship_number = voivodeship_number
        self. voivodeship_name = voivodeship_name
        self.counts = []
        self.VOIVODESHIPS.append(self)  # adding voivodeship instance to list of all created voivodeship instances


    def add_count(self,count_obj):
        '''Methods that adds instance of Count class to instance of Voivodeship class.'''

        self.counts.append(count_obj)


    def statistics(self, voivodship_name):
        '''Method that extract statistical data about given instance of Voivodeship class.'''

        counts_counter = 0  # counters for each type of community and count
        municipal_communities_counter = 0
        agricultural_communities_counter = 0
        municipal_agricultural_communities_counter = 0
        agricultural_areas_counter = 0
        towns_counter = 0
        city_counts_counter = 0

        municipal_community = '1'  # numbers from csv file that indicate type of community
        agricultural_community = '2'
        municipal_agricultural_community = '3'
        agricultural_area = '5'
        town = '4'

        for voivodeship in self.VOIVODESHIPS:
            if voivodeship.voivodeship_name == voivodship_name:
                for count in voivodeship.counts:
                    counts_counter = len(voivodeship.counts)

                    if count.count_type == 'miasto na prawach powiatu':
                        city_counts_counter += 1

                    for community in count.communities:
                        if community.type_of_community == municipal_community:
                            municipal_communities_counter += 1

                        elif community.type_of_community == agricultural_community:
                            agricultural_communities_counter += 1

                        elif community.type_of_community == municipal_agricultural_community:
                            municipal_agricultural_communities_counter += 1

                        elif community.type_of_community ==  agricultural_area:
                            agricultural_areas_counter += 1

                        elif community.type_of_community == town:
                            towns_counter += 1

                        else:
                            None

            return (str(counts_counter), 'powiaty', str(municipal_communities_counter), 'gmina miejska',
                    str(agricultural_communities_counter), 'gmina wiejska',
                    str(municipal_agricultural_communities_counter), 'gmina miejsko-wiejska',
                    str(agricultural_areas_counter), 'obszar wiejski', str(towns_counter), 'miasto',
                    str(city_counts_counter), 'miasto na prawach powiatu')  # changing output into string so it can be
                                                                            # processed by instance of Display class


    def longest_names(self, voivodship_name):
        '''Method that indicates 3 communities from given voivodeship that are cities, with longest names.'''

        community_names = []
        city = '4'

        for voivodeship in self.VOIVODESHIPS:
            if voivodeship.voivodeship_name == voivodship_name:
                for count in voivodeship.counts:
                    for community in count.communities:
                        if community.type_of_community == city:  # determining whether community is a city
                         community_names.append(community.community_name)


        longest_names = sorted(community_names, key = lambda name: len(name), reverse = True )

        return (longest_names[0], longest_names[1], longest_names[2])

    def county_largest_number_communities(self, voivodeship_name):
        '''Method that indicates county  from a given voivodeship with largest number of communities.'''

        largest_number_communities = '0'
        county_largest_number_communities = None
        for voivodeship in self.VOIVODESHIPS:
            if voivodeship.voivodeship_name == voivodeship_name:
                for county in voivodeship.counts:
                    if county.communities[-1].community_number > largest_number_communities:
                        largest_number_communities = county.communities[-1].community_number
                        county_largest_number_communities = county.count_name

        return county_largest_number_communities

    def locations_belonging_to_more_categories(self,voivodeship_name):
        '''Method that indicates locations from a given voivodeship belonging to more categories.'''

        locations_belonging_to_many_categories = []
        municipal_agricultural_community = '3'

        for voivodeship in self.VOIVODESHIPS:
            if voivodeship.voivodeship_name == voivodeship_name:
                for count in voivodeship.counts:
                    if count.count_type == 'miasto na prawach powiatu':
                        locations_belonging_to_many_categories.append(count.count_name)
                    for community in count.communities:
                        if community.type_of_community == municipal_agricultural_community:
                                locations_belonging_to_many_categories.append(community.community_name)

        return locations_belonging_to_many_categories

    def advanced_search(self, searched_location):
        '''Method that search for location based on the given name or part of given name.'''

        results = []

        for voivodeship in self.VOIVODESHIPS:
            for county in voivodeship.counts:
                if searched_location in county.count_name:
                    count = [county.count_name,county.count_type]
                    results.append(count)

                for community in county.communities:
                    if searched_location in community.community_name:
                        community = [community.community_name, community.type_of_community]
                        results.append(community)

        for element in results:
            if element[1] == '1':
                element[1] = 'gmina miejska'

            elif element[1] == '2':
                element[1] = 'gmina wiejska'

            elif element[1] == '3':
                element[1] = 'gmina miejsko-wiejska'

            elif element[1] == '4':
                element[1] = 'miasto'

            elif element[1] == '5':
                element[1] = 'obszar wiejski'

            elif element[1] == '9':
                element[1] = 'delegatura'

        if results:
            return sorted(results)

        else:
            return None


    def __str__(self):
        '''Method that returns basic information about instance of Voivodeship class.'''

        return '{},{}'.format(self.voivodeship_number, self.voivodeship_name)


    @classmethod
    def loading_data_from_file(cls, filename):
        '''Method that loads data from csv file and based on that data creates instances of Voivodeship class, instances
         of Count class and instances of Community class.'''

        with open(filename, 'r') as data_file:
            for line in data_file:
                row_data = []
                data_list_from_file = line.strip('\n').split('\t')

                for data in data_list_from_file:
                    if data:
                        row_data.append(data)

                if 'rgmi' in row_data:  # to avoid creating instances of classes using data from heading of csv file
                    pass

                elif len(row_data) == 3:
                    created_voivodeship = Voivodeship(row_data[0], row_data[1])

                elif len(row_data) == 4:
                    created_count = Count(row_data[1], row_data[2], row_data[3])

                    if row_data[0] == created_voivodeship.voivodeship_number:
                        created_voivodeship.add_count(created_count)        #

                elif len(row_data) == 6:
                    if row_data[1] == created_count.count_number:
                        created_count.add_community(Community(row_data[2], row_data[4],row_data[3]))


class Count:
    '''Class that serves for creating instances containing data pertaining to counts (numbers, names, types, communities
     within given count).'''

    def __init__(self, count_number, count_name, count_type):
        '''Method that creates instance of count class containing also list of all instances of Community class
        within given instance of Count class.'''

        self.count_number =  count_number
        self.count_name = count_name
        self.count_type = count_type
        self.communities = []


    def add_community(self, community_obj):
        '''Method that adds intances'of Community class into instance of Count class.'''

        self.communities.append(community_obj)

    def __str__(self):
        '''Method that returns basic information about instance of Count class.'''

        return '{}, {}, {}'.format(self.count_number, self.count_name, self.count_type)



class Community:
    '''Class that serves for creating instances containing basic data pertaining to community (number, name, type).'''

    def __init__(self,community_number, community_name, type_of_community):
        self.community_number = community_number
        self.community_name = community_name
        self.type_of_community = type_of_community

    def __str__(self):
        '''Method that returns basic information about instance of Community class.'''

        return '{}, {}, {}'.format(self.community_number,self.community_name, self.type_of_community)







