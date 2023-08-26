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
