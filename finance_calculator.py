import math

print("Choose either 'investment' or 'bond' from\
the menu below to proceed: " + "\n" + "\n" + 
"Investment      - to calculate the amount of int\
erest you'll earn on interest" + "\n" + "\n" + 
"Bond            - to calculate the amount you'll \
have to pay on a home loan"+ "\n" + "\n")

#Manipulate the string to lower case into all lower case

calc_options = input("Enter your option here: ").lower() 

if calc_options == "investment":

  # input variables to be used to calc invesment
  
  P = int(input("\n" + "Please input amount of money being deposited: R "))
  
  rate = float(input("Please input interet rate (without % sign): "))
  
  t = int(input("Please input number of intended years of investment: "))
  
  interest = input("Please select 'simple' or 'compound' interest: ").lower()

  # real rate

  r = rate * 0.01

    #calc for compound interest

  if interest == "compound":
    A = P* math.pow((1 + r), t)
    print("Total investment amount based on compound interest: " + str(A))

    # calc for simple interest
  elif interest == "simple":
    A = P* (1 + r*t)
    print("Total investment amount based on simple interest: " + str(A))

    # Message to be shown if neither compound or simple interest are chosen

  else:
    print("Please choose between 'compound' and 'simple' interest options!")

if calc_options == "bond":

  # input variables used to calc bond

  P = float(input("\n" + "Please input present value of house: R "))
  interest = float(input("Please input yearly interest rate: "))
  rate = interest * 0.01
  i = rate / 12
  months = int(input("Please enter number of months over which the bond will be repaid: "))
  n = months * -1

  # Monthly amount calc 
  x = (i * P) / (1 - math.pow((1+i), n))
  print("Amount to be repaid on homeload each month is: R " + str(x))

  # Message to be shown if neither investment or bond are chosen

if calc_options != "investment" and calc_options != "bond":
  print("Error: Please choose an option listed. 'Investment' or 'Bond'.")
