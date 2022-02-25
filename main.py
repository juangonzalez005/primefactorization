import math
#function primecheck checks if a number is prime or not
def primecheck(number):
  for possiblefactors in range(2,math.isqrt(number)+1): 
    #loop through numbers from 2 to the sqrt of number
    if number%possiblefactors==0: 
      #if at any point number is divisible by something other than itself, number is not prime
      return False 
  #assuming the number is only divisible by one and itself, it's prime
  return True

'''
def printfactors(factorlist):
  noDuplicatesList = []
  for factor in factorlist:
      if factor not in noDuplicatesList:
          noDuplicatesList.append(factor)
  factorsstring=""
  if len(factorlist)==1:
    print(str(factorlist[0])+" * 1")
  else:
    for factor in range(len(noDuplicatesList)):
      factorsstring+=str(noDuplicatesList[factor])+"^"+str(factorlist.count(noDuplicatesList[factor]))
      #i concatenate the factor and how many of that factor was in the original list
      if factor != len(noDuplicatesList)-1:
        factorsstring+=" * "
    print(factorsstring)
'''
########MAIN############
inputNumber=int(input("Enter a positive integer: "))
#print(primecheck(2))
primefactors=[]
factor=2
initialNumber=inputNumber
if initialNumber ==0:
  print("Zero does not have a prime factorization")
elif initialNumber==1:
  print("The only factor of 1 is 1")
elif initialNumber<0:
  print("This is not a positive number")
else:
  #this code runs if a positive, non-zero integer is entered

  #this gathers every prime factor
  while math.prod(primefactors) != initialNumber:
    if primecheck(factor)==True:
      while inputNumber%factor==0:
        if inputNumber%factor==0:
          primefactors.append(factor)
          inputNumber/=factor
    factor+=1
  

  print("The factors are:")
  #this section prints the prime factors
  noDuplicatesList = []
  for factor in primefactors:
      if factor not in noDuplicatesList:
          noDuplicatesList.append(factor)
  factorsstring=""
  if len(primefactors)==1:
    print(str(primefactors[0])+" * 1")
  else:
    for factor in range(len(noDuplicatesList)):
      factorsstring+=str(noDuplicatesList[factor])+"^"+str(primefactors.count(noDuplicatesList[factor]))
      #i concatenate the factor and how many of that factor was in the original list
      if factor != len(noDuplicatesList)-1:
        factorsstring+=" * "
    print(factorsstring)