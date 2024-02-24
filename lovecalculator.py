name1= input("what is your name ?")
name2= input("what is his/her name ?")

combine= name1 + name2
lower_case= combine.lower()

t = lower_case.count('t')
r = lower_case.count('r')
u = lower_case.count('u')
e = lower_case.count('e')

l = lower_case.count('l')
o = lower_case.count('o')
v = lower_case.count('v')
e = lower_case.count('e')


true= t+r+u+e
love= l+o+v+e

love_score = str(true) + str(love)

print(f"your love score is {love_score}")
#this is a new change
#version 3