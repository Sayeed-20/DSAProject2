class House:
    def __init__(self, id, price, city, propType, long, lat, bedrooms, baths):
        self.id = id
        self.price = price
        self.city = city
        self.propType = propType
        self.long = long
        self.lat = lat
        self.bedrooms = bedrooms
        self.baths = baths

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price

    def __eq__(self, other):
        return self.price == other.price

    def __ne__(self, other):
        return self.price != other.price

    def __le__(self, other):
        return self.price <= other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __str__(self):
        return f"id: {self.id},  price: {self.price},  city: {self.city},  propType: {self.propType},  beds: {self.bedrooms},  baths: {self.baths}"