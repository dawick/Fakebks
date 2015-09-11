#this is the full master index finder w/ thin-list function & offset
#Fixes problem with contractions

#still need to accommodate for input errors during menu phase

#need to provide access to Appendix pages (A1, A2, etc.)



#from subprocess import Popen
import webbrowser

pgset = {'Colorado':'+3', 'EvansBk':'+3', 'JazzFake':'-1',
       'JazzLTD':'+7', 'Library':'+4', 'NewReal1':'+15',
           'NewReal2':'+12', 'NewReal3':'+10', 'Realbk1':'+13',
           'RealBk2':'+7', 'RealBk3':'+5'}

def menu(locs):
    count = 1
    for entry in locs:
        print count, entry[0], ': ', entry[1], entry[2]
        #count = count + 1
        count += 1 #same thing
    print
    user = raw_input('Make selection: ')
    user = int(user)
    return locs[user - 1] #need to add 'else' statement, in case input is out of range
    
def calc_pg(offset, base):
    if offset[0] == '-':
        base = base - int(offset[1:])
    else:
        base = base + int(offset[1:])
    return base




#def pyFake():
if __name__ == "__main__":
    infile = open('Master.txt', 'r')
    data = infile.readlines()
    infile.close
    newfile = []
    for line in data:
        newfile.append(line[:-1].split(' '))
    #for line in newfile:
     #   print ' '.join(line[:-2])


    while True:
        search_string = str(raw_input('Enter Song Title: '))
        search_cap = []
        search_list = search_string.split()
        for x in search_list:
            search_cap.append(x.capitalize())

        oldlst = newfile
        newlist = []
        locs = []
        for word in search_cap:
            newlist = []
            for entry in oldlst:
                if word in entry:
                    newlist.append(entry)
            oldlst = newlist
        #print newlist

        for line in newlist:
            page = line[-1]
            filename = line[-2]
            title = ' '.join(line[:-2])
            locs.append([title, filename, page])

        if len(locs)>=1:
            choice = menu(locs)#runs menu function
            print choice
            filen = choice[-2]
            base = int(choice[-1])
            offset = pgset[filen]
            base = str(calc_pg(offset, base))#runs calc_pg function
            if choice[-2] == 'Colorado':
                choice[-2] = 'COLOBK.PDF'
            elif choice[-2] == 'EvansBk':
                choice[-2] = 'EvansBk.pdf'
            elif choice[-2] == 'JazzFake':
                choice[-2] = 'JAZZFAKE.PDF'
            elif choice[-2] == 'JazzLTD':
                choice[-2] = 'JazzLTD.pdf'
            elif choice[-2] == 'Library':
                choice[-2] = 'Library.pdf'
            elif choice[-2] == 'NewReal1':
                choice[-2] = 'NEWREAL1.PDF'
            elif choice[-2] == 'NewReal2':
                choice[-2] = 'NEWREAL2.PDF'
            elif choice[-2] == 'NewReal3':
                choice[-2] = 'NEWREAL3.PDF'
            elif choice[-2] == 'Realbk1':
                choice[-2] = 'REALBK1.PDF'
            elif choice[-2] == 'RealBk2':
                choice[-2] = 'REALBK2.PDF'
            elif choice[-2] == 'RealBk3':
                choice[-2] = 'REALBK3.PDF'

                
            #webbrowser.open("http://www.bearishwearish.com/fakebooks/"+choice[-2]+"#page="+base)
            print '"C:\\Program Files\\Adobe\\Reader 9.0\\Reader\\AcroRd32.exe" /A "page='+base+'" "C:\\Test\\FakeBook\\'+choice[-2]+'.pdf"'
            #p = Popen('"C:\\Program Files\\Adobe\\Reader 9.0\\Reader\\AcroRd32.exe" /A "page='+base+'" "'+choice[-2]+'.pdf"')
        else:
            print
            print 'Title not found'
            print
                    



        quits = raw_input("Submit Q to quit, Press (Enter) to continue... ")
        print
        if quits == "q" or quits == "Q":
                        break

