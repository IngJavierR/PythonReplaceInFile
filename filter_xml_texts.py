"""regexLines"""
import re

def regex_lines(file_object):
    """regexLines"""
    regex = r"<string \w.*>(.+)<\/string>"
    return re.findall(regex, file_object)

def get_lines():
    """getLines"""
    lines = []
    with open("./Files/stringss_out.xml", "r") as file_object:
        lines = regex_lines(file_object.read())
    return lines

def write_in_file(lines):
    """writeInFile"""
    with open('./Files/toTranslate.txt', 'w') as output_file:
        for line in lines:
            output_file.write(line + " - \n")

def __main__():
    print "Init"
    lines = get_lines()
    write_in_file(lines)
    print "Finish"

__main__()
