medical_cause=input("Did you have a medical cause? Say Y or N")
attendance=int(input("Please enter your attendance"))
if medical_cause=="Y":
    print("You are allowed")
else:
    if attendance>=75:
        print("You are allowed")
    else:
        print("You are not allowed")

           