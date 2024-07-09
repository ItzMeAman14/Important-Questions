amount = int(input("Enter amount:"))

count100 = 0
count50 = 0
count10 = 0
count1= 0
l = []
# amount = amount%100
if amount//100 != 0:
    l.append(f"100 :{amount//100}")
    amount %= 100
# print(count100)
while amount>0:
    if count100 == 0:
        l.append(f"50 :{amount//50}") 
        amount %= 50
        if count50 == 0:
            l.append(f"10 :{amount//10}")
            amount %= 10
            if count10 == 0:
                l.append(f"1 :{amount//1}")
                count1 += amount//1
                amount = amount%1

print("Amount = ",amount)
print(l)