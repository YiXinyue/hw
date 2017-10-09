def bsearch(data,target):
    low=0
    high=len(data)-1
    while low<=high:
        mid=(low+high)//2
        if target>data[mid]:
            low=mid+1
        elif target<data[mid]:
            high=mid-1
        else:
            return mid
            break
lst=[1,2,3,4,5]
pt= bsearch(lst,4)
print(pt)
