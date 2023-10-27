class CodeWriter:
    def __init__(self,vm_file_path):
        self.lines = []
        self.output_file_path = ''
        self.file_name = ''
        self.eq_i = 0
        self.gt_i = 0
        self.lt_i = 0
        """Create a new .asm file and prepare it for writing."""
        self.set_file_name(vm_file_path)
        with open(self.output_file_path, 'w', encoding='utf-8') as f:
            f.write('')
    def set_file_name(self, file_path):
        """Set the name of the .asm file."""
        file_name = file_path.split('/')[-1]
        file_name = file_name.replace('.vm', '.asm')
        directory = file_path.split('/')[:-1]
        directory = '/'.join(directory) + '/'
        self.output_file_path = directory + file_name
        self.file_name = file_name
    def write_arithmetic(self, command):
        """Writes the assembly code that is the translation of the given arithmetic command."""
        if command == 'add':
            # pop topmost value from stack to D
            # pop next value from stack to M
            # add D and M
            # push result to stack
            self.lines.append('@SP')
            self.lines.append('M=M-1')
            self.lines.append('A=M')
            self.lines.append('D=M')
            self.lines.append('@SP')
            self.lines.append('M=M-1')
            self.lines.append('A=M')
            self.lines.append('M=D+M')
            self.lines.append('@SP')
            self.lines.append('M=M+1')
        if command == 'sub':
            # pop topmost value from stack to D
            # pop next value from stack to M
            # subtract D from M
            # push result to stack
            self.lines.append('@SP')
            self.lines.append('M=M-1')
            self.lines.append('A=M')
            self.lines.append('D=M')
            self.lines.append('@SP')
            self.lines.append('M=M-1')
            self.lines.append('A=M')
            self.lines.append('M=M-D')
            self.lines.append('@SP')
            self.lines.append('M=M+1')
        if command == 'neg':
            # pop topmost value from stack and negate it
            # push result to stack
            self.lines.append('@SP')
            self.lines.append('M=M-1') # decrement SP
            self.lines.append('A=M') # A = SP
            self.lines.append('M=-M') # RAM[SP] = -RAM[SP]
            self.lines.append('@SP')
            self.lines.append('M=M+1')
        if command == 'eq':
            self.eq_i += 1
            # pop topmost value from stack to D
            # pop next value from stack to M
            # if D == M, push -1 to stack
            # else push 0 to stack
            self.lines.append('@SP')
            self.lines.append('M=M-1')
            self.lines.append('A=M')
            self.lines.append('D=M') # D = RAM[SP]
            # self.lines.append('M=0')
            self.lines.append('@SP')
            self.lines.append('M=M-1')
            self.lines.append('A=M')
            self.lines.append('D=D-M') # D = RAM[SP] - RAM[SP-1]
            # self.lines.append('M=0')
            self.lines.append('@EQ' + str(self.eq_i))
            self.lines.append('D;JEQ') # if D == 0, jump to EQ
            self.lines.append('@NE' + str(self.eq_i))
            self.lines.append('D;JNE') # if D != 0, jump to NE
            self.lines.append('(EQ' + str(self.eq_i) + ')')
            self.lines.append('@SP')
            self.lines.append('A=M')
            self.lines.append('M=-1') # push -1 to stack
            self.lines.append('@ENDEQ' + str(self.eq_i))
            self.lines.append('0;JMP') # jump to ENDEQ
            self.lines.append('(NE' + str(self.eq_i) + ')')
            self.lines.append('@SP')
            self.lines.append('A=M')
            self.lines.append('M=0') # push 0 to stack
            self.lines.append('(ENDEQ' + str(self.eq_i) + ')')
            self.lines.append('@SP')
            self.lines.append('M=M+1') # increment SP
        if command == 'gt':
            self.gt_i += 1
            # pop topmost value(=y) from stack to D
            # pop next value(=x) from stack to M
            # if M > D, push -1 to stack
            # else push 0 to stack
            self.lines.append('@SP')
            self.lines.append('M=M-1')
            self.lines.append('A=M')
            self.lines.append('D=M') # D = y
            self.lines.append('@SP')
            self.lines.append('M=M-1')
            self.lines.append('A=M')
            self.lines.append('D=M-D') # D = x - y
            self.lines.append('@GT' + str(self.gt_i))
            self.lines.append('D;JGT') # if D > 0, jump to GT
            self.lines.append('@LE' + str(self.gt_i))
            self.lines.append('D;JLE') # if D <= 0, jump to LE
            self.lines.append('(GT' + str(self.gt_i) + ')')
            self.lines.append('@SP')
            self.lines.append('A=M')
            self.lines.append('M=-1') # push -1 to stack
            self.lines.append('@ENDGT' + str(self.gt_i))
            self.lines.append('0;JMP') # jump to ENDEQ
            self.lines.append('(LE' + str(self.gt_i) + ')')
            self.lines.append('@SP')
            self.lines.append('A=M')
            self.lines.append('M=0') # push 0 to stack
            self.lines.append('(ENDGT' + str(self.gt_i) + ')')
            self.lines.append('@SP')
            self.lines.append('M=M+1') # increment SP
        if command == 'lt':
            self.lt_i += 1
            # pop topmost value(=y) from stack to D
            # pop next value(=x) from stack to M
            # if M < D, push -1 to stack
            # else push 0 to stack
            self.lines.append('@SP')
            self.lines.append('M=M-1')
            self.lines.append('A=M')
            self.lines.append('D=M') # D = y
            self.lines.append('@SP')
            self.lines.append('M=M-1')
            self.lines.append('A=M')
            self.lines.append('D=M-D') # D = x - y
            self.lines.append('@LT' + str(self.lt_i))
            self.lines.append('D;JLT') # if D < 0, jump to LT
            self.lines.append('@GE' + str(self.lt_i))
            self.lines.append('D;JGE') # if D >= 0, jump to GE
            self.lines.append('(LT' + str(self.lt_i) + ')')
            self.lines.append('@SP')
            self.lines.append('A=M')
            self.lines.append('M=-1') # push -1 to stack
            self.lines.append('@ENDLT' + str(self.lt_i))
            self.lines.append('0;JMP') # jump to ENDEQ
            self.lines.append('(GE' + str(self.lt_i) + ')')
            self.lines.append('@SP')
            self.lines.append('A=M')
            self.lines.append('M=0') # push 0 to stack
            self.lines.append('(ENDLT' + str(self.lt_i) + ')')
            self.lines.append('@SP')
            self.lines.append('M=M+1') # increment SP
        if command == 'and':
            # pop topmost value(=y) from stack to D
            # pop next value(=x) from stack to M
            # if D & M, push -1 to stack
            # else push 0 to stack
            self.lines.append('@SP')
            self.lines.append('M=M-1')
            self.lines.append('A=M')
            self.lines.append('D=M') # D = y
            self.lines.append('@SP')
            self.lines.append('M=M-1')
            self.lines.append('A=M')
            self.lines.append('M=D&M') # M = y & x
            self.lines.append('@SP')
            self.lines.append('M=M+1') # increment SP
        if command == 'or':
            # pop topmost value(=y) from stack to D
            # push D | netx value(=x) to stack
            self.lines.append('@SP')
            self.lines.append('M=M-1')
            self.lines.append('A=M')
            self.lines.append('D=M') # D = y
            self.lines.append('@SP')
            self.lines.append('M=M-1')
            self.lines.append('A=M')
            self.lines.append('M=D|M') # M = y | x
            self.lines.append('@SP')
            self.lines.append('M=M+1') # increment SP
        if command == 'not':
            # push !topmost value to stack
            self.lines.append('@SP')
            self.lines.append('M=M-1')
            self.lines.append('A=M')
            self.lines.append('M=!M') # M = !y
            self.lines.append('@SP')
            self.lines.append('M=M+1') # increment SP
    def write_push_pop(self, command, seg, val):
        """Writes the assembly code that is the translation of the given push or pop command."""
        if command == 'C_PUSH':
            if seg in ('constant', 'pointer', 'temp','static'):
                if seg == 'constant':
                    # push constant val to stack
                    self.lines.append('@' + val)
                    self.lines.append('D=A') # D = val
                else:
                    if seg =='pointer':
                        # push poinrer val to stack
                        addr = str(3 + int(val))
                    if seg == 'temp':
                        # push temp val to stack
                        addr = str(5 + int(val))
                    if seg == 'static':
                        # push static val to stack
                        addr = self.file_name + '.' + val
                    self.lines.append('@' + addr)
                    self.lines.append('D=M') # value = RAM[addr]
                self.lines.append('@SP')
                self.lines.append('A=M')
                self.lines.append('M=D')
                self.lines.append('@SP')
                self.lines.append('M=M+1')
            elif seg in ('local', 'argument' , 'this' , 'that'):
                if seg == 'local':
                    addr = 'LCL'
                if seg == 'argument':
                    addr = 'ARG'
                if seg == 'this':
                    addr = 'THIS'
                if seg == 'that':
                    addr = 'THAT'
                # push local/argument/this/that val to stack
                self.lines.append('@' + val)
                self.lines.append('D=A')
                self.lines.append('@' + addr)
                self.lines.append('D=M+D') # address = RAM[addr] + val
                self.lines.append('A=D')
                self.lines.append('D=M') # D = RAM[address]
                self.lines.append('@SP')
                self.lines.append('A=M')
                self.lines.append('M=D') # RAM[SP] = RAM[address]
                self.lines.append('@SP')
                self.lines.append('M=M+1') # increment SP
            
        if command == 'C_POP':
            if seg in('pointer' , 'temp', 'static'):
                if seg == 'pointer':
                    addr = str(3 + int(val))
                if seg == 'temp':
                    addr = str(5 + int(val))
                if seg == 'static':
                    addr = self.file_name + '.' + val
                # pop topmost value from stack
                self.lines.append('@SP')
                self.lines.append('M=M-1') # decrement SP
                self.lines.append('A=M')
                self.lines.append('D=M') # D = RAM[SP]
                self.lines.append('@' + addr)
                self.lines.append('M=D') # RAM[address] = RAM[SP]
            else:
                if seg == 'local':
                    addr = 'LCL'
                if seg == 'argument':
                    addr = 'ARG'
                if seg == 'this':
                    addr = 'THIS'
                if seg == 'that':
                    addr = 'THAT'
                # pop topmost value from stack to local val
                self.lines.append('@' + val)
                self.lines.append('D=A')
                self.lines.append('@' + addr)
                self.lines.append('D=M+D')
                self.lines.append('@R13')
                self.lines.append('M=D') # R13 = address
                self.lines.append('@SP')
                self.lines.append('M=M-1') # decrement SP
                self.lines.append('A=M')
                self.lines.append('D=M') # D = RAM[SP]
                self.lines.append('@R13')
                self.lines.append('A=M')
                self.lines.append('M=D') # RAM[address] = RAM[SP]
    def close(self):
        """Writes the assembly code """
        with open(self.output_file_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(self.lines) + '\n')