import math
# test = [181, 187, 196, 196, 198, 203, 207, 211, 215, 123, 199]
# test2 = [7, 4, -2]

def median(numbers_array):
    currency_prices = sorted(numbers_array)
    index = len(currency_prices) // 2
    
    if len(currency_prices) % 2 != 0:
        return currency_prices[index]
    else:
        return (currency_prices[index - 1] + currency_prices[index]) / 2
    
def dominant(numbers_array):
    counts = {}
    max_value = 0
    for number in numbers_array:
        if number not in counts:
            counts[number] = 1
        else:
            counts[number] = counts[number] + 1
    
    for number in counts:
        if counts[number] > max_value:
            dominant = number
            max_value = counts[number]
            
    return dominant

def standard_deviation(numbers_array):
    mean = sum(numbers_array) / len(numbers_array)
    dominator = list(map(lambda x: pow(x-mean,2), numbers_array))
    variation = sum(dominator) / len(dominator)
    return math.sqrt(variation)

def coefficient_of_variation(numbers_array):
    mean = sum(numbers_array) / len(numbers_array)
    deviation = standard_deviation(numbers_array)
    return mean / deviation

    