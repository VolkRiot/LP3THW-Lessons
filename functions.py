
def print_two(*args):
    arg1, arg2 = args
    print(f'arg1: {arg1}, arg2: {arg2}')


def print_void():
    print('nothing to print')


print_two('Misha', 'Met')
print_void()


def cheese_and_crackers(cheese, crackers):
    print(f'You have {cheese} cheeses!')
    print(f'You ahve {crackers} crackers')
