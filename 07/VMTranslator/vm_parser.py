class VMParser:
    def __init__(self, vm_file_path) -> None:
        with open(vm_file_path, 'r', encoding='utf-8') as f:
            self.lines = f.readlines()
            for i,line in enumerate(self.lines):
                line = line.split()
                if len(line) > 0:
                    if line[0][0] == '/' and line[0][1] == '/':
                        line = None
                self.lines[i] = line
        self.lines = [line for line in self.lines if line is not None and line != []]
        # print(self.lines)
        self.current_line_num = -1
        self.current_line = self.lines[self.current_line_num]
    def has_more_commands(self):
        self.current_line_num += 1
        return self.current_line_num < len(self.lines)
    def advance(self):
        self.current_line = self.lines[self.current_line_num]
    def get_command_type(self):
        if self.current_line[0] == 'push':
            return 'C_PUSH'
        if self.current_line[0] == 'pop':
            return 'C_POP'
        if self.current_line[0] == 'label':
            return 'C_LABEL'
        if self.current_line[0] == 'goto':
            return 'C_GOTO'
        if self.current_line[0] == 'if-goto':
            return 'C_IF'
        if self.current_line[0] == 'function':
            return 'C_FUNCTION'
        if self.current_line[0] == 'return':
            return 'C_RETURN'
        if self.current_line[0] == 'call':
            return 'C_CALL'
        if self.current_line[0] is not None:
            return 'C_ARITHMETIC'
    def get_arg1(self):
        if self.get_command_type() == 'C_ARITHMETIC':
            return self.current_line[0]
        return self.current_line[1]
    def get_arg2(self):
        return self.current_line[2]
        