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

    def avarage_star_rating(self):  
          if len(self.reviews) == 0:
              return 0
          return sum(review.star_rating for review in self.reviews) / len(self.reviews)
       


