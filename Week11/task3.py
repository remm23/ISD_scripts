class CashRegister():
    # initalizing properties on instantiation
    def __init__(self):
        self._itemCount = 0
        self._totalPrice = 0.0

    # incresces the the itemCount when an item is added
    # totalPrice is increased by the price of the item added
    def addItem(self,price):
        self._itemCount = self._itemCount + 1
        self._totalPrice = self._totalPrice + price

    # returns the value of totalPrice
    def getTotal(self):
        return self._totalPrice

    # returns the value of itemCount
    def getCount(self):
        return self._itemCount

    # resets the itemCount and totalPrice to inital values
    def clear(self):
        self._itemCount = 0
        self._totalPrice = 0.0

    # removes the decimal and returns an integer
    def getPounds(self):
        # return "£ %d" % int(self._totalPrice) #<< rounds down
        return "£ %.0f" % self._totalPrice #<< rounds up

    # returns a float value of payment
    def giveChange(self,payment):
        return payment - self._totalPrice


r1 = CashRegister()
r1.addItem(0.90)
r1.addItem(0.95)
r2 = CashRegister()
r2.addItem(1.90)

# register1 has 2 items and a total of 1.85
# register2 has 1 item and a total of 1.9


# print(r1.getCount()) 
# print(r1.getTotal())
# print(r2.getCount())
# print(r2.getTotal())
# print(r1.getPounds())
# print(r1.giveChange(10)) # <-- returns 8.15