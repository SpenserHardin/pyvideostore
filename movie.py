class Movie(object):

    CHILDRENS = 2
    REGULAR = 0
    NEW_RELEASE = 1

    BASE_PRICE = 1.5
    CHILD_PRICE = 1.5
    REGULAR_PRICE = 2
    NEW_RELEASE_PRICE = 3

    CHILD_MIN_DAYS = 3
    REGULAR_MIN_DAYS = 2

    def __init__(self, title, price_code):
        self.BASE_PRICE = 1.5
        self._title = title
        self._price_code = price_code

    @property
    def price_code(self):
        return self._price_code

    @price_code.setter
    def price_code(self, code):
        self._price_code = code

    @property
    def title(self):
        return self._title

    @classmethod
    def calculate_children_price(cls, days_rented):
        return cls.calculate_price(days_rented, cls.CHILD_MIN_DAYS, Movie.CHILD_PRICE)

    @classmethod
    def calculate_reg_price(cls, days_rented):
        return cls.calculate_price(days_rented, cls.REGULAR_MIN_DAYS, Movie.REGULAR_PRICE)

    @classmethod
    def calculate_new_release_price(cls, days_rented):
        return days_rented * Movie.NEW_RELEASE_PRICE

    @classmethod
    def calculate_price(cls, days_rented, min_days, movie_price):
        return cls.more_than_min_day_price(movie_price, days_rented, min_days) \
            if cls.is_greater_than_min_days(days_rented, min_days) else movie_price

    @staticmethod
    def more_than_min_day_price(genre_price, days_rented, min_days):
        return genre_price + (days_rented - min_days) * Movie.BASE_PRICE

    @staticmethod
    def is_greater_than_min_days(days_rented, min_days):
        return days_rented > min_days
