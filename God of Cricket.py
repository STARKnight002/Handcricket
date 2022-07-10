team_names=schedule=[]

print("WELCOME TO THE 'GOD OF CRICKET'\n")
print("""1)BEGINNER
PRESS ANYTHING IF YOU ARE AN EXISTING USER""")
ch=input('ENTER CHOICE-')
if ch=='1':
    print('''This is a Data Management system for a Cricket Game.
It includes the following features:-
1) Creating Teams and Sorting players into given teams
2) Scheduling matches for a tournament with given teams
3) 
          
READ THE INSTRUCTIONS CAREFULLY\n
STEPS TO USE-
1)YOU HAVE TO GIVE THE LIST OF PLAYERS AND THE TEAM NAMES
  THE PROGRAM WILL CREATE THE TEAMS FOR YOU
2)THE SCHEDULE WILL BE PROVIDED AND MATCHES WILL START ACCORDINGLY
3)YOU HAVE TO PROVIDE THE NAME FOR THE LEAGUE. THIS WILL HELP YOU ACCESS THIS LEAGUE LATER
    
INSTRUCTIONS-\n
(The Leaguename is the Unique Primary Code for a specific tournament)
RULES FOR LEAGUENAME -
1)NO SPECIAL CHARACTERS
2)SHOULD NOT START WITH NUMBER
3)NO NULL VALUES
    
Entering Values-
1)Enter appropriate values for overs. Don't Enter 5.8 overs. 
  Approx. Value will be taken in such case
2)Keep the Scores as Logical as Possible
3)YOU CAN CHOOSE TO VIEW POINTS TABLE AS PER YOUR WISH
4)ONCE LEAGUE STAGES ARE DONE, THE QUALIFIERS BEGIN
5)THE PROGRAM ENDS WHEN THE CHAMPION IS CHOSEN

THINGS TO NOTE-
1)YOU CAN KILL THE PROGRAM ANYTIME YOU WANT AND CONTINUE LATER PROVIDED YOU REMEMBER THE LEAGUENAME
''')
else:
    pass
    
def team():
    print("\nCreate Your Team")
    import random
    global team_names,schedule
    while (1>0):
        try:
            players=int(input('Enter number of players participating:'))
            teams=int(input('Enter number of teams in the league:'))
            while (players<=0)or(teams<=0)or(players/teams!=players//teams):        # To make sure given values are positive
                print("ENTER APPROPRIATE VALUES\n")
                players=int(input('Enter number of players participating:'))
                teams=int(input('Enter number of teams in the league:'))
            break
        except:
            print('ENTER APPROPRIATE VALUES')

    player_names=[]
    team_names=[]
    tempnames=[]
    #Create list of players
    for i in range(0,players):
        oneplayer=input('Enter the player\'s name:')
        while (oneplayer in player_names):
            print("ENTER UNIQUE NAMES\n")
            oneplayer=input('Enter the player\'s name:')
        player_names.append(oneplayer)
    print('\nThe list of players playing in the league is:\n')
    for i in player_names:
        print(i)

    #Create list of teams
    for j in range(0,teams):
        oneteam=input('\nEnter a team name you want in the league:')
        while (oneteam in team_names):
            print("ENTER UNIQUE NAMES\n")
            oneteam=input('\nEnter a team name you want in the league:')
        team_names.append(oneteam)
        tempnames.append(oneteam)
    print("Teams Playing")
    for i in tempnames:
        print(i)
    #Create the matches required
    l=len(tempnames)
    matches=[]
    for i in range(0,l):
        for j in range(i+1,l):
            match=tempnames[i]+ ' vs ' +tempnames[j]
            matches.append(match)

    #Players to teams
    for k in range(0,teams):
        team_players=[]

        #Selecting players for a single team
        for l in range(0,players//teams):
            randomplayer=random.choice(player_names)
            team_players.append(randomplayer)
            index=player_names.index(randomplayer)
            del player_names[index]

        #Selecting THAT team
        randomteam=random.choice(tempnames)
        ind=tempnames.index(randomteam)
        del tempnames[ind]

        #The Captain
        captain=random.choice(team_players)
        print('\nThe players of',randomteam,'are')
        for i in team_players:
            if i==captain:
                print(i,"(Captain)")
            else:
                print(i)
    
    schedule=[]
    n=1
    #Displaying the schedule
    while len(matches)>0 :
        ch=random.choice(matches)
        print('\nMatch',n,':',ch)
        n+=1
        schedule.append(ch)
        i=matches.index(ch)
        del matches[i]

#team()

import mysql.connector as mc
con=mc.connect(host='localhost',user='root',passwd='Pythonhaha123!',auth_plugin='mysql_native_password')
l=len(team_names)

leaguename=''
def install():
    global leaguename
    cur=con.cursor()
    cur.execute("USE HC1")
    cur.execute("SELECT * FROM hcc")
    result=cur.fetchall()
    hcl=[]
    for i in result:
        hcl.append(i[0])
    while (1>0):    
        try:
            leaguename=input('\nENTER LEAGUENAME YOU WANT TO CREATE-')
            while leaguename in hcl:
                print("LEAGUE ALREADY EXISTS")
                leaguename=input('\nENTER LEAGUENAME YOU WANT TO CREATE-')
            cur.execute("create table "+leaguename+"""(SL_NO int(3), Team varchar(20), Matches_played int(3), Won int(3), Lost int(3),
Draw int(3), Points int(3), Runs_Scored int(5),Balls_played int(5),Runs_conceded int(5),
Balls_bowled int(5),Team_RR float(10), OPP_RR float(10), Net_RR float(10))""")
            break
        except:
            print('Not applicable')
    l=len(team_names)
    for i in range(l):
        sql = "INSERT INTO "+leaguename+"""(SL_NO, Team, Matches_played, Won, Lost, Draw, Points, Runs_Scored, Balls_played,
    Runs_conceded, Balls_bowled, Team_RR, OPP_RR, Net_RR)
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        rows = [(i+1,team_names[i],0,0,0,0,0,0,0,0,0,0,0,0)]
        cur.executemany(sql,rows)
        con.commit()

bowling=batting=''
team_name=[]
#GETTING INPUT OF WHICH TEAM IS BATTING AND BOWLING
def toss(t1,t2):
    global batting,bowling,team_name
    team_name=[t1,t2]
    dump = list(team_name)
    batting=input('Team batting first:')
    while batting not in team_name:
        print('Invalid team name for current match')
        batting=input('Team batting:')
    dump.remove(batting)

    bowling=dump[0]    

#GLOBALISATION OF VARIABLES
#GETTING SCORES IN RUNS AND OVERS
#CONVERTING OVERS TO BALLS
#OVERS ARE NOT SAVED, BALLS PLAYED ARE SAVED
ball2=ball1=over2=over1=secondscore=firstscore=0
def values():
    dum=[0,1,2,3,4,5]
    global firstscore,secondscore,over1,over2,ball1,ball2
    firstscore=int(input('Enter the score of the team batting first-'))
    over1=float(input('Enter the overs played by the team batting first-'))
    while (round((over1-int(over1)),1)*10) not in dum:
        print("Invalid. Enter Appropriate Value")
        over1=float(input('Enter the overs played by the team batting first-'))
    secondscore=int(input('Enter the score of the team batting second-'))
    over2=float(input('Enter the overs played by the team batting second-'))
    while (round((over2-int(over2)),1)*10) not in dum:
        print("Invalid. Enter Appropriate Value")
        over2=float(input('Enter the overs played by the team batting first-'))
    ball1=(int(over1)*6)+round((over1-int(over1)),1)*10
    ball2=(int(over2)*6)+round((over2-int(over2)),1)*10

#THE MATCH PROCEDURE
#USING LOOPS TO AVOID ERRORS
#SUPER OVER MECHANISM REPEATS THE MATCH
draw=win1=win2=batpoint=ballpoint=winner=0
def match(t1,t2):
    global firstscore,secondscore,over1,over2,win1,win2,draw,batpoint,ballpoint,winner
    toss(t1,t2)
    while (batting not in team_name)or(bowling not in team_name)or(bowling==batting):
        print('INVALID ENTRY')
        print('TRY AGAIN')
        toss(t1,t2)
    while (1>0):    
        try:
            values()
            while (firstscore<0)or(secondscore<0)or(over1<=0)or(over2<=0):
                print("DON'T Enter Negative valuees\n")
                print("DON'T Enter 0 for overs... Atleast play one ball\n")
                values()
            break
        except:
            print('ENTER APPROPRIATE VALUES')

    if (firstscore>secondscore):
        print('\n',batting,'Wins the game')
        winner=batting
        win1+=1
        batpoint+=2
    elif (firstscore<secondscore):
        print('\n',bowling,'Wins the game')
        winner=bowling
        win2+=1
        ballpoint+=2
    else:
        print("It's a tie!!")
        while (1>0):    
            try:
                ch=int(input('''1)SUPER OVER
2)DRAW MATCH
Enter your choice-'''))
                while (ch<=0)or(ch>=3):
                    print("Enter Appropriate valuees\n")
                    ch=int(input('''1)SUPER OVER
 2)DRAW MATCH
 Enter your choice-'''))
                break
            except:
                print('ENTER APPROPRIATE VALUES')
        if (ch==1):
            print('SUPER OVER')
            print('Play Ideally one over')
            print('More than one over can also be played')
            match(t1,t2)
        elif (ch==2):
            print("It's a DRAW")
            draw+=1
            batpoint+=1
            ballpoint+=1
            winner=str(t1)+' and '+str(t2)

#UPDATING POINTS TO BE ADDED TO THE TABLE IN MYSQL
#OBTAINING VALUES FROM DATABASE AND UPDATING IT
mat2=won2=los2=draw2=points2=mat1=won1=los1=draw1=points1=0
def points():
    global mat1,won1,los1,draw1,points1,mat2,won2,los2,draw2,points2,batpoint,ballpoint,win1,win2,draw
    cur = con.cursor()
    cur.execute('USE HC1')
    sql = """SELECT team,Matches_played,won,lost,draw,points FROM """+leaguename+""" where team=%s"""
    val=[(batting)]
    cur.execute(sql,val)
    result = cur.fetchall()

    mat1=result[0][1]
    won1=result[0][2]
    los1=result[0][3]
    draw1=result[0][4]
    points1=result[0][5]
    mat1+=1
    won1+=win1
    los1+=win2
    draw1+=draw
    points1+=batpoint

    sql = "SELECT team,Matches_played,won,lost,draw,points FROM "+leaguename+""" where team=%s"""
    val=[(bowling)]
    cur.execute(sql,val)
    result = cur.fetchall()
    mat2=result[0][1]
    won2=result[0][2]
    los2=result[0][3]
    draw2=result[0][4]
    points2=result[0][5]
    mat2+=1
    won2+=win2
    los2+=win1
    draw2+=draw
    points2+=ballpoint
    draw=win1=win2=batpoint=ballpoint=0

#UPDATING SCORES TO BE ADDED TO THE TABLE IN MYSQL JUST LIKE POINTS
giveball2=giveball1=giverun2=giverun1=getball2=getball1=getrun2=getrun1=0
def scoreadd():
    global getrun1,getrun2,getball1,getball2,giverun1,giverun2,giveball1,giveball2
    cur=con.cursor()
    cur.execute('USE HC1')
    sql = """SELECT team,Runs_scored,Balls_played,Runs_conceded,
Balls_bowled FROM """+leaguename+" where team=%s"
    val=[(batting)]
    cur.execute(sql,val)
    result = cur.fetchall()

    getrun1=result[0][1]
    getball1=result[0][2]
    giverun1=result[0][3]
    giveball1=result[0][4]

    sql = """SELECT team,Runs_scored,Balls_played,Runs_conceded,
Balls_bowled FROM """+leaguename+" where team=%s"
    val=[(bowling)]
    cur.execute(sql,val)
    result = cur.fetchall()

    getrun2=result[0][1]
    getball2=result[0][2]
    giverun2=result[0][3]
    giveball2=result[0][4]

    getrun1+=firstscore
    getrun2+=secondscore
    getball1+=ball1
    getball2+=ball2
    giverun1+=secondscore
    giverun2+=firstscore
    giveball1+=ball2
    giveball2+=ball1
    
#CALCULATING NET RUN RATE
nrr2=nrr1=rpo22=rpo11=rpo2=rpo1=0
def runrate():
    global rpo1,rpo2,nrr1,nrr2,rpo11,rpo22
    rpo1=(getrun1/getball1)*6
    rpo11=(giverun1/giveball1)*6
    rpo2=(getrun2/getball2)*6
    rpo22=(giverun2/giveball2)*6
    nrr1=rpo1-rpo11
    nrr2=rpo2-rpo22
    
#ADDING POINTS TO THE TABLE IN MYSQL
def save():
    cur = con.cursor()
    cur.execute('USE HC1')
    sql = "UPDATE "+leaguename+""" SET Matches_played= %s, Won= %s, Lost= %s, Draw= %s, Points= %s, Runs_scored= %s, Balls_played= %s,
Runs_conceded= %s, Balls_bowled= %s, Team_rr= %s, OPP_rr= %s,
Net_rr= %s WHERE Team= %s"""
    x=(mat1,won1,los1,draw1,points1,getrun1,getball1,giverun1,giveball1,rpo1,rpo11,nrr1,batting)
    y=(mat2,won2,los2,draw2,points2,getrun2,getball2,giverun2,giveball2,rpo2,rpo22,nrr2,bowling)
    val=[x,y]
    cur.executemany(sql,val)
    con.commit()

def tables():
    cur=con.cursor()
    cur.execute('USE HC1')
    sql = "SELECT Team,Matches_played,Won,Lost,Draw,Points,Net_rr FROM "+leaguename+" order by points desc, Net_rr desc"
    cur.execute(sql)
    result = cur.fetchall()

    from prettytable import PrettyTable
    table=PrettyTable(['Team','Matches played','Won','Lost','Draw','Points','Net-RunRate'])
    for t in result:
        table.add_row(t)
    print(table)

def pointstable():
    print('''\nDO YOU WANT TO VIEW THE POINTS TABLE?
IF YES ENTER "yes"
IF NOT THEN PRESS "ENTER KEY"''')
    ch=input('ENTER YOUR CHOICE-')
    if (ch.lower()=='yes'):
        tables()
    else:
        pass
    
#UPDATING SCORES TO BE ADDED TO THE TABLE IN MYSQL JUST LIKE POINTS
def semiscoreadd():
    global firstscore,secondscore,over1,over2,batting,bowling,winner
    cur=con.cursor()
    cur.execute('USE HC1')
    try:
        cur.execute('CREATE TABLE '+leaguename+'_semi'+' (Teamname varchar(30),Runs_Scored int(5),Overs float(5),Outcome varchar(15))')
    except:
        pass
    
    sql = "INSERT INTO "+leaguename+'_semi'+""" 
VALUES(%s, %s, %s, %s)"""
    if batting==winner:
        rows = [(batting,firstscore,over1,'Won')]
    elif bowling==winner:
        rows = [(bowling,secondscore,over2,'Won')]
    cur.executemany(sql,rows)
    con.commit()
    
    if batting==winner:
        rows = [(bowling,secondscore,over2,'Lost')]
    elif bowling==winner:
        rows = [(batting,firstscore,over1,'Lost')]
    cur.executemany(sql,rows)
    con.commit()
    
    sql = "INSERT INTO "+leaguename+'_semi'+""" 
VALUES(%s, %s, %s, %s)"""
    rows = [('---',000,000,'---')]
    cur.executemany(sql,rows)
    con.commit()
    
def stats():
    cur=con.cursor()
    cur.execute('USE HC1')
    sql = "SELECT Team,Matches_played,Won,Lost,Draw,Points,Runs_Scored, Balls_played,Net_rr FROM "+leaguename+" order by points desc, Net_rr desc"
    cur.execute(sql)
    result = cur.fetchall()
    
    print("\nPOINTS TABLE with STATS")
    from prettytable import PrettyTable
    table=PrettyTable(['Team','Matches played','Won','Lost','Draw','Points','Runs Scored','Balls played','Net-RunRate'])
    for t in result:
        table.add_row(t)
    print(table)

    sql = "SELECT Teamname,Runs_Scored,Overs,Outcome FROM "+leaguename+'_semi'
    cur.execute(sql)
    result = cur.fetchall()
    
    print("\nQualifiers Table")
    
    from prettytable import PrettyTable
    table=PrettyTable(['Teamname','Runs Scored','Overs','Outcome'])
    for t in result:
        table.add_row(t)
    print(table)
    
def displaystats():
    ask=input("Do you want to view the stats now? (y/n) - ")
    if ask=='y':
        stats()
    else:
        pass
    
def champ():
    global winner
    cur=con.cursor()
    cur.execute('USE HC1')
    try:
        cur.execute("CREATE TABLE "+leaguename+'champ'+" (Sno int(2), Teamname varchar(30))")
    except:
        pass
    sql = "INSERT INTO "+leaguename+'champ'+""" 
VALUES(%s,%s)"""
    rows = [(1,winner)]
    cur.executemany(sql,rows)
    con.commit()

def qualifiers():
    global winner
    cur=con.cursor()
    cur.execute('USE HC1')
    
    sql = "SELECT Team,Matches_played,Won,Lost,Draw,Points,Net_rr FROM "+leaguename+" order by points desc, Net_rr desc"
    cur.execute(sql)
    result = cur.fetchall()
    
    cur.execute("SELECT * FROM "+leaguename+'2')
    result2=cur.fetchall()
    team_names=[]
    for i in result2:
        team_names.append(i[1])
    l=len(team_names)
    
    if 2<=l<=4 :
        if l==3 :
            quali=result[1:3]
            team_name=[]
            if (quali[0][5]==quali[1][5])and(quali[0][6]==quali[0][6]):
                print('2nd and 3rd team having same statistics. Deciding finalist now...')
                match(quali[0][0],quali[1][0])
                semiscoreadd()
                while winner==str(quali[0][0])+' and '+str(quali[1][0]) :
                    print('Since the finalist deciding match tied, you play the match again..')
                    match(quali[0][0],quali[1][0])
                    semiscoreadd()
                result=result[0]  #result is now a tuple
                team_name.append(winner)
                team_name.append(result[0])
                print('GRAND FINALE \n')
                print(team_name[0],' vs ',team_name[1])
                match(team_name[0],team_name[1])
                print('\nCONGRATS TO',winner,'FOR WINNING THE LEAGUE AS A RESULT OF THEIR ULTIMATE PERFORMANCE')
                champ()

            else:
                result=result[0:2]  #gettin 1st 2 teams
                team_name=[]
                for t in result:
                    team_name.append(t[0])#appending team names to list
                print('GRAND FINALE \n')
                print(team_name[0],' vs ',team_name[1])
                match(team_name[0],team_name[1])
                semiscoreadd()
                print('\nCONGRATS TO',winner,'FOR WINNING THE LEAGUE AS A RESULT OF THEIR ULTIMATE PERFORMANCE')                 
                champ()
                
        else:
            result=result[0:2]  #gettin 1st 2 teams
            team_name=[]
            for t in result:
                team_name.append(t[0])#appending team names to list
            print('\nGRAND FINALE \n')
            print(team_name[0],' vs ',team_name[1])
            match(team_name[0],team_name[1])
            semiscoreadd()
            print('\nCONGRATS TO',winner,'FOR WINNING THE LEAGUE AS A RESULT OF THEIR ULTIMATE PERFORMANCE') 
            champ()
            
    elif l>4 :
        result=result[0:4]  #gettin 1st 4 teams
        sem=[]
        fin=[]
        for t in result:
            sem.append(t[0])
        
        print('\nSemi final 1:',sem[0],' vs ',sem[3])
        match(sem[0],sem[3])
        semiscoreadd()
        fin.append(winner)
        print('\nCongrats to',winner,'for qualifying to the GRAND FINALE')

        print('\nSemi final 2:',sem[1],' vs ',sem[2])
        match(sem[1],sem[2])
        semiscoreadd()
        fin.append(winner)
        print('\nCongrats to',winner,'for qualifying to the grand finale')

        team_name=fin

        print('\n GRAND FINALE \n')
        print(team_name[0],' vs ',team_name[1])
        match(team_name[0],team_name[1])
        semiscoreadd()
        print('\n CONGRATS TO',winner,'FOR WINNING 1st PLACE IN THE LEAGUE AS A RESULT OF THEIR ULTIMATE PERFORMANCE') 
        print('\n THE CHAMPION-',winner)
        champ()

def leaguecheck():
    global leaguenam
    cur=con.cursor()
    cur.execute("USE HC1")
    cur.execute('Select * from hcc')
    res=cur.fetchall()
    print('The existing league names are-')
    verif=[]
    for i in range(1,len(res)-1,2):
        if res[i][0] not in verif:
            print(res[i][0])
            verif.append(res[i][0])
        leaguenam.append(res[i][0])

def run():
    global leaguename,schedule,leaguenam
    cur=con.cursor()
    cur.execute("USE HC1")
    try:
        cur.execute('CREATE TABLE hcc (league varchar(30))')
    except:
        pass
    sql="INSERT INTO hcc (league) VALUES(%s)"
    v=[(leaguename)]
    cur.execute(sql,v)
    
    leaguenam=[]
    
    print('''\nDo you want to start fresh or continue?\n
Once your start a league you cannot change the teams playing in it!!\n
Enter 'new' to start fresh
If you want to continue press "ENTER" key''')
    ins=input('Enter choice-')
    if ins.lower()=='new':
        team()
        install()
    else:
        leaguecheck()
        leaguename=input('ENTER LEAGUENAME YOU CREATED-')
        while leaguename not in leaguenam:
            if leaguename in leaguenam:
                break
            else:
                print('LEAGUENAME DOES NOT EXIST. START PROGRAM AGAIN')
                leaguename=input('ENTER LEAGUENAME YOU CREATED-')
    
    cur=con.cursor()
    cur.execute("USE HC1")
    sql="INSERT INTO hcc (league) VALUES(%s)"
    v=[(leaguename)]
    cur.execute(sql,v)
    
    try:
        cur.execute('CREATE TABLE '+leaguename+'1'+' (SL int(5), matchs varchar(30))')
    except:
        pass
    for i in schedule:
        sql="INSERT INTO "+leaguename+'1'+" (SL, matchs) VALUES(%s, %s)"
        v=[(1,i)]
        cur.executemany(sql,v)
    
    try:
        cur.execute('CREATE TABLE '+leaguename+'2'+' (SL int(5), teams varchar(30))')
    except:
        pass
    for i in team_names:
        sql="INSERT INTO "+leaguename+'2'+" (SL, teams) VALUES(%s, %s)"
        v=[(1,i)]
        cur.executemany(sql,v)
    
    prev=input('''Enter "YES" if you wanna play with previous data
Press anything to just view stats of given league:''')
    
    cur=con.cursor()
    cur.execute("USE HC1")
    try:
        cur.execute('CREATE TABLE '+leaguename+'0'+' (SL int(5), matchs varchar(30))')
    except:
        pass
    
    if prev=='yes' :
        try:
            stats()    
            try:
                cur.execute("SELECT Sno,Teamname FROM "+leaguename+'champ')
                won=cur.fetchall()
                champ=won[0][1]
                print('')
                print(champ," is the CHAMPION")
                
            except:
                print("Replay Qualifiers")
                cur.execute("SELECT matchs FROM "+leaguename+'0')
                result0=cur.fetchall()
                cur.execute("SELECT matchs FROM "+leaguename+'1')
                result1=cur.fetchall()
                if result0[len(result0)-1]==result1[len(result1)-1]:
                    try:
                        cur.execute("DROP TABLE "+leaguename+'_semi')
                    except:
                        pass
                    qualifiers()
                    
        except:
            cur.execute("SELECT * FROM "+leaguename+'0')
            result1=cur.fetchall()
        
            cur.execute("SELECT * FROM "+leaguename+'1')
            result=cur.fetchall()
            schedule=[]
            for i in result:
                schedule.append(i[1])
        
            for i in result1:
                a=i[1]
                schedule.remove(a)
        
            for i in schedule:
                vs=i.find(' vs ')
                t1=i[0:vs]
                t2=i[4+vs:]
                print('\n',i)
                match(t1,t2)
                print(i)
        
                sql="INSERT INTO "+leaguename+'0'+" (SL, matchs) VALUES(%s, %s)"
                val=[1,i]
                cur.execute(sql,val)
                
                points()
                scoreadd()
                runrate()
                save()
                if (schedule.index(i) != len(schedule)-1):
                    pointstable()
    
        tables()
        try:
            stats()    
            try:
                cur.execute("SELECT Sno,Teamname FROM "+leaguename+'champ')
                won=cur.fetchall()
                champ=won[0][1]
                print('')
                print(champ," is the CHAMPION")
            
            except:
                print("Replay Qualifiers")
                cur.execute("SELECT matchs FROM "+leaguename+'0')
                result0=cur.fetchall()
                cur.execute("SELECT matchs FROM "+leaguename+'1')
                result1=cur.fetchall()
                if result0[len(result0)-1]==result1[len(result1)-1]:
                    try:
                        cur.execute("DROP TABLE "+leaguename+'_semi')
                    except:
                        pass
                    qualifiers()
                
        except:
            try:
                cur.execute("SELECT Team FROM "+leaguename+'champ')
                won=cur.fetchall()
                champ=won[0][1]
            except:
                cur.execute("SELECT matchs FROM "+leaguename+'0')
                result0=cur.fetchall()
                cur.execute("SELECT matchs FROM "+leaguename+'1')
                result1=cur.fetchall()
                if result0[len(result0)-1]==result1[len(result1)-1]:
                    try:
                        cur.execute("DROP TABLE "+leaguename+'_semi')
                    except:
                        pass
                    qualifiers()
            
    else:
        try:
            stats()    
            try:
                cur.execute("SELECT Sno,Teamname FROM "+leaguename+'champ')
                won=cur.fetchall()
                champ=won[0][1]
                print('')
                print(champ," is the CHAMPION")
                
            except:
                print("Replay Qualifiers")
                cur.execute("SELECT matchs FROM "+leaguename+'0')
                result0=cur.fetchall()
                cur.execute("SELECT matchs FROM "+leaguename+'1')
                result1=cur.fetchall()
                if result0[len(result0)-1]==result1[len(result1)-1]:
                    try:
                        cur.execute("DROP TABLE "+leaguename+'_semi')
                    except:
                        pass
                    qualifiers()
                    
        except:
            for i in schedule:
                vs=i.find(' vs ')
                t1=i[0:vs]
                t2=i[4+vs:]
                print('\n',i)
                match(t1,t2)
        
                sql="INSERT INTO "+leaguename+'0'+" (SL, matchs) VALUES(%s, %s)"
                v=[(1,i)]
                cur.executemany(sql,v)
                
                points()
                scoreadd()
                runrate()
                save()
                print(i)
                if (schedule.index(i) != len(schedule)-1):
                    pointstable()
    
        try:
            stats()    
            try:
                cur.execute("SELECT Sno,Teamname FROM "+leaguename+'champ')
                won=cur.fetchall()
                champ=won[0][1]
                print('')
                print(champ," is the CHAMPION")
            
            except:
                print("Replay Qualifiers")
                cur.execute("SELECT matchs FROM "+leaguename+'0')
                result0=cur.fetchall()
                cur.execute("SELECT matchs FROM "+leaguename+'1')
                result1=cur.fetchall()
                if result0[len(result0)-1]==result1[len(result1)-1]:
                    try:
                        cur.execute("DROP TABLE "+leaguename+'_semi')
                    except:
                        pass
                    qualifiers()
                
        except:
            try:
                cur.execute("SELECT Team FROM "+leaguename+'champ')
                won=cur.fetchall()
                champ=won[0][1]
            except:
                cur.execute("SELECT matchs FROM "+leaguename+'0')
                result0=cur.fetchall()
                cur.execute("SELECT matchs FROM "+leaguename+'1')
                result1=cur.fetchall()
                if result0[len(result0)-1]==result1[len(result1)-1]:
                    try:
                        cur.execute("DROP TABLE "+leaguename+'_semi')
                    except:
                        pass
                    qualifiers()
        

if __name__=="__main__":
    run()
    while True:
        ask = input('Do you want to re-run the program? (y/n) - ')
        if ask=='y':
            sp=0
            sc=0
            run()
        else:
            print("The End")
            con.close()
            break


