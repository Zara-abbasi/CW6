class Score:
    def __init__(self, value):

        if not isinstance(value, int):
            raise TypeError("value must be number")
        else:

            self.value = value

    def __add__(self, other):
        if isinstance(other, Score):
            return Score(self.value + other.value)

    def __sub__(self, other):
        if isinstance(other, Score):
            result = self.value - other.value
            return Score(result)

    def __str__(self):
        return f"{self.value}"

    def __lt__(self, other):
        if isinstance(other, Score):
            return other.value < self.value
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Score):

            return self.value == other.value
        else:
            return NotImplemented

    def __le__(self, other):
        if isinstance(other, Score):
            return self.value <= other.value
        else:
            return NotImplemented


s1 = Score(60)
s2 = Score(20)
s3 = Score(20)
s3 = s1 + s2
s4 = s1 - s2
s4 <= s3
print(s4)
print(s3)
print(type(s4))
print(s1 == s2)
print(s4 <= s3)
print(type(s3))
print(s2 == s3)
print(s3 > s2)

# class Score(int):
#     def __init__(self, value):

#         if not isinstance(value, int):
#             raise TypeError("value must be number")
#         else:

#             self.value = value

#     def __add__(self, other):
#         if isinstance(other, Score):
#             return Score(self.value + other.value)

#         # raise TypeError("   ")

#     def __sub__(self, other):
#         if isinstance(other, Score):
#             result = self.value - other.value
#             return result

#     def __str__(self):
#         return f"{self.value}"


# # a = 2
# # print(type(a))


# # class Sample:
# #     pass


# # print(dir(Sample))
