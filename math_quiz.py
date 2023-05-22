#import the os to assist with determining terminal width for the banner, and for the clear screen function used by the actual program
import os

#import time to enable sleep()
import time

#import sys to enable the sys.exit() function
import sys

#import random to assign random intergers for problems
import random

#define variables for banner text color:
color_red = "\033[1;31;40m \n"
color_green = "\033[1;32;40m \n"
color_white = "\033[1;37;40m \n"
color_cyan = "\033[1;36;40m \n"
color_yellow = "\033[1;33;40m \n"

#create the function for the banner, first argument is the text printed in the banner, second is the color variable from above:
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


#define global variable for correct question count and total question count:
global_correct = 0
global_total = 0

#create the function to increase the count of global_correct:
def correct_count():
    global global_correct
    global_correct += 1

#create the function to create a counter for the total number of questions answered:
def total_count():
    global global_total
    global_total += 1

#create a function to print the number correct out of the number of total questions:
def print_progress():
    global global_correct
    global global_total
    percent_correct = global_correct / global_total * 100
    #rounded_percent = (str(round(percent_correct, 2)))
    #the :.2f rounds the percentage to 2 decimal places, eliminating the need for the above rounded_percent variable
    print(f"You have answered a total of {global_total} questions, of which you have answered {global_correct} correctly for a score of {percent_correct:.2f}%.") 
    

#create a function to clear the screen:
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

#define functions for the arithmetic operations:

#addition function
def addition():
    while True:
        clear_screen()
        cent_banner("Addition", color_cyan)

        #ask the user if they want single or single and double digit problems
        digit_choice = input("Do you want single digit or single and double digit problems? (Enter 1 or 2): ")
        
        #assign random intergers to num1 and num2
        if digit_choice == '1':
            num1 = random.randint(1,10)
            num2 = random.randint(1,10)

        elif digit_choice == '2':
            num1 = random.randint(11,99)
            num2 = random.randint(11,99)

        else:
            print("Invalid input, please enter a 1 or a 2.")
            time.sleep(3)
            continue
                   
        try:
            answer = int(input(f"What is {num1} + {num2}? "))
        except ValueError:
            print("Invalid input! Please enter an interger.")
            time.sleep(3)
            continue
        #calculate the result
        result = num1 + num2
        if answer == result:
            print("Correct!")
            #add count to correct answer counter
            correct_count()
            #add count to attempts
            total_count()
        else:
            print("I got a different answer, please check your work and try again.")
            #add count to attempts
            total_count()

        choice = input("Enter 1 to repeat, 2 to return to the main menu, or 3 to exit...")
        if choice == '1':
            clear_screen()
            print_progress()
            time.sleep(3)
            continue
        elif choice == '2':
            clear_screen()
            print_progress()
            time.sleep(3)
            break
        elif choice == '3':
            clear_screen()
            print("Thank you for playing!")
            time.sleep(3)
            print_progress()
            time.sleep(3)
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

        #ask the user if they want single or single and double digit problems
        digit_choice = input("Do you want single digit or single and double digit problems? (Enter 1 or 2): ")
        
        #assign random intergers to num1 and num2
        if digit_choice == '1':
            while True:
                num1 = random.randint(1,10)
                num2 = random.randint(1,10)
                if num2 <= num1:
                    break

        elif digit_choice == '2':
            while True:
                num1 = random.randint(11,99)
                num2 = random.randint(11,99)
                if num2 <= num1:
                    break

        else:
            print("Invalid input, please enter a 1 or a 2.")
            time.sleep(3)
            continue

        try:
            answer = int(input(f"What is {num1} - {num2}? "))
        except ValueError:
            print("Invalid input! Please enter an interger.")
            time.sleep(3)
            continue
        #calculate the result
        result = num1 - num2
        if answer == result:
            print("Correct!")
            correct_count()
            total_count()
        else:
            print("I got a different answer, please check your work and try again.")
            total_count()

        choice = input("Enter 1 to repeat, 2 to return to the main menu, or 3 to exit...")
        if choice == '1':
            clear_screen()
            print_progress()
            time.sleep(3)
            continue
        elif choice == '2':
            clear_screen()
            print_progress()
            time.sleep(3)
            break
        elif choice == '3':
            clear_screen()
            print("Thank you for playing!")
            time.sleep(3)
            clear_screen()
            print_progress()
            time.sleep(3)
            sys.exit()
        else:
            print("Invalid input, please enter a number between 1-3")
            time.sleep(5)


