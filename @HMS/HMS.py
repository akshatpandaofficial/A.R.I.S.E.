def getdate():
    import datetime
    return datetime.datetime.now()
time = str(getdate())


print('Welcome to your personal Health Management System')
client = input('Enter your name:')
operation = input('Would you like to retrieve data or log it in:')
datatype = input('Would you like diet data or exercise data:')

def health_management_system(client):
    if operation == 'log':
        if datatype == 'diet':
            food = input('enter your food name:')
            quantity = input('enter your intake quantity:')
            with open('{name}_{data_type}'.format(name = client, data_type = datatype), 'a') as f:
                f.write('[')
                f.write(time)
                f.write(']')
                f.write(',')
                f.write(food)
                f.write(',')
                f.write(quantity)
                f.write('\n')
            permission = input('do you have anything else to log:')
            if permission == 'yes':
                while permission == 'yes':
                    food = input('enter your food name:')
                    quantity = input('enter your intake quantity:')
                    with open('{name}_{data_type}'.format(name=client, data_type=datatype), 'a') as f:
                        f.write('[')
                        f.write(time)
                        f.write(']')
                        f.write(',')
                        f.write(food)
                        f.write(',')
                        f.write(quantity)
                        f.write('\n')
                    permission = input('do you have anything else to log:')
        elif datatype == 'exercise':
            exercise = input('enter your exercise name:')
            number_of_sets = input('enter number of sets completed:')
            with open('{name}_{data_type}'.format(name = client, data_type = datatype), 'a') as f:
                f.write('[')
                f.write(time)
                f.write(']')
                f.write(',')
                f.write(exercise)
                f.write(',')
                f.write(number_of_sets)
                f.write('\n')
            permission = input('do you have anything else to log:')
            if permission == 'yes':
                while permission == 'yes':
                    exercise = input('enter your exercise name:')
                    number_of_sets = input('enter number of sets completed:')
                    with open('{name}_{data_type}'.format(name=client, data_type=datatype), 'a') as f:
                        f.write('[')
                        f.write(time)
                        f.write(']')
                        f.write(',')
                        f.write(exercise)
                        f.write(',')
                        f.write(number_of_sets)
                        f.write('\n')
                    permission = input('do you have anything else to log:')
    elif operation == 'retrieve':
        if datatype == 'diet':
            with open('{name}_{data_type}'.format(name = client, data_type = datatype), 'r') as f:
                print(f.read())
        elif datatype == 'exercise':
            with open('{name}_{data_type}'.format(name = client, data_type = datatype), 'r') as f:
                print(f.read())
health_management_system(client)