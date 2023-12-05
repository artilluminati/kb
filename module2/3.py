with open('my_name.txt', 'w') as file:
    file.write('Максим\n' * 10000)

with open('my_name.txt', 'r') as file:
    names = file.read().splitlines()

declined_names = [name + 'а' for name in names]

with open('my_name_declined.txt', 'w') as file:
    file.write('\n'.join(declined_names))
