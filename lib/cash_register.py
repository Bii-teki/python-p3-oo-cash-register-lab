class CashRegister:

  def __init__(self, discount=None):
    self.total = 0
    if discount is None:
        self.discount = 0  
    else:
        self.discount = discount
    self.items = []
    self.last_transaction_amount = 0   

  def add_item(self, title, price, quantity=1):
    item_total = price * quantity
    self.total += item_total
    self.last_transaction_amount = item_total
    self.items.extend([title] * quantity)

  def apply_discount(self):
      if self.discount != 0:
       self.total = self.total - (self.discount * 0.01 * self.total)
       print(f"After the discount, the total comes to ${int(self.total)}.")
      else:
           print("There is no discount to apply.")

  def void_last_transaction(self):
        if self.last_transaction_amount:
            self.total -= self.last_transaction_amount
            self.items.pop()
            self.last_transaction_amount = 0  

# Create an instance of the CashRegister class
cash_register = CashRegister()
cash_register.add_item("macbook air", 1000)  # Add an item with a price of 1440
cash_register.apply_discount()  # Apply the discount