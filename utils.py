import os
import getpass
import time

# lambda function to clear cli
clear = lambda: os.system("cls")


def banner():
    print("                                 _ _ _ _ _ _ _ _ _ _ _ _")
    print("                                |                      |")
    print("  _ _ _ _ _ _ _ _ _ _           |                      |")
    print("|                    |           - - - - - - - - - -   |")
    print("|     _ _ _ _ _ _ _ _|                            /    /")
    print("|    |                                          /    /")
    print("|    |                                         /    /")
    print("|    |                                       /   /")
    print("|    |                                      /   /")
    print("|    |                                    /   /")
    print("|    |                                   /   /")
    print("|    |           _ _ _ _ _ _           /   /")
    print("|    |          |            |        /   /")
    print("|    |          |_ _      _ _|      /   /")
    print("|    |              |    |         /   /")
    print("|    |              |    |       /   /")
    print("|    |              |    |      /   /")
    print("|    | _ _ _ _ _ _ _|    |      |   - - - - - - - - - -|")
    print("|                        |      |_ _ _ _ _ _ _ _ _ _ _ | Productions")
    print("|_ _ _ _ _ _ _ _ _ _ _ _ |      ")


def get_creds():
    """
    This function asks the admin user to provide credentials
    :return: Returns Username and Password for the SSH connection
    """
    clear()
    print("\n*** Give admin credentials ***\n")
    time.sleep(2)
    username = input("Username: ")
    # use input only for IDE testing
    # password = input("password: ")
    # use getpass for production
    password = getpass.getpass(prompt='Password: ', stream=None)
    print("\n")
    time.sleep(1)
    clear()
    return {"username": username, "password": password}


def get_secret():
    """
    This function asks the user to input a new password enable secret.
    :return: Returns the New password to be configured
    """
    clear()
    time.sleep(2)
    # The loop will be true until the user inputs passwords that match
    while True:
        # use getpass in production
        new_secret = getpass.getpass(prompt='Give New Secret: ', stream=None)
        confirm_secret = getpass.getpass(prompt='Verify New Secret: ', stream=None)
        # use input for IDE testing only
        # new_secret = input("new_secret: ")
        # confirm_secret = input("confirm_secret: ")
        if new_secret != confirm_secret:
            print("\n********** Secrets do not match. Please, try again! **********\n")
            time.sleep(2)
            # If the secrets do not match, then skip everything else into the loop and run the loop from scratch
            continue
        else:
            print("success\n")
            time.sleep(1)
            return new_secret


def menu():
    """
    This function prints out the Menu, informing the user for the available options
    :return:
    """
    clear()
    print("\n*********** Menu ************\n")
    print("The following options are about configuring a cisco IOS router\n")
    print("Press 1 to rotate the enable secret")
    print("Press Ctrl + C to quit \n")
    answer = input("Answer: ")
    return answer
