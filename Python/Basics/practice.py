# You are given a list of marks: [90, 40, 75, 88, 35]. For each mark, print the mark and Pass if it is at least 40, otherwise Fail. Then print how many students passed and the average of all marks. Sample Input: No input Sample Output: 90 Pass 40 Pass 75 Pass 88 Pass 35 Fail Passed: 4 Average: 65.6


#1
def  introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

# introduce("Nazmul", 20)

# #2

# data = [1, 2, 3, 4, 5, 6, 7, 8]
# batch_size = 3

# def batch_generator(data, batch_size):
#     for i in range(0, len(data), batch_size):
#         yield data[i: i+batch_size]

# batch = batch_generator(data, batch_size)
# print(next(batch))
# print(next(batch))
# print(next(batch))

#3

l = [1,2,3,4]

square = list(map(lambda x: x**2, l))
print(square)

#4

def power(base, exponent = 2):
    return base ** exponent

# print(power(5, 3))

#5

numbers = [1, 2, 3, 4, 5, 6]

ans = list(filter(lambda x: x%2 == 0, numbers))

result = list(map(lambda x: x**2, ans))
print(result)

