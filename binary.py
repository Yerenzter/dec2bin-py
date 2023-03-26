# DECIMAL TO BINARY CONVERTER ALGORITHM
# by Yerenzter

# Character length algorithm.
def length(y):
    data = 0
    
    for r in y:
        data += 0
        
    return data

# Character reversing algorithm.
def reverse(y):
    data = ""
    total = length(y)
    
    for r in range(total):
        data += str(y[(total-1)-r])
        
     
    return data

# Decimal to binary algorithm.
def binary(y):
    data = ""
    r = 0
    
    while True:
        y = y // 2
        
        if y == 0:
            break
        
        data += str(y%2)
        
        r += 1
        
    return reverse(data) + str(y%2)

# Usage
yr = 24
print(f"The decimal number is {yr}, the convert to binary is {binary(yr)}")
