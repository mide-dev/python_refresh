import csv


class Item:
    pay_rate = 0.8 #pay rate after 20% discount
    all = []
    
    def __init__(self, name: str, price: float, quantity: int) -> None:
        assert isinstance(price, (float, int)), 'Price needs to be float or int'
        assert price >= 0, 'Price needs to be greater than 0'
        assert quantity >= 0, 'quantity needs to be greater than 0'
        
        self.__name = name
        self.price = price
        self.quantity = quantity
    
        Item.all.append(self)
        
    @property
    # read only attr
    def name(self):
        return self.__name
    
    @name.setter
    def set_name(self, value):
        self.__name = value
    
    def calculate_total_price(self) -> float: 
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate
        
    @classmethod
    def instantiate_from_csv(cls):   
        with open('C:\\Users\\Ayomide\\Desktop\\Development\\Python\\Python_refresh\\recipe_box\\item.csv', 'r') as file:
            reader = csv.DictReader(file, quotechar="'", skipinitialspace=True)
            items = list(reader)
            
        for item in items:
            Item(
            name = item.get('name'),
            price = float(item.get('price')),
            quantity = int(item.get('quantity')),
            )
        
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int): 
            return True
        
        
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
