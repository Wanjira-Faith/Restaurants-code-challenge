class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        Restaurant.all_restaurants.append(self)

    def add_review(self,review):
            self.reviews.append(review)

    def customers(self):
            return list({review.customer for review in self.reviews})     


