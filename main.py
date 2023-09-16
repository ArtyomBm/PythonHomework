def output(a):
    for key in a:
        print()
        print(f'Name of the restaurant: {key}')
        print(f'The nubmer of Michelin stars: {a[key][0]}')
        print(f'Average check per person in rubles: {a[key][1]}')
        print(f'Day of may it can be possible to deserve: {a[key][2]}')
        print(f'Cuisine is on the menu: {a[key][3]}')
        print(f'Is there a summer terrace? {a[key][4]}')
        print(f'Minutes for transfer from the city center to the restaurant: {a[key][5]}')

def check(a):
    if len(a) == 1:
        print('We have only 1 restaurant for your selected options')
        output(a)
        b = input('Will you consider him? Yes/No ')
        while b != 'Yes' and b != 'No':
            b = input("Don't understand you. Enter Yes/No ")
        if b == 'No':
            print('We are so sorry for not having suitable restaurants for you. You can try again with other options)')
            exit(0)
        elif b == 'Yes':
            for key in a:
                print(f'Thank you for your reservation at {key} restaurant on {a[key][2]} of May. '
                    f'We are looking forward to seeing you.')
                exit(0)

name = {'The Grill House': [2, 1500, 11, 'Russian', 'Yes', 4], 'The Diner': [1, 1300, 13, 'French', 'No', 15],
'The Bistro': [2, 1700, 12, 'Russian', 'Yes', 11], 'The Café': [1, 1500, 12, 'Russian', 'No', 3],
'The Corner Kitchen': [1, 1700, 11, 'French', 'No', 5], 'The Kitchen Table': [2, 1300, 11, 'Russian', 'Yes', 14],
'The Local': [1, 1500, 13, 'French', 'No', 6], 'The Spot': [2, 1700, 12, 'Russian', 'No', 7],
'The Nook': [2, 1300, 13, 'Russian', 'Yes', 8], 'The Fork': [1, 1300, 12, 'Russian', 'No', 9],
'The Spoon': [2, 1500, 11, 'French', 'Yes', 10], 'The Cookhouse': [1, 1700, 12, 'French', 'No', 11],
'The Griddle': [2, 1300, 13, 'Russian','Yes', 12], 'The Pantry': [2, 1700, 12, 'French', 'Yes', 13]}
"""For each key list of characteristics is a list, which includes information about the number of Michelin 
stars this restaurant has, average check per person in rubles, on what day of may it can be possible to reserve 
a table, how many hours it can be possible to reserve a table for, what cuisine is on the menu, is there a summer 
terrace and minutes for transfer from the city center to the restaurant"""
name1 = {}
print('Hello')
while not name1:
    a = int(input('When do you want to arrive? Please, enter the date from 11, 12 or 13 of May '))
    for key in name:
        if name[key][2] == a:
            name1[key] = name[key]
    if not name1:
        b = input(f'Sorry, all tables are occupied on {a} of May. '
                 f'Do you want to specify another date? Yes/No ')
        while b != 'Yes' and b != 'No':
            b = input("Don't understand you. Please enter Yes/No ")
        if b == 'No':
            print('We are so sorry for not having suitable restaurants for you. You can try again with other options)')
            exit(0)
name2 = {}
while not name2:
    a = int(input('How many Michelin stars does the restaurant need to have? Please, enter the number 1 or 2 '))
    for key in name1:
        if name1[key][0] == a:
            name2[key] = name1[key]
    if not name2:
        print(f'Sorry, there are no available restaurants this day with {a} Michelin stars.')
        b = input('Do you want to specify another number of Michelin stars? Yes/No ')
        while b != 'Yes' and b != 'No':
            b = input("Don't understand you. Please enter Yes/No ")
        if b == 'No':
            print('We are so sorry for not having suitable restaurants for you. You can try again with other options)')
            exit(0)
name3 = {}
a = input('Which cuisine do you prefer? Choose and enter between Russian and French cuisines ')
for key in name2:
    if name2[key][3] == a:
        name3[key] = name2[key]
if not name3:
    print(f'Sorry, there are no available restaurants with {a} cuisine and previously selected options.')
    b = ('We can offer you some restaurants with another cuisine, will you consider them? Yes/No ')
    while b != 'Yes' and b != 'No':
        b = input("Don't understand you. Please enter Yes/No ")
    if b == 'No':
        print('We are so sorry for not having suitable restaurants for you. You can try again with other options)')
        exit(0)
    else:
        if a == 'Russian':
            for key in name2:
                if name2[key][3] == 'French':
                    name3[key] = name2[key]
        elif a == 'French':
            for key in name2:
                if name2[key][3] == 'Russian':
                    name3[key] = name2[key]
check(name3)
name4 = {}
a = input('Is it vital for restaurant to have summer terrace? Yes/No ')
for key in name3:
    if name3[key][4] == a:
        name4[key] = name3[key]
if not name4:
    if a == 'No':
        b = input('Sorry, all the restaurants with summer terrace, will you consider them? Yes/No ')
        while b != 'Yes' and b != 'No':
            b = input("Don't understand you. Please enter Yes/No ")
        if b == 'No':
            print('We are so sorry for not having suitable restaurants for you. You can try again with other options)')
            exit(0)
        else:
            for key in name3:
                if name3[key][4] == 'Yes':
                    name4[key] = name3[key]
    elif a == 'Yes':
        b = input('Sorry, all the restaurants without summer terrace, will you consider them? Yes/No ')
        while b != 'Yes' and b != 'No':
            b = input("Don't understand you. Please enter Yes/No ")
        if b == 'No':
            print('We are so sorry for not having suitable restaurants for you. You can try again with other options)')
            exit(0)
        else:
            for key in name3:
                if name3[key][4] == 'No':
                    name4[key] = name3[key]
check(name4)
name5 = {}
b = str()
for key in name4:
    b += str(name4[key][5])
    b += ' '
print(f'There are only restaurants with following number of minutes for transfer '
      f'from the city center to restaurant: {b}')
b = input('Do you want to choose specific variants? Yes/No ')
while b != 'Yes' and b != 'No':
    b = input("Don't understand you. Please enter Yes/No ")
if b == 'No':
    d = input('All the minutes are right for you or none? All/None ')
    while d != 'All' and d != 'None':
        d = input("Don't understand you. Please enter All/None ")
    if d == 'All':
        name5 = name4
    else:
        print('We are so sorry for not having suitable restaurants for you. You can try again with other options)')
        exit(0)
else:
    c = []
    for i in input(f'Enter one or more minutes among {b} that suits you. Example: 1 2 3 4').split():
        for j in c:
            for key in name4:
                if name4[key][5] == j:
                    name[5] = name[4]
check(name5)
name6 = {}
while not name6:
    a = int(input('What check per person in rubles do you prefer? Please choose and enter 1300, 1500 or 1700 '))
    for key in name5:
        if name5[key][1] == a:
            name6[key] = name5[key]
    if not name6:
        print(f'Sorry, there are no restaurants with {a} rubles check per person')
        b = input('Do you want to choose another check? Yes/No ')
        while b != 'Yes' and b != 'No':
            b = input("Don't understand you. Please enter Yes/No ")
        if b == 'No':
            print('We are so sorry for not having suitable restaurants for you. You can try again with other options)')
            exit(0)
print('We have final list of restaurants for you:')
output(name6)
print()
b = input('Choose one of the restaurants and enter its name ')
while b not in name6.keys():
    b = input('Please enter correct name of the restaurant ')
for key in name6:
    if key == b:
        print(f'Thank you for your reservation at {key} restaurant on {name6[key][2]} of May. '
              f'We are looking forward to seeing you.')