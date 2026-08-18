class product:
    pname=" "
    price=0
    quantity=0
    total_value=0

    def accept(self):
        self.pname=input("Enter product name= ")
        self.price=int(input("Enter product price= "))
        self.quantity=int(input("Enter quantity of product= "))

    def cal_total(self):
        self.total_value=self.price*self.quantity

    def update_stock(self):
        qty=int(input("Enter quantity to add or remove the product= "))
        self.quantity+=qty
        self.cal_total()

    def display(self):
        print("Product Name: ",self.pname)
        print("total price: ",self.total_value)

p1=product()
p1.accept()
p1.update_stock()
p1.display()
