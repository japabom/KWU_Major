# Please fill out this stencil and submit using the provided submission script.


## 1: (Task 1) Minutes in a Week
print("#1")
min_in_week=7*24*60
print("a week is",(min_in_week),"minutes")
print("")
## 2: (Task 2) Remainder

print("#2")
remain=2304811%47
print("2304811%47 =",remain)
print("")
## 3: (Task 3) Divisibility

print("#3")

print("673:",673%3==0)
print("909:",909%3==0)
print("")

## 4: (Task 4) Conditional Expression
print("#4")
x=-9
y=1/2
print(2**(y+1/2) if x+10<0 else 2**(y-1/2))
print("")

## 5: (Task 5) Squares Set Comprehension

print("#5")
sqr={x**2 for x in {1,2,3,4,5}}
print(sqr, '\n')

## 6: (Task 6) Powers-of-2 Set Comprehension

print("#6")
val={2**x for x in {0,1,2,3,4}}
print(val)
print("")

## 7: (Task 7) Double comprehension evaluating to nine-element set

print("#7")
val={x*y for x in {4,5,6} for y in {7,8,9}}
print(val)
print("")

## 8: (Task 8) Double comprehension evaluating to five-element set

print("#8")
val={x*y for x in {4,5,6} for y in {7,8,9} if x*y>=40}
print(val)
print("")

## 9: (Task 9) Set intersection as a comprehension
S = {1, 2, 3, 4}
T = {3, 4, 5, 6}
# Replace { ... } with a one-line set comprehension that evaluates to the intersection of S and T
print("#9")
val={x for x in S if x in T} # membership test int a filter at the end of comprehension
print(val)
print("")

## 10: (Task 10) Average
list_of_numbers = [20, 10, 15, 75]
# Replace ... with a one-line expression that evaluates to the average of list_of_numbers.
# Your expression should refer to the variable list_of_numbers, and should work
# for a list of any length greater than zero.

print("#10")
val=(float)(sum(list_of_numbers)/len(list_of_numbers))
print("average = %f" %(val))
print("")

## 11: (Task 11) Cartesian-product comprehension
# Replace ... with a double list comprehension over ['A','B','C'] and [1,2,3]

print("#11")
val=[[x,y] for x in ['A','B','C'] for y in [1,2,3]]
print(val)
print("")

## 12: (Task 12) Sum of numbers in list of list of numbers
LofL = [[.25, .75, .1], [-1, 0], [4, 4, 4, 4]]
# Replace ... with a one-line expression of the form sum([sum(...) ... ]) that
# includes a comprehension and evaluates to the sum of all numbers in all the lists.
print("#12")
val=sum([sum(x) for x in LofL ])
print(val)
print("")


## 13: (Task 13) Three-element tuples summing to zero
S = {-4, -2, 1, 2, 5, 0}
# Replace [ ... ] with a one-line list comprehension in which S appears

print("#13")
val=[(i,j,k) for i in S for j in S for k in S if i+j+k==0]
print(val)
print("")

## 14: (Task 14) Nontrivial three-element tuples summing to zero
S = {-4, -2, 1, 2, 5, 0}
# Replace [ ... ] with a one-line list comprehension in which S appears

print("#14")
val=[(i,j,k) for i in S for j in S for k in S if i+j+k==0 if (i,j,k)!=(0,0,0)]
print(val)
print("")

## 15: (Task 15) One nontrivial three-element tuple summing to zero
S = {-4, -2, 1, 2, 5, 0}
# Replace ... with a one-line expression that uses a list comprehension in which S appears

print("#15")
val=[(i,j,k) for i in S for j in S for k in S if i+j+k==0 if (i,j,k)!=(0,0,0)][0]
print(val)
print("")

## 16: (Task 16) List and set differ
# Assign to example_L a list such that len(example_L) != len(list(set(example_L)))

print("#16")
L=[1,1,2,3,4,5]
len_of_list=len(L)
len_of_set=len(list(set(L)))
print('len(L)= %d len(list(set(L)))= %d'%(len(L),len(list(set(L)))))
print("")

## 17: (Task 17) Odd numbers
# Replace {...} with a one-line set comprehension over a range of the form range(n)

print("#17")
val={x for x in set(range(1,100,2))}
print(val)
print("")

## 18: (Task 18) Using range and zip
# In the line below, replace ... with an expression that does not include a comprehension.
# Instead, it should use zip and range.
# Note: zip() does not return a list. It returns an 'iterator of tuples'
L = ['A','B','C','D','E']
#range_and_zip = [(a, b) for (a, b) in zip(range(5), L) ]

