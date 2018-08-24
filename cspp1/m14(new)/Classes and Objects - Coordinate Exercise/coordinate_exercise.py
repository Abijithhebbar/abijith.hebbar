"""# Exercise: coordinate
# Consider the following code from the last lecture video:"""
class Coordinate(object):
    """ coordinate function"""
    def __init__(self, inp_x, inp_y):
        """intialize"""
        self.inp_x = inp_x
        self.inp_y = inp_y
    def get_x(self):
        """ Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly"""
        return self.inp_x
    def get_y(self):
        """ Getter method for a Coordinate object's y coordinate"""
        return self.inp_y
    def __str__(self):
        return '<' + str(self.get_x()) + ',' + str(self.get_y()) + '>'
    def __eq__(self, other):
        if self.get_x() == other.get_x():
            if self.get_y() == other.get_y():
                return True
        return False
    def __repr__(self):
        return 'Coordinate(' + str(self.get_x()) + ',' + str(self.get_y()) + ')'
    # object with the same value. In other words,
    # eval(repr(c)) == c given the definition of __eq__ from part 1.
def main():
    """main """
    data = input()
    data = data.split(' ')
    data = list(map(int, data))
    print(Coordinate(data[0], data[1]) == Coordinate(data[2], data[3]))
    print(Coordinate(data[4], data[5]).__repr__())

if __name__ == "__main__":
    main()
