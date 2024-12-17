# heimdall.py
# BadBytePunk
# 2024-12-16

""" +++ HEIMDALL password generator version 1.0 by BadBytePunk +++ """
# Customizable strong password generator with input validation
# This program allows the user to generate strong passwords of a custom length and quantity,
# ensuring the password length is at least 8 characters and the quantity is a positive integer.

# IMPORT NECESSARY MODULES
import secrets  # Provides cryptographically secure random numbers suitable for managing data such as passwords, account authentication, and security tokens.
import string   # Provides a collection of string constants (such as all letters, digits, punctuation) and utility functions to manipulate strings.
import getpass  # Allows you to securely handle password input without echoing it on the screen.
import os       # Provides a way of using operating system-dependent functionality like reading or writing to the file system.
import time     # Provides various time-related functions, such as sleeping for a specified duration.


""" --- CLEAR SCREEN --- """
# FUNCTION CLEAR SCREEN
def clear_screen():
    # Detect Operating System
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux & macOS 
        os.system('clear')
# Call the clear screen funciton
clear_screen()


""" --- AINSI COLOR CODES --- """
def colorize(text, color):  # define a function named colorize
    """ Applies color to text using ANSI codes. This includes:

    Colors: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, and WHITE

    Reset code to prevent color or style propagation (RESET)

    Args:
        - text (str): The text to color.
        - color (str): The ANSI color code.

    Returns:
        - str: The colorized text.
    """
    # ANSI color codes dictionary
    colors = {
        # ANSI COLOR CODES
        'RESET': '\033[0m',       # reset color
        'BLACK': '\033[30m',      # black color
        'RED': '\033[91m',        # red color
        'GREEN': '\033[32m',      # green color
        'YELLOW': '\033[33m',     # yellow color
        'BLUE': '\033[34m',       # blue color
        'MAGENTA': '\033[35m',    # magenta color    
        'CYAN': '\033[36m',       # cyan color
        'WHITE': '\033[37m',      # white color       
        # ANSI COLOR STYLE CODES FOR BOLD & UNDERLINE
        'BOLD': '\033[1m',        # bold style
        'UNDERLINE': '\033[4m',   # underline style
    }
    return colors.get(color, colors['RESET']) + text + colors['RESET']  # retreives ANSI code for the given color
                                                                        # (or uses RESET if the color is not found) and
                                                                        # concatanates it with the text. The RESET code
                                                                        # to ensure the color does not propagate

""" --- DISPLAY TITLE AND HEADER --- """
# FUNCTION TO DISPLAY, CENTER & COLORIZE THE TITLE
def display_title():    # Declare a function to display title
    console_wide_lenght = 84    # Define console wide lneght
    new_line ="\n"  # Add a new line
    colored_sub_title = colorize(colorize("password(s) generator".center(console_wide_lenght), 'WHITE'), 'BOLD')
    colored_author_name = colorize(colorize(" BadBytePunk".center(console_wide_lenght), 'GREEN'), 'BOLD')
    colored_header_full_up = colorize(colorize("ᚠᚢᚦᚨᚱᚲᚷᚹᚺᚾᛁᛃᛇᛈᛉᛋᛏᛒᛖᛗᛚᛜᛞᛟᚠᚢᚦᚨᚱᚲᚷᚹᚺᚾᛁᛃᛇᛈᛉᛋᛏᛒᛖᛗᛚᛜᛞᛟᚠᚢᚦᚨᚱᚲᚷᚹᚺᚾᛁᛃᛇᛈᛉᛋᛏᛒᛖᛗᛚᛜᛞᛟ".center(console_wide_lenght),'WHITE'),'BOLD')
    colored_header_full_down = colorize(colorize("ᚠᚢᚦᚨᚱᚲᚷᚹᚺᚾᛁᛃᛇᛈᛉᛋᛏᛒᛖᛗᛚᛜᛞᛟᚠᚢᚦᚨᚱᚲᚷᚹᚺᚾᛁᛃᛇᛈᛉᛋᛏᛒᛖᛗᛚᛜᛞᛟᚠᚢᚦᚨᚱᚲᚷᚹᚺᚾᛁᛃᛇᛈᛉᛋᛏᛒᛖᛗᛚᛜᛞᛟ".center(console_wide_lenght),'WHITE'),'BOLD')
    colored_ascii_title = colorize(colorize("""
    $$\   $$\ $$$$$$$$\ $$$$$$\ $$\      $$\ $$$$$$$\   $$$$$$\  $$\       $$\  
    $$ |  $$ |$$  _____|\_$$  _|$$$\    $$$ |$$  __$$\ $$  __$$\ $$ |      $$ |
    $$ |  $$ |$$ |        $$ |  $$$$\  $$$$ |$$ |  $$ |$$ /  $$ |$$ |      $$ |
    $$$$$$$$ |$$$$$\      $$ |  $$\$$\$$ $$ |$$ |  $$ |$$$$$$$$ |$$ |      $$ | 
    $$  __$$ |$$  __|     $$ |  $$ \$$$  $$ |$$ |  $$ |$$  __$$ |$$ |      $$ | 
    $$ |  $$ |$$ |        $$ |  $$ |\$  /$$ |$$ |  $$ |$$ |  $$ |$$ |      $$ | 
    $$ |  $$ |$$$$$$$$\ $$$$$$\ $$ | \_/ $$ |$$$$$$$  |$$ |  $$ |$$$$$$$$\ $$$$$$$$\\
    \__|  \__|\________|\______|\__|     \__|\_______/ \__|  \__|\________|\________| 
 """.center(console_wide_lenght), 'WHITE'), 'BOLD'",\n")
    print(new_line, colored_header_full_up, new_line, colored_ascii_title,colored_sub_title, new_line,\
        colored_author_name, new_line * 2,colored_header_full_down, new_line)
