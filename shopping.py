#!/usr/bin/python

production_list = [
    ('iphone', 8000),
    ('mac pro', 9800),
    ('coffee',30),
    ('roy',2000)
]
shooping_list = []
salary = raw_input("Input your salary:")

if salary.isdigit():
    salary = int(salary)
    while True:
        for index, item in enumerate(production_list):
            print(index,item)
        user_input = raw_input("buy?>>>:")
        if user_input.isdigit():
            user_input = int(user_input)
            if user_input < len(production_list) and user_input >= 0:
                p_item = production_list[user_input]
                if p_item[1] <= salary:
                    shooping_list.append(p_item)
                    salary -= p_item[1]
                    print ("Added %s into shopping cart, your current balance is \033[31;1m%s\033[0m" %(p_item,salary))
                else:
                    print("\033[41:1m your money is [%s],can't buy \033[0m" %salary)
            else:
                print("production [%s] is not exsit")
        elif user_input == 'q':
            print ("------shopping list-------")
            for p in shooping_list:
                print (p)
            print ("Your current balance is :", salary)
            exit()
        else:
            print('invalid option')

