class CodeWriter:
    file_name = ''
    def __init__(self,file_name):
        """Create a new .asm file and prepare it for writing."""
        self.setFileName(file_name)
        self.output_file = open(CodeWriter.file_name + '.asm', 'x', encoding='utf-8')
    def setFileName(self, file_name):
        CodeWriter.file_name = file_name
    def write_arithmetic(self):
        """Writes the assembly code that is the translation of the given arithmetic command."""
        pass