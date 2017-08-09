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
            if self.is_greater_than_min_days(self.REGULAR_MIN_DAYS):
                return Movie.regular_price(self.days_rented, self.REGULAR_MIN_DAYS)
            else:
                return Movie.REGULAR_PRICE
        elif self.movie.price_code == Movie.NEW_RELEASE:
            return Movie.new_release_price(self.days_rented)
        elif self.movie.price_code == Movie.CHILDRENS:
            if self.is_greater_than_min_days(self.CHILD_MIN_DAYS):
                return Movie.children_price(self.days_rented, self.CHILD_MIN_DAYS)
            else:
                return Movie.CHILD_PRICE

    def is_greater_than_min_days(self, min_days):
        return self.days_rented > min_days
