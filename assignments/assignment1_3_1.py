from unittest import *    
import doctest
import io
from contextlib import redirect_stdout

def function_to_unittest(list):
    ordered = []
    for item in list:
        if item < 0:
            item *= -1
            item += 1
            
        if item % 2 == 1:
            if not is_prime(item):
                continue
        ordered = insert(item, ordered)
    return ordered


def insert(item, list):
    for index in range(0, len(list)):
        if list[index] > item:
            list.insert(index, item)
            break
    else:
        list.append(item)

    return list


def is_prime(n):
    if n < 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True

class ExerciseTest(TestCase):
    def setUp(self):
        #TODO schrijf hier globale dingen die nodig zijn voordat de tests gedraait gaan worden.
        self.testlist = [0, 1]
        self.testnegativity = [-1, -5, -7]
        self.testprime = [3, 5, 9]
        self.testorder = [1, 2, 0]
        pass # Pass om syntax errors te voorkomen in de notebook

    #TODO definieer hieronder je tests
    # LET OP: de functies die je als tests schrijft moeten in de naam met 'test' beginnen!
    def test_1(self): # voorbeeld
        testoutput = function_to_unittest(self.testlist)
        self.assertEqual([0, 1], testoutput, "Function doesn't handle [0, 1] correctly")
        pass # Pass om syntax errors te voorkomen in de notebook
    
    def test_negativity(self):
        testoutput = function_to_unittest(self.testnegativity)
        self.assertEqual([2, 6, 8], testoutput, "Function doesn't handle negativity correctly")
        pass
    
    def test_prime(self):
        testoutput = function_to_unittest(self.testprime)
        self.assertEqual([3, 5], testoutput, "Function doesn't handle odd non-primes correctly")
    
    def test_order(self):
        testoutput = function_to_unittest(self.testorder)
        self.assertEqual([0, 1, 2], testoutput, "Function doesn't handle order correctly")
        
test = ExerciseTest()
suite = TestLoader().loadTestsFromModule(test)
TextTestRunner().run(suite)