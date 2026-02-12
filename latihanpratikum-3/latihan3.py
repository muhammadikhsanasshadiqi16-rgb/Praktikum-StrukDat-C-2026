# name chararcter skill and exxcet
class character:
    def __init__(self, char, skill, excess):
        self.char = char 
        self.skill = skill
        self.excess = excess

    def introduce_self(self):
        print(f"char{self.char}, skill{self.skill}, excess{self.excess}")

    def change_char(self, newchar):
        self.char=newchar
        print(f"char {self.char}")

c1=character("goro", "1", "bigpunch" )
c2=character("lapet", "4", "longpunch")
c3=character("lolok", "6", "flypunch")

c1.introduce_self()
c2.introduce_self()
c3.introduce_self()






