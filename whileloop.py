numbers = []


def run_while(num):
    i = 0
    while i < num:
        print(f'At the top i is {i}')
        numbers.append(i)
        i = i + 1
        print('Numbers now: ', numbers)


run_while(6)

for num in numbers:
    print(f'Number is {numbers}')
