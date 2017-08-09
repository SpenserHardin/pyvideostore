class Movie(object):

    CHILDRENS = 2
    REGULAR = 0
    NEW_RELEASE = 1

    BASE_PRICE = 1.5
    CHILD_PRICE = 1.5
    REGULAR_PRICE = 2
    NEW_RELEASE_PRICE = 3

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
    def new_release_price(cls, days_rented):
        return days_rented * Movie.NEW_RELEASE_PRICE

    @classmethod
    def children_price(cls, days_rented, min_days):
        return cls.more_than_min_day_price(Movie.CHILD_PRICE, days_rented, min_days) \

    @classmethod
    def regular_price(cls, days_rented, min_days):
        return cls.more_than_min_day_price(Movie.REGULAR_PRICE, days_rented, min_days)

    @staticmethod
    def more_than_min_day_price(genre_price, days_rented, min_days):
        return genre_price + (days_rented - min_days) * Movie.BASE_PRICE