print('HANGMAN')
print('''INSTRUCTIONS-
1)Player 1 gives the word to guess
1)Player 2 has to guess the word within 5 tries
\nPLAY FAIR''')
def cls():
    print('\n'*1000)
    
def enclosure():
    global word1,word,display,n
    word1=input('Enter the word/sentence to be found-')
    word=list(word1)
    cls()
    display=[]
    display.extend(word)
    n=len(word)
    for a in range(n):
        display[a]='_'

def guess():
    global word1,word,display,n
    count=0
    x=5
    blank=' '
    while (count<n):
        if (count==0) and (blank in word1):
            guess=blank
        else:
            print(' '.join(display))
            guess=input('GUESS A LETTER-')
        if guess in word:
            if guess in display:
                print('Word already entered')
            else:
                if len(guess)==1:
                    for i in range(n):
                        if word[i]==guess:
                            display[i]=guess
                            count+=1
                    if display==word:
                        print(' '.join(display))
                        print('WAY TO GO!!!!')
                else:
                    print('Enter single letter')
        else:
            if x<1:
                print('Sorry')
                print('THE WORD IS-',word1)
                break
            print('Letter Not Found. Try Again')
            x=x-1
            print("You have",x+1,"chances left")
        
if __name__=="__main__":
    enclosure()
    guess()
    while True:
        ask = input('Do you want to play again? (y/n) - ')
        if ask=='y':
            enclosure()
            guess()
        else:
            print("Game Over")
            break
    
        
        

    
        
        

    
        
        
