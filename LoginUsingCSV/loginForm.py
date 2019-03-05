import csv
tampungUsers=[]
def loadData():
    with open('dataUser.csv','r') as data:
        readFile=csv.reader(data,delimiter=',')
        for line in readFile:
            tampungUsers.append(line)
    return True

def login(state):
    while state:
        username = input('Username:')
        password = input('Password:')
        for user in tampungUsers:
            if user[0] == username and user[1] == password:
                print('You are logged in.')
                state = False
                break
        else:
            print('Wrong input.')
loadData()
login(True)
