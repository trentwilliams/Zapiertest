more test here
# Boc Calulator
#
# Trent
# 050718
 
# get and set vars
items = int(input("Please enter the number of items to pack: \n"))

rptitems=items
big=0
med=0
sml=0

# check how many big boxes needed
if items >= 5:
    big = items // 5
    items = items % 5

# check how many medium boxes needed
if items >= 3:
    med = items // 3
    items = items % 3

# check how many small boxes needed
if items >= 1:
    sml = items // 1
    items = items % 1

# calculate total boxes
total=big + med + sml

# report to user
print ("your ", rptitems , "items are packed in a total of", total ,"boxes")

print (big , "x Big boxes")
print (med , "x Medium boxes")
print (sml , "x Small boxes")


# 9 will return, 1, 1, 1
# 10 will return, 2 , 0 ,0
# 4 will return , 0, 1, 1

 
