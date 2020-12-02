f = open("inputforadding.txt", "r")
nums = f.readlines()
nums = [int(i) for i in nums]
wantedNumbers = []
wantedNumbers2 = []
for num in nums:
    n = 2020 - num
    if num < n :
        wantedNumbers.append(num)
    for j in range(len(wantedNumbers)):
        if num + wantedNumbers[j]< 2020:
            wantedNumbers2.append(num)
        for k in range(len(wantedNumbers2)):
            if num + wantedNumbers[j] + wantedNumbers2[k] == 2020:
                print(num*wantedNumbers[j]*wantedNumbers2[k])