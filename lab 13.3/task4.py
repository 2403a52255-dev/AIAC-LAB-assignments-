# AI suggested a list comprehension

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [i * i for i in nums]
cubes = [i ** 3 for i in nums]
even_squares = [i * i for i in nums if i % 2 == 0]
numbers_str = [str(i) for i in nums]

print("Numbers:", nums)
print("Squares:", squares)
print("Cubes:", cubes)
print("Even Squares:", even_squares)
print("Numbers as strings:", numbers_str)



