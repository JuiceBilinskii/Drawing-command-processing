class MessageParser:
    def __init__(self):
        self.__message = None
        self.__command_types = {
            'cd': 0,
            'dp': 2,
            'dl': 4,
            'dr': 4,
            'fr': 4,
            'de': 4,
            'fe': 4
        }
        self.__parsed_commands = []
        self.__command_attributes = []

        self.__start_symbol = '%'
        self.__end_symbol = '@'
        self.__command_size = 2  # =2
        self.__num_attribute_limit = 4  # <4
        self.__colour_attribute_size = 6  # =6
        self.__numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        self.__24bit_symbols = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value: str):
        self.__message = value

    def parse(self):
        result = self.__state_1(index=0)

        if result:
            result = self.__parsed_commands
        else:
            print('Command specification is violated')

        self.__parsed_commands = []
        return result

    def __state_1(self, index):
        if self.__message[index] == self.__start_symbol:
            index += 1
            return self.__state_2(index)
        else:
            return False

    def __state_2(self, index):
        if self.__message[index + self.__command_size] == '_' and self.__message[index:index + self.__command_size] in self.__command_types:
            self.__command_attributes.append(self.__message[index:index + self.__command_size])
            num_of_attributes = self.__command_types[self.__message[index:index + self.__command_size]]
            index += self.__command_size + 1
            return self.__state_3(index, num_of_attributes)
        else:
            return False

    def __state_3(self, index, num_of_attributes):
        for i in range(num_of_attributes):
            for j in range(self.__num_attribute_limit):
                if self.__message[index + j] == '_':
                    if j == 0:
                        return False
                    else:
                        command_num_attribute = int(self.__message[index:index+j])
                        self.__command_attributes.append(command_num_attribute)
                        index += j + 1
                        break

                if self.__message[index + j] not in self.__numbers:
                    return False
                if j == 3 and self.__message[index + j] != '_':
                    return False

        return self.__state_4(index)

    def __state_4(self, index):
        for i in range(self.__colour_attribute_size):
            if self.__message[index + i] not in self.__24bit_symbols:
                return False
        self.__command_attributes.append(self.__message[index:index+6])
        index += 6
        return self.__state_5(index)

    def __state_5(self, index):
        if self.__message[index] != self.__end_symbol:
            return False

        self.__parsed_commands.append(self.__command_attributes)
        self.__command_attributes = []

        if index + 1 == len(self.__message):
            return True
        else:
            index += 1
            return self.__state_1(index)
