print('HANGMAN')
print('''INSTRUCTIONS-
YOU HAVE TO GUESS THE WORD WITHIN 5 TRIES\n
Type a SPACE and ENTER in your zeroth guess to identify spaces in the given puzzle
PLAY FAIR''')
def cls():
    print('\n'*1000)
word1=input('Enter word to Guess - ')
word=list(word1)
cls()
display=[]
display.extend(word)
n=len(word)
for a in range(n):
    display[a]='_'
print(' '.join(display))
count=0
x=6
while (count<n):
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
                print(' '.join(display))
                if display==word:
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
        


    
        
        
