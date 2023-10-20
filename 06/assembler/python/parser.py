class Parser:
    def __init__(self,asmFilePath):
        # Read the file and remove all the comments and white spaces
        with open(asmFilePath) as f:
            self.lines = f.readlines()
        for i in range(len(self.lines)):
            self.lines[i] = self.lines[i].split()[0]
            if self.lines[i] == '' or (self.lines[i][0] == '/' and self.lines[i][1] == '/'):
                self.lines[i] = None
        self.currentLineNum = -1
        self.currentLine = self.lines[self.currentLineNum]
    
    def hasMoreCommands(self):
        self.currentLineNum += 1
        if self.currentLineNum < len(self.lines):
            return True
        else:
            return False
    
    def advance(self):
        if self.hasMoreCommands():
            self.currentLine = self.lines[self.currentLineNum]
    
    def getCommandType(self):
        self.advance()
        if self.currenline[0] == '@':
            return 'A_COMMAND'
        elif self.currentLine[0] == '(':
            return 'L_COMMAND'
        elif self.currentLine[0] is not None:
            return 'C_COMMAND'
        return None

    def getSymbol(self):
        if self.getCommandType() == 'A_COMMAND':
            return self.currentLine[1:]
        elif self.getCommandType() == 'L_COMMAND':
            return self.currentLine[1:-1]
        return None
    
    def getDest(self):
        if self.getCommandType() == 'C_COMMAND':
            if '=' in self.currentLine:
                return self.currentLine.split('=')[0]
        return None
    
    def getComp(self):
        if self.getCommandType() == 'C_COMMAND':
            if '=' in self.currentLine:
                return self.currentLine.split('=')[1]
        return None
    
    def getJump(self):
        if self.getCommandType() == 'C_COMMAND':
            if ';' in self.currentLine:
                return self.currentLine.split(';')[1]