f = open("inputforadding.txt", "r")
nums = f.readlines()
nums = [int(i) for i in nums]
wantedNumbers = []
for num in nums:
    n = 2020 - num
    wantedNumbers.append(n)
    if num in wantedNumbers:
        print(num*n)
        break
    
    
    