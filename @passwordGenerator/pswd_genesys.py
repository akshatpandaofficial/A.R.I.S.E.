lalpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ualpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
special_char_list = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
int_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

from random import randint

# this function generates password by taking inputs as length,number of ints,alphabets(UPPER and lower) and special characters and prints it at the end
def pswd_gen():
    password = []
    global pswd
    pswd = ''
    randomizing_list = []
    global url
    url = input('enter url or name of system:')
    length = int(input('enter length of password:'))
    n_spchar = int(input('enter number of special characters:'))
    n_int = int(input('enter number of integers:'))
    n_ualpha = int(input('enter number of UPPERCASE alphabets:'))
    n_lalpha = int(input('enter number of LOWERCASE alphabets:'))
    if n_int > 0:
        randomizing_list.append('int')
    if n_lalpha > 0:
        randomizing_list.append('lalpha')
    if n_ualpha > 0:
        randomizing_list.append('ualpha')
    if n_spchar > 0:
        randomizing_list.append('spchar')

    if length < n_spchar + n_int + n_ualpha + n_lalpha:
        print('exceeding length of password')
    elif length > n_spchar + n_int + n_ualpha + n_lalpha:
        print('undermining length of password')
    else:
        while len(randomizing_list) > 0:
            ingredient = randomizing_list.pop(randint(0, len(randomizing_list) - 1))
            if ingredient == 'int':
                while n_int > 0:
                    password.append(int_list[randint(0, len(int_list) - 1)])
                    n_int = n_int - 1
            elif ingredient == 'lalpha':
                while n_lalpha > 0:
                    password.append(lalpha_list[randint(0, len(lalpha_list) - 1)])
                    n_lalpha = n_lalpha - 1
            elif ingredient == 'ualpha':
                while n_ualpha > 0:
                    password.append(ualpha_list[randint(0, len(ualpha_list) - 1)])
                    n_ualpha = n_ualpha - 1
            elif ingredient == 'spchar':
                while n_spchar > 0:
                    password.append(special_char_list[randint(0, len(special_char_list) - 1)])
                    n_spchar = n_spchar - 1
        while len(password) > 0:
            real_ingredient = password.pop(randint(0, len(password) - 1))
            pswd = pswd + real_ingredient
    print(url+':'+pswd)

# this function adds the password to a textfile database as <url:password> format
def add_to_database():
    with open('pswd_database.txt', 'a') as f:
        f.write(f'{url}:{pswd}\n')

# this function deletes a password from database on command input of url
def delete_from_database():
    url = input('enter url or name of system:')
    with open('pswd_database.txt','r') as f:
        result_list = f.readlines()
        for i in result_list:
            if i.split('\n')[0].split(':')[0] == url:
                result_list.remove(i)
                break
    with open('pswd_database.txt','w') as f:
        f.writelines(result_list)

# this function changes password linked to a url on command input of url
def change_from_database():
    with open('pswd_database.txt', 'r') as f:
        result_list = f.readlines()
        for i in range(len(result_list)):
            if result_list[i].split('\n')[0].split(':')[0] == url:
                result_list[i] = f'{url}:{pswd}\n'
                break
    with open('pswd_database.txt','w') as g:
        g.writelines(result_list)

# this function reads a url and its password on command input of url
def read_from_databse():
    url = input('enter url or name of system:')
    with open('pswd_database.txt', 'r') as f:
        result_list = f.readlines()
        for i in range(len(result_list)):
            if result_list[i].split('\n')[0].split(':')[0] == url:
                print(result_list[i].split('\n')[0])

# this is the main loop of application that runs all functions in a particular order
while True:
    command = input('add or delete or change or read or quit (choose any one):')
    if command == 'add':
        pswd_gen()
        add_to_database()
    elif command == 'delete':
        delete_from_database()
    elif command == 'change':
        pswd_gen()
        change_from_database()
    elif command == 'read':
        read_from_databse()
    elif command == 'quit':
        break