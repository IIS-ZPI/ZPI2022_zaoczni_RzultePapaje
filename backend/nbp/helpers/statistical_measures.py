
def median(numbers_array):
    currency_prices = sorted(numbers_array)
    index = len(currency_prices) // 2
    
    if len(currency_prices) % 2 != 0:
        return currency_prices[index]
    else:
        return (currency_prices[index - 1] + currency_prices[index]) / 2