#multiplication function
def multiplication():
    while True:
        clear_screen()
        cent_banner("Multiplication", color_cyan)

        #ask the user if they want single or single and double digit problems
        digit_choice = input("Do you want single digit or single and double digit problems? (Enter 1 or 2): ")
        
        #assign random intergers to num1 and num2
        if digit_choice == '1':
            num1 = random.randint(1,10)
            num2 = random.randint(1,10)

        elif digit_choice == '2':
            num1 = random.randint(11,99)
            num2 = random.randint(11,99)

        else:
            print("Invalid input, please enter a 1 or a 2.")
            time.sleep(3)
            continue
         
        try:
            answer = int(input(f"What is {num1} * {num2}? "))
        except ValueError:
            print("Invalid input! Please enter an interger.")
            time.sleep(3)
            continue
        #calculate the result
        result = num1 * num2
        if answer == result:
            print("Correct!")
            correct_count()
            total_count()
        else:
            print("I got a different answer, please check your work and try again.")
            total_count()

        choice = input("Enter 1 to repeat, 2 to return to the main menu, or 3 to exit...")
        if choice == '1':
            clear_screen()
            print_progress()
            time.sleep(3)
            continue
        elif choice == '2':
            clear_screen()
            print_progress()
            time.sleep(3)
            break
        elif choice == '3':
            clear_screen()
            print("Thank you for playing!")
            time.sleep(3)
            clear_screen()
            print_progress()
            time.sleep(3)
            sys.exit()
        else:
            print("Invalid input, please enter a number between 1-3")
            time.sleep(5)

#division function
def division():
    while True:
        clear_screen()
        cent_banner("Division", color_cyan)

        #ask the user if they want single or single and double digit problems
        digit_choice = input("Do you want single digit or single and double digit problems? (Enter 1 or 2): ")
        
        #assign random intergers to num1 and num2
        if digit_choice == '1':
            num1 = random.randint(1,10)
            num2 = random.randint(1,num1)

        elif digit_choice == '2':
            num1 = random.randint(11,99)
            num2 = random.randint(11,num1)

        else:
            print("Invalid input, please enter a 1 or a 2.")
            time.sleep(3)
            continue

        try:
            answer = int(input(f"What is {num1} / {num2}? "))
            answer_rem = int(input("What remainder do you have, enter 0 if no remainder: "))
        except ValueError:
            print("Invalid input! Please enter an interger.")
            time.sleep(3)
            continue
        #calculate the result
        result = num1 // num2
        result_rem = num1 % num2
        if answer == result and answer_rem == result_rem:
            print("Correct!")
            correct_count()
            total_count()
        else:
            print("I got a different answer, please check your work and try again.")
            total_count()

        choice = input("Enter 1 to repeat, 2 to return to the main menu, or 3 to exit...")
        if choice == '1':
            clear_screen()
            print_progress()
            time.sleep(3)
            continue
        elif choice == '2':
            clear_screen()
            print_progress()
            time.sleep(3)
            break
        elif choice == '3':
            clear_screen()
            print("Thank you for playing!")
            time.sleep(3)
            clear_screen()
            print_progress()
            time.sleep(3)
            sys.exit()
        else:
            print("Invalid input, please enter a number between 1-3")
            time.sleep(5)

#Main menu function
while True:
    clear_screen()
    cent_banner("Math Quiz", color_cyan)
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
        clear_screen()
        print("Thank you for playing!")
        time.sleep(3)
        clear_screen()
        print_progress()
        time.sleep(3)
        sys.exit()
    else:
        print("Invalid input, please enter a number between 1-5")
        time.sleep(5)



