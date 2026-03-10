class Customer:
    def __init__(self, customer_id, name, phone):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone

    def display_customer(self):
        print(f"Customer ID: {self.customer_id}")
        print(f"Name: {self.name}")
        print(f"Phone: {self.phone}")

customer1 = Customer(1, "John", "9876543210")
customer1.display_customer()