# FILE NAME - convert_C_to_F_02.py

# NAME:Kandise Perkins
# DATE: October 5, 2025
# BRIEF DESCRIPTION: Convert temperature both ways using if statements



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########
def main():
    convert_C_to_F_02()

def convert_C_to_F_02():
  print('===== Temperature Converter =====')
  print()
  #temperature conversion options
  #option_1
  print('  1. Convert from Celsius to Fahrenheit')
  #option_2
  print('  2. Convert from Fahrenheit to Celsius')
  print()
  choice=input('Please choose from the above menu: ')
  #if 
  if choice == '1':
       celsius =float(input('Enter a temperature to convert: '))
#Formula: C * 9/5 + 32
       degree_f = celsius * 9/5 + 32
       print()
       print(f'{celsius} degrees Celsius is {degree_f:.1f} degrees Fahrenheit.')
  elif choice == '2':
       fahrenheit =float(input('Enter a temperature to convert: '))
       degree_c = (fahrenheit-32)*5/9
       print()
       print(f'{fahrenheit} degrees Fahrenheit is {degree_c:.1f} degrees Celsius.') 

#run
main()









########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?
indentation is critical to a successful code and sequence matters.






'''
