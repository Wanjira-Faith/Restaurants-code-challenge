from Customer import Customer
from Restaurant import Restaurant

# create customers
customer1 = Customer("Linda", "Wambui")
customer2 = Customer("Ali", "Malik")

# create restaurants
restaurant1 = Restaurant("Dusit Princess")
restaurant2 = Restaurant("Delicious Eatery")

# Add reviews for customers
customer1.add_review(restaurant1, 7)
customer1.add_review(restaurant2, 5)
customer2.add_review(restaurant1, 4)
