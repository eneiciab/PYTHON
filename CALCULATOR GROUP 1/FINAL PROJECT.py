######## MAIN CALCULATOR ##############
import sys
import os
import time

def main_calc():
        os.system('cls')

        print ('''
+  -  /  *  =  -  /  *   Welcome to Calculator   +  -  /  *  +  -  /  *

                      Please select an Operation :

                        1 : Simple Calulations
                        2 : Temperature Converter
                        3 : Area Calculation
                        4 : To Quit''')
                        
        choice = input('\nEnter Choice (1 - 4) : ')
        
        if choice == '1':
            simple_calc()
        elif choice == '2':
            temp_conv()
        elif choice == '3':
            area_calc()
        elif choice == '4':
            print('GoodBye!')
            exit()
        else:
            print('\nInvalid Choice, Please Try Again.')
            input()
            main_calc()

###### SIMPLE CALCULATOR #######

def simple_calc():
        print ('''
                        Simple Calculator
                ---------------------------------        
            Which simple calculation do you want to use?
                        1. Addition
                        2. Subtraction
                        3. Multiplication
                        4. Division
                        5. Return to Main Menu''')

        choice = input('Enter Choice (1 - 5) : ')
        
        if choice == '1':
            try:
                number_1 = float(input('Please enter the first number: '))
                number_2 = float(input('Please enter the second number: '))
            except Exception: 
                print ('Invalid input detected, Please Try Again.')
                simple_calc()
                
            print(number_1, '+', number_2, '=', (number_1 + number_2))
            simple_calc()                
    
        elif choice == '2':
            try:
                number_1 = float(input('Please enter the first number: '))
                number_2 = float(input('Please enter the second number: '))
            
            except Exception: 
                print ('Invalid input detected, Please Try Again.')
                simple_calc()
            
            print(number_1, '-', number_2, '=', (number_1 - number_2))
            simple_calc()
    
        elif choice == '3':
            try:
                number_1 = float(input('Please enter the first number: '))
                number_2 = float(input('Please enter the second number: '))
            
            except Exception: 
                print ('Invalid input detected, Please Try Again.')
                simple_calc()

            print(number_1, '*', number_2, '=', (number_1 * number_2))
            simple_calc()

        elif choice == '4':
            try:
                number_1 = float(input('Please enter the first number: '))
                number_2 = float(input('Please enter the second number: '))
                if number_2 == 0 :
                        print ('Cannot divide by 0, Please Try Again.')
                        simple_calc()
                else:
                        print(number_1, '/', number_2, '=', (number_1 / number_2))
                        simple_calc()
            except Exception: 
                print ('Invalid input detected, Please Try Again.')
                simple_calc()  
                
        elif choice == '5':
            main_calc()
            
        else :
            print('Invalid Choice, Please Try Again.')
            simple_calc()
            

######## TEMPERATURE CONVERSION ##########
def temp_conv():
    print ('''
                      Tempurature Calculator
                ---------------------------------  
        Which temperature conversion would you like to use?
                    1. Fahrenheit to Celsius
                    2. Celsius to Fahrenheit
                    3. Return to Main Menu 
                    ''')
    
    choice = input('Enter Choice (1 - 3) : ')
    
    if choice == '1' :
        try:
            fahrenheit = float(input("Enter temperature in fahrenheit: "))
            celsius = (fahrenheit - 32) * 5 / 9
            print('%.2f°F is %0.2f°C' %(fahrenheit, celsius))
        except Exception: 
                print ('Invalid input detected, Please Try Again.')
                temp_conv()

    
    elif choice == '2':
        try:
            celsius = float(input("Enter temperature in celsius: "))
            fahrenheit = (celsius * 9 / 5) + 32
            print('%.2f°C is %0.2f°F' %(celsius, fahrenheit))
        except Exception: 
                print ('Invalid input detected, Please Try Again.')
                temp_conv()

    
    elif choice == '3':
        main_calc()

    else:
        print('Invalid input, Please Try Again.')
        temp_conv()

    choice = input('Would you like to convert another temperature? Y for Yes/ N for No ')
    
    if choice.upper() == 'Y':
        temp_conv()
    
    elif choice.upper() == 'N':
        main_calc()
    
    else:
        print ('Invalid Choice, Please Try Again.')
        temp_conv()
        

############## AREA CALCULATOR ############

def area_calc():
            os.system('cls')

            print("""
            Area Calculator
            ----------------
              1. Square
              2. Circle
              3. Rectangle
              4. Triangle
              5. Return to Main Menu
            """)

            choice = input('Enter Choice (1 - 5) : ')
                  
            if choice == '1':
               f_square()
            elif choice == '2':
               f_circle()
            elif choice == '3':
               f_rectangle()
            elif choice == '4':
               f_triangle()
            elif choice == '5':
               main_calc()           
            else:
                print('\nInvalid Option Selected, Please Try Again.')
                input()
                
                area_calc()


def f_square():
    os.system('cls')

    print("""
    1. Square Area Calculator
    -------------------------
    """)

    try:
       
       side = float(input("Enter a Number Greater than zero for the Square side: "))
         
    except:
       print("\nThat is not a Valid Number, Please Try Again.")

    else:
        if side > 0:     
           area = (side ** 2)
           print ("\nThe Square Calculated Area is: %.2f" % area)

        else:   
           print("\nThat is not a Valid Number, Please Try Again.")

    input()    
    area_calc()

def f_circle():
    os.system('cls')

    print("""
    2. Circle Area Calculator
    -------------------------
    """)

    pie = 3.14
    
    try:
       radius = float(input("Enter a Number Greater than Zero for the Circle Radius: "))
     
    except:
       print("\nThat is not a Valid Number, Please Try Again.")

    else:
       if radius > 0:
           area =  (2 * pie * radius)
           print ("\nThe Circle Calculated Area is: %.2f" % area)
           
       else:
           print("\nThat is not a Valid Number, Please Try Again.")

    input()
    area_calc()
    
def f_rectangle():
    os.system('cls')

    print("""
    3. Rectangle Area Calculator
    -----------------------------
    """)

    try:
       length = float(input("Enter a Number Greater than Zero for the Rectangle length: "))
              
    except:
       print("\nThat is not a Valid Number, Please Try Again.")

    else:
     
        if length > 0:
          
           try:
              width = float(input("\nEnter a Number Greater than Zero for the Rectangle width: "))
           
           except:
               print("\nThat is not a Valid Number, Please Try Again.")

           else:
               if width > 0:
                   area =  (length * width)
                   print ("\nThe Rectangle Calculated Area is: %.2f" % area)
               else:
                   print("\nThat is not a Valid Number, Please Try Again.")    
        
        else:
            print("\nThat is not a Valid Number, Please Try Again.")

   
    input()
    area_calc()
    

def f_triangle():
    os.system('cls')

    print("""
    4. Triangle Area Calculator
    ---------------------------
    """)

    try:
       base = float(input("Enter a Number Greater than Zero for the Triangle Base: "))
              
    except:
       print("\nThat is not a Valid Number, Please Try Again.")

    else:
     
        if base > 0:
          
           try:
              height = float(input("\nEnter a Number Greater than Zero for the Triangle height: "))
           
           except:
               print("\nThat is not a Valid Number, Please Try Again.")

           else:
               if height > 0:
                   area = (0.5 * base * height)
                   print ("\nThe Triangle Calculated Area is: %.2f" % area)
               else:
                   print("\nThat is not a Valid Number, Please Try Again.")    
        
        else:
            print("\nThat is not a Valid Number, Please Try Again.")


main_calc()
