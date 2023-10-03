import random

class Player:
    def __init__(self,n:str):
        self.name = n
        self.__dice1 = random.randint(1,6)
        self.__dice2 = random.randint(1,6)
        self.__dice3 = random.randint(1,6)
        self.__dice4 = random.randint(1,6)

class Player:
    def __init__(self):
        pass

    def __play(self) -> int:
        while True:
            dice = [self.__dice1,self.__dice2,self.__dice3,self.__dice4]
            if dice[1] == dice[2] == dice[3] == dice[4]:
                print(f"得分為:score == {}")
                
                break
            elif dice[1] == dice[2] == dice[3] or dice[1] == dice[2] == dice[4]:   
                print("此局作廢")
                continue
            elif dice[1] == dice[3] == dice[4] or dice[2] == dice[3] == dice[4]:   
                print("此局作廢")
                continue
            elif dice[1] == dice[2] and dice[3] == dice[4]:     
                if (dice[1] == dice[2]) > (dice[3] == dice[4]):
                 print(f"得分為:score =={}")
                 return
                



    @property
    def value(self) -> int:
        return self.__play()

    def __repr__(self) -> str:
        descript = ""
        descript += "徐國堂\n"
        descript += "骰子1=5\n"
        descript += "骰子2=3\n"
        descript += "骰子3=5\n"
        descript += "骰子4=5\n"
        dsecript += "得分=15分"
        return descript
    
if __name__ == "__main__":
    p1 = Player("robert")
    print(p1.value)
    print(p1)

    p2 = Player("robert")
    print(p2.value)
    print(p2)

