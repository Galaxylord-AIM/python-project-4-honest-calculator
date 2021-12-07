# # write your code here
# # message list
# msg_0 = "Enter an equation"
# msg_1 = "Do you even know what numbers are? Stay focused!"
# msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
# msg_3 = "Yeah... division by zero. Smart move..."
# msg_4 = "Do you want to store the result? (y / n):"
# msg_5 = "Do you want to continue calculations? (y / n):"
# # variable initialisation
# result = 0  # output of the calc
# memory = 0
# x, y = 0, 0
# while True:
#     print(memory)
#     # while loop to get inputs
#     while True:
#         print(msg_0)
#         calc = input()
#         calc = calc.split(' ')
#         # checking the variables
#         print(calc)
#         try:
#             x, oper, y = (calc[0]), calc[1], (calc[2])  # splitting the variables
#             # checking for "M"
#             if x == 'M':
#                 x = memory
#             elif y == 'M':
#                 y = memory
#             # checking for number
#             else:
#                 x, y = float(calc[0]), float(calc[2])
#
#             # checking operator
#             print(y)
#             if oper == "+":
#                 result = x + y
#                 break
#             elif oper == "-":
#                 result = x - y
#                 break
#             elif oper == "/":
#                 if (oper == "/") and (y == 0):
#                     print(msg_3)
#                     continue
#                 result = x / y
#                 break
#             elif oper == "*":
#                 result = x * y
#                 break
#             else:
#                 print(msg_2)
#         except ValueError:
#             print(msg_1)
#
#     outcome = 0
#     temp = str(result)
#     print(temp)
#     test_result = temp.split('.')
#     print(test_result)
#     if test_result[1] == '0':
#         print(int(test_result[0]))
#
#     print(result)
#
#     # saving calculation
#     while True:
#         print(msg_4)
#         answer = input()
#         if answer == "y":
#             memory = result
#             # print(memory)
#             break
#         elif answer == "n":
#             break
#
#     # continuing calculation
#     while True:
#         print(msg_5)
#         answer = input()
#         if answer == "y":
#             break
#         elif answer == "n":
#             exit(0)


# start
memory = 0
result = 0

# message list
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
while True:
    # print(memory)
    while True:
        print(msg_0)
        calc = input()
        # print("input check", calc)
        calc_split = calc.split(" ")
        # print('split check', calc_split)
        x, oper, y = calc_split[0], calc_split[1], calc_split[2]
        # print('y =', y)
        # print('operator =', oper)
        # print('x =', x)

        if x == 'M':
            x = memory
            # print('value changed for x = ', x)
        elif y == 'M':
            y = memory
            # print(type(y))
            # print('value changed for y = ', y)
        else:
            try:
                x, y = float(x), float(y)
                # print(type(x), type(y))
                # print(x, y)
                # if float(x) == int(x):
                #     x = int(x)
                # else:
                #     x = float(x)
                # if float(y) == int(y):
                #     y = int(y)
                # else:
                #     y = float(y)
                # print(type(x), '--->', x)
                # print(type(y), '--->', y)
            except ValueError:
                print(msg_1)
        if (oper == "+") or (oper == "-") or (oper == "*") or (oper == "/"):
            if oper == "+":
                result = float(x) + float(y)
                # print(result)
                break
            elif oper == "-":
                result = x - y
                # print(result)
                break
            elif oper == "*":
                result = x * y
                # print(result)
                break
            else:
                if (oper == "/") and (y == 0):
                    print(msg_3)
                    continue
                else:
                    result = x / y
                    # print(result)
        else:
            print(msg_2)
    # if float(result) == int(result):
    #     result = int(result)
    # else:
    #     result = float(result)
    print(result)
    while True:
        # print(memory)
        print(msg_4)
        answer = input()
        if answer == 'y':
            memory = result
            # print(result)
            # print(memory)
            break
        elif answer == 'n':
            break

    while True:
        print(msg_5)
        answer = input()
        if answer == 'y':
            break
        elif answer == 'n':
            exit(0)
