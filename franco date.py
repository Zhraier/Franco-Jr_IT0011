date = input("Enter date (mm/dd/yyyy): ")
sepa = date.split('/')

#assigns the splitted date input to the corresponding format
month = sepa[0]
day = sepa[1]
year = sepa[2]

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

#converts the month number to a date
mname = months[int(month) - 1]

print("Date : ",mname,int(day),",",year)