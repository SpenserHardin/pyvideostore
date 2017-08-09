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
            rental_amount = rental.determine_amount()

            frequent_renter_points = rental.determine_renter_points(frequent_renter_points)

            result += '\t' + rental.movie.title + '\t' + str(rental_amount) + '\n'
            total_amount += rental_amount

        result += 'You owed ' + str(total_amount) + '\n'
        result += 'You earned ' + str(frequent_renter_points) + ' frequent ' \
                  'renter points\n'

        return result
