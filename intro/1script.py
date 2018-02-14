print('hello world')

print('what is your name?')

myName=input()

if myName != '':
    print('nice to meet you')
else:
    print('dupa')

print('the lenght of your name is: '+ str(len(myName)))

print('what is you age?')
myAge=input()

print('your age will be '+ str(int(myAge)+1)+ ' in a year')

if myName == 'Alice':
    print('hi ' + myName)
