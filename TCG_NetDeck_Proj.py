POKEMON_TCG = 1
MTG_TCG = 2
decklist = list()

#Functions
def input_decklist(flag):
    while True : 
        card_entry = input()
        
        if card_entry == "done" :
            break
        
        if flag == POKEMON_TCG :
            tmp_split = card_entry.split()
            card_entry = ""
            for i in range( len(tmp_split)-2 ) :
                card_entry += tmp_split[i] + " "
            
            card_entry += tmp_split[-1] #last element is index -1
        
        decklist.append(card_entry)
    return



print("Select the TCG: \n 1 for Pokemon\t 2 for MTG")

TCG_type = input()
notInt = False

try:
    TCG_type = int(TCG_type)
    notInt = False
except ValueError:
    notInt = True

# be careful of data types in python. It will shit itself.
while (notInt) or (TCG_type <1 or TCG_type > 2) :
    print("Re-enter the number for the TCG: \n 1 for Pokemon\t 2 for MTG")
    TCG_type = input()
    try:
        TCG_type = int(TCG_type)
        notInt = False
    except ValueError:
        notInt = True

TCG_type = int(TCG_type)
#only gets number of singles for now
if TCG_type == POKEMON_TCG :
    print("\nEnter Pokemon Decklist. (Format: n copies, card name, card set) \nI.e. 1 Ultra Ball PAF 91") 
    #for pokemon, we only want num of cards + name + card number of the set. Cut out 3 letter set name imo. Do a check after
elif TCG_type == MTG_TCG :
    print("\nEnter MTG decklist in MTG Goldfish format (Format: n copies, cardname)\nI.e. 3 Beanstalk Giant")

#get the queue to store strings. Just implment singles
input_decklist(TCG_type)

#debug
for x in decklist:
    print(x)


#know how to parse the strings.




#Search how to make it search stuff on the web.

#1. 1st practice. Make it scrape data for a single card. From Youtube vid.
print("\nTERMINATE")

