import copy
spam = ['A','B','C','D']
Cheese = copy.copy(spam)
Cheese[1] = 42


print(spam)
print(Cheese)