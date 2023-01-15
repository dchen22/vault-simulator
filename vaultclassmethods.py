import _pickle as pickle
from bisect import bisect_left, bisect_right
from helperfunctions import bin_search_username

class User:

    username: str
    password: str
    balance: float
    messages: list
    items: list

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = 0
        self.messages = []
        self.items = []


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
    existing_usernames: list
    new_account: User

    def __init__(self, existing_accounts):
        self.existing_accounts = existing_accounts
        self.existing_usernames = [x[1].username for x in self.existing_accounts]

    def add_account(self, new_account):
        '''
        Insert (username, user account object) in a sorted fashion
        '''
        # look for already existing username
        v = bisect_left([x[0] for x in self.existing_accounts], new_account.username)
        if v < len(self.existing_accounts) and new_account.username != self.existing_accounts[v][0]:
            self._addupdate_accounts(new_account)
            print('----- Account successfully created! -----', end='\n\n')
        else:
            print('\!!!/ Username already exists! \!!!/', end='\n\n')

        with open('accountsPICKLE.pkl', 'wb') as acc_file:
            pickle.dump(self, acc_file)
            # pickle-store this object (which holds a list of all existing users)

    def login(self, username: str, password: str):
        loc = bin_search_username(self.existing_usernames, username)
        if password == self.existing_accounts[loc][1].password:
            print('----- Log in successful! -----', end='\n\n')
        else:
            print('*** Incorrect password. ***', end='\n\n')

    def _addupdate_accounts(self, account):
        self.existing_accounts.insert(bisect_right(self.existing_accounts, (account.username, account)), (account.username, account))
        self.existing_usernames.insert(bisect_right(self.existing_accounts, (account.username, account)), account.username)