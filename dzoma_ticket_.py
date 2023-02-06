class Types_ticket:

    def __init__(self, type, discount = 0):
        self.type = type
        if not isinstance(discount, int | float):
            raise ValueError
        self.discount = discount

    def __str__(self):
        return f'{self.type}'


class Ticket:

    def __init__(self, number, price: float, type):
        number_set = set([])
        if number in number_set:
            raise ValueError
        else:
            number_set.add(number)
        self.number = number

        if not isinstance(price, float | int):
            raise TypeError('Price must be number')
        self.price = price

        if not isinstance(type, Types_ticket):
            raise ValueError
        self.type = type

    def ask_number(self):
        return self.number

    def discount_type(self):
        self.price = self.price - (self.type.discount / 100 * self.price)
        return self.price


    def __str__(self):
        return f'Number of ticket {self.number}\n\tType: {self.type}\n\tDiscount: {self.type.discount} % \n\tPrice: {self.price}\n'


if __name__ == '__main__':
    type_regular = Types_ticket('regular ticket')
    type_advance = Types_ticket('advance ticket', 40)
    type_late = Types_ticket('late ticket',  10)
    type_student = Types_ticket('student ticket', 50)


    a = Ticket(125, 15, type_regular)
    b = Ticket(128, 15, type_advance)
    a.discount_type()
    b.discount_type()

    print(a)
    print(b)