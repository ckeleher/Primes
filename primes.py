def main():
  #reads in all previously calculated primes
  f = open('primes.txt', 'r')
  primeSet = []
  for word in f.read().split():
    primeSet.append(word)
  f.close()
  f = open('primes.txt', 'a')
  
  #establish starting point
  startingPoint = primeSet[len(primeSet)-1]
  curr = int(startingPoint)
  for i in range(0,10000000):
    isPrime = True
    curr = curr + 1
    #print curr
    for j in primeSet:
      #print(j)
      #raw_input('Press Enter to continue...')
      if curr % int(j) == 0:
        isPrime = False
        break
    if isPrime:
      f.write(str(curr) + " ")
      primeSet.append(str(curr))
   
  #print(primeSet)
  #print curr
  f.close()
  raw_input('Press Enter to continue...')
  

if __name__ == '__main__':
  main()