# import sys
# sys.path.append(
#     '/Users/sekiguchi/Documents/nand2tetris/projects/06/assembler/python')
from _assembler import Assembler
INPUT_FILE = "/Users/sekiguchi/Documents/nand2tetris/projects/06/pong/Pong.asm"
assembler = Assembler(INPUT_FILE)

assembler.assemble()
