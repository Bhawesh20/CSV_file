import csv
inp = input()
list1 = inp.split(" ")   # split input to get diferent values
f = open(list1[1])
csv_f = csv.reader(f)
length_list1 = len(list1)
no_prod = {}  # dict for number of products to purchase
temp_amt = {}  # dict for bill at each shop 
row_count = sum(1 for row in csv_f)
f.seek(0)
for row in csv_f:
    row_length = len(row)
    mFlag = -1
    for j in range(2, row_length):
        for i in range(2, length_list1):
            if(row[j] == list1[i]):
                if no_prod.get(row[0]) is None:
                    no_prod[row[0]] = 0
                no_prod[row[0]] = no_prod[row[0]] + 1
                if(mFlag == -1):
                    if temp_amt.get(row[0]) is None:
                        temp_amt[row[0]] = 0
                    temp_amt[row[0]] = temp_amt[row[0]] + float(row[1])
                    mFlag = 0

flag = 0
max_amt=0
for i in temp_amt:
    if(max_amt <= temp_amt[i]):
        max_amt = temp_amt[i]
min_amt = max_amt
for i in temp_amt:
    if((no_prod[i] == length_list1-2) and (min_amt >= temp_amt[i])):
        min_amt = temp_amt[i]
        flag = i
if (flag):
    print(flag, ",", min_amt)
else:
    print('none')
f.close()
