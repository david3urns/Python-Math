#import the os to assist with determining terminal width for the banner, and for the clear screen function used by the actual program
import os

#import time to enable sleep()
import time

#import sys to enable the sys.exit() function
import sys

#define variables for banner text color:
color_red = "\033[1;31;40m \n"
color_green = "\033[1;32;40m \n"
color_white = "\033[1;37;40m \n"
color_cyan = "\033[1;36;40m \n"
color_yellow = "\033[1;33;40m \n"

#create the function for the banner, first argument is the text, second is the color variable from above:
def cent_banner(banner_title, banner_color):

    #define variables declaring the ascii art used for the borders:
    horz_border = "═"
    vert_border = "║"
    top_left_corner = "╔"
    top_right_corner = "╗"
    bot_left_corner = "╚"
    bot_right_corner = "╝"

    #get the terminal width for the centering function:
    size = os.get_terminal_size()
    columns = size.columns
    title_len = len(banner_title)

    #determine if the terminal width is an even or odd number, and if odd, make even:
    if (columns % 2) == 0:
        columns = columns
    else:
        columns = columns + 1

    #determine if the banner_title is an odd or even number, and if odd, make even:
    if (title_len % 2) == 0:
        banner_title = banner_title
    else:
        banner_title = banner_title + " "

    #creates box 1/4 the width of the screen:
    banner_width = columns // 4
    if (banner_width % 2) == 0:
        banner_width = banner_width
    else:
        banner_width = banner_width + 1

    #do math to center the banner_title text based on the terminal width:
    banner_mid_space = banner_width - title_len
    banner_mid_space_half = banner_mid_space // 2
    banner_mid_spaces = banner_mid_space_half * " "

    #creates the actual box based on the terminal width:
    banner_top = top_left_corner + horz_border * banner_width + top_right_corner
    banner_mid = vert_border + banner_mid_spaces +  banner_title + banner_mid_spaces + vert_border
    banner_bot = bot_left_corner + horz_border * banner_width + bot_right_corner

    #centers the banner in the terminal window:
    cent_banner_top = banner_top.center(columns)
    cent_banner_mid = banner_mid.center(columns)
    cent_banner_bot = banner_bot.center(columns)

    #print the actual banner:
    print(banner_color)
    print(cent_banner_top)
    print(cent_banner_mid)
    print(cent_banner_bot)
    print(color_white) #resets text color to white so following text won't inherit banner color


#create a function to clear the screen:
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')


#define functions for the arithmetic operations:

#addition function
def addition():
    while True:
        clear_screen()
        cent_banner("Addition", color_cyan)

        try:
            num1 = int(input("Please enter the first number in the problem: "))
            num2 = int(input("Please enter the second number in the problem: "))
        except ValueError:
            print("Invalid input! Please enter an interger.")
            time.sleep(3)
            continue

        result = num1 + num2
        try:
            answer = int(input(f"What is {num1} plus {num2}? "))
        except ValueError:
            print("Invalid input! Please enter an interger")
            time.sleep(3)
            continue

        if answer == result:
            print("Correct!")
        else:
            print("I got a different answer, please check your work and try again.")

        choice = input("Enter 1 to repeat, 2 to return to the main menu, or 3 to exit...")
        if choice == '1':
            clear_screen()
            continue
        elif choice == '2':
            clear_screen()
            break
        elif choice == '3':
            clear_screen()
            sys.exit()
        else:
            print("Invalid input, please enter a number between 1-3")
            time.sleep(5)


#subtraction function
def subtraction():
    while True:
        clear_screen()
        cent_banner("Subtraction", color_cyan)

        try:
            num1 = int(input("Please enter the first number in the problem: "))
            num2 = int(input("Please enter the second number in the problem: "))
        except ValueError:
            print("Invalid input! Please enter an interger.")
            time.sleep(3)
            continue

        result = num1 - num2
        try:
            answer = int(input(f"What is {num1} minus {num2}? "))
        except ValueError:
            print("Invalid input! Please enter an interger.")
            time.sleep(3)
            continue

        if answer == result:
            print("Correct!")
        else:
            print("I got a different answer, please check your work and try again.")

        choice = input("Enter 1 to repeat, 2 to return to the main menu, or 3 to exit...")
        if choice == '1':
            clear_screen()
            continue
        elif choice == '2':
            clear_screen()
            break
        elif choice == '3':
            clear_screen()
            sys.exit()
        else:
            print("Invalid input, please enter a number between 1-3")
            time.sleep(5)

#multiplication function
def multiplication():
    while True:
        clear_screen()
        cent_banner("Multiplication", color_cyan)
        try:
            num1 = int(input("Please enter the first number in the problem: "))
            num2 = int(input("Please enter the second number in the problem: "))
        except ValueError:
            print("Invalid input! Please enter an interger.")
            time.sleep(3)
            continue

        result = num1 * num2

        try:
            answer = int(input(f"What is {num1} times {num2}? "))
        except ValueError:
            print("Invalid input! Please enter an interger.")
            time.sleep(3)
            continue

        if answer == result:
            print("Correct!")
        else:
            print("I got a different answer, please check your work and try again.")

        choice = input("Enter 1 to repeat, 2 to return to the main menu, or 3 to exit...")
        if choice == '1':
            clear_screen()
            continue
        elif choice == '2':
            clear_screen()
            break
        elif choice == '3':
            clear_screen()
            sys.exit()
        else:
            print("Invalid input, please enter a number between 1-3")
            time.sleep(5)

#division function
def division():
    while True:
        clear_screen()
        cent_banner("Division", color_cyan)
        
        try:
            num1 = int(input("Please enter the first number in the problem: "))
            num2 = int(input("Please enter the second number in the problem: "))
        except ValueError:
            print("Invalid input! Please enter an interger.")
            time.sleep(3)
            continue

        try:
            answer = int(input(f"What is {num1} divided by {num2}? "))
            answer_remainder = int(input("What remainder did you have? If you didn't have one, enter 0: "))
        except ValueError:
            print("Invalid input! Please enter an interger.")
            time.sleep(3)
            continue

        result = num1 // num2
        remainder_result = num1 % num2
        if remainder_result == answer_remainder:
            answer = result
        else:
            answer = "invalid"
        if answer == result:
            print("Correct!")
        else:
            print("I got a different answer, please check your work and try again.")

        choice = input("Enter 1 to repeat, 2 to return to the main menu, or 3 to exit...")
        if choice == '1':
            clear_screen()
            continue
        elif choice == '2':
            clear_screen()
            break
        elif choice == '3':
            clear_screen()
            sys.exit()
        else:
            print("Invalid input, please enter a number between 1-3")
            time.sleep(5)

#Main menu function
while True:
    clear_screen()
    cent_banner("Math Checker", color_cyan)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Please enter your selection (1-5): ")

    if choice == '1':
        addition()
    elif choice == '2':
        subtraction()
    elif choice == '3':
        multiplication()
    elif choice == '4':
        division()
    elif choice == '5':
        sys.exit()
    else:
        print("Invalid input, please enter a number between 1-5")
        time.sleep(5)