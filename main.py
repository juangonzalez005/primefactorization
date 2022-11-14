import math
#function primecheck(number) checks if a number is prime or not, returning true if so
def primecheck(number):
  for possibleFactors in range(2, math.isqrt(number)+1): 
    #loop through numbers from 2 to the sqrt of number
    #sqrt is used because there are two factors before and after the square root, sqrt shortens run time
    if number % possibleFactors==0: 
      #if at any point number is divisible by something other than itself, number is not prime
      return False 
  #assuming the number is only divisible by one and itself, it's prime
  return True

'''#main'''
inputNumber=int(input("Enter a positive integer: "))

factor=2 #factor is started at 2 
initialNumber=inputNumber
if initialNumber ==0: #test if an input has a special factorization
  print("Zero does not have a prime factorization")
elif initialNumber==1:
  print("The only factor of 1 is 1")
elif initialNumber<0:
  print("This is not a positive number")
else:
  #this code runs if a positive, non-zero integer is entered
  primeFactors=[] #primeFactors will hold every prime factor of a number
  
  #this gathers every prime factor
  ''' UNDER CONSTRUCTION FOR A BETTER ALGORITHM
  
  while math.prod(primeFactors) != initialNumber:
  #i will keep dividing the initial numbers if the divisor is prime
  #divide until all factors in primeFactors equal the initialNumber when multiplied
    if primecheck(factor)==True:
      while inputNumber%factor==0:
        if inputNumber%factor==0:
          primeFactors.append(factor)
          # each prime divisor is counted as a prime factor in the list
          inputNumber/=factor
    factor+=1
  '''
  owo = initialNumber
  while math.prod(primeFactors) !=initialNumber:
    for i in range(2, math.isqrt(owo)+1):
      if owo%i ==0 and primecheck(i)==True:
        primeFactors.append(factor)
        owo /=i
        
  
  
  #this section prints the prime factors
  print("The factors are:")
  noDuplicateFactors = list(set(primeFactors))
  noDuplicateFactors.sort()
  #make a list without duplicates from primefactors

  factorsString="" #initialize the organized output of the factors
  if len(primeFactors)==1:
    #just print out "factor * 1" if the number was already prime
    print(str(primeFactors[0])+" * 1")
  else:
    for factor in range(len(noDuplicateFactors)):
      factorsString+=str(noDuplicateFactors[factor])
      factorsString+="^"
      factorsString+=str(primeFactors.count(noDuplicateFactors[factor]))
      #concatenate the factor + how many of that factor was in original primefactors 
      if factor != len(noDuplicateFactors)-1:
        #put an asterick for multiplication if this isnt the last factor
        factorsString+=" * "
    print(factorsString)
