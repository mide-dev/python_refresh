
# START

# recipe main menu

# learn class
import csv

from item import Item        

# Item.instantiate_from_csv()
# print(Item.all)


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, broken_phones: int):
        # call parent class super function
        super().__init__(
            name, price, quantity
        )
       
        # run validations to arguments
        assert broken_phones >= 0, 'quantity needs to be greater than 0'
        

# phone1 = Phone('nokia', 450, 3, 1)
# print(phone1.calculate_total_price())
# print(Phone.all)


item1 = Item('phone', 200, 2)
# print(item1.__name)
item1.name = 'shoe'







# item1 = Item('phone', 200, 2)
# item2 = Item('laptop', 1000, 3)
# item3 = Item('cable', 10, 5)
# item4 = Item('mouse', 50, 5)
# item5 = Item('keyboard', 70, 1)