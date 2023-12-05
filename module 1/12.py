import random

members = []


def rand_separate(arr: list) -> object:
    gr_a = []
    gr_b: list = []
    random.shuffle(arr)
    flag = True
    for i in arr:
        if flag:
            gr_a.append(i)
        else:
            gr_b.append(i)
        flag = not(flag)
    return gr_a, gr_b


def main():
    inval = input()
    while inval != 'stop':
        members.append(inval)
        inval = input()

    print(members)
    if len(members) > 3:
        team_a, team_b = rand_separate(members)

        print(f'Команда А: {team_a}')
        print(f'\n Команда Б: {team_b}')

    else:
        print(f'Все {members}')

if __name__ == "__main__":
    main()
