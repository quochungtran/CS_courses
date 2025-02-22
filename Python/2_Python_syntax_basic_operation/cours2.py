# case_sentive 

myvar = 2
myVar = 3
print(myvar)

def run():
    print("Running in 10 km")

# data_type

a = 1
print(type(a))  # type() function to show data type 

b = 3.14
print(type(b))

text = "Hello"
another_string = 'Python is fun'

print(type(text))
print(type(text[0])) # [] indexing operator allowing to access at index i_th arr[i]
print(type(another_string))

# Arithmetic Operations
a = 10
b = 3

sum_result = a + b       # 13
diff_result = a - b      # 7
prod_result = a * b      # 30
quot_result = a / b      # 3.3333...
mod_result = a % b       # 1

print("sum of 10 vs 3: " , sum_result)
print("mod of 10 vs 3: " , mod_result)


# f-string
name1 = "Dung"
name2 = "Mai"

print(f"{name1} is {name2} brother")