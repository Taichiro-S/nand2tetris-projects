"""Translates VM commands into Hack assembly code."""

class CodeWriter:
    """Translates VM commands into Hack assembly code.
    Attributes:
        lines (list): list of lines in the .asm file
        output_file_path (str): path to .asm file
        file_name (str): name of .asm file
        eq_i (int): number of eq commands
        gt_i (int): number of gt commands
        lt_i (int): number of lt commands
        call_i (int): number of call commands
    Methods:
        set_file_name(): Set the name of the .asm file.
        write_init(): Writes assembly code that effects the VM initialization.
        write_arithmetic(): Writes the assembly code that is the translation of the given arithmetic command.
        write_push_pop(): Writes the assembly code that is the translation of the given push or pop command.
        write_label(): Writes assembly code that effects the label command.
        write_goto(): Writes assembly code that effects the goto command.
        write_if(): Writes assembly code that effects the if-goto command.
        write_call(): Writes assembly code that effects the call command.
        write_return(): Writes assembly code that effects the return command.
        write_function(): Writes assembly code that effects the function command.
        close(): Writes the assembly code to the .asm file.
    """
    def __init__(self,vm_file_path):
        """Constructor.
        Args:
            vm_file_path (str): path to .vm file
        """
        self.lines = []
        self.output_file_path = ''
        self.file_name = ''
        self.eq_i = 0
        self.gt_i = 0
        self.lt_i = 0
        self.call_i = 0
        """Create a new .asm file and prepare it for writing."""
        self.set_file_name(vm_file_path)
        with open(self.output_file_path, 'w', encoding='utf-8') as f:
            f.write('')
        # self.write_init()
    def set_file_name(self, file_path):
        """Set the name of the .asm file.
        Args:
            file_path (str): path to .vm file
        """
        file_name = file_path.split('/')[-1]
        file_name = file_name.replace('.vm', '.asm')
        directory = file_path.split('/')[:-1]
        directory = '/'.join(directory) + '/'
        self.output_file_path = directory + file_name
        self.file_name = file_name
    def write_init(self):
        """Writes assembly code that effects the VM initialization."""
        self.lines += ['@256','D=A','@SP','M=D']
    def write_arithmetic(self, command):
        """Writes the assembly code that is the translation of the given arithmetic command.
        Args:
            command (str): add, sub, neg, eq, gt, lt, and, or, not
        """
        if command == 'add':
            # pop topmost(=y) and next value(=x) from stack,
            # push y+x to stack
            self.lines += ['@SP','M=M-1','A=M','D=M', # D = x
                           '@SP','M=M-1','A=M','M=D+M', # y += x
                           '@SP','M=M+1']
        if command == 'sub':
            # pop topmost(=y) and the next value(=x) from stack, 
            # push y-x to stack
            self.lines += ['@SP','M=M-1','A=M','D=M', # D = x
                           '@SP','M=M-1','A=M','M=M-D', # y -= x
                           '@SP','M=M+1']
        if command == 'neg':
            # pop topmost value(=y) from stack
            # push -y to stack
            self.lines += ['@SP','M=M-1','A=M','M=-M', # y = -y
                           '@SP','M=M+1']
        if command == 'eq':
            # pop topmost(=y) and the next value(=x) from stack, 
            # if x == y, push -1 to stack, else push 0 to stack
            self.eq_i += 1
            self.lines += ['@SP','M=M-1','A=M','D=M', # D = y
                            '@SP','M=M-1','A=M','D=D-M', # D = y - x
                            '@EQ' + str(self.eq_i),'D;JEQ', # if D == 0, jump to EQ
                            '@NE' + str(self.eq_i),'D;JNE', # if D != 0, jump to NE
                            '(EQ' + str(self.eq_i) + ')','@SP','A=M','M=-1', # push -1 to stack
                            '@ENDEQ' + str(self.eq_i),'0;JMP', # jump to ENDEQ
                            '(NE' + str(self.eq_i) + ')','@SP','A=M','M=0', # push 0 to stack
                            '(ENDEQ' + str(self.eq_i) + ')','@SP','M=M+1']
        if command == 'gt':
            self.gt_i += 1
            # pop topmost(=y) and the next value(=x) from stack, 
            # if x > y, push -1 to stack, else push 0 to stack
            self.lines += ['@SP','M=M-1','A=M','D=M', # D = y
                            '@SP','M=M-1','A=M','D=M-D', # D = x - y
                            '@GT' + str(self.gt_i),'D;JGT', # if D > 0, jump to GT
                            '@LE' + str(self.gt_i),'D;JLE', # if D <= 0, jump to LE
                            '(GT' + str(self.gt_i) + ')','@SP','A=M','M=-1', # push -1 to stack
                            '@ENDGT' + str(self.gt_i),'0;JMP', # jump to ENDEQ
                            '(LE' + str(self.gt_i) + ')','@SP','A=M','M=0', # push 0 to stack
                            '(ENDGT' + str(self.gt_i) + ')','@SP','M=M+1'] 
        if command == 'lt':
            self.lt_i += 1
            # pop topmost(=y) and the next value(=x) from stack, 
            # if x < y, push -1 to stack, else push 0 to stack
            self.lines += ['@SP','M=M-1','A=M','D=M', # D = y
                           '@SP','M=M-1','A=M','D=M-D', # D = x - y
                           '@LT' + str(self.lt_i),'D;JLT', # if D < 0, jump to LT
                           '@GE' + str(self.lt_i),'D;JGE', # if D >= 0, jump to GE
                           '(LT' + str(self.lt_i) + ')','@SP','A=M','M=-1', # push -1 to stack
                           '@ENDLT' + str(self.lt_i),'0;JMP', # jump to ENDEQ
                           '(GE' + str(self.lt_i) + ')','@SP','A=M','M=0', # push 0 to stack
                           '(ENDLT' + str(self.lt_i) + ')','@SP','M=M+1']
        if command == 'and':
            # pop topmost(=y) and the next value(=x) from stack, 
            # push y&x to stack
            self.lines += ['@SP','M=M-1','A=M','D=M', # D = y
                           '@SP','M=M-1','A=M','M=D&M', # y &= x
                           '@SP','M=M+1']
        if command == 'or':
            # pop topmost(=y) and the next value(=x) from stack, 
            # push y|x to stack
            self.lines += ['@SP','M=M-1','A=M','D=M', # D = y
                           '@SP','M=M-1','A=M','M=D|M', # y |= x
                           '@SP','M=M+1']
        if command == 'not':
            # push !topmost value to stack
            self.lines += ['@SP','M=M-1','A=M','M=!M', # y = !y
                           '@SP','M=M+1'] 
    def write_push_pop(self, command, seg, val):
        """Writes the assembly code that is the translation of the given push or pop command.
        Args:
            command (str): C_PUSH, C_POP
            seg (str): segment name
            val (str): index
        """
        if command == 'C_PUSH':
            if seg in ('constant', 'pointer', 'temp','static'):
                if seg == 'constant':
                    # push constant val to stack
                    self.lines += ['@' + val,'D=A'] # D = val
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
                    self.lines += ['@' + addr,'D=M']
                self.lines += ['@SP','A=M','M=D', # RAM[SP] = RAM[addr]
                                '@SP','M=M+1']
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
                self.lines += ['@' + val,'D=A','@' + addr,'D=M+D', # address = RAM[addr] + val
                               'A=D','D=M','@SP','A=M','M=D', # RAM[SP] = RAM[address]
                               '@SP','M=M+1']
        if command == 'C_POP':
            if seg in('pointer' , 'temp', 'static'):
                if seg == 'pointer':
                    addr = str(3 + int(val))
                if seg == 'temp':
                    addr = str(5 + int(val))
                if seg == 'static':
                    addr = self.file_name + '.' + val
                # pop topmost value from stack
                self.lines += ['@SP','M=M-1', 'A=M','D=M', # D = RAM[SP-1]
                               '@' + addr,'M=D'] # RAM[address] = RAM[SP-1]
            else:
                if seg == 'local':
                    addr = 'LCL'
                if seg == 'argument':
                    addr = 'ARG'
                if seg == 'this':
                    addr = 'THIS'
                if seg == 'that':
                    addr = 'THAT'
                # pop topmost value from stack to local/argument/this/that val
                self.lines += ['@' + val,'D=A','@' + addr,'D=M+D','@R13','M=D', # R13 = address
                               '@SP','M=M-1', 'A=M','D=M', # D = RAM[SP-1]
                               '@R13','A=M','M=D'] # RAM[address] = RAM[SP-1]
    def write_label(self, label):
        """Writes assembly code that effects the label command.
        Args:
            label (str): label name
        """
        self.lines += ['(' + label + ')']
    def write_goto(self, label):
        """Writes assembly code that effects the goto command.
        Args:
            label (str): label name
        """
        self.lines += ['@' + label,'0;JMP']
    def write_if(self, label):
        """Writes assembly code that effects the if-goto command.
        Args:
            label (str): label name
        """
        self.lines += ['@SP','M=M-1','A=M','D=M', # D = RAM[SP-1]
                       '@' + label,'D;JNE']
    def write_call(self, function_name, num_args):
        """Writes assembly code that effects the call command.
        Args: 
            function_name (str): function name
            num_args (str): number of arguments
        """
        self.lines += ['@RETURN_ADDRESS' + str(self.call_i),'D=A','@SP','A=M','M=D', # push return-address
                       '@SP','M=M+1',
                       '@LCL','D=M','@SP','A=M','M=D', # push LCL
                       '@SP','M=M+1',
                       '@ARG','D=M','@SP','A=M','M=D', # push ARG
                       '@SP','M=M+1',
                       '@THIS','D=M','@SP','A=M','M=D', # push THIS
                       '@SP','M=M+1',
                       '@THAT','D=M','@SP','A=M','M=D', # push THAT
                       '@SP','M=M+1',
                       '@SP','D=M','@5','D=D-A','@' + num_args,'D=D-A','@ARG','M=D', # ARG = SP - 5 - nArgs
                       '@SP','D=M','@LCL','M=D', # LCL = SP
                       '@' + function_name,'0;JMP', # goto function_name
                       '(RETURN_ADDRESS' + str(self.call_i) + ')']
        self.call_i += 1
    def write_return(self):
        """Writes assembly code that effects the return command."""
        self.lines += ['@LCL','D=M','@R13','M=D', # R13 = LCL
                       '@5','D=A','@R13','A=M-D','D=M','@R14','M=D', # R14 = *(R13-5)
                       '@SP','M=M-1','A=M','D=M','@ARG','A=M','M=D', # *ARG = pop()
                       '@ARG','D=M+1','@SP','M=D', # SP = ARG + 1
                       '@R13','AM=M-1','D=M','@THAT','M=D', # THAT = *(R13-1)
                       '@R13','AM=M-1','D=M','@THIS','M=D', # THIS = *(R13-1)
                       '@R13','AM=M-1','D=M','@ARG','M=D', # ARG = *(R13-1)
                       '@R13','AM=M-1','D=M','@LCL','M=D', # LCL = *(R13-1)
                       '@R14','A=M','0;JMP']
    def write_function(self, function_name, num_locals):
        """Writes assembly code that effects the function command.
        Args:
            function_name (str): function name
            num_locals (str): number of local variables
        """
        self.lines += ['(' + function_name + ')']
        for _ in range(int(num_locals)):
            self.lines += ['@SP','A=M','M=0','@SP','M=M+1']
    def close(self):
        """Writes the assembly code """
        with open(self.output_file_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(self.lines) + '\n')
            