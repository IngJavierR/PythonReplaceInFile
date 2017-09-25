"""Replace trans"""

def get_translates():
    """get_translates"""
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
    dictionary = get_translates()
    file_to_trans = open("./Files/strings.xml", "r+")
    output_file = open('./Files/stringss_out.xml', 'w')
    for line in file_to_trans:
        for dic in dictionary:
            line = line.replace(dic, dictionary[dic])
        output_file.write(line)
    print "Finish"

_main_()
