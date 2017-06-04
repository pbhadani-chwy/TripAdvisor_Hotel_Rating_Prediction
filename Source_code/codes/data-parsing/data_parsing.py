import os

def ReadText():
    #************** setting the path for all files retrieval from the given folder *************#
    path = "C:\\Users\\bhada\Downloads\SMM\Data_Project\\Texts"
    for filename in os.listdir(path):
    #********************* Reading and opening files *******************************************#
        with open("C:\\Users\\bhada\Downloads\SMM\Data_Project\\Texts\\" + filename, mode= 'r', encoding= "latin-1") as f:

            inplist = []
            finlist = []
            fin_list = []
            count = 0


            for line in f:
                inplist.append(line)
                strp = inplist[0].strip('\n')
                if (len(inplist[0]) == 0):
                    continue
                keylist = []
                wordlist = []
        #************************** the given for loop fetches the tag from the input text folder *******#
                for i in range(len(inplist[0])):
                    if (inplist[0][i] == '<'):
                        while (inplist[0][i] != '>'):
                            keylist.append(inplist[0][i])
                            i +=1
                        keylist.append(inplist[0][i])
                        k = i+1
        #*************************** checking if the fetched tag is the pointing to reviewer username******#
                    if ("".join(keylist) == '<Author>'):
                        for j in range(k,len(inplist[0])):
                            wordlist.append(inplist[0][j])
                            i += 1
        #*************************** checking if the fetched tag is the pointing to reviewer reviews******#
                    elif("".join(keylist) == '<Content>'):
                        for j in range(k,len(inplist[0])):
                            wordlist.append(inplist[0][j])
                            i += 1
        #*************************** checking if the fetched tag is the pointing to reviewer ratings******#

                    elif("".join(keylist) == '<Rating>'):
                        for j in range(k,len(inplist[0])):
                            wordlist.append(inplist[0][j])
                            i += 1

                    if (i ==0 or i == 1 or i == 2):
                        continue
                    else:
                        break

                if (len("".join(wordlist)) != 0 and count != 3):
                    if count == 2:
#********************* This forloop take cares of rating and inseritng the rating to output list *************#
                        for k in range(len(wordlist)):
                            if (wordlist[k] != '\t'):
                                if (wordlist[k] == '-'):
                                    pass
                                elif (wordlist[k-1] == '-'):
                                    finlist.append('-' + wordlist[k])
                                else:
                                    finlist.append(wordlist[k])
                        count +=1
                    else:
                        finlist.append("".join(wordlist))
                        count +=1
#********************** This if condition flushes everything after three non-empty tag read ****************#
                if (count == 3):
                    for word in finlist:
                        fin_list.append(word.strip('\n'))
                    outfile = open("C:\\Users\\bhada\Downloads\SMM\Data_Project\\out_file\\finout.csv","a",encoding= 'latin-1')
                    finout = "^".join(fin_list)
                    outfile.write(filename + '^' + finout)
                    outfile.write("\n")

#********************** flushing of all lists after 3 read tag read to fetch next customer data**************#
                    count = 0
                    finlist = []
                    fin_list = []

                inplist = []

#********************** calling the function to initiate the reading ***************************************#
ReadText()

