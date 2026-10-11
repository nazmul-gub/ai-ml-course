prompt = "What is your name ?"

tokens = prompt.split()
print(tokens)
print(type(tokens))

sen = " ".join(tokens)
print(sen)
print(type(sen))



# list comprehension

even = [x for x in range(2,11) if x % 2 == 0]
print(even)