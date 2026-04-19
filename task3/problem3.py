def sets(set1 , set2):
    set3= set ()
    for i in set1 :
        for j in set2: 
            if i == j:
                set3.add(i)
    return set3

set1 = set(input("Enter set-1 elements : ").split())
set2 = set(input("Enter set-2 elements : ").split())
result = sets(set1, set2)
if not result :
    print ("ther is no common")
else :
    print("the common elements are:", result)