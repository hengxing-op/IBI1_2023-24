def chocolate_affordability(total_money, price_per_bar):
    # Calculate the number of chocolate bars that can be bought
    number_of_bars = total_money // price_per_bar
    # Calculate the remaining change
    change_left = total_money % price_per_bar
    
    return int(number_of_bars), change_left

# Example function call
total_money = 10 # Input position
price_per_bar = 7 # Input position

bars, change = chocolate_affordability(total_money, price_per_bar)
print(f"You can buy {bars} chocolate bars and have {change} money left.")