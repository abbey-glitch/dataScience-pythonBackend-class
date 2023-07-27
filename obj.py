class Person:
    def __init__(self, name) -> None:
        self.name=name
    def talk(self):
       print(f'hi! i am {self.name}')

class Management(Person):
    def position(self):
        print(f"a software")
# john = Person('mary')
# mng = Management("ade")
# mng.talk()
# print(mng)

# print(john)