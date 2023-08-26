from Customer import Customer
from Restaurant import Restaurant
from Review import Review

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

print("Reviews for Restaurant 1:")
for review in restaurant1.reviews:
   print(str(review))
   print("--------------------------------------------------------")

print("Customers who reviewed Restaurant 1:")
print([customer.full_name() for customer in restaurant1.customers()])
print("-------------------------------")

print("Customer 1 reviewed restaurants:")
print([restaurant.name for restaurant in customer1.restaurants()])
print("-------------------------------")

print("Number of reviews by Customer 1:")
print(Customer.num_reviews(customer1))
print("-------------------------------")

print("Finding customer by name 'Ali Malik':")
print(Customer.find_by_name("Ali Malik").full_name())
print("-------------------------------")

print("Finding customers by given name 'Linda':")
print([customer.full_name() for customer in Customer.find_all_by_given("Linda")])
print("-------------------------------")

print("Average start rating for Restaurant 1:")
print(restaurant1.average_star_rating())
print("-------------------------------")

