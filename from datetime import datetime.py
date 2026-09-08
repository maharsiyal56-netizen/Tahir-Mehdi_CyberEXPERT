from datetime import datetime
Name=input("Enter your Name:")
Dob=input("DD-MM-YY")

birth_date=datetime.strptime(Dob,"%d_%m_%y")
today=datetime.today()
age=today-birth_date

print("Welcome! MR,",Name)
print(f"MashAllah you are in now {age} years old")

