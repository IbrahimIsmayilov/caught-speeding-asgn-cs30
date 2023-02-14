# Caught Speeding Assignment

print("WELCOME TO THE CAUGHT SPEEDING PROGRAM \nEnter the speeds and speed limits for 3 drviers to determine the type of ticket they will receive")

# Asking the user to enter the speed and speed limit for three drivers
print("DRIVER 1")
driver1_speed = int(input("Enter speed for driver 1:"))
driver1_speed_limit = int(input("Enter speed limit for driver 1:"))

print("DRIVER 2")
driver2_speed = int(input("Enter speed for driver 2:"))
driver2_speed_limit = int(input("Enter speed limit for driver 2:"))

print("DRIVER 3")
driver3_speed = int(input("Enter speed for driver 3:"))
driver3_speed_limit = int(input("Enter speed limit for driver 3:"))

# Function to Determine Ticket Type
def determineTicket(speed, limit):
    if speed - 40 > limit:
        return "Really Big Ticket"
    elif speed - 20 > limit and speed - 40 <= limit:
        return "Big Ticket"
    elif speed > limit and speed - 20 <= limit:
        return "Small Ticket"
    elif speed <= limit:
        return "No Ticket"

# Determining the type of ticket based on user input
driver1_ticket = determineTicket(driver1_speed, driver1_speed_limit)    
driver2_ticket = determineTicket(driver1_speed, driver1_speed_limit)    
driver3_ticket = determineTicket(driver1_speed, driver1_speed_limit)    

print(f"\nDriver 1 Ticket Type: {driver1_ticket}")
print(f"\nDriver 2 Ticket Type: {driver2_ticket}")
print(f"\nDriver 3 Ticket Type: {driver3_ticket}")