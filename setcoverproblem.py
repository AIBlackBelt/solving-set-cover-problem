
from math import *
def IdifferentfromU(U,I):

      for i in range(0,len(U)):
          if U[i] not in I:
             return True
      return False
   

def min(T):

    n = len(T)
    min = T[0]

    a = 0
    for i in range(0,n):

        if T[i] < min:


            min = T[i]
            a = i


    return a


def search(T,x):

    n = len(T)

    for u in range(0,n):

        if T[u] == x:

           return u


def solver(U,cost,S):

   I = []
   m = len(S)
   x = [None]*m
   T = []
   while IdifferentfromU(U,I) == True:

       T = []
       for i in range(0,m):
           set_difference = set(S[i]) - set(I)

           list_difference = len(list(set_difference))



           if  list_difference != 0 :



              a = cost[i]/list_difference
              T = T + [a]

           else:

              T = T + [1000]



       z = min(T)
       I = I + S[z]
       x[z] = 1

   for y in range(0,m):

       if x[i] == None:

           x[i] = 0

   return x

an = input("do you want to enter the input data manually by adding them in the code press yes (see in the readme file, the correct format to enter),or no you can be assisted by the script while entering them\n")
if an == "no"
 print("how many zone you want to cover ? (zones will be encoded using integers from 1 to the number of zones) \n")
 n = int(input("\n")) 
 U = [i for i in range(1,n+1)]
 m = int(input("enter the universe of possiblities (number of possiblities)\n"))
 S = []
 cost = []
 for i in range(1,m+1):
    print("the possiblity number",i,"\n")
    print("enter the list of zones (encoded from 1 to number of zones) that this possibility will cover\n")
    print("enter the zones codes that this possibilty covers\n")
    stop = False
    while stop == False :
      T = []
      n = int(input("enter the zone code :\n"))
      T = T + [n]
      print("good, now if this possiblity still covers other zones, press next, otherwise press stop and move on to another possibility")
      t = input("")
      if t == "stop":
         break
         
    S = S + [T]     
    cos = float(input("Enter the cost of the said possiblity\n"))
    cost = cost + [cos] 
 print(solver(U,cost,S))
 


   
























































