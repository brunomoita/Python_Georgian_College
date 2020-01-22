try:
    hours = float(input("Enter hours: "))
except:
    print("Please enter a numeric value")

try:
    rate = float(input("Enter rate: "))
except:
    print("Please enter a numeric value")

if hours<=40:
    print("Pay", hours*rate)
else:
    overtime=hours-40
    normal_hours=40
    print("Pay", (normal_hours*rate)+(overtime*(rate*1.5)))