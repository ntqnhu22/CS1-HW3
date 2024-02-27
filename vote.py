import sys


def main():
    print('Vote for animals you like by entering 0,1,2\nWhale:0\nTurtle:1\nPanda:2')
    #set every vote=0
    whale_votes=0
    turtle_votes=0
    panda_votes=0
    votes=int(sys.argv[1])
    for _ in range (votes):
        a=int(input("Type the number for your animal:"))
        if a==0:
            whale_votes = whale_votes+1
        elif a==1:
            turtle_votes=turtle_votes+1
        elif a==2:
            panda_votes= panda_votes+1
        else:
            print('Invalid')
    # print the winner
    if whale_votes > turtle_votes and whale_votes > panda_votes:
        print ('The winner is whale with',whale_votes ,'votes')
    elif turtle_votes >whale_votes and turtle_votes > panda_votes:
        print ('The winner is turtle with', turtle_votes ,'votes')
    elif panda_votes > whale_votes and panda_votes > turtle_votes:
        print('The winner is panda with', panda_votes , 'votes')
    else: 
        print("It's a tie!")

    if whale_votes==turtle_votes==panda_votes:
        print('All three animals get the same votes with', whale_votes, 'votes')
    elif whale_votes==turtle_votes and whale_votes > panda_votes:
        print('It is a tie between whale and turtle with', whale_votes , 'votes' )
    elif whale_votes==panda_votes and whale_votes > turtle_votes:
        print('It is a tie between whale and panda with', whale_votes , 'votes' )
    elif turtle_votes == panda_votes and turtle_votes > whale_votes:
        print('It is a tie between turtle and panda with', turtle_votes , 'votes' )
   
if __name__ == "__main__":
    main()