import _pickle as pickle
from bisect import bisect_left, bisect_right
from helperfunctions import bin_search_username

class User:

    username: str
    password: str
    balance: float
    inbox: list
    items: list[dict]

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = 0.0
        self.inbox = []
        self.items = []
        self.sent_requests = []
        self.incoming_reqs = []
        print('reset lol ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo')

    def display_stats(self):
        print('|||||||||||||||||      YOUR HOMEPAGE      |||||||||||||||||', end='\n\n')
        print(f'Username: {self.username}')
        print(f'Balance: ${self.balance}')
        if len(self.items) > 0:
            print(f'Items: {self.items}')
        else:
            print('No items to display')
        print(f'Inbox ({len(self.inbox)})')
        print()

    def display_item_stats(self):
        for item in self.items:
            for stat in item:
                print(f'{stat}: {item[stat]}')

    def homepage_actions(self):
        # users should be able to send trade requests to other users and send/request coins and items, and send messages
        # should also be able to mine for more Vulcoin (e.g. invest in spaceships that search on other planets), and this
        # will have a timer based on local clock
        # TODO
        pass

    def update_user_attributes(self):

        try:
            # self.newattribute = self.oldattribute  # use this to change attribute names
            # del self.oldattribute  # use this if the attribute is mutable (then you get rid of the old reference),
            # # otherwise you have two attributes that point to the same thing
            pass
        except AttributeError:
            # print(f'{self.username} FAILED')
            pass


class StoreUserAccounts:
    '''
    - Must use self._update_attributes() after making any changes to the users stored
    in self.existing_users in order to make sure these changes are saved to pickle
    
    When updating instances of this class, try not to directly reference the object, but
    instead create an entirely new instance and just update it with the existing accounts.

    This is because if you update the attributes or the methods of this class, it won't update
    the pickle-stored instance, but if you create an entirely new one and just copy relevant info over
    from the old one, then it will be updated.

    I.e. don't keep using your old car; take its tires and leftover bits to help make a new one
    '''
    existing_accounts: dict[str, User]
    new_account: User

    def __init__(self, existing_accounts):
        self.existing_accounts = existing_accounts
        self._update_attributes()


    def add_account(self, new_account):
        '''
        Insert (username, user account object) in a sorted fashion
        '''
        # look for already existing username
        if new_account.username not in self.existing_accounts:
            self.existing_accounts[new_account.username] = new_account
            print('----- Account successfully created! -----', end='\n\n')
        else:
            print('\!!!/ Username already exists! \!!!/', end='\n\n')

        with open('accountsPICKLE.pkl', 'wb') as acc_file:
            pickle.dump(self, acc_file)
            # pickle-store this object (which holds a list of all existing users)

    def login(self, username: str, password: str) -> bool:
        if username in self.existing_accounts and password == self.existing_accounts[username].password:
            print('----- Log in successful! -----', end='\n\n')
            return True
        else:
            print('*** Incorrect password. ***', end='\n\n')
            return False


    def request_money(self, account: User, req_username: str):
        if req_username in self.existing_accounts:
            desired_amount = float(input('Enter request amount: '))
            supplement_msg = input('Include message (enter to skip): ')
            if not supplement_msg:
                supplement_msg = 'No message included.'
            self.existing_accounts[req_username].incoming_reqs.append({
                'Username': account.username,
                'Amount': desired_amount,
                'Message': supplement_msg
            })
            self.existing_accounts[req_username].inbox.append(
                f'''{account.username} has sent a money request. Please 
                    check your inbox for more details.
                 ''')
            self._update_attributes()
        else:
            print('User does not exist!')


    def delete_account(self, username, password):
        if self.login(username, password):
            del self.existing_accounts[username]


    def _terminate_account(self, username):
        del self.existing_accounts[username]

    def _update_attributes(self):
        '''
        Invoke this method when you change the attributes of StoreUserAccounts
        It will reupload the new state of the classes

        '''
        for account in self.existing_accounts:
            self.existing_accounts[account].update_user_attributes()
            # print(self.existing_accounts[account].__dict__)

            # TODO
            # the user accounts created after the changes will have the new attributes
            # maybe you can go through all of the old ones and make the necessary changes
            # maybe do this automatically each time on startup. its slower but it prevents bugs
        with open('accountsPICKLE.pkl', 'wb') as acc_file:
            pickle.dump(self, acc_file)