class Money:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def display_amount(self):
        print(f"Amount: {self.dollars}.{self.cents:02}")

    def set_amount(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add(self, other_money):
        total_cents = self.cents + other_money.cents
        carry_dollars, remaining_cents = divmod(total_cents, 100)
        self.dollars += other_money.dollars + carry_dollars
        self.cents = remaining_cents

    def subtract(self, other_money):
        total_cents = self.cents - other_money.cents
        borrow_dollars, remaining_cents = divmod(total_cents, 100)
        self.dollars -= other_money.dollars + borrow_dollars
        self.cents = remaining_cents

class Product(Money):
    def __init__(self, name, price_dollars, price_cents):
        super().__init__(price_dollars, price_cents)
        self.name = name

    def display_product_info(self):
        print(f"Product: {self.name}")
        self.display_amount()

    def reduce_price(self, reduction_dollars, reduction_cents):
        reduction_money = Money(reduction_dollars, reduction_cents)
        self.subtract(reduction_money)


money1 = Money(10, 50)
money1.display_amount()

product1 = Product("Laptop", 1200, 75)
product1.display_product_info()

reduction_money = Money(500, 50)
product1.reduce_price(reduction_money.dollars, reduction_money.cents)
product1.display_product_info()