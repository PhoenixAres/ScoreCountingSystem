import random
from math import ceil

class STU:
    def read(self, ls):
        self.__ID = ls[0]
        self.__NAME = ls[1]
        self.__CLASS = ls[2]
        self.__SCORE = []
        for i in range(3, 6):
            self.__SCORE.append(int(ls[i]))
    def generate(self):
        self.__CLASS = 'B18'
        x = random.randint(1, 20)
        if 1 <= x < 10:
            self.__CLASS += '0' + str(x)
        else:
            self.__CLASS += str(x)
        x = random.randint(1, 20)
        if 1 <= x < 10:
            self.__CLASS += '0' + str(x)
        else:
            self.__CLASS += str(x)
        self.__ID = self.__CLASS
        x = random.randint(1, 40)
        if 1 <= x < 10:
            self.__ID += '0' + str(x)
        else:
            self.__ID += str(x)
        x = random.randint(3, 5)
        self.__NAME = ''
        for i in range(0, x):
            y = random.randint(0, 25)
            self.__NAME += chr(97+y)
        self.__SCORE = []
        for i in range(2):
            x = random.randint(40, 100)
            self.__SCORE.append(x)
        x = random.randint(57, 100)
        if x == 57:
            x = -1
        self.__SCORE.append(x)
    def cal(self):
        if self.__SCORE[2] == -1:
            self.__SCORE.append(-1)
        elif self.__SCORE[1] == 0:
            self.__SCORE.append(ceil(0.3*self.__SCORE[0] + 0.7*self.__SCORE[2]))
        else:
            self.__SCORE.append(ceil(0.3*self.__SCORE[1] + 0.6*self.__SCORE[2] + 0.1*self.__SCORE[0]))
        self.__ori = self.__ID + ' ' + self.__NAME + ' ' + self.__CLASS
        for i in self.__SCORE:
            self.__ori += ' ' + str(i)
        self.__ori += '\n'
    def __lt__(self, other):
        if self.__SCORE[-1] == other.__SCORE[-1]:
            return self.__SCORE[-2] > other.__SCORE[-2]
        return self.__SCORE[-1] > other.__SCORE[-1]
    def GetTotalGrade(self):
        return self.__SCORE[-1]
    def GetFinalGrade(self):
        return self.__SCORE[-2]
    def GetID(self):
        return self.__ID
    def GetStr(self):
        return self.__ori