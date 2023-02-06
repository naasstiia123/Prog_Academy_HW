class Goods:

    def __init__(self, name, price: float, description, size):
        self.name = name
        self.description = description
        self.size = size
        self.price = price

        if self.price < 0:
            raise Price_error(f'Price {self.price} must be positive')

    def __str__(self):
        return f'{self.name}, {self.size}, {self.price}'

class Customer:

    def __init__(self, surname,  name, phone_number):
        self.surname = surname
        self.name = name
        self.phone_number = phone_number

    def __str__(self):
        return f'{self.surname} {self.name}'

class Order:

    def __init__(self, customer: Customer):
        self.customer = customer
        self.order = []
        self.amount = []
        self.index = 0

    def __next__(self):
        if self.index < len(self.order):
            self.index += 1
            return self.order[self.index - 1]
        else:
            raise StopIteration


    def __iter__(self):
        return self

    def __getitem__(self, index):
        if isinstance(index, slice):
            start = 0 if index.start == None else index.start
            stop = len(self.order) - 1 if index.stop == None else index.stop
            step = 1 if index.step == None else index.step
            if index.start < 0 or index.stop > len(self.order):
                raise IndexError
            else:
                result = []
            for i in range(start, stop, step):
                result.append(self.order)
            return result
        if isinstance(index, int):
            if index < len(self.order):
                return self.order[index]
            else:
                raise IndexError
        raise TypeError


    def __len__(self):
        return len(self.order)

    def add_goods(self, order: Goods, quantity):
        self.order.append(order)
        self.order.append(quantity)
        self.amount.append(order.price * quantity)

    def __str__(self):
        return f'{self.customer} - amount due:{sum(self.amount)}\n\t'\
               + '\n\t'.join(map(str, self.order))


class Price_error(Exception):
    def __init__(self, massage):
        super().__init__(massage)
        self.massage = massage

    def error_massage(self):
        return self.massage


if __name__ == '__main__':
    good_1 = Goods('Shirt', 10, 'White', 'S')
    good_2 = Goods('T-Shirt', 12.1, 'Blue', 'M')
    good_3 = Goods('Pants', 25, 'Black', 'M')
    good_4 = Goods('Skirt', 17.5, 'White', 'S')



    customer_1 = Customer('Ivanov', 'Ivan', '+380111111111')
    customer_2 = Customer('Dzoma', 'Anastasiia', '+380222222222')
    customer_3 = Customer('Dzoma', 'Anna', '+380333333333')

    order_1 = Order(customer_2)
    order_1.add_goods(good_2, 5)
    order_1.add_goods(good_3, 2)
    order_1.add_goods(good_4, 1)


    for i in order_1:
        print(i)

    print(order_1[0])
