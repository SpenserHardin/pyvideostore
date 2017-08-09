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

    def determine_amount(self, this_amount):
        if self.movie.price_code == Movie.REGULAR:
            this_amount += 2
            if self.days_rented > 2:
                this_amount += (self.days_rented - 2) * 1.5
        elif self.movie.price_code == Movie.NEW_RELEASE:
            this_amount += self.days_rented * 3
        elif self.movie.price_code == Movie.CHILDRENS:
            this_amount += 1.5
            if self.days_rented > 3:
                this_amount += (self.days_rented - 3) * 1.5
        return this_amount