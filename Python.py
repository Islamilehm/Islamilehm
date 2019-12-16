punktid = 0
print("Mitu jalga on koeral?")
vastus1 = input()
õige1 = "4"
if vastus1 == õige1:
    punktid += 1
print("Mis värvi on taevas?")
vastus2 = input()
õige2 = "sinine"
if vastus2 == õige2:
    punktid += 1
print("Kes on USA president?")
print("1. Clinton")
print("2. Trump")
print("3. Obama")
vastus3 = input()
õige3 = "2"
if vastus3 == õige3:
    punktid += 1
    
if (punktid == 3):
    print("Tubli, kõik õige")
else:
    print("peaaegu õige")




    