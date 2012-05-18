
def is_paired(func):
    def gen(a,b):
        #search metod to get params
        for item in [a,b]:
            if item%2:
                print '%s is not positive!'% item
                return
        return func(a,b)
    print func
    return gen
    

#positiveSum = is_positive(positiveSum)
@is_paired
def positiveSum(a,b):
    return a+b

print positiveSum(2,4)