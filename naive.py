import pandas as pd

data = pd.read_csv('Sales.csv') 
a = data["BookingID"].values 
b = data["Quantity"].values
c= data["Discount"].values 
p = data["SaleStatus"].values

count = 0 
for i in a:
    count += 1

inpl =input("Enter Booking id (1/2): ") 
inp2 =input("Enter qty (1/2): ") 
inp3 =input("Enter disc (1/2): ")

proby = 0 
probn=0 
for i in p: 
    if(i== 'Yes'):
        proby += 1
    else:
        probn+= 1

proy = proby/count 
pron = proby/count
phy = 0 
phn = 0 
ploy = 0 
plon = 0 
pshy = 0 
pshn = 0 
ply = 0
pln = 0 
p18y = 0
p18n = 0 
p13y = 0 
p13n = 0

x = 0 
for j in a:
    k=x 
    if(j== "1"):

     if(p[k] == 'Yes'):
        phy += 1 
     else:
        phn += 1 
    elif(j== "2"): 
     if(p[k] == 'Yes'):
        ploy += 1 
    else:
        plon += 1 
    x += 1 
x = 0 
for j in b:
 k=x 
 if(j=="1"):
    if(p[k] == 'Yes'):
     pshy += 1 
    else:
     pshn += 1 
 elif(j == "2"):
     if(p[k] == 'Yes'):
        ply += 1 
     else:
        pln += 1
 x += 1
X=0 
for j in c:
 k= x 
 if(j == "1"): 
    if(p[k] == 'Yes'):
        p18y += 1 
    else:
        p18n += 1 
 elif(j=="2"):
        if(p[k] == 'Yes'):
            p13y += 1 
        else:
            p13n+= 1 
 x += 1 
x = 0
phy = phy/(count*proy) 
phn = phn/(count*pron) 
ploy = ploy/(count*proy) 
plon = plon/(count*pron) 
pshy = pshy/(count*proy) 
pshn = pshn/(count*pron) 
ply = ply/(count*proy) 
pln = pln /(count*pron)
p18y=p18y/(count*proy) 
p18n=p18n/(count*pron)
p13y=p13y/(count*proy) 
p1on = plon/(count*pron)

print("The probability of booking being done ",proy) 
print("The probability of booking not being done ",pron) 
# print("The probability of High rated movie being watched ",phy) 
# print("The probability of High rated movie not being watched ",phn) 
# print("The probability of Low rated movie being watched ",ploy) 
# print("The probability of Low rated movie not being watched ",plon) 
# print("The probability of qty being 1 ",pshy) 
# print("The probability of qty not being 1 ",pshn) 
# print("The probability of qty being 2 ",ply) 
# print("The probability of qty not being 2 ",pln) 
# print("The probability of discount being given ",p18y) 
# #print("The probability of  ",p18n) 
# print("The probability of disocunt not being given ",p13y) 
# #print("The probability of 13+ age group movie not being watched ",p13n)
if(inpl == '1'): 
    if(inp2 == '1'):
         if(inp3 == '2'):
            probY = phy*pshy*p13y*proy
            probN = phn*pshn*p13n*pron 
         elif(inp3 == "2"):
            probY = phy*pshy*p18y*proy
            probN = phn*pshn*p18n*pron 
         elif(inp2 == '2'): 
            if(inp3 == '2'):
                probY = phy*ply*p13y*proy
                probN = phn*pln*p13n*pron 
            elif(inp3 == "1"):
                probY = phy*ply*p18y*proy
                probN = phn*pln*p18n*pron 
            elif(inpl == '2'): 
             if(inp2 == '1'):
                if(inp3 == '2'):
                    probY = ploy*pshy*p13y*proy
                    probN = plon*pshn*p13n*pron 
                elif(inp3 == '1'):
                    probY = ploy*pshy*p18y*proy
                    probN = plon*pshn*p18n*pron 
                elif(inp2 == '2'): 
                 if(inp3 == '2'):
                    probY = ploy*ply*p13y*proy
                    probN = plon*pln*p13n*pron 
                elif(inp3 == "1"):
                    probY = ploy*ply*p18y*proy 
                    probN = plon*pln*p18n*pron
print("The probability of sale status yes: ",proby/17)
print("The probability of sale status:",probn/17)
if(proby> probn):
    print("Will it be bought: Yes")
else:
    print("Will it be bought: No")
