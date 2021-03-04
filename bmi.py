# Prompt for input variables
heightft = input("Enter your height (feet): ")    
heightin = input("Enter your height (inches): ")
weight = input("Enter your weight (pounds): ")

# Ensure that entries are not blanks
if heightft == "" or heightin =="":
    print ("Please enter your height.")
    exit()
if weight == "":
    print ("Please enter your weight.")
    exit()

# Format entries as float data type
heightft = float(heightft)
heightin = float(heightin)
weight = float(weight)



# Handle abnormal entries for heights and weights
if heightft <0 or heightin <0:
    print ("You cannot possibly have a negative height!")
    exit()
if heightft > 10:
    print ("Are you really " + str(heightft) + " feet tall ?!")
    exit()
if heightin > 12:
    print ("Your height in inches shouldn't exceed 12!")
    exit()
if weight < 0:
    print ("Your weight cannot be negative on Earth ...")
if weight > 750:
    print ("Do you really weigh " + str(weight) + " pounds?!")
    exit()

# Calculate total height in inches
height = heightft*12 + heightin  
# Compute BMI
thisBMI =  round((weight /(height*height)) * 703.06957964,2)



# Interpret BMI  
if thisBMI < 18.5: 
    print ("Your BMI is ", thisBMI, " Underweight - Eat a healthy balanced diet!")
elif  18.5 <= thisBMI <= 24.99:
    print ("Your BMI is ", thisBMI, " - Normal, keep it up!")
elif  25 <= thisBMI <= 29.99:
    print ("Your BMI is ", thisBMI, " - Overweight, exercise more!")
elif 30 <= thisBMI <=  39.99:
    print ("Your BMI is ", thisBMI, " - Obese, Eat more healthy!")
elif thisBMI >=40:
    print ("Your BMI is ", thisBMI, " - Obese - Go for a walk!")
else:  
    print("Please check your input values, BMI cannot be calculated.")
