class Score:
    def __init__(self, value):
        self.value = value
        if isinstance(value, int):
            raise TypeError("value must be number")

        def __add__(self, number):
            if isinstance(number, value):
                return Score(value + number)
            raise TypeError("   ")

        def __sub__(self, number):
            if isinstance(self, number):
                return Score(value - number)
            raise TypeError("   ")

        def __lt__(self, number):
            if isinstance(value, number):
                return value > number
            else:
                return NotImplemented

        def __eq__(self, number):
            if isinstance(value, number):
                return value == number
            else:
                return NotImplemented

        def __le__(self, number):
            if isinstance(value, number):
                return value >= number
            else:
                return NotImplemented


s1 = Score(60)
s2 = Score(20)

s3 = s1 + s2
s4 = s1 - s2

print(s3)
print(s1 == s2)


#anything 
# anything else