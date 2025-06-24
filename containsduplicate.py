Repeated=True
nums=[1,2,3,1]
for i in range(0,len(nums)):
    for j in range(i,len(nums)):
        if nums[i]==nums[j]:
            Repeated=True
        else:
            Repeated=False

print(Repeated)