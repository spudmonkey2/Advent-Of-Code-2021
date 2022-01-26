swag = open("radar.txt","r")
nums = swag.readlines()
listlength = len(nums)
increases = 0
print(int(nums[0]) + int(nums[1]))
print(listlength)
for x in range(listlength):
    if x > 0:
        if int(nums[x]) > int(nums[x-1]):
            increases += 1
            continue
        else:
            continue
    else:
        continue
print(increases)
