"""Parser for VM files."""

class VMParser:
    """Parser for a single .vm file.
    Args:
        vm_file_path (str): path to .vm file
    Attributes:
        lines (list): list of lines in the .vm file
        current_line_num (int): current line number
        current_line (list): current line
    Methods:
        has_more_commands(): Are there more commands in the input?
        advance(): Reads the next command from the input and makes it the current command.
        get_command_type(): Returns the type of the current VM command.
        get_arg1(): Returns the first argument of the current command.
        get_arg2(): Returns the second argument of the current command.
    """
    def __init__(self, vm_file_path) -> None:
        """Constructor.
        Args:
            vm_file_path (str): absolute path to .vm file
        """
        with open(vm_file_path, 'r', encoding='utf-8') as f:
            self.lines = f.readlines()
            for i,line in enumerate(self.lines):
                line = line.split()
                if len(line) > 0:
                    if line[0][0] == '/' and line[0][1] == '/':
                        line = None
                self.lines[i] = line
        self.lines = [line for line in self.lines if line is not None and line != []]
        self.current_line_num = -1
        self.current_line = self.lines[self.current_line_num]
    def has_more_commands(self):
        """Are there more commands in the input?
        Returns:
            bool: True if there are more commands, False if not.
        """
        self.current_line_num += 1
        return self.current_line_num < len(self.lines)
    def advance(self):
        """Reads the next command from the input and makes it the current command.
        Should be called only if has_more_commands() is true.
        """
        self.current_line = self.lines[self.current_line_num]
    def get_command_type(self):
        """Returns the type of the current VM command.
        Returns:
            str: C_ARITHMETIC, C_PUSH, C_POP, C_LABEL, C_GOTO, C_IF, C_FUNCTION, C_RETURN, C_CALL
        """
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
        """Returns the first argument of the current command.
        Returns:
            str: the first argument of the current command.
            In the case of C_ARITHMETIC, the command itself (add, sub, etc.) is returned.
            Should not be called if the current command is C_RETURN.
        """
        if self.get_command_type() == 'C_ARITHMETIC':
            return self.current_line[0]
        return self.current_line[1]
    def get_arg2(self):
        """Returns the second argument of the current command.
        Returns:
            int: the second argument of the current command.
            Should be called only if the current command is C_PUSH, C_POP, C_FUNCTION, or C_CALL.
        """
        return self.current_line[2]
        