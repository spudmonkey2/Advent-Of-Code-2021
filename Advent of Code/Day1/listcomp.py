swag = open("input.txt","r")
nums = swag.readlines()
increases = 0
numsbig = [x for x in range(len(nums)) if x > 0 if int(nums[x]) > int(nums[x-1])]
print(len(numsbig))
