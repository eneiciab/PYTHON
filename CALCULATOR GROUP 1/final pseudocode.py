DEFINE main_calc
    PRINT
"+  -  /  *  =  -  /  *   Welcome to Calculator   +  -  /  *  +  -  /  *
                      Please select an Operation :

                        1. Simple Calulations
                        2. Temperature Converter
                        3. Area Calculation
                        4. To Quit'
                        

        USER INPUT selection PRINT "Enter Choice (1 - 4) : "
        WHEN choice is 1 :
            CALL FUNCTION simple_calc
        WHEN choice is 2 :
            CALL FUNCTION temp_conv
        WHEN choice is 3 :
            CALL FUNCTION area_calc
        WHEN choice is 4 :
            PRINT "GoodBye!"
            EXIT PROGRAM
        ELSE :
            PRINT "Invalid Choice."
            CALL FUNCTION main_calc

####################################


DEFINE simple_calc
    PRINT '''
                            Simple Calculator
                ---------------------------------        
            Which simple calculation do you want to use?
                        1 for Addition
                        2 for Subtraction
                        3 for Multiplication
                        4 for Division
                        5 to return to Main Menu'''
                        
                        
                        

    USER INPUT choice PRINT "Enter Choice (1 - 5) :"
    
    WHEN choice 1 is selected :
        TRY FOR ERROR :
            USER INPUT number_1 PRINT "Please enter the first number: "
            USER INPUT number_2 PRINT "Please enter the second number: "
        EXCEPT IF NO ERROR :
            PRINT 'Invalid input detected, Please Try Again.'
            CALL FUNCTION simple_calc() 
        PRINT number_1 + number_2 = TOTAL
        CALL FUNCTION simple_calc
        
    WHEN choice 2 is selected :
        TRY FOR ERROR :
            USER INPUT number_1 PRINT "Please enter the first number: "
            USER INPUT number_2 PRINT "Please enter the second number: "
        EXCEPT IF NO ERROR :
            PRINT 'Invalid input detected, Please Try Again.'
            CALL FUNCTION simple_calc() 
        PRINT number_1 - number_2 = TOTAL
        CALL FUNCTION simple_calc
        
    WHEN choice 3 is selected :
        TRY FOR ERROR :
            USER INPUT number_1 PRINT "Please enter the first number: "
            USER INPUT number_2 PRINT "Please enter the second number: "
        EXCEPT IF NO ERROR :
            PRINT 'Invalid input detected, Please Try Again.'
            CALL FUNCTION simple_calc() 
        PRINT number_1 * number_2 = TOTAL
        CALL FUNCTION simple_calc
    
    WHEN choice 4 is selected :
        TRY FOR ERROR:
            USER INPUT number_1 PRINT "Please enter the first number: "
            USER INPUT number_2 PRINT "Please enter the second number: "
            IF USER INPUT is 0 :
                PRINT "Cannot divide by 0."
                CALL FUNCTION simple_calc
            ELSE : 
                PRINT number_1 / number_2 = TOTAL
                CALL FUNCTION simple_calc
        EXCEPT IF NO ERROR :
            PRINT 'Invalid input detected, Please Try Again.'
            CALL FUNCTION simple_calc() 
    WHEN choice 5 is selected :
        CALL FUNCTION main_calc
    
    ELSE :
        PRINT "Invalid Choice"
        CALL FUNCTION simple_calc

####################################

