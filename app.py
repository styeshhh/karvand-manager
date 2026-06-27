import json  # noqa: F401
file_name = "data/karvand.json"
APP_TITLE = "Karvand studen Manager"
try :
    with open(file_name , "r") as file : 
        data = json.load(file)
        print(data)
except FileNotFoundError:
    data = {"Bootcamp" :{
        "title" : "Karavand Python",
        "year" : 2026
    },
    "karvands":[]

    }
    with open (file_name,"w") as file :
        json.dump(data, file, indent=4)

def add_user(id, fullname, city, degree, field):
    with open(file_name, "r") as file:
        data = json.load(file)
    data["karvands"].append({
    "id": id,
    "full_name": fullname,
    "city": city,
    "education": {
        "degree": degree,
        "field": field
    }
})    
    with open(file_name, "w") as file:
        json.dump(data, file ,indent=4)

def show_users():
    with open(file_name, "r") as f:
        data = json.load(f)
    return data
msg = '''
enter your choice :
1)add user 
2)show users
3)exit

'''
while True : 
    choice = input (msg)
    if choice.lower() in ["1","add","add user"]:
        add_user(input("enter your id: "), input("enter your fullname: "), input("enter your city: "),  input("enter your degree: "), input("enter your field: "))
    elif choice.lower() in ["2","show","show user"]:
        print(show_users())
    elif choice.lower() in ["3","exit"]:
        break
    else : 
        print ("invalid input")
        





