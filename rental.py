from movie import Movie


class Rental(object):
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
            return Movie.calculate_reg_price(self.days_rented)
        elif self.movie.price_code == Movie.NEW_RELEASE:
            return Movie.calculate_new_release_price(self.days_rented)
        elif self.movie.price_code == Movie.CHILDRENS:
            return Movie.calculate_children_price(self.days_rented)
