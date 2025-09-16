#contact
#F-strings
#print
#float



# get temp in celsius
celsius = float(input("Enter temperature in Celsius: "))

# convert to F
fahrenheit = (celsius * 9/5) + 32

#display result
print(str(celsius) + "°C is equal to" + str(fahrenheit) +"" + "°F")

#template literals
print(f"{celsius}°C is equal to {fahrenheit} °F")