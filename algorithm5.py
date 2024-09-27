peremennie = ['x', 'y', 'z']
min_form = []
count = -1
for x in range(2):
    for y in range(2):
        for z in range(2):
            if ((bool(not(x)) <= bool(not(y))) <= ((bool(y) and bool(z)) <= (bool(not(x)) and bool(z)))) == 1:
                min_form.append([])
                count += 1
                if x == 1:
                    print('x', end = '')
                    min_form[count].append(1)
                else:
                    print('not(', 'x', ')', end = '', sep = '')
                    min_form[count].append(0)
                if y == 1:
                    print('y', end = '')
                    min_form[count].append(1)
                else:
                    print(' not(', 'y', ')', end = '', sep = '')
                    min_form[count].append(0)
                if z == 1:
                    print('z', end = '')
                    min_form[count].append(1)
                else:
                    print(' not(', 'z', ')', end = '', sep = '')
                    min_form[count].append(0)
                print(' U ', end = '')
print('\n', min_form)
qwe = 0
for i in range(3):
    for j in range(len(min_form)):
        qwe += min_form[j][i]
    if qwe == 4:
        print(peremennie[i], end = '')
    else:
        if len(min_form) - qwe == 4:
            print('not(', peremennie[i], ')', end = '', sep = '')
    qwe = 0


print('\n')
min_form = []
count = -1
for x in range(2):
    for y in range(2):
        for z in range(2):
            if ((bool(not(x)) <= bool(not(y))) <= ((bool(y) and bool(z)) <= (bool(not(x)) and bool(z)))) == 0:
                min_form.append([])
                count += 1
                if x == 0:
                    print('(x U ', end = '')
                    min_form[count].append(1)
                else:
                    print('(not(', 'x', ') U ', end = '', sep = '')
                    min_form[count].append(0)
                if y == 0:
                    print('y U ', end = '')
                    min_form[count].append(1)
                else:
                    print('not(', 'y', ') U ', end = '', sep = '')
                    min_form[count].append(0)
                if z == 0:
                    print('z)', end = '')
                    min_form[count].append(1)
                else:
                    print('not(', 'z', '))', end = '', sep = '')
                    min_form[count].append(0)
                print(' ', end = '')
qwe = 0
for i in range(3):
    for j in range(len(min_form)):
        qwe += min_form[j][i]
    if qwe == 4:
        print('not(', peremennie[i], ')', end = '', sep = '')
    else:
        if len(min_form) - qwe == 4:
            print(peremennie[i], end = '')
    qwe = 0
