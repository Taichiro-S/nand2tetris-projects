"""Translates VM code into Hack assembly code."""

from vm_parser import VMParser
from code_writer import CodeWriter

def translate(input_file):
    """Translates the input file into an assembly file.
    Args:
        input_file (str): path to .vm file or directory containing .vm files
    """
    parser = VMParser(input_file)
    code_writer = CodeWriter(input_file)
    while parser.has_more_commands():
        parser.advance()
        command_type = parser.get_command_type()
        if command_type == 'C_ARITHMETIC':
            code_writer.write_arithmetic(parser.get_arg1())
        elif command_type == 'C_LABEL':
            code_writer.write_label(parser.get_arg1())
        elif command_type == 'C_GOTO':
            code_writer.write_goto(parser.get_arg1())
        elif command_type == 'C_IF':
            code_writer.write_if(parser.get_arg1())
        elif command_type == 'C_FUNCTION':
            code_writer.write_function(parser.get_arg1(), parser.get_arg2())
        elif command_type == 'C_RETURN':
            code_writer.write_return()
        elif command_type == 'C_CALL':
            code_writer.write_call(parser.get_arg1(), parser.get_arg2())
        elif command_type in ('C_PUSH','C_POP'):
            code_writer.write_push_pop(command_type, parser.get_arg1(), parser.get_arg2())
    code_writer.close()

INPUT_FILE = "/Users/sekiguchi/Documents/nand2tetris/projects/08/FunctionCalls/SimpleFunction/SimpleFunction.vm"
translate(INPUT_FILE)
