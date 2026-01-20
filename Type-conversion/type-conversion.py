#type conversion
a = 5
print(type(a)) #int
b = 3.2
print(type(b)) #float

#type casting --> int() , float() , str()

# converting integer to float
a_float = float(a) #type casting

# converting float to integer
b_int = int(b) #type casting

print("Integer a: ", a)
print("Converted to float a_float: ", a_float)
print("Float b :", b)
print("Converted to integer b_int ", b_int)

# converting integer to string
a_str = str(a)

# converting float to string
b_str = str(b)

print("Converted to string a_str: ", a_str)
print("Converted to string b_str: ", b_str)

# converting string to integer
c_str = "10"
c_int = int(c_str)

print("String c_str: ", c_str)
print("Converted to integer c_int: ", c_int)
# converting string to float
d_str = "7.5"
d_float = float(d_str)

print("String d_str: ", d_str)
print("Converted to float d_float: ", d_float)
#END