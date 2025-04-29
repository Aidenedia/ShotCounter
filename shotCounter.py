import os

names = {}
while True:
    name = input("enter the names, when done type done ").strip().lower()
    os.system("cls")
    if name == "done":
        break
    elif name in names:
        print(f"{name} is already in ")
    else: 
        names[name] = 0
        print(name, "added")

print("Game started, type a players name to add a shot to the counter. ")


while True:
    os.system("cls")
    for name, shots in names.items():
        print(f"{name}: {shots} shot(s)")
    nameadd = input("type a name to add a shot to the person ")
    if nameadd.startswith("-"):
        if nameadd[1:] in names:
            names[nameadd[1:]] -=1
    elif nameadd in names:
        names[nameadd] +=1