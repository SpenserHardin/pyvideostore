from movie import Movie


class Customer(object):

    def __init__(self, name):
        self._name = name
        self._rentals = []

    def add_rental(self, rental):
        self._rentals.append(rental)

    @property
    def name(self):
        return self._name

    def statement(self):
        total_amount = 0
        frequent_renter_points = 0
        rentals = self._rentals
        result = 'Rental Record for ' + self.name + '\n'

        for rental in rentals:
            this_amount = 0

            this_amount = self.determine_amount(rental, this_amount)

            frequent_renter_points = self.determine_renter_points(frequent_renter_points, rental)

            result += '\t' + rental.movie.title + '\t' + str(this_amount) + '\n'
            total_amount += this_amount

        result += 'You owed ' + str(total_amount) + '\n'
        result += 'You earned ' + str(frequent_renter_points) + ' frequent ' \
                  'renter points\n'

        return result

    def determine_renter_points(self, frequent_renter_points, rental):
        frequent_renter_points += 1
        if (rental.movie.price_code == Movie.NEW_RELEASE and
                    rental.days_rented > 1):
            frequent_renter_points += 1
        return frequent_renter_points

    def determine_amount(self, rental, this_amount):
        if rental.movie.price_code == Movie.REGULAR:
            this_amount += 2
            if rental.days_rented > 2:
                this_amount += (rental.days_rented - 2) * 1.5
        elif rental.movie.price_code == Movie.NEW_RELEASE:
            this_amount += rental.days_rented * 3
        elif rental.movie.price_code == Movie.CHILDRENS:
            this_amount += 1.5
            if rental.days_rented > 3:
                this_amount += (rental.days_rented - 3) * 1.5
        return this_amount
