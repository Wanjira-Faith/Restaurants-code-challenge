from Review import Review

class Customer:
    all_customers = []
    
    def __init__(self, given_name,family_name):
        self.given_name = given_name
        self.family_name = family_name
        Customer.all_customers.append(self)

    def given_name(self):
        return self.given_name

    def family_name(self):
        return self.family_name   
    
    def full_name(self):
        return self.given_name + " " + self.family_name

    def restaurants(self):
        return list({review.restaurant for review in self.reviews})

    def add_review(self, restaurant,rating):
        review = Review(self, restaurant, rating)
        self.reviews.append(review)
        restaurant.add_review(review)
    
    def num_reviews(self):
        return len(self.reviews)
    
    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name() == name:
                return customer
        return None
    
    @classmethod
    def find_all_by_given(cls, name):
        customers = []
        for customer in cls.all_customers:
            if customer.given_name() == name:
                customers.append(customer)
        return customers
