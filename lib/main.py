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

# Test sample instances
print("----------Testing methods--------")
print("")

print("Customer 1 full name:")
print(customer1.full_name())  
print("-------------------------------")

print("Customer 1 reviewed restaurants:")
print([restaurant.name for restaurant in customer1.restaurants()])
print("-------------------------------")

print("Ratings for Restaurant 1:")
print([review.rating for review in restaurant1.reviews])
print("-------------------------------")

print("Customers who reviewed Restaurant 1:")
print([customer.full_name for customer in restaurant1.customers])
print("-------------------------------")




