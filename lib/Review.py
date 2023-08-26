class Review:
    all_reviews = []

    def __init__(self,customer,restaurant,rating):
        self._customer = customer
        self._restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self)

    def rating(self):
        return self.rating 
    
    def customer(self):
        return self.customer
    
    def restaurant(self):
        return self.restaurant
