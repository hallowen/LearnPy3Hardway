from sys import argv

script, user_name = argv
prompt = '>'

print("Hi {}, I am the  {} script".format(user_name, script))
print("I'd like to ask you few questions")
print("Do you like me {}".format(user_name))
likes = input(prompt)

print("Where do you live {}".format(user_name))
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("So you said {} likes about me. You live in {}. Not sure where that is. And you have a {} computer. Nice".format(likes, lives,computer))