print("#18")
val=list(zip(range(5),L))
print(val)
print("")

## 19: (Task 19) Using zip to find elementwise sums
A = [10, 25, 40]
B = [1, 15, 20]
# Replace [...] with a one-line comprehension that uses zip together with the variables A and B.
# The comprehension should evaluate to a list whose ith element is the ith element of
# A plus the ith element of B.
print("#19")
val=[x+y for (x,y) in zip(A,B)]
print(val)
print("")


## 20: (Task 20) Extracting the value corresponding to key k from each dictionary in a list
dlist = [{'James':'Sean', 'director':'Terence'}, {'James':'Roger', 'director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}]
k = 'James'
# Replace [...] with a one-line comprehension that uses dlist and k
# and that evaluates to ['Sean','Roger','Pierce']

print("#20")
val=[ x[k] for x in dlist]
print(val)
print("")

## 21: (Task 21) Extracting the value corresponding to k when it exists
dlist = [{'Bilbo':'Ian','Frodo':'Elijah'},{'Bilbo':'Martin','Thorin':'Richard'}]

print("#21")



k = 'Bilbo'
#Replace [...] with a one-line comprehension 
# <-- Use conditional expression here
val=[ x[k] if k in x else 'NOT PRESENT' for x in dlist]
print(val)
k = 'Frodo'
# <-- Use .get(key, default) here
val=[x.get(k,'NOT PRESENT') for x in dlist] # dictionary function
print(val)
print("")


## 22: (Task 22) A dictionary mapping integers to their squares
# Replace {...} with a one-line dictionary comprehension
print("#22")
val = { key:key**2 for  key in range(100)}
print(val)
print("")


## 23: (Task 23) Making the identity function
D = {'red','white','blue'}
# Replace {...} with a one-line dictionary comprehension

print("#23")
val={v:v for v in D}
print(val)
print("")

## 24: (Task 24) Mapping integers to their representation over a given base
base = 10
digits = set(range(base))
# Replace { ... } with a one-line dictionary comprehension
# Your comprehension should use the variables 'base' and 'digits' so it will work correctly if these
# are assigned different values (e.g. base = 2 and digits = {0,1})

print("#24")
val={k:(x,y,z) for k in range(base**3) for x in digits for y in digits for z in digits if x*(base**2)+y*(base*1)+z==k }
print(val)
print("")

## 25: (Task 25) A dictionary mapping names to salaries
id2salary = {0:1000.0, 1:1200.50, 2:990}
names = ['Larry', 'Curly', 'Moe']
# Replace { ... } with a one-line dictionary comprehension that uses id2salary and names.

print("#25")
val={names[k]:id2salary[k] for k in id2salary.keys() }
print(val)
print("")

## 26: (Task 26) Procedure nextInts
# Complete the procedure definition by replacing [ ... ] with a one-line list comprehension

print("#26")
def nextInts(L):
    return [x+1 for x in L]

input=[1,5,7]
print(nextInts(input))
print("")

## 27: (Task 27) Procedure cubes
# Complete the procedure definition by replacing [ ... ] with a one-line list comprehension

print("#27")
def cubes(L):
    return [x**3 for x in L]
input=[1,2,3]
print(cubes(input))
print("")

## 28: (Task 28) Procedure dict2list
# Input: a dictionary dct and a list keylist consisting of the keys of dct
# Output: the list L such that L[i] is the value associated in dct with keylist[i]
# Example: dict2list({'a':'A', 'b':'B', 'c':'C'},['b','c','a']) should equal ['B','C','A']
# Complete the procedure definition by replacing [ ... ] with a one-line list comprehension

print("#28")
def dict2list(dct,keylist):
    return [dct[i] for i in keylist]
dct={'a':'A', 'b':'B', 'c':'C'}
keylist=['b','c','a']
print(dict2list(dct,keylist))
print("")

## 29: (Task 29) Procedure list2dict
# Input: a list L and a list keylist of the same length
# Output: the dictionary that maps keylist[i] to L[i] for i=0,1,...len(L)-1
# Example: list2dict(['A','B','C'],['a','b','c']) should equal {'a':'A', 'b':'B', 'c':'C'}
# Complete the procedure definition by replacing { ... } with a one-line dictionary comprehension

print("#29")
def list2dict(L,keylist):
    return {k:l for (k,l) in zip(keylist,L)}
#def list2dict(L, keylist): return { keylist[i]:L[i] for i in range(len(L)) }

L=['A','B','C']
keylist=['a','b','c']
print(list2dict(L,keylist))
print("")