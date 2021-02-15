import functionality


class CommandConverter:
    def __init__(self):
        self.__command_types = {
            'cd': functionality.ClearDisplay,
            'dp': functionality.DrawPixel,
            'dl': functionality.DrawLine,
            'dr': functionality.DrawRectangle,
            'fr': functionality.FillRectangle,
            'de': functionality.DrawEllipse,
            'fe': functionality.FillEllipse
        }
        self._commands = [

        ]

    def convert_command(self, parsed_attributes):
        command = list(parsed_attributes)
        if command[0] == b'cd':
            command[1] = '#' + parsed_attributes[1].decode()
        elif command[0] == b'dp':
            command.insert(3, parsed_attributes[1] + 1)
            command.insert(4, parsed_attributes[2])
            command[5] = '#' + parsed_attributes[5].decode()
        elif command[0] == b'dl':
            command[5] = '#' + parsed_attributes[5].decode()
        elif command[0] == b'dr':
            command[3] = parsed_attributes[3] + parsed_attributes[1]
            command[4] = parsed_attributes[4] + parsed_attributes[2]
            command[5] = '#' + parsed_attributes[5].decode()
        elif command[0] == b'fr':
            command[3] = parsed_attributes[3] + parsed_attributes[1]
            command[4] = parsed_attributes[4] + parsed_attributes[2]
            command[5] = '#' + parsed_attributes[5].decode()
        elif command[0] == b'de':
            command[1] = parsed_attributes[1] - parsed_attributes[3] // 2
            command[2] = parsed_attributes[2] - parsed_attributes[4] // 2
            command[3] = parsed_attributes[1] + parsed_attributes[3] // 2
            command[4] = parsed_attributes[2] + parsed_attributes[4] // 2
            command[5] = '#' + parsed_attributes[5].decode()
        elif command[0] == b'fe':
            command[1] = parsed_attributes[1] - parsed_attributes[3] // 2
            command[2] = parsed_attributes[2] - parsed_attributes[4] // 2
            command[3] = parsed_attributes[1] + parsed_attributes[3] // 2
            command[4] = parsed_attributes[2] + parsed_attributes[4] // 2
            command[5] = '#' + parsed_attributes[5].decode()

        return tuple(command)
