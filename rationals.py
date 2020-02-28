from math import gcd

#rational number class definiton
class Rational:
    def __init__(self, num=0, denom=1):
        if type(num) is not int or type(denom) is not int:
            print("arguments must be integers. numerator set to 0 and denominator set to 1.")
            self.numerator = 0
            self.denominator = 1
        else:
            self.numerator = num
            self.denominator = denom
        
    def reduced(self):
        GCD = gcd(self.numerator, self.denominator)
        reduced = Rational(int(self.numerator/GCD), int(self.denominator/GCD))
        return reduced

    def __str__(self):
        if self.denominator == 1 or self.numerator == 0:
            return f'{self.numerator}'
        return f'{self.numerator}/{self.denominator}'

    def __repr__(self):
        if self.denominator == 1 or self.numerator == 0:
            return f'{self.numerator}'
        return f'{self.numerator}/{self.denominator}'
    
    def __add__(self, other):
        return(Rational(self.numerator*other.denominator+self.denominator*other.numerator,
                            self.denominator*other.denominator).reduced())

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __sub__(self, other):
        return(Rational(self.numerator*other.denominator-self.denominator*other.numerator,
                            self.denominator*other.denominator).reduced())

    def __mul__(self, other):
        return(Rational(self.numerator*other.numerator, self.denominator*other.denominator).reduced())

    def __truediv__(self, other):
        return(Rational(self.numerator*other.denominator, self.denominator*other.numerator).reduced())

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