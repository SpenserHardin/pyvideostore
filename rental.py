from movie import Movie


class Rental(object):
    BASE_PRICE = 1.5
    CHILD_PRICE = 1.5
    REGULAR_PRICE = 2
    NEW_RELEASE_PRICE = 3

    CHILD_MIN_DAYS = 3
    REGULAR_MIN_DAYS = 2

    def __init__(self, movie, days_rented):
        self._movie = movie
        self._days_rented = days_rented

    @property
    def days_rented(self):
        return self._days_rented

    @property
    def movie(self):
        return self._movie

    def determine_renter_points(self, frequent_renter_points):
        frequent_renter_points += 1
        if self.movie.price_code == Movie.NEW_RELEASE and self.days_rented > 1:
            frequent_renter_points += 1
        return frequent_renter_points

    def determine_amount(self):
        if self.movie.price_code == Movie.REGULAR:
            return self.regular_price()
        elif self.movie.price_code == Movie.NEW_RELEASE:
            return self.new_release_price()
        elif self.movie.price_code == Movie.CHILDRENS:
            return self.children_price()

    def new_release_price(self):
        return self.days_rented * self.NEW_RELEASE_PRICE

    def children_price(self):
        return self.more_than_min_day_price(self.CHILD_PRICE, self.CHILD_MIN_DAYS) \
            if self.is_greater_than_min_days(self.CHILD_MIN_DAYS) else self.CHILD_PRICE

    def regular_price(self):
        return self.more_than_min_day_price(self.REGULAR_PRICE, self.REGULAR_MIN_DAYS) \
            if self.is_greater_than_min_days(self.REGULAR_MIN_DAYS) else self.REGULAR_PRICE

    def more_than_min_day_price(self, genre_price, min_days):
        return genre_price + (self.days_rented - min_days) * self.BASE_PRICE

    def is_greater_than_min_days(self, min_days):
        return self.days_rented > min_days
