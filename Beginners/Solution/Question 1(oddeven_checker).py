def oddeven_checker(number):                   #create a function
    if number%2 ==0:                           #use modulo operator to check odd or even number
        return "This number is even number."
    else:
        return "This number is odd number."    #return value 


if __name__=='__main__':
    input_number=int(input("Enter the number:"))
    print(oddeven_checker(input_number))       #function call and print
