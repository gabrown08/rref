# import built-in gcd
from math import gcd

#rational number class definiton
class Rational:
    # define Rational instantiation
    def __init__(self, num=0, denom=1):
        if type(num) is not int or type(denom) is not int:
            print("arguments must be integers. numerator set to 0 and denominator set to 1.")
            print()
            self.numerator = 0
            self.denominator = 1
        else:
            self.numerator = num
            self.denominator = denom
            self.decimal = self.numerator/self.denominator
            self.reduced()
        
    # define how Rationals are printed 
    def __str__(self):
        if self.denominator == 1 or self.numerator == 0:
            return f'{self.numerator}'
        return f'{self.numerator}/{self.denominator}'

    # define how Rationals are printed in lists
    def __repr__(self):
        return self.__str__()

    # define length of a Rational
    def __len__(self):
        return 1
    
    # define equality between Rationals
    def __eq__(self, other):
        if type(other) == int:
            other = Rational(other)
        if self.numerator*other.denominator == self.denominator*other.numerator:
            return True
        return False

    # define addition between Rationals
    def __add__(self, other):
        if type(other) == int:
            other = Rational(other)
        return(Rational(self.numerator*other.denominator+self.denominator*other.numerator,
                        self.denominator*other.denominator).reduced())

    # define reflective addtion between Rationals
    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    # define subtraction between Rationals
    def __sub__(self, other):
        if type(other) == int:
            other = Rational(other)
        return(Rational(self.numerator*other.denominator-self.denominator*other.numerator,
                        self.denominator*other.denominator).reduced())
    
    # define reflective subtraction between Rationals
    def __rsub__(self, other):
        if type(other) == int:
            other = Rational(other)
        return other.__sub__(self)

    # define multiplication
    def __mul__(self, other):
        if type(other) == int:
            other = Rational(other)
        return(Rational(self.numerator*other.numerator, self.denominator*other.denominator).reduced())

    # definte reflecdtive multiplication
    def __rmul__(self, other):
        if type(other) == int:
            other = Rational(other)
        return self.__mul__(other)

    # define division
    def __truediv__(self, other):
        if type(other) == int:
            other = Rational(other)
        return(Rational(self.numerator*other.denominator, self.denominator*other.numerator).reduced())

    # define reflective division
    def __rtruediv__(self, other):
        if type(other) == int:
            other = Rational(other)
        return other.__truediv__(self)

    # define rounding to the nearest whole number
    def __round__(self):
        return round(self.decimal)

    # reduce Rational
    def reduced(self):
        GCD = gcd(self.numerator, self.denominator)
        if GCD > 1:
            self.numerator = self.numerator//GCD
            self.denominator = self.denominator//GCD
        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1
        return self

if __name__ == "__main__":
    #testing
    number1 = Rational(8.2351342,.134523)
    number2 = Rational(50,70)
    print(f'{number1} + {number2} = {number1+number2}')
    number3 = Rational(81342,4523)
    number4 = Rational(564,17)
    print(f'{number3} + {number4} = {number3+number4}')
    print(f'{number3} - {number4} = {number3-number4}')
    print(f'{number3} * {number4} = {number3*number4}')
    print(f'{number3} / {number4} = {number3/number4}')
    print(gcd(number1.numerator, number1.denominator))
    print(Rational(2,1).reduced())
    print(Rational(0, 50))

    print(sum([number1, number2, number3, number4]))

    print(number1 == number2)
    print(number1 == number1)
    print(Rational(2,1) == 2)
    print(Rational(32,16)==Rational(8,4))

    print(5+Rational(16,5))

    print(Rational(Rational(18)))


    print(Rational(2)/3)
    print(2/Rational(3))

    print(1-Rational(2))

    print(1/Rational(2))


    print(gcd(14229953751227572130132919320576,7114976875613804079464969142272))

    print(Rational(14229953751227572130132919320576,7114976875613804079464969142272).reduced())
    print()
    number5 = Rational(14229953751227572130132919320576,7114976875613804079464969142272)
    print(number5)
    number5.reduced()
    print(number5)

    print(number5.decimal)