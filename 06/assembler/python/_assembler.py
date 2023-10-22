from code import Code
from asm_parser import AsmParser
from symbol_table import SymbolTable

class Assembler:
    """Genrates .hack file from .asm file."""

    def __init__(self, input_file):
        self.input_file = input_file
        self.output_file = input_file.replace('.asm', '.hack')
        self.symbol_table = SymbolTable()
        self.next_variable_address = 16

    def assemble(self):
        self.first_pass()
        self.second_pass()

    def first_pass(self):
        """Builds the symbol table (with labels) going through the .asm file line by line."""
        parser = AsmParser(self.input_file)
        rom_address = 0
        while parser.has_more_commands():
            parser.advance()
            command_type = parser.get_command_type()
            if command_type == 'L_COMMAND':
                symbol = parser.get_symbol()
                self.symbol_table.add_entry(symbol, rom_address)
            else:
                rom_address += 1

    def second_pass(self):
        parser = AsmParser(self.input_file)
        code = Code()
        binary = []
        while parser.has_more_commands():
            parser.advance()
            command_type = parser.get_command_type()
            print(command_type)
            if command_type == 'A_COMMAND':
                symbol = parser.get_symbol()
                if symbol.isdigit():
                    binary.append('0' + bin(int(symbol))[2:].zfill(15))
                else:
                    if not self.symbol_table.contains(symbol):
                        self.symbol_table.add_entry(
                            symbol, self.next_variable_address)
                        self.next_variable_address += 1
                    binary.append(
                        '0' + bin(self.symbol_table.get_address(symbol))[2:].zfill(15))
            elif command_type == 'C_COMMAND':
                print(parser.get_dest(), parser.get_comp(), parser.get_jump())
                binary.append('111' + code.comp_n_to_bits(parser.get_comp()) +
                              code.dest_n_to_bits(parser.get_dest()) +
                              code.jump_n_to_bits(parser.get_jump()))
        with open(self.output_file, 'w', encoding="utf-8") as f:
            f.write('\n'.join(binary) + '\n')
