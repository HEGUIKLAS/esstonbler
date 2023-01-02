import sys

# lang class is responsible for holding and handeling stack, memory, function memory
# also has all operations as methods
class Lang:
    # all memory is in form of arrays
    def __init__(self):
        self.stack = []
        self.memory = []
        self.functions = []

    def ADD(self):
        a, b = self.stack.pop(), self.stack.pop()
        self.stack.append(a + b)

    def SUB(self):
        if len(self.stack) < 2:
            raise Exception("insuficient numbers on stack")
        a, b = self.stack.pop(), self.stack.pop()
        self.stack.append(b - a)

    # sta incerases the lenght of the array which stores memory if necesary
    #handles rewriting and writing in it
    def STA(self, val, adr):
        if adr >= len(self.memory):
            for i in range(adr - len(self.memory) + 1):
                self.memory.append(None)
        self.memory[adr] = val
        print(f"MEMORY: {self.memory}")

    def LDA(self, val, adr):
        if val != None:
            self.stack.append(val)
        elif adr != None:
            self.stack.append(self.memory[adr])


    def PNT(self):
        print(self.stack)

    # fnc takes a parameer df, whis is true when a fuction is being defined
    # parameters lenght and x(current line) are only needed when function is being defined
    def FNC(self, name, df, lenght = 0, x = 0):
        if df is True:
            self.functions.append((name, x + 1, lenght))
        elif df is False:
            for i in self.functions:
                if name == i[0]:
                    mlist = get_lst("program.txt")
                    for j in range(0, i[2]):
                        self.run_line(mlist[i[1] + j], i[1] + j)

    def EQL(self):
        if len(self.stack) < 2:
            raise Exception("insuficient numbers on stack") 
        a, b = self.stack.pop(), self.stack.pop()
        if a == b:
            return True
        else: return False

    def IQL(self):
        if len(self.stack) < 2:
            raise Exception("insuficient numbers on stack") 
        a, b = self.stack.pop(), self.stack.pop()
        if a != b:
            return True
        else: return False
        
    def EOH(self):
        if len(self.stack) < 2:
            raise Exception("insuficient numbers on stack")
        a, b = self.stack.pop(), self.stack.pop()
        if a >= b:
            return True
        else: return False
        
    def EOS(self):
        if len(self.stack) < 2:
            raise Exception("insuficient numbers on stack")
        a, b = self.stack.pop(), self.stack.pop()
        if a <= b:
            return True
        else: return False
        
    def SML(self):
        if len(self.stack) < 2:
            raise Exception("insuficient numbers on stack")
        a, b = self.stack.pop(), self.stack.pop()
        if a > b:
            return True
        else: return False
        
    def BIG(self):
        if len(self.stack) < 2:
            raise Exception("insuficient numbers on stack")
        a, b = self.stack.pop(), self.stack.pop()
        if a < b:
            return True
        else: return False

    def IMP(self):
        self.stack.append(int(input()))

    # calss IFF method, uses slice of line as input to remove WHL and IFF instructions
    def WHL(self, line):
        if line[1] != "IFF":
            raise Exception("invalid operation:", line[1])
        while True:
            if not self.IFF(line[2:]):
                break

    # takes line slice which starts with operator, returns true or false(only needed for WHL)
    def IFF(self, line):
        if line[0] == "EQL":
            if self.EQL():
                self.FNC(str(line[3]), False)
                return True
        elif line[0] == "IGL":
            if self.IQL():
                self.FNC(str(line[3]), False)
                return True
        elif line[0] == "SML":
            if self.SML():
                self.FNC(str(line[3]), False)
                return True
        elif line[0] == "EOH":
            if self.EOH():
                self.FNC(str(line[3]), False)
                return True
        elif line[0] == "BIG":
            if self.BIG():
                self.FNC(str(line[3]), False)
                return True
        elif line[0] == "EOS":
            if self.EOS():
                self.FNC(str(line[3]), False)
                return True
        else:
            raise Exception("unknown operator:", line[0])
        return False
    
    def EXT(self,line):
        sys.exit()

# gets lina and line number as input, check which instruction is called, and returns
# an interger to he main loop which tells it where to move the head and which line to read
    def run_line(self, line, x):
        print(f"CURRENT LINE {x}: {line} | STACK: {self.stack}")
        if line[0] == "ADD":
            if len(self.stack) < 2:
                raise Exception("insuficient numbers on stack")
            self.ADD()
            return 1
                            
        elif line[0] == "SUB":
            if len(self.stack) < 2:
                raise Exception("insuficient numbers on stack")
            self.SUB()
            return 1
                        
        elif line[0] == "LDA":
            if line[1] == "VAL":
                self.LDA(int(line[2]), None)
            elif line[1] == "ADR":
                self.LDA(None, int(line[2]))
            return 1
                            
        elif line[0] == "STA":
            if line[1] == "VAL":
                self.STA(int(line[2]),int(line[3]))
            elif line[1] == "SCT":
                self.STA(self.stack.pop(), int(line[2]))
            else:
                raise Exception("unknown command:", line[1])
            return 1
        
        elif line[0] == "PNT":
            self.PNT()
            return 1

        elif line[0] == "DEF":
            if line[1] == "FNC":
                self.FNC(str(line[2]), True, int(line[3]), x)
                return int(line[3]) + 1
            else:
                raise Exception("unknown command:", line[1])

        elif line[0] == "EXE":
            if line[1] == "FNC":
                self.FNC(str(line[2]), False)
                return 1
            else:
                raise Exception("unknown command:", line[1])

        elif line[0] == "IFF":
            self.IFF(line[1:])
            return 1

        elif line[0] == "IMP":
            self.IMP()
            return 1

        elif line[0] == "WHL":
            self.WHL(line)
            return 1

        elif line[0] == "EXT":
            self.EXT(line)
        
        else: return 1
        
# opens program.txt and makes in into a 2d array bz lines and insteuctions
def get_lst(name):
    with open(str(name), 'r') as file:
        line_lst = file.readlines()
        return [line.split() for line in line_lst]

# gets the lenght of program.txt in lines   
def get_length(name):
    with open(name, 'r') as file:
        return len(file.readlines())

# houses the head which reads the lines and sends them to lang.run_line()
# evaluetes when the program will end, if there isnt a EXT instruction
def main():
    lang = Lang()
    running = True
    x = 0
    lst = get_lst("program.txt")
    lenght = get_length("program.txt")
    # main loop checking for empty lines and sending lines to be executed
    while running is True:
        if lst[x] == "":
            pass
        else:
            x += lang.run_line(lst[x], x)
            
        if x >= lenght:
            running = False
            print("koniec")

main()













    
