def isPandigitalString(string):
#    """ Check if string contains a pandigital number. """
    digits = len(string)

    if digits >= 10:
        return False

    for i in xrange(1,digits+1):
        if str(i) not in string:
            return False
    return True
#We also need a check if a product of two numbers is 9-pandigital:

def gives9PandigitalProduct(a, b):
    numbers = str(a) + str(b) + str(a*b)  
    if len(numbers) != 9:
        return False
    return isPandigitalString(numbers)
#Now you need to figure out how to go through all possible combinations:

products = []
for a in xrange(0, 100000):
    for b in xrange(a, 100000):
        if len(str(a*b) + str(a) + str(b)) > 9:
            break
        if gives9PandigitalProduct(a, b):
            products.append(a*b)
            print("%i x %i = %i" % (a, b, a*b))
print(sum(set(products)))
      
