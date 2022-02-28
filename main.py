import math
#function primecheck(number) checks if a number is prime or not
def primecheck(number):
  for possiblefactors in range(2,math.isqrt(number)+1): 
    #loop through numbers from 2 to the sqrt of number
    if number%possiblefactors==0: 
      #if at any point number is divisible by something other than itself, number is not prime
      return False 
  #assuming the number is only divisible by one and itself, it's prime
  return True

'''#main'''
inputNumber=int(input("Enter a positive integer: "))
primeFactors=[] 
#primeFactors will hold every prime factor of a number
factor=2 #factor is tarted at 2 
initialNumber=inputNumber
if initialNumber ==0: #test if an input has a special factorization
  print("Zero does not have a prime factorization")
elif initialNumber==1:
  print("The only factor of 1 is 1")
elif initialNumber<0:
  print("This is not a positive number")
else:
  #this code runs if a positive, non-zero integer is entered

  #this gathers every prime factor
  while math.prod(primeFactors) != initialNumber:
  #i will keep dividing the initial numbers assuming the divisor is prime
  # each prime divisor is counted as a prime factor in the list
    if primecheck(factor)==True:
      while inputNumber%factor==0:
        if inputNumber%factor==0:
          primeFactors.append(factor)
          inputNumber/=factor
    factor+=1
  
  #this section prints the prime factors
  print("The factors are:")
  noDuplicateFactors = [] 
  #make a list without duplicates from primeFactors
  for factor in primeFactors:
      if factor not in noDuplicateFactors:
          noDuplicateFactors.append(factor)
  factorsString="" #initialize the organized output of the factors
  if len(primeFactors)==1:
    #just print out the factor * 1 if the number was already prime
    print(str(primeFactors[0])+" * 1")
  else:
    for factor in range(len(noDuplicateFactors)):
      factorsString+=str(noDuplicateFactors[factor])+"^"+str(primeFactors.count(noDuplicateFactors[factor]))
      #i concatenate the factor and how many of that factor was in the original primeFactors list
      if factor != len(noDuplicateFactors)-1:
        #put an asterick for multiplication if this isnt the last factor
        factorsString+=" * "
    print(factorsString)