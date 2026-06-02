def print_hello(name):
    print(f"Hello, {name}!")


string = "Patrik"
print_hello(string)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
    
print(gcd(2,20))
