from code_writer import CodeWriter
from vm_parser import VMParser

class VMTranslator:
    def __init__(self,input_file) -> None:
        self.input_file = input_file
    def translate(self):
        parser = VMParser(self.input_file)
        code_writer = CodeWriter(self.input_file)
        while parser.has_more_commands():
            parser.advance()
            command_type = parser.get_command_type()
            if command_type == 'C_ARITHMETIC':
                code_writer.write_arithmetic(parser.get_arg1())
            else:
                code_writer.write_push_pop(command_type, parser.get_arg1(), parser.get_arg2())
        code_writer.close()
        