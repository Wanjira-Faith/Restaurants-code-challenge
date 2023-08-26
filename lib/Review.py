class Review:
    all_reviews = []

    def __init__(self,customer,restaurant,rating):
        self._customer = customer
        self._restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self)

    def rating(self):
        return self.rating 

    @property
    def customer(self):
        return self._customer
    
    @property
    def restaurant(self):
        return self._restaurant
    
    def __str__(self):
        return f"Review: {self.customer.full_name()} rated {self.rating} stars"

    @classmethod
    def all(cls):
        return cls.all_reviews