from math import sqrt
#************************ Q1 ***************************
'''def keyword is used to create a functions'''
def odd():
    l=[]
    for i in range(1,26):
        if i%2!=0:
         l.append(i)
    return l
print(odd())
# #*********************** Q2 *****************************
# *args = with the help of *args we can take multiple input as a argument and type of argument is will be tuple
# **kargs = with the help of **kargs we can take multiple input as a argument and type of argument is will be dict and  argument will be in "key":"value " formate
def test1(*args):
      return args
print(test1("jyotish kushwaha","BCA 2ND YEAR",1024,[1,2,3,4,5]))

def test2(**kvargs):
    return kvargs
print(test2(name='jyotish kushwaha',course='data master science',rollno=1024))

# #*********************** Q3 *************************************
'''iterator= it is an object or data by which we can retreive the data from it by using 'next' keyword
iter() and next() fuction to return the next item in the sequences'''
l=[2,4,6,8,10,12,14,16,18,20]
iterator=iter(l)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

    
# ********************** Q4 ***************************************
''' generator function = is an function that return an iterator that produce a sequences of values when iterated over
when we want to run program without storing in memory then we can use the generator function '''
'''yield= the yield keyword similiar to a return statement used for returning values or object ,but there is slight difference 
 the yield statement returns a generator object to the one who calls the function which contains yield instead of simply returning a values'''
def jyotish(n):
    for i in n: 
      yield i
      
jk=jyotish("jyotish kushwaha")
for i in jk:
    print(i)
    
#****************************** Q5 *************************************
    
def isprime(num):
    for i in range(2,num):
        if num % i ==0:
            return False
    return True
    
def prime_generator(n):
    num=2
    while n:
        if isprime(num):
            yield num
            n-=1
        num+=1
    return
it=prime_generator(20)
for i in it:
    print(i)
    
    
# #********************************** Q6 ************************************
def fibo(n):
    a,b=0,1
    count=0
    while count<n:
        print(a) 
        a,b=b,a+b
        count+=1
        
fibo(10)

#******************************** Q7 ****************************************
l="pwskills"
print(list(i for i in l))  #if we type cast the string in list so we get this result

#********************************** Q8 *******************************************
n=int(input("enter the number : "))
a=n
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
if a==rev:
    print("this number is palindrome : " , a)
else:
    print("this is not a palindrome")
    
#********************************** Q9 ******************************************
l=[]
l1=[]
[l.append(i) for i in range(1,101)]
[l1.append(i) for i in l if i%2!=0]
print(l)
print(l1)

    
    

            
                
    
         
       
                   
    
               
               
