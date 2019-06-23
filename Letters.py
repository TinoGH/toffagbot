import random


class Letters:

    def __init__(self, *args):
        self.order = args[0]
        if len(args) == 1:
            self.rec = args[0]
        elif len(args) == 2:
            self.rec = args[1]
        else:
            raise TypeError("expected at most 2 arguments, got {}".format(len(args)))
        self.table = {}
                
    def __str__(self):
        text = "\n"
        for char in self.table.keys():
            text += "\t" * (self.order - self.rec) + char + ": " + str(self.table[char]['iteration']) + str(self.table[char]['table']) + "\n"
        return text
        
    def read_file(self, filename):
        with open(filename, 'r') as myFile:
            text = "".join(myFile.readlines())
        self.read(text)           
        
    def read(self, text):
        for i in range(len(text)):
            chars = text[i:min(i + self.rec, len(text))]
            self.learn(chars)
    
    def learn(self, chars):
        if chars[0] not in self.table.keys():
            self.table[chars[0]] = {'iteration': 0, 'table': Letters(self.order, self.rec - 1)}
        self.table[chars[0]]['iteration'] += 1
        if len(chars) > 1:
            self.table[chars[0]]['table'].learn(chars[1:])
                
    def write(self, length):
        text = ""
        for i in range(length):
            chars = text[max(i - (self.order - 1), 0):i]
            text += self.pick_letter(chars)
        return text
    
    def pick_letter(self, chars):
        if len(chars) == 0:
            cumul = 0
            pick_table = []
            if len(self.table) > 0:
                for char in self.table.keys():
                    cumul += self.table[char]['iteration']
                    pick_table.append((cumul, char))
            else:
                return ' '
            choice = random.randint(1, pick_table[-1][0])
            for i, cumul in enumerate([pick[0] for pick in pick_table]):
                if choice - cumul <= 0:
                    return pick_table[i][1]
        else:
            if chars[0] in self.table.keys():
                return self.table[chars[0]]['table'].pick_letter(chars[1:])
            else:
                return '\n'

