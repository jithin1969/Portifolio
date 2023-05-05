class OnlineStore:
    def __init__(self):
        self.products = {
            "electronics": {
                "001": {"name": "iPhone", "price": 1000},
                "004": {"name": "Laptop", "price": 1500},
            },
            "clothing": {
                "002": {"name": "T-shirt", "price": 20},
                "005": {"name": "Pants", "price": 30},
            },
            "books": {
                "003": {"name": "Book", "price": 10},
                "006": {"name": "Magazine", "price": 5},
            },
        }
        self.order = {}

    def display_all_products(self):
        print("Here are all the products we have for sale:")
        print("Category | ID | Product Name | Price")
        for category, products in self.products.items():
            for item_id, product in products.items():
                name = product["name"]
                price = product["price"]
                print(f"{category.capitalize()} | {category[0]}{item_id} | {name} | ${price:.2f}")

    def get_order_item(self, category_choice):
        while True:
            choice = input("Enter the product ID to add to your order (or 'done' to finish): ")
            if choice == "done":
                break
            if choice[1:] not in self.products[category_choice]:
                print("Invalid product ID. Please try again.")
                continue
            quantity = int(input("Enter the quantity: "))
            if quantity <= 0:
                print("Quantity should be greater than 0. Please try again.")
                continue
            self.order[(category_choice, choice[1:])] = self.order.get((category_choice, choice[1:]), 0) + quantity
            print(f"{quantity} {self.products[category_choice][choice[1:]]['name']} added to your order.")

    def calculate_price(self):
        subtotal = 0

        for item, quantity in self.order.items():
            price = self.products[item[0]][item[1]]["price"]

            if quantity >= 10:
                price *= 0.95  # apply a 5% discount for bulk orders

            subtotal += price * quantity

        tax = subtotal * 0.13  # calculate 13% tax
        shipping_fee = 9.99 if subtotal < 75 else 0  # add $9.99 shipping fee if the order value is less than $75

        total = subtotal + tax + shipping_fee

        return subtotal, tax, shipping_fee, total


    def calculate_subtotal(self):
        subtotal = 0
        for item, quantity in self.order.items():
            price = self.products[item[0]][item[1]]["price"]
            if quantity >= 10:
                price *= 0.95  # apply a 5% discount for bulk orders
            total_price = price * quantity
            subtotal += total_price
        return subtotal

    def calculate_tax(self, subtotal):
        return subtotal * 0.13

    def calculate_shipping_fee(self, subtotal):
        if subtotal < 75:
            return 9.99
        else:
            return 0

    def generate_receipt(self):
        print("===== RECEIPT =====")
        for item, quantity in self.order.items():
            name = self.products[item[0]][item[1]]["name"]
            price = self.products[item[0]][item[1]]["price"]
            if quantity >= 10:
                price *= 0.95  # apply a 5% discount for bulk orders
            total_price = price * quantity
            print(f"{name} x {quantity}: ${total_price:.2f}")

        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax(subtotal)
        shipping_fee = self.calculate_shipping_fee(subtotal)

        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Tax: ${tax:.2f}")
        print(f"Shipping fee: ${shipping_fee:.2f}")

        total_price = subtotal + tax + shipping_fee
        print(f"Total price: ${total_price:.2f}")

    def get_order_item(self, category_choice):
        while True:
            item_id = input("Enter the product ID to add to your order (or 'done' to finish): ")
            if item_id == "done":
                break
            if item_id not in self.products[category_choice]:
                print("Invalid product ID. Please try again.")
                continue
            quantity = int(input("Enter the quantity: "))
            if quantity <= 0:
                print("Quantity should be greater than 0. Please try again.")
                continue
            order_item = (category_choice, item_id)
            self.order[order_item] = self.order.get(order_item, 0) + quantity
            print(f"{quantity} {self.products[category_choice][item_id]['name']} added to your order.")
            return order_item

    def main_menu(self):
        print("Welcome to our online store!")
        while True:
            category_choice = input("Select a product category (electronics, clothing, books): ")
            if category_choice not in self.products:
                print("Invalid product category. Please try again.")
                continue
            print(f"Here are the {category_choice} products we have for sale:")
            print("ID | Product Name | Price")
            for item_id, product in self.products[category_choice].items():
                name = product["name"]
                price = product["price"]
                print(f"{category_choice[0]}{item_id} | {name} | ${price:.2f}")
            break
        while True:
            order_item = self.get_order_item(category_choice)
            if order_item == None:
                break
        self.generate_receipt()


if __name__ == "__main__":
    online_store = OnlineStore()
    online_store.main_menu()
