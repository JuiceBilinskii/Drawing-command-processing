class MessageParser:
    start_symbol = b'%'
    end_symbol = b'@'
    separator_symbol = b'_'

    num_size = 3
    color_size = 6

    cmd_clear_display = b'cd'
    cmd_draw_pixel = b'dp'
    cmd_draw_line = b'dl'
    cmd_draw_rectangle = b'dr'
    cmd_fill_rectangle = b'fr'
    cmd_draw_ellipse = b'de'
    cmd_fill_ellipse = b'fe'

    def __init__(self):
        self._command = None
        self._args = None
        self._error = False
        self._message = None

        self._commands = [
            (self.cmd_clear_display,
             self._parse_color),
            (self.cmd_draw_pixel,
             self._parse_number, self._parse_number, self._parse_color),
            (self.cmd_draw_line,
             self._parse_number, self._parse_number, self._parse_number, self._parse_number, self._parse_color),
            (self.cmd_draw_rectangle,
             self._parse_number, self._parse_number, self._parse_number, self._parse_number, self._parse_color),
            (self.cmd_fill_rectangle,
             self._parse_number, self._parse_number, self._parse_number, self._parse_number, self._parse_color),
            (self.cmd_draw_ellipse,
             self._parse_number, self._parse_number, self._parse_number, self._parse_number, self._parse_color),
            (self.cmd_fill_ellipse,
             self._parse_number, self._parse_number, self._parse_number, self._parse_number, self._parse_color)
        ]

    command = property(lambda self: self._command)
    args = property(lambda self: self._args)
    error = property(lambda self: self._error)
    message = property(lambda self: self._message)

    def _parse_number(self, text):
        result = None
        if text and len(text) <= self.num_size and text.isdigit():
            result = int(text)
        return result

    def _parse_color(self, text):
        result = None
        if (len(text) == self.color_size) and self._ishexnumber(text):
            result = text
        return result

    def _ishexnumber(self, text):
        hexdigits = b'01234567890abcdefABCDEF'
        return all(c in hexdigits for c in text)

    def parse(self, text):
        if (text[:1] != self.start_symbol) or (text[-1:] != self.end_symbol):
            self._error = True
            self._message = 'Not found begin or end char'
            return
        #
        text = text[1:-1]
        line = text.split(self.separator_symbol)
        if not line:
            self._error = True
            self._message = 'Empty command'
            return
        #
        for item in self._commands:
            if line[0] != item[0]:
                continue
            if len(item) != len(line):
                self._error = True
                self._message = 'Number of params for command %s must be %s' % (item[0], len(item) - 1)
                break
            #
            args = []
            for i, (t_arg, arg_parser) in enumerate(map(lambda x, y: (x, y), line[1:], item[1:])):
                arg = arg_parser(t_arg)
                if arg is not None:
                    args.append(arg)
                else:
                    self._error = True
                    self._message = 'Bad argument #%s %s' % (i, t_arg)
                    break
            if not self._error:
                self._command = item[0]
                self._args = tuple(args)
            break

        if (not self._error) and (self._command is None):
            self._error = True
            self._message = 'Command %s not found' % line[0]


def _test(text):
    parser = MessageParser()
    parser.parse(text)

    print('packet:', text)
    if parser.error:
        print('Error: ', parser.message)
    else:
        print('command:', parser.command, parser.args)


if __name__ == '__main__':
    _test(b'%cd_000000@')

    _test(b'%dp_100_200_000001@')
    _test(b'%dl_130_240_10_20_000001@')

    _test(b'%dr_100_200_300_300_000002@')
    _test(b'%fr_100_200_300_300_000003@')

    _test(b'%de_100_200_30_20_000004@')
    _test(b'%fe_100_200_40_50_000005@')

    _test(b'%c0_000000@')
    _test(b'%cd_000000')
    _test(b'cd_000000@')
    _test(b'%cd_12_000000@')
    _test(b'%fe_100_200_40_000005@')
    _test(b'%cd_00000w@')
    _test(b'%fe_100_a200_40_50_000005@')
