def div(fnum, snum):
    if snum == 0:
        print("Denominator cannot be zero.")
        return None
    return fnum / snum

def expo(fnum, snum):
    return fnum ** snum

def rem(fnum, snum):
    if snum == 0:
        print("Denominator cannot be zero.")
        return None
    return fnum % snum

def summ(fnum, snum):
    if fnum >= snum:
        print("The 2nd number must be greater than the 1st number.")
        return None
    return sum(range(fnum, snum + 1))
    
while True:
    print("\n===== MATH OPERATIONS =====")
    print("[D] - Divide")
    print("[E] - Exponentiation")
    print("[R] - Remainder")
    print("[F] - Summation")
    print("[Q] - Quit")
        
    choice = input("Enter your choice: ").upper()
    
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print()
            
        if choice == 'D':
            result = div(num1, num2)
        elif choice == 'E':
            result = expo(num1, num2)
        elif choice == 'R':
            result = rem(num1, num2)
        elif choice == 'F':
            result = summ(num1, num2)
        elif choice == 'Q':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice.")
                
        if result is not None:
            print("Result:", result)
            
    except ValueError:
        print("Please enter valid integers.")