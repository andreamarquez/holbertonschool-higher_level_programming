class MyList(list):
    """
    A class that inherits from list and provides a method to print
    the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.

        Assumes that all elements of the list are of type int.
        """
        print(sorted(self))
