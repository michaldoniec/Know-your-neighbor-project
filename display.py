class Display:
    '''Class that serves for displaying information returned by methods used by instances of other classes.'''

    def __init__(self, headings, content):
        '''Method that creates instance of Display class.'''

        self.headings = headings
        self.content = content


    def get_width_columns(self):
        '''Determines width of columns necessary for table of data so that all content fits within column.'''

        column_width = []

        element_from_list = None
        for heading in self.headings:
            for element in self.content:
                if element.isdigit():
                    element_from_list = 'number'


                if len(heading) > len(element):
                    column_width.append(len(heading) + 2)


                else:
                    column_width.append(len(element) + 2)

        if element_from_list == 'number':
            columns_width =  [6] + sorted(column_width)[-len(self.headings):]

        else:
            columns_width = sorted(column_width)[-len(self.headings):]


        return (columns_width)


    def get_table_many_headings_many_columns(self,column_width,total_width):
        '''Method that returns table with many headings and many columns.'''

        output = ''

        output += '/' + ('-' * (total_width + 1)) + '\\' + '\n'  # adding headings

        for heading in range(len(self.headings)):
            output += '|{0:^{1}}|'.format(self.headings[heading], column_width[heading])  # adding headings
        output += '\n'
        output += ('-' * (total_width + 3))
        output += '\n'
        row = 0

        while row < len(self.content):  # adding rows

            for heading in range(len(self.headings)):
                output += '|{0:^{1}}|'.format(self.content[row], column_width[heading])

                row += 1

            output += '\n'
            output += ('-' * (total_width + 3))
            output += '\n'
        output += '\\' + ('-' * (total_width + 1)) + '/'

        return output.replace('||', '|')

    def get_table_one_heading_two_columns(self,column_width,total_width):
        '''Method that returns table with one heading and two columns.'''

        output = ''
        output += '/' + ('-' * (total_width + column_width[0] + 1)) + '\\' + '\n'  # adding heading
        spaces_lines = 3
        output += '|{0:^{1}}|'.format(self.headings[0], column_width[0] + 1 + total_width)
        output += '\n'
        output += ('-' * (total_width + column_width[0] + spaces_lines))
        output += '\n'
        row = 0
        columns = 2


        while row < len(self.content):  # adding rows with 2 columns
            try:
                for heading in range(columns):
                    output += '|{0:^{1}}|'.format(self.content[row], column_width[heading] + spaces_lines)

                    row += 1

                output += '\n'
                output += ('-' * (total_width + column_width[0] + 3))
                output += '\n'
            except IndexError:
                output += '\n'
                output += ('-' * (total_width + column_width[0] + 3))
                output += '\n'
                break

        output += '\\' + ('-' * (total_width + column_width[0] + 1)) + '/'

        return output.replace('||', '|')

    def get_table_one_column(self, column_width,total_width):
        '''Method that returns table with one column and one heading.'''

        output = ''
        output += '/' + ('-' * (total_width + 1)) + '\\' + '\n'

        output += '|{0:^{1}}|'.format(self.headings[0], column_width[0] + 1) # adding heading
        output += '\n'
        output += ('-' * (total_width + 3))
        output += '\n'
        row = 0
        column = 1
        while row < len(self.content):

            for heading in range(column):
                output += '|{0:^{1}}|'.format(self.content[row], column_width[heading] + 1)

                row += 1

            output += '\n'
            output += ('-' * (total_width + 3))
            output += '\n'
        output += '\\' + ('-' * (total_width + 1)) + '/'

        return output.replace('||', '|')


    def get_table(self, option):
        '''Prints out table with information about territorial units.'''

        column_width = self.get_width_columns()

        total_width = 0
        for element in column_width:
            total_width += element


        if option == '1':
            return self.get_table_many_headings_many_columns(column_width,total_width)

        elif option == '2':
            return self.get_table_one_heading_two_columns(column_width,total_width)

        elif option == '3':
            return self.get_table_one_column(column_width,total_width)
