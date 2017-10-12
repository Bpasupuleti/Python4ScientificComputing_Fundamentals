str1="Lucamarcosara"
Firstletter=str1[0]
last_letter=str1[-1]
Justfirstname=str1[0:4]
Newname="ali"
Names=str1+Newname

#Lists
L1=[2,5,"Luca",9]#first list
L2=[3,8,7]#second list
L3=L1+L2 #concatenation

name2=L1[2]
lastone=L1[-1]
twoelements=L1[1:3]

Resistance=["cond",1.5,0.008,0.78]#glass layer

#list assignment
L3[3]=1000#changing the values

#second compound object tuple()
t1=(4,5,6,7)
t2=(8,9,10,999)
t3=t1+t2
t3[0]
t3[1]=2000 #we don't uasually use tuple as it can't change values once asiigned

#list assignment
L3[3]=1000
#L3[7]=3000# you cant do this because only 6places are there and here it's asking 7

L3.append(3000)#used for adding new element in and between

names=['luca','matteo','manoj','tarun','ali']

#for loop

for thisisnotimportant in names:
    print'hi'+thisisnotimportant
    print'i am still inside the loop'#remove it while performing the lower step
print'i am not inside the loop'

resistance_values=[0.003,0.03,0.5,0.1]
total_resistance=0
for resistancevalue in resistance_values:
    total_res=total_resistance+resistancevalue
    print'resistance value is'+str(resistancevalue)
print'total resistance is'+str(total_res)

R1=[1.5,0.008,0.78] #area:0,length:1,conductivity:3
R2=[1.5,0.01,0.08]
R3=[1.5,0.04,0.78]

L_R1=R1[1]
A_R1=R1[0]
k_R1=R1[2]
Rvalue_R1=L_R1/(A_R1*k_R1)

Listofresistances =[R1,R2,R3]
TotalResvalue=0

for anyResistance in Listofresistances:
    L_anyResistance= anyResistance[1]
    A_anyResistance = anyResistance[0]
    k_anyResistance=anyResistance[2]
    RValue_anyResistance = L_anyResistance/(A_anyResistance*k_anyResistance)
    TotalResValue = TotalResValue+RValue_anyResistance
    print "so the calculated resistance is: "+str(RValue_anyResistance)
    print "***********"
print "so the total Resistance is: "+str(TotalResValue)

    
    
