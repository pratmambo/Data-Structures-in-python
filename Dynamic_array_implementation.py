import ctypes


class DynamicArray(object):

    def __init__(self):

        self.n = 0                          # n is size of array initially 0
        self.cap = 1                        # cap is capacity of array initially 1
        self.A = self.make_array(self.cap)   # A is the reference of array and create array of size 1

    def len(self):

        return self.n                           # returns n i.e size of array

    def __getitem__(self, item):

        if not 0 <= item <= self.n:             # check if item asked is in range
            return IndexError("index value out of bounds")

        return self.A[item]                     # if item is in range returns value in that index

    def append(self, val):

        if self.n == self.cap:                  # check if array is full
            self._resize(2 * self.cap)          # increase size to two times the original

        self.A[self.n] = val                    # put val in end
        self.n += 1                             # increase size of array by 1

    def _resize(self, new_cap):

        b = self.make_array(new_cap)             # reference of new array of twice the size

        for i in range(new_cap):                # copying old elements to new array (referencing)
            b[i] = self.A[i]
        self.cap = new_cap                      # updating capacity
        self.A = b                              # referencing B array with A

    def make_array(self, capacity):

        return(capacity * ctypes.py_object)()   # creating a static array of size = capacity

