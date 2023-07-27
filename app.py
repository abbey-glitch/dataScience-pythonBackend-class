import random
class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second
    
# dice = Dice()
# print(dice.roll())
# for i in range(3):
#     num = random.randint(10, 20)
#     print(num)
# import obj
# fname = obj.Person('tolu')
# fname.talk()
# # fname.talk()
# print(fname)
# import math
# x=2.9
# print(math.floor(x))
# y=-3
# print(round(x))
# print(abs(y))
# fname = "john"
# last = "smith"

# message = fname + ' ['+last+']'+' is a coder'
# msg = f'{fname} [{last}] is a coder'
# print(msg)

# course = 'python for beginners'
# print(course.replace('beginners', 'absolute beginner'))
# print('Python' in course)
# secret_number = 9
# guess_count = 3
# guess_limit = 0
# while guess_limit < guess_count:
#     guess = int(input('Guess: '))
#     guess_limit +=1
#     if(guess == secret_number):
#         print("You won")
#         break;
# else:
#     print("sorry you failed")
# cout_len = [1, 12, 7, 10, 9, -5]
# cout_len.clear()
# print(cout_len)
# max = cout_len[0]
# for num in cout_len:
#     if(num > max):
#         max=num
# print(max)
# for numLen in cout_len:
#     num = ""
#     for i in range(numLen):
#         num += "x"
#         print(num)
#     # print(num)
    
# num = [1, 2, 2, 4, 5, 1, 3]
# uniques = []
# for nun in num:
#     if(nun not in uniques):
#         uniques.append(nun)
# print(uniques)
# uniques.sort()
# uniques.reverse()
# print(uniques)
item = [1, 2, 3]
a,b,c = item
print(c)