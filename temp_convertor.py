def convert_temperature(temp, unit):
    if unit == 'F':
        # Convert Fahrenheit to Celsius
        converted_temp = (temp - 32) * 5 / 9
    elif unit == 'C':
        # Convert Celsius to Fahrenheit
        converted_temp = (temp * 9 / 5) + 32
    else:
        raise ValueError("Invalid unit.")
    
    # Round the result to 2 decimal places
    return round(converted_temp, 2)

# Get user input
try:
    temp = float(input("Enter the temperature to convert: "))
    unit = input("Enter the unit of the temperature (F for Fahrenheit, C for Celsius): ").strip().upper()

    # Call the conversion function and print the result
    converted_temp = convert_temperature(temp, unit)
    print(f"The converted temperature is: {converted_temp}°{'C' if unit == 'F' else 'F'}")
except ValueError as e:
    print(e)
