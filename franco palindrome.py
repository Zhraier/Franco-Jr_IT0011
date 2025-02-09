try:
    file = open("numbers.txt", 'w')
    file.write("""10,20,30,40,50
90,10,1
20,2,80,120
200,171,459,151,20
50,60,33,22,6
101,202,303,404,505
1000,800,200,2
85,56,34,44,23
5,10,20,40,80
305,700,1058,587,12
""")

    file = open("numbers.txt", 'r')
    file = file.readlines()
    
    i = 1
    #this reads and splits each line and in the for loop it will convert it to integer and get the total
    for file in file:
        file = file.strip()
        numbers = file.split(',')
        total = 0
        i += 1
        for num in numbers:
            total += int(num)
        
        #this slices the sum by flipping it in reverse and comparing it to the original to see if its still the same
        if str(total) == str(total)[::-1]:
            pal = "Is a Palindrome"
        else:
            pal = "Is not a palindrome"
            
        print(file," = ", total," - ",pal)
except FileNotFoundError:
    print("Error: The file 'numbers.txt' was not found.")
