import functionality


class CommandBuilder:
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

    def build_commands(self, parsed_attributes):
        commands = []
        for attributes in parsed_attributes:
            command = self.__command_types[attributes[0]]
            commands.append(command(*attributes[1:]))
        return commands
