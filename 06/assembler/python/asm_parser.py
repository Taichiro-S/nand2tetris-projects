class AsmParser:
    """Parses the .asm file and provides access to the components of the current command."""

    def __init__(self, asm_file_path):
        # Read the file and remove all the comments and white spaces
        with open(asm_file_path,'r', encoding='utf-8') as f:
            self.lines = f.readlines()
        for i,line in enumerate(self.lines):
            line = line.split()
            if len(line) > 0:
                line = line[0]
                if line == '' or (line[0] == '/' and line[1] == '/'):
                    line = None
            self.lines[i] = line
        self.lines = [line for line in self.lines if line is not None and line != []]
        print(self.lines)
        self.current_line_num = -1
        self.current_line = self.lines[self.current_line_num]

    def has_more_commands(self):
        self.current_line_num += 1
        return bool(self.current_line_num < len(self.lines))

    def advance(self):
        self.current_line = self.lines[self.current_line_num]

    def get_command_type(self):
        if self.current_line[0] == '@':
            return 'A_COMMAND'
        if self.current_line[0] == '(':
            return 'L_COMMAND'
        if self.current_line[0] is not None:
            return 'C_COMMAND'

    def get_symbol(self):
        if self.get_command_type() == 'A_COMMAND':
            return self.current_line[1:]
        if self.get_command_type() == 'L_COMMAND':
            return self.current_line[1:-1]

    def get_dest(self):
        # if self.get_command_type() == 'C_COMMAND':
        if '=' in self.current_line:
            return self.current_line.split('=')[0]
        if ';' in self.current_line:
            return 'null'

    def get_comp(self):
        # if self.get_command_type() == 'C_COMMAND':
        if '=' in self.current_line:
            return self.current_line.split('=')[1]
        if ';' in self.current_line:
            return self.current_line.split(';')[0]

    def get_jump(self):
        # if self.get_command_type() == 'C_COMMAND':
        if ';' in self.current_line:
            return self.current_line.split(';')[1]
        if '=' in self.current_line:
            return 'null'
