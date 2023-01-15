from typing import TextIO
import _pickle as pickle
from vaultclassmethods import User, StoreUserAccounts
from bisect import bisect_right, bisect_left

with open('accountsPICKLE.pkl', 'rb') as acc_file:
    try:
        running_storage = StoreUserAccounts(
            pickle.load(acc_file).existing_accounts)  # grab the pickle-storage object
        # but, if it's empty, there is no stored object to grab
    except ReferenceError:
        running_storage = StoreUserAccounts(
            [])  # create an entirely new storage object, with an empty list of existing users


def main():
    while True:
        option = int(input('''Select an action: 
        [1] Log in
        [2] Open an account
        '''))
        if option == 1:
            log_in_account(input('Enter your username: '), input('Enter your password: '))
        elif option == 2:  # Open a new account
            set_up_account(input('Enter a username: '), input('Enter a password: '))
        print()


def set_up_account(username: str, password: str) -> None:
    running_storage.add_account(User(username, password))


def log_in_account(username: str, password: str) -> None:
    if running_storage.login(username, password):  # if login is successful
        _acc_homepage(running_storage.existing_accounts[username])


def _acc_homepage(account: User):
    account.display_stats()


main()
