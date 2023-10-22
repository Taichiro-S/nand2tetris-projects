class SymbolTable:
    def __init__(self):
        self.table = {
            'SP': 0,
            'LCL': 1,
            'ARG': 2,
            'THIS': 3,
            'THAT': 4,
            'SCREEN': 16384,
            'KBD': 24576
        }
        for i in range(16):
            self.table['R' + str(i)] = i

    def add_entry(self, symbol, address):
        self.table[symbol] = address

    def contains(self, symbol):
        return bool(symbol in self.table)

    def get_address(self, symbol):
        return self.table[symbol]