DEFINE temperature converter
    PRINT ('''
                      Tempurature Calculator
                ---------------------------------  
        Which temperature conversion would you like to use?
                    1. Fahrenheit to Celsius
                    2. Celsius to Fahrenheit
                    3. Return to Main Menu 
                    ''')
    USER INPUT choice PRINT 'Enter Choice (1 - 3) : '
    
    WHEN choice 1 is selected
        TRY FOR ERROR:
            fahrenheit = float(input("Enter temperature in fahrenheit: "))
            celsius = (fahrenheit - 32) * 5 / 9
            PRINT ('%.2f°F is %0.2f°C' %(fahrenheit, celsius))
        EXCEPT IF NO ERROR :
            PRINT 'Invalid input detected, Please Try Again.'
            CALL FUNCTION temp_conv 
            
    WHEN choice 2 is selected
        TRY FOR ERROR:
            celsius = float(input("Enter temperature in celsius: "))
            fahrenheit = (celsius * 9 / 5) + 32
            PRINT('%.2f°C is %0.2f°F' %(celsius, fahrenheit))
        EXCEPT IF NO ERROR :
            PRINT 'Invalid input detected, Please Try Again.'
            CALL FUNCTION temp_conv        
    WHEN choice 3 is selected
        CALL FUNCTION main_calc
    
    ELSE
        PRINT 'Invalid input, Please Try Again.'
        CALL FUNCTION temp_conv
    
    USER INPUT choice = PRINT('Would you like to convert another temperature? Y for Yes/ N for No ')
    
    WHEN choice.UPPERCASE == 'y':
        CALL FUNCTION temp_conv
    
    WHEN choice.UPPERCASE == 'n':
        CALL FUNCTION main_calc
    
    ELSE
        PRINT 'Invalid Choice, Please Try Again.'
        CALL FUNCTION temp_conv

####################################
IMPORT sys
IMPORT os
IMPORT time

    call function menu arez_calc()

    # Function Menu (area_calc)
      clear screen
      print title "Area Calculator"
      print Menu with options:
              1.Square
              2.Circle
              3.Rectangle
              4.Triangle
              5.Return to Main Menu
    # Options
      When option selected is 1:
           call function f_square
      When option selected is 2:
           call function f_circle
      When option selected is 3:
           call function f_rectangle
      When option selected is 4:
           call function f_triangle
      When option selected is 5:
           call function f_quit
      When any other option is selected:
           display message "Invalid Option"
           loop menu area_calc()
 
    # Function Square (f_square)
      clear screen
      show title " 1. Square Area Calculator"
      input side =  "Enter a Number Greater than Zero for the Square side: " as float 
      validate side for a valid value greater than 0
         if error:
            send exception message "That is not a Valid Number!, Please try again."
         else
            calculate area as (side ** 2)
            print area calculated formatted 99.99
        
      input to wait for the enter
      show the menu area_calc()
 
    # Function Circle (f_circle)
      clear screen
      show title " 2. Circle Area Calculator"
      pie = 3.14
      input radius =  "Enter a Number Greater than Zero for the Circle Radius: " as float 
      validate radius for a valid value greater than 0
        if error:
           send exception message "That is not a Valid Number!, Please try again."
        else
           calculate area as (2 * pie * radius)
           print area calculated formatted 99.99

      input to wait for the enter
      show the menu area_calc()

    # Function Rectangle (f_rectangle)
      clear screen
      show title " 3. Rectangle Area Calculator"
      input length ="Enter a Number Greater than Zero for the Rectangle Length: " as float Value
      validate length for a valid value greater than 0
         if error:
            send exception message "That is not a Valid Number!, Please try again."
         else
            input width =  "Enter a Number Greater than Zero for the Rectangle Width: " as float Value
            if error:
               send exception message "That is not a Valid Number!, Please try again."
            else:
                calculate area as (length * width)
                print area calculated formatted 99.99
      input value to continue
      show the menu area_calc()

    # Function Triangle (f_triangle)
      clear screen
      show title " 4. Triangle Area Calculator"
      input base ="Enter a Number Greater than Zero for the Triangle Base: " as float Value
      validate base for a valid value greater than 0
         if error:
            send exception message "That is not a Valid Number!, Please try again."
         else
            input height =  "Enter a Number Greater than Zero for the Triangle Height: " as float Value
            if error:
               send exception message "That is not a Valid Number!, Please try again."
            else:
                calculate area as  (0.5 * base * height)
                print area calculated formatted 99.99
      input value to continue
      show the menu area_calc()
      
 
    # Function Quit
      Return to Main Menu