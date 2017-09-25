#!/usr/bin/python
def getTranslates():
    file_object = open("./Files/translate.txt", "r")
    dictionary = {}
    for line in file_object:
        dic = line.split("-")
        if len(dic) >= 2:
            print dic[0]
            dictionary[dic[0].strip(' \t\n\r')] = dic[1].strip(' \t\n\r')
    return dictionary

def _main_():
    print "Started"
    dictionary = getTranslates()
    fileToTrans = open("./Files/strings.xml", "r+")
    outputFile = open('./Files/stringss_out.xml', 'w')
    for line in fileToTrans:
        for dic in dictionary:
            line = line.replace(dic, dictionary[dic])
        outputFile.write(line)
    print "Finish"

_main_()
