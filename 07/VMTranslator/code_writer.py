class CodeWriter:
    output_file_path = ''
    file_name = ''
    def __init__(self,vm_file_path):
        """Create a new .asm file and prepare it for writing."""
        self.set_file_name(vm_file_path)
        with open(CodeWriter.output_file_path, 'x', encoding='utf-8') as f:
            self.output_file = f
    def set_file_name(self, file_path):
        """Set the name of the .asm file."""
        file_name = file_path.split('/')[-1]
        file_name = file_name.replace('.vm', '.asm')
        directory = file_path.split('/')[:-1]
        directory = '/'.join(directory) + '/'
        CodeWriter.output_file_path = directory + file_name
        CodeWriter.file_name = file_name
    def write_arithmetic(self, command):
        """Writes the assembly code that is the translation of the given arithmetic command."""
        if command == 'add':
            # pop topmost value from stack to D
            # pop next value from stack to M
            # add D and M
            # push result to stack
            self.output_file.write('@SP\n')
            self.output_file.write('M=M-1\n')
            self.output_file.write('A=M\n')
            self.output_file.write('D=M\n')
            self.output_file.write('@SP\n')
            self.output_file.write('M=M-1\n')
            self.output_file.write('A=M\n')
            self.output_file.write('M=D+M\n')
            self.output_file.write('@SP\n')
            self.output_file.write('M=M+1\n')
        if command == 'sub':
            # pop topmost value from stack to D
            # pop next value from stack to M
            # subtract D from M
            # push result to stack
            self.output_file.write('@SP\n')
            self.output_file.write('M=M-1\n')
            self.output_file.write('A=M\n')
            self.output_file.write('D=M\n')
            self.output_file.write('@SP\n')
            self.output_file.write('M=M-1\n')
            self.output_file.write('A=M\n')
            self.output_file.write('M=M-D\n')
            self.output_file.write('@SP\n')
            self.output_file.write('M=M+1\n')
        if command == 'neg':
            # pop topmost value from stack and negate it
            # push result to stack
            self.output_file.write('@SP\n')
            self.output_file.write('M=M-1\n')
            self.output_file.write('A=M\n')
            self.output_file.write('M=-M\n')
            self.output_file.write('@SP\n')
            self.output_file.write('M=M+1\n')
        if command == 'eq':
            # pop topmost value from stack to D
            # pop next value from stack to M
            # if D == M, push -1 to stack
            # else push 0 to stack
            self.output_file.write('@SP\n')
            self.output_file.write('M=M-1\n')
            self.output_file.write('A=M\n')
            self.output_file.write('D=M\n') # D = y
            self.output_file.write('@SP\n')
            self.output_file.write('M=M-1\n')
            self.output_file.write('A=M\n')
            self.output_file.write('D=D-M\n') # D = y - x
            self.output_file.write('@EQ\n')
            self.output_file.write('D;JEQ\n') # if D == 0, jump to EQ
            self.output_file.write('@NE\n')
            self.output_file.write('D;JNE\n') # if D != 0, jump to NE
            self.output_file.write('(EQ)\n')
            self.output_file.write('@SP\n')
            self.output_file.write('A=M\n')
            self.output_file.write('M=-1\n') # push -1 to stack
            self.output_file.write('(NE)\n')
            self.output_file.write('@SP\n')
            self.output_file.write('A=M\n')
            self.output_file.write('M=0\n') # push 0 to stack
            self.output_file.write('@SP\n')
            self.output_file.write('M=M+1\n') # increment SP
        if command == 'gt':
            # pop topmost value(=y) from stack to D
            # pop next value(=x) from stack to M
            # if D > M, push -1 to stack
            # else push 0 to stack
            self.output_file.write('@SP\n')
            self.output_file.write('M=M-1\n')
            self.output_file.write('A=M\n')
            self.output_file.write('D=M\n') # D = y
            self.output_file.write('@SP\n')
            self.output_file.write('M=M-1\n')
            self.output_file.write('A=M\n')
            self.output_file.write('D=D-M\n') # D = y - x
            self.output_file.write('@GT\n')
            self.output_file.write('D;JGT\n') # if D > 0, jump to GT
            self.output_file.write('@LT\n')
            self.output_file.write('D;JLT\n') # if D < 0, jump to LT
            self.output_file.write('(GT)\n')
            self.output_file.write('@SP\n')
            self.output_file.write('A=M\n')
            self.output_file.write('M=-1\n') # push -1 to stack
            self.output_file.write('(LT)\n')
            self.output_file.write('@SP\n')
            self.output_file.write('A=M\n')
            self.output_file.write('M=0\n') # push 0 to stack
            self.output_file.write('@SP\n')
            self.output_file.write('M=M+1\n') # increment SP
        if command == 'lt':
            # pop topmost value(=y) from stack to D
            # pop next value(=x) from stack to M
            # if D < M, push -1 to stack
            # else push 0 to stack
            self.output_file.write('@SP\n')
            self.output_file.write('M=M-1\n')
            self.output_file.write('A=M\n')
            self.output_file.write('D=M\n') # D = y
            self.output_file.write('@SP\n')
            self.output_file.write('M=M-1\n')
            self.output_file.write('A=M\n')
            self.output_file.write('D=D-M\n') # D = y - x
            self.output_file.write('@LT\n')
            self.output_file.write('D;JLT\n') # if D < 0, jump to LT
            self.output_file.write('@GT\n')
            self.output_file.write('D;JGT\n') # if D > 0, jump to GT
            self.output_file.write('(LT)\n')
            self.output_file.write('@SP\n')
            self.output_file.write('A=M\n')
            self.output_file.write('M=-1\n') # push -1 to stack
            self.output_file.write('(GT)\n')
            self.output_file.write('@SP\n')
            self.output_file.write('A=M\n')
            self.output_file.write('M=0\n') # push 0 to stack
            self.output_file.write('@SP\n')
            self.output_file.write('M=M+1\n') # increment SP
        if command == 'and':
            # pop topmost value(=y) from stack to D
            # pop next value(=x) from stack to M
            # if D & M, push -1 to stack
            # else push 0 to stack
            self.output_file.write('@SP\n')
            self.output_file.write('M=M-1\n')
            self.output_file.write('A=M\n')
            self.output_file.write('D=M\n') # D = y
            self.output_file.write('@SP\n')
            self.output_file.write('M=M-1\n')
            self.output_file.write('A=M\n')
            self.output_file.write('M=D&M\n') # M = y & x
            self.output_file.write('@SP\n')
            self.output_file.write('M=M+1\n') # increment SP
        if command == 'or':
            # pop topmost value(=y) from stack to D
            # push D | netx value(=x) to stack
            self.output_file.write('@SP\n')
            self.output_file.write('M=M-1\n')
            self.output_file.write('A=M\n')
            self.output_file.write('D=M\n') # D = y
            self.output_file.write('@SP\n')
            self.output_file.write('M=M-1\n')
            self.output_file.write('A=M\n')
            self.output_file.write('M=D|M\n') # M = y | x
            self.output_file.write('@SP\n')
            self.output_file.write('M=M+1\n') # increment SP
        if command == 'not':
            # push !topmost value to stack
            self.output_file.write('@SP\n')
            self.output_file.write('M=M-1\n')
            self.output_file.write('M=!M\n') # M = !y
            self.output_file.write('@SP\n')
            self.output_file.write('M=M+1\n') # increment SP
    def write_push_pop(self, command, seg, val):
        """Writes the assembly code that is the translation of the given push or pop command."""
        if command == 'C_PUSH':
            if seg == 'constant':
                # push constant val to stack
                self.output_file.write('@' + val + '\n')
                self.output_file.write('D=A\n') # D = val
                self.output_file.write('@SP\n')
                self.output_file.write('A=M\n') # address = RAM[SP]
                self.output_file.write('M=D\n') # RAM[address] = D
                self.output_file.write('@SP\n')
                self.output_file.write('M=M+1\n') # increment SP
            if seg == 'local':
                # push local val to stack
                self.output_file.write('@' + val + '\n')
                self.output_file.write('D=A\n')
                self.output_file.write('@LCL\n')
                self.output_file.write('D=M+D\n') # address = RAM[LCL] + val
                self.output_file.write('A=D\n')
                self.output_file.write('D=M\n') # D = RAM[address]
                self.output_file.write('@SP\n')
                self.output_file.write('A=M\n')
                self.output_file.write('M=D\n') # RAM[SP] = D
                self.output_file.write('@SP\n')
                self.output_file.write('M=M+1\n') # increment SP
            if seg == 'argument':
                # push argument val to stack
                self.output_file.write('@' + val + '\n')
                self.output_file.write('D=A\n')
                self.output_file.write('@ARG\n')
                self.output_file.write('D=M+D\n') # address = RAM[ARG] + val
                self.output_file.write('A=D\n')
                self.output_file.write('D=M\n') # D = RAM[address]
                self.output_file.write('@SP\n')
                self.output_file.write('A=M\n')
                self.output_file.write('M=D\n') # RAM[SP] = D
                self.output_file.write('@SP\n')
                self.output_file.write('M=M+1\n') # increment SP
            if seg == 'this':
                # push this val to stack
                self.output_file.write('@' + val + '\n')
                self.output_file.write('D=A\n')
                self.output_file.write('@THIS\n')
                self.output_file.write('D=M+D\n') # address = RAM[THIS] + val
                self.output_file.write('A=D\n')
                self.output_file.write('D=M\n') # D = RAM[address]
                self.output_file.write('@SP\n')
                self.output_file.write('A=M\n')
                self.output_file.write('M=D\n') # RAM[SP] = D
                self.output_file.write('@SP\n')
                self.output_file.write('M=M+1\n') # increment SP
            if seg == 'that':
                # push that val to stack
                self.output_file.write('@' + val + '\n')
                self.output_file.write('D=A\n')
                self.output_file.write('@THAT\n')
                self.output_file.write('D=M+D\n') # address = RAM[THAT] + val
                self.output_file.write('A=D\n')
                self.output_file.write('D=M\n') # D = RAM[address]
                self.output_file.write('@SP\n')
                self.output_file.write('A=M\n')
                self.output_file.write('M=D\n') # RAM[SP] = D
                self.output_file.write('@SP\n')
                self.output_file.write('M=M+1\n') # increment SP
            if seg =='pointer':
                # push poinrer val to stack
                addr = str(3 + int(val))
                self.output_file.write('@' + addr + '\n')
                self.output_file.write('D=M\n') # address = RAM[3 + val]
                self.output_file.write('@THAT\n')
                self.output_file.write('D=M+D\n') # D = RAM[THAT + val
                self.output_file.write('A=D\n')
                self.output_file.write('D=M\n') # D = RAM[THAT + val]
                self.output_file.write('@SP\n')
                self.output_file.write('A=M\n')
                self.output_file.write('M=D\n') # RAM[SP] = RAM[THAT + val]
                self.output_file.write('@SP\n')
                self.output_file.write('M=M+1\n')
            if seg == 'temp':
                # push temp val to stack
                addr = str(5 + int(val))
                self.output_file.write('@'+addr+'\n')
                self.output_file.write('D=A\n')
                self.output_file.write('@SP\n')
                self.output_file.write('A=M\n')
                self.output_file.write('M=D\n')
                self.output_file.write('@SP\n')
                self.output_file.write('M=M+1\n')