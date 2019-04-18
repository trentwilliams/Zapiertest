# Bingo
#
# Trent
# 050718

#set the bingo card
card=[7,26,40,58,73,14,22,34,55,68]
card=[1,2,3,4]

#welcome the player
print("\n" *20)
print("Welcome to the Bingo checker\n")
print("please enter random numbers until you get Bingo\n\n")

#While there are numbers left to check, run the process
while len(card)>0:

    #request number
    call=int(input("Please enter a number:"))

    #check number in range
    if call>=1 and call<=80:

        #try to find called number
        try:
            i=card.index(call)  #return postions or error if not found
            card.pop(i) #if value - remove number

            #if number left say so
            if len(card)>0:
                print("\nYAY!! you have a",call,"!! Only",len(card),"to go...")  # advise number found

        #called number not found
        except ValueError:
            print("\nSorry no",call,"found.") #advise not found

    #number outside range
    else:
        print("please enter a number between 1-80 (inclusive)")
            
#BINGO only once the card contains no numbers
print("\n\n","BINGO!!   "*5)



#assertions
#if numbers set to 1,2 enter 1,2 will bingo

#if numbers set to 1,2 enter and number but 1 or 2 will cause to loop,
#until 1 and 2 have each been enter
