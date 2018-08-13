import sys

script, user_name = sys.argv

prompt = '> '

print(f'Hi {user_name}, I am the {script} script')
print(f'Dow you like me {user_name}?')

likes = input(prompt)

print('What kind of computer do you have?')

computer = input(prompt)

print(f"""
Alright so you said you {likes} about liking me.
And you have a {computer} computer. Nice
""")
