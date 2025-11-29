from pandas.core.computation.expr import intersection

my_set = {1,2,3}
print(my_set)

set_ =set([4,5,6,6])
print(set_)

set1= {1,2,3}
set2= {3,4,5}

union_result_method =set1.union(set2)
union_result_operator = set1 | set2

print('union of set1 and set2 using method:',union_result_method) #12345
print('union of set1 and set2 using operator:',union_result_operator) #12345

#intersecion

intersection_method = set1.intersection(set2)
intersection_operator = set1 & set2
print('intersecion of set1 and set2 using intersecion method:',intersection_method) #3
print('intersecion of set1 and set2 using intersecion operator:',intersection_operator) #3

#difference
difference_method = set1.difference(set2) #1,2
difference_operator = set1 - set2
print('difference of set1 and set2 using difference method:',difference_method)
print('difference of set1 and set2 using difference operator:',difference_operator)

#symetric_diffrence
symetric_method = set1.symmetric_difference(set2)
symmetric_operator = set1 ^ set2
print('symmetric diffrence of set1 and set2 using diffrence method:' ,symetric_method) #1,2,3,4,5
print('symmetric diffrence of set1 and set2 using diffrence operator:' ,symmetric_operator) #1,2,3,4,5

my_set= {1,2,3}
my_set.remove(3)
print(my_set)

my_set.add(5)
print(my_set)

my_set.discard(7)
print(my_set)