display_title()


""" --- DISPLAY WELCOME MESSAGE --- """
# FUNCTION TO DISPLAY A WELCOME MESSAGE
def show_welcome_message(): # Declare function to display a message
    username = getpass.getuser()    # Get username
    colored_username = colorize(username, 'YELLOW')
    welcome_start_colored = colorize("Welcome,", 'GREEN')
    welcome_end_colored = colorize("!!", 'GREEN')
    print(welcome_start_colored, colored_username, welcome_end_colored)
    heimdall_pwgen_colored = colorize("HEIMDALL password generator will help you create secure password(s).\n ", 'GREEN')
    print(heimdall_pwgen_colored)
show_welcome_message()


""" --- GENERATE PASSWORD --- """
# FUNCTION TO GENERATE A STRONG PASSWORD
def generate_strong_password(length):   # Declare a function to generate a strong password
    """Generates a strong password of the specified length.

    Args:
        length: The desired length of the password.

    Returns:
        A string representing the generated password.
    """
    characters = string.ascii_letters + string.digits + string.punctuation  # Combine leters, digits, and punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))   # Randomly select characters to form the password
    return password # Return the generated password



""" --- DESIRED PASSWORD(S) LENGTH --- """
# LOOP TO GET THE DESIRED LENGTH OF THE PASSWORD 
while True:
    try:
        question_length_pass_colored = colorize("Please enter the desired length for your password(s) (minimum 8 characters): ", 'GREEN')
        length = int(input(question_length_pass_colored))
        if length < 8:
            raise ValueError    # Ensure length  is at least 8 characters
        break
    except ValueError:
        error_message01_colored = colorize("Invalid input. Please enter an integer greater than or equal to 8.", 'RED')
        print(error_message01_colored)

# LOOP TO GET THE NUMBER OF PASWORDS TO GENERATE
while True:
    try:
        pass_num_gen_colored = colorize("Please enter the number of passwords to generate: ", "GREEN")
        quantity = int(input(pass_num_gen_colored))
        if quantity <= 0:
            raise ValueError    # Ensure the quantity is a positive integer
        break
    except ValueError:
        error_message02_colored = colorize("Invalid input. Please enter a positive integer.", 'RED')
        print(error_message02_colored)

# GENERATE AND PRINT PASSWORDS
while True:
    for _ in range(quantity):
        password = generate_strong_password(length) # Generate a strong password
        password_colored = colorize((password), 'WHITE')
        print(password_colored)

    # ASK IF THE USER WANTS TO GENERATE MORE PASSWORDS
    while True:
        message_reponse_colored = colorize("Do you want to generate more password(s)? (yes/no): ", "GREEN")
        response = input(message_reponse_colored)
        if response.lower() in ['yes', 'y']:
            break   # Continue to generate more passwords
        elif response.lower() in ['no', 'n']:
            colored_write_down_pass =  colorize("\nBefore exiting HEIMDALL password(s) generator, please take the time to ", 'GREEN') + colorize(colorize("write down your password(s)", 'UNDERLINE'), 'YELLOW') + colorize(" !", 'GREEN')
            print(colored_write_down_pass)
            colored_reminder_mesage_exit = colorize("Type 'exit' when you are finished.", 'GREEN')      
            
            while True:
                exit_response = input(colorize("When you're done, type 'exit': ", "YELLOW"))  # Initialize inside the loop
                if exit_response.lower() == 'exit':
                    clear_screen()
                    colored_thanks_msg = colorize("Thank you for using the HEIMDALL password(s) generator!", 'GREEN')
                    colored_exiting_msg = colorize("Exiting the program.", "GREEN")

                    print(colored_thanks_msg)
                    print(colored_exiting_msg)
                    time.sleep(3)
                    clear_screen()
                    exit()  # Exit the program
                else:
                    invalid_exit_msg = colorize("Invalid input. Please type 'exit' when you are ready.", "RED")
                    print(invalid_exit_msg)           
            
        else:
            colored_invalid_msg = colorize("Invalid input. Please answer 'yes' or 'no'.", 'RED')
            print(colored_invalid_msg)