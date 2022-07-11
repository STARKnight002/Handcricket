import mysql.connector as mc
con=mc.connect(host='localhost',user='root',passwd='Pythonhaha123!')
cur=con.cursor()
cur.execute("Drop DATABASE if exists HC1")
cur.execute("CREATE DATABASE HC1")

def importing():
    print('''1.Install prettytable and mysql connector
2.Already installed''')
    ch=int(input("Enter the choice:"))
    if ch==1:
        import subprocess
        def ins(pack):
            subprocess.call(['python','-m','pip','install',pack])
        ins('prettytable')
        ins('mysql.connector')

    if ch==2:
        print("The package already exists")

importing()

print('INSTALL FINISHED')
