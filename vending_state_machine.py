import transitions
from transitions import Machine

class VendingMachine(object):
    products = {
        '1A' : ['Fruiti', 20],
        '1B' : ['Lays', 10]
    }
    states = ['default', 'prod_select', 'dispensing', 'give_change']

    curr_product, curr_coins = [], None

    transitions = [
        { 'trigger':'insert', 'source':'default', 'dest':'prod_select', 'after':'insert_coin'},
        {'trigger': 'selection', 'source': 'prod_select', 'dest': 'dispensing','after': 'get_product'},
        { 'trigger':'dispense', 'source':'dispensing', 'dest':'give_change', 'conditions':'sufficient_balance', 'after':'dispense_object' },
        {'trigger':'change', 'source':'give_change', 'dest':'default', 'before': 'give_change'}
    ]
    
    def __init__(self, name):
        self.name = name
        self.machine = Machine(model = self, states = VendingMachine.states, transitions= VendingMachine.transitions, initial= 'default')
    
    def insert_coin(self):
        coins = int(input('Please enter coins:'))
        VendingMachine.curr_coins = coins
        print('Inserted', VendingMachine.curr_coins, 'coins')
    
    def get_product(self):
        prod_code = input('Please select product: ')
        if prod_code in VendingMachine.products:
            VendingMachine.curr_product = VendingMachine.products[prod_code]
            print('Product Selected:', VendingMachine.curr_product[0])
        else:
            print('Incorrect product code')
    
    def valid_product(self):
        if VendingMachine.curr_product is not None:
            return True
        else:
            return False

    def dispense_object(self):
        print('Dispensing the product. Please collect from tray')
        if VendingMachine.curr_coins >= VendingMachine.curr_product[1]:
            VendingMachine.curr_coins -= VendingMachine.curr_product[1]
        VendingMachine.curr_product = []


    def sufficient_balance(self):
        if VendingMachine.curr_product is not None and VendingMachine.curr_coins >= VendingMachine.curr_product[1]:
            return True
        else:
            return False
    
    def give_change(self):
        print('Please collect change amount:', VendingMachine.curr_coins)


vending_machine = VendingMachine('Dispenser')
vending_machine.insert()
vending_machine.selection()
vending_machine.dispense()
vending_machine.change()
