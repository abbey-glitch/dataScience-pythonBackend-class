import re
# function in regex
# 1) findall: returns a list containing all matches
# 2) search: returns a match object
# 3) split: returns a list where the string has been split 
# 4) sub: replaces one or many matches with a string
# txt = "the rain in spain"
# x = re.search("portugal", txt)
# if x:
#     print("the space is found: ", x.start())
# else:
#     raise TypeError("not a match")
# y= re.split("\s", txt, 1)
# print(y)
# z = re.sub("\s", "9", txt, 1)
# print(z.group())
profiles = ["john", "kemi", "mathew", "chisom"]
username = input("username: ")
for profile in profiles:
    if (re.search(str(username), profile, re.IGNORECASE)):
        print('true')
        break;
else:
    raise TypeError("username not a match")