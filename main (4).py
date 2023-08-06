def calculate_years_to_double(rate, initial_investment):
    years = 0
    current_value = initial_investment
    
    while current_value < (2 * initial_investment):
        current_value += current_value * (rate / 100)
        years += 1
    
    return years


# Example usage
interest_rate = float(input("Enter the annualized interest rate (%): "))
investment_amount = float(input("Enter the initial investment amount: "))

years_to_double = calculate_years_to_double(interest_rate, investment_amount)

print("It will take approximately", years_to_double, "years for the investment to double.")
