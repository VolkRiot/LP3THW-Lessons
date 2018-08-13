
def print_two(*args):
    arg1, arg2 = args
    print(f'arg1: {arg1}, arg2: {arg2}')


def print_void():
    print('nothing to print')


print_two('Misha', 'Met')
print_void()
