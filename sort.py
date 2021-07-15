
#comparison-based algorithm in which each pair of adjacent elements is 
# compared and the elements are swapped if they are not in order.
def bubblesort(my_list):
    # Swap the elements to arrange in order
    for i in range (len(my_list)-1,0,-1):
        for j in range(i):
            if my_list[j]> my_list[j+1]:
                my_list[j],my_list[j+1] = my_list[j+1],my_list[j]

'''
Insertion sort involves finding the right place for a given element in a sorted list. So in beginning we 
compare the first two elements and sort them by comparing them. Then we pick the third element and find 
its proper position among the previous two sorted elements. This way we gradually go on adding more elements 
to the already sorted list by putting them in their proper position.
'''
#Insertion sort
def insertion(L):
    for i in range(1,len(L)):
        j = i-1
        while L[j]>L[j+1] and j>=0:
            L[j],L[j+1] = L[j+1],L[j]
            j = j-1
    return L

        
#Selection sort:  
# In selection sort we start by finding the minimum value in a given list and move it to a sorted list. 
# Then we repeat the process for each of the remaining elements in the unsorted list. 

#Merge Sort
def merge_sort(unsorted_list):
    n = len(unsorted_list)
    if n == 1:
        return unsorted_list
# Find the middle point and devide it
    middle = n // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return merge(left_list, right_list)

# Merge the sorted halves

def merge(left_half,right_half):
    res = []
    i1,i2 = 0,0
    while i1 < len(left_half) and i2 < len(right_half):
        if left_half[i1] < right_half[i2]:
            res.append(left_half[i1])
            i1 += 1
        else:
            res.append(right_half[i2])
            i2 += 1
    if i1 == len(left_half):
        res = res + right_half[i2:]
    else:
        res = res + left_half[i1:]
    return res

#Quick sort
def quick_sort(L,p,r):
    if p < r:
        q = partition(L,p,r) #pivot
        quick_sort(L,p,q)
        quick_sort(L,q+1,r)

def partition(L,p,r):
    '''Met tous les éléments inf à L[r] ) gauche et les autres à droite et renvoie l indicde du pivot à la fin'''

    x = L[r]
    i = p-1
    for j in range(p,r):
        if L[j] <= x:
            i += 1
            L[i],L[j] = L[j],L[i]
    L[i+1],L[r] = L[r],L[i+1]
    return i

my_list = [19,2,31,45,6,11,121,27]
quick_sort(my_list,0,len(my_list)-1)
print(my_list)