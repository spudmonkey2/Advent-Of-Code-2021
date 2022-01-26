input = open("input.txt","r")
scans = input.readlines()
sliding = []
increases = 0
increaseslide = 0
for x in range(len(scans)):
    if x+2 <= len(scans)-1:
        math = int(scans[x])+int(scans[x+1])+int(scans[x+2])
        sliding.append(int(math))
    if x == 1:
        print(int(scans[x])+int(scans[x+1])+int(scans[x+2]))
#    if x != 0:
#        if int(scans[x]) > int(scans[x-1]):
#            increases += 1
for x in range (len(sliding)):
    if x != 0:
        if int(sliding[x]) > int(sliding[x-1]):
            increaseslide += 1
print(sliding[0], sliding[1], sliding[2])
#print(increases)
print(increaseslide)