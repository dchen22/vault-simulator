from typing import TextIO
import _pickle as pickle
from bisect import bisect_right, bisect_left

def main():
    while True:
        option = int(input('''Select an action: 
        [1] Log in
        [2] Open an account
        '''))
        if option == 2: # Open a new account
            set_up_account(input('Enter a username: '), input('Enter a password: '))


def set_up_account(username: str, password: str) -> None:

    with open('accountsPICKLE.pkl', 'rb') as acc_file:
        try:
            temp_storage = StoreUserAccounts(pickle.load(acc_file).existing_accounts)  # grab the pickle-storage object
            # but, if it's empty, there is no stored object to grab
        except ReferenceError:
            temp_storage = StoreUserAccounts([])  # create an entirely new storage object, with an empty list of existing users
        temp_storage.add_account(User(username, password))
        # print(temp_storage.stored_accounts)
        # # use the above to see which


class User:

    username: str
    password: str
    balance: float
    messages: list

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = 0
        self.messages = []



class StoreUserAccounts:
    '''
    When updating instances of this class, try not to directly reference the object, but
    instead create an entirely new instance and just update it with the existing accounts.

    This is because if you update the attributes or the methods of this class, it won't update
    the pickle-stored instance, but if you create an entirely new one and just copy relevant info over
    from the old one, then it will be updated.

    I.e. don't keep using your old car; take its tires and leftover bits to help make a new one
    '''
    existing_accounts: list[tuple[str, User]]  # [(username: username account object)]

    def __init__(self, existing_accounts):
        self.existing_accounts = existing_accounts

    def add_account(self, new_account):
        '''
        Insert (username, user account object) in a sorted fashion
        '''
        # look for already existing username
        v = bisect_left([x[0] for x in self.existing_accounts], new_account.username)
        if v < len(self.existing_accounts) and new_account.username != self.existing_accounts[v][0]:
            self.existing_accounts.insert(
                bisect_right(self.existing_accounts, (new_account.username, new_account)),
                    (new_account.username, new_account))
            print('----- Account successfully created! -----', end='\n\n')
        else:
            print('\!!!/ Username already exists! \!!!/', end='\n\n')

        with open('accountsPICKLE.pkl', 'wb') as acc_file:
            pickle.dump(self, acc_file)
            # pickle-store this object (which holds a list of all existing users)

    def login(self):
        pass

main()
