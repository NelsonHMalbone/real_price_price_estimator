# this is a real estate price estimator

# city is 250 per square foot this is hardcoded for now
# suburbs is 150 per square foot this is hardcoded for now

property_size_input = float(input("Enter the size of the property in square feet: "))

# added the input for user to add there own input for cost per sqft
cost_per_sq_ft = int(input("Enter the cost of the property Per Sqft: "))

location_input = input("Enter the location (city or suburbs): ").lower()

# logic to know if user has enter city or suburbs

if location_input == 'city':
    price_per_sqft = cost_per_sq_ft * property_size_input
    print(f"The estimated price for a {property_size_input} sq ft property in the {location_input} is: {'${:,.2f}'.format(price_per_sqft)}") # format function turns values to string following formatting instructions
elif location_input == 'suburbs':
    price_per_sqft = cost_per_sq_ft * property_size_input
    print(f"The estimated price for a {property_size_input} sq ft property in the {location_input} is: {'${:,.2f}'.format(price_per_sqft)}") # format function turns values to string following formatting instructions
else:
    print("Please enter suburbs or city")