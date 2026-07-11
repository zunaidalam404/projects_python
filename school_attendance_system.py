def login():
    pasword="1234"
    print("============================================")
    print("-------Teerthanker Mahaveer University-------")
    print("============================================")
    print("----Welcome to ERP portal---")
    print("\nPlease Login Your Portal")

    user_password=input("Enter a password: ")
    
    if user_password != pasword:
        print("\nInvalid Password")
        return False
    
    print("\nWelcome To portal\n")
    return True
       
students=[
    ("zunaid",91223),
    ("khan",22114),
    ("ali",44213),
    ("chaudhary",23454),
    ("ruhil",25467),
    ("asjad",63428),
    ("faiz",97063)
]
def Student_attendance():
    attendance=[]
    
    print('=====Attendance=====')
    
    for name, roll in students:
        
        while True:
            status=input(f"{name} ({roll}) [A/P]: ").upper()
            
            if status in ["A","P"]:
               attendance.append((name, roll, status))
               break
            else:
                print("Invalid Input! Please enter only P or A.")
    return attendance

def show_report(attendance):
    present=0
    absent=0
    print("\n")
    print("="*45)
    print("{:<15}{:<10}{:<10}".format("Name","Roll","Status"))
    print("="*45)

    for name,roll,status in attendance:
        print("{:<15}{:<10}{:<10}".format(name,roll,status))
        
        if status=="P":
            present+=1
        if status=="A":
            absent+=1
    total=len(attendance)
    percentage=(present/total)*100
    
    print("=" * 45)
    print(f"Total Students : {total}")
    print(f"Present        : {present}")
    print(f"Absent         : {absent}")
    print(f"Attendance %   : {percentage:.2f}%")
    print("=" * 45)

        
if login():        
    record=Student_attendance()
    show_report(record)