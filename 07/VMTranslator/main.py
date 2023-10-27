from vm_translator import VMTranslator

INPUT_FILE = "/Users/sekiguchi/Documents/nand2tetris/projects/07/MemoryAccess/StaticTest/StaticTest.vm"
translator = VMTranslator(INPUT_FILE)
translator.translate()
