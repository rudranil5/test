''' A program to take vote from user on a particular topic, and return the
highest voted item and no. of votes for all candidates.
Identifies duplicate candidates or invalid candidates '''

from TheRandomGenerator import randomElement
accept=["YES","YA","YEAH","HM",'HMMM']
deny=["NO",'END','FINISH','NA','.']

def initialize():
    global Candidates,num_candidates,Purpose
    print(" Initialisation  Of Voting \n ")
    votes=[]
    poll={}
    while True:
        try:
            Purpose=input("Enter the purpose of voting \n●◡● ")
            Candidates=[]
            num_candidates=int(input("How many candidates/Choices ?  "))
            i=0
            while i<num_candidates:
                candidate_name=input("Enter the candidate  {} name : ".format(i+1) )
                if candidate_name.upper() not in Candidates:
                    Candidates.append(candidate_name.upper())
                else:
                    print("Candidate Already in list !!!")
                    continue
                   # poll[candidate_name]=0   #adds candidates as key one by one, it is implemented as whole
                i+=1
            break
        except:
            print("""Theres an error in input !!!\t
            perhaps 'number of candidates'  is not an integer
            \tpls try again\n""")
    poll=dict.fromkeys(Candidates,0)    #creates a dictionary from the list , with default values as second argument 
    print(poll )
    voteTaking_singlechoice(poll)

def calculate(poll,num_votes):
    print(f"For The Vote on {Purpose}\n\n")
    temp_poll=poll.copy()
    print(f"\nRESULT\n\nNumber of voters : {num_votes}") #string formatting
    #for i in poll.items():
    print(*poll.items(),sep="\n",end="\n\n")
    winner=[]   #the list of winner
    winning_vote=max(poll.values()) #The max vote
    count=0
    for i,j in poll.items():
        if j==winning_vote:
            count+=1
            print(f"'{i}' got ~ {j} votes")
            winner.append(i)
    if count==1:      
        print("This is the winner ...\^o^/")
    else:
        choice=input(f"""Above is the list of winners ...
\n\nThere's a tie between candidates {winner}  
want to choose a random winner among them?\n""")
        if choice.upper()in accept:
            print("The Lucky Winner is : ",randomElement(winner))
            #call other module from another file
    
        
    

def voteTaking_singlechoice(poll):
    Voters=int(input("ENTER THE NUMBER OF VOTERS : ")) #No more needed
    formatted_cList=""
    for i in range (num_candidates):
        formatted_cList+=(f"{i+1}. {Candidates[i]}\n")  
                  
    i=0
    while i<Voters:
        print("\nChoose From The Options Below : \n")
        #print(*Candidates,sep = "\n{}".format(i),end='\n___\n\n')    # * operator unpacks a list
        print(formatted_cList,"___\n")
        userChoice=(input(" VOTER {} Enter your choice : ".format(i+1)).upper())
        
        if userChoice in poll.keys() :
            poll[userChoice]+=1
            i+=1
        elif userChoice.isnumeric() and int(userChoice) <= num_candidates and int(userChoice)>0 :
            poll[Candidates[int(userChoice)-1]]+=1  #finds the Candidates list for the index and Then finds the candidates associated in the dict
            i+=1
        elif userChoice in deny:
            break
        else:
            print("\n\nPerhaps There's a typo in your input \n\t◑﹏◐\ntry again !\n")
            continue
    print("\nDONE\n")
    calculate(poll,i)
    #print(poll )
'''
 def voteTaking_bestNworst(poll):
    Voters=int(input("ENTER THE NUMBER OF VOTERS : ")) #No more needed
    formatted_cList=""
    for i in range (num_candidates):
        formatted_cList+=(f"{i+1}. {Candidates[i]}\n")  
                  
    i=0
    while i<Voters:
        print("\nChoose From The Options Below : \n")
        #print(*Candidates,sep = "\n{}".format(i),end='\n___\n\n')    # * operator unpacks a list
        print(formatted_cList,"___\n")
        userChoice_best=(input(" VOTER {} Enter the best as per your choice : ".format(i+1)).upper())
        userChoice_worst=(input(" VOTER {} Enter the worst as per your choice : ".format(i+1)).upper())
        if userChoice_best in poll.keys() and userChoice_worst in poll.keys() :
            poll[userChoice_best]+=1
            poll[userchoice_worst]-=2
            i+=1
        elif userChoice.isnumeric() and int(userChoice) <= num_candidates and int(userChoice)>0 :
            poll[Candidates[int(userChoice)-1]]+=1  #finds the Candidates list for the index and Then finds the candidates associated in the dict
            i+=1
        elif userChoice in deny:
            break
        else:
            print("\n\nPerhaps There's a typo in your input \n\t◑﹏◐\ntry again !\n")
            continue
    print("\nDONE\n")
    calculate(poll,i)           
'''#This Part will be updated after impplementing tkinter
 #update required , a choice to detect duplicate voter 
if __name__=="__main__":
    initialize()

    
