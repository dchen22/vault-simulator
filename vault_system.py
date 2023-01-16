from typing import TextIO
import _pickle as pickle
from vaultclassmethods import User, StoreUserAccounts
from bisect import bisect_right, bisect_left
import os

with open('accountsPICKLE.pkl', 'rb') as acc_file:
    try:
        running_storage = StoreUserAccounts(
            pickle.load(acc_file).existing_accounts)  # grab the pickle-storage object
        # but, if it's empty, there is no stored object to grab
    except ReferenceError:
        running_storage = StoreUserAccounts(
            [])  # create an entirely new storage object, with an empty list of existing users


def main():
    bank_hub_screen()


def bank_hub_screen():
    while True:
        print('''
----------------------------------------------------------------------------------------------------
 ___ ___  _______  _____    ______  _______  _______  _______      ______  _______  _______  __  __ 
|   |   ||   |   ||     |_ |      ||       ||_     _||    |  |    |   __ \|   _   ||    |  ||  |/  |
|   |   ||   |   ||       ||   ---||   -   | _|   |_ |       |    |   __ <|       ||       ||     < 
 \_____/ |_______||_______||______||_______||_______||__|____|    |______/|___|___||__|____||__|\__|
 
----------------------------------------------------------------------------------------------------
        
Welcome to the VulCoin Bank! 
        ''')

        option = input('''Select an action: 
        [1] Log in
        [2] Create an account
        [X] Exit
        > ''')

        if option == '1':
            log_in_account(input('Enter your username: '), input('Enter your password: '))
        elif option == '2':  # Open a new account
            set_up_account(input('Enter a username: '), input('Enter a password: '))
        elif option.lower() == 'x':
            print('stay fresh, gamer')
            exit(-1)
        else:
            print('Invalid option!')

def set_up_account(username: str, password: str) -> None:
    running_storage.add_account(User(username, password))


def log_in_account(username: str, password: str) -> None:
    opened_account = None  # this is the account that we will be doing stuff in
    if running_storage.login(username, password):  # if login is successful
        opened_account = running_storage.existing_accounts[username]
        _acc_homepage(opened_account)


def _acc_homepage(account: User):

    while True:
        account.display_stats()
        option = input('''Select an action:
        [1] View Items
        [2] Send money
        [3] Request money
        [4] Add Mission
        [5] View Missions
        [L] Log out
        > ''')
        if option == '1':
            if len(account.items) > 0:
                account.display_item_stats()
            else:
                print('No items to display!')

        elif option == '2':
            print(f'Balance: ${account.balance}')
        elif option == '3':
            running_storage.request_money(account, input('Enter their username: '))
        elif option == '2':
            # TODO
            pass
        elif option == '2':
            # TODO
            pass
        elif option.lower() == 'l':
            print('\n' * 80)  # this should clear the screen (kinda???)
            break
        else:
            print('Invalid option!')
        input('Continue? (enter)')
        print()



main()
