print('''You enter a dark room with doors 1 and 2. Choose one ''')

door = input('> ')

if door == '1':
    print('There is a giant bear eating a cake')
    print('What do you do?')
    print('1. Take the cake')
    print('2. Scream at the bear')

    bear = input('> ')

    if bear == '1':
        print('Bear eats your face')
    elif bear == '2':
        print('Bear eats your legs off')
    else:
        print(f'Doing {bear} is probably better')
        print('Bear runs away')

elif door == '2':
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input('> ')

    if insanity == '1' or insanity == '2':
        print('Your body survives powered by a mind of jello')
        print('Good job')
    else:
        print('The insanity rots your eyes into a pool of muck')
        print('Good job')

else:
    print("You stumble around and fall on a knife and die. Good job!")
