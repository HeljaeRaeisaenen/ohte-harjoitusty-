'''functions for reading and writing files'''

import os

def fileread(filepath: str):
    output = []
    with open(filepath) as file:
        for line in file:
            line = line.replace("\n", "")
            cleanline = line.split(",", maxsplit=1)
            cleanline[1] = cleanline[1].replace('"', "")
            cleanline[1] = cleanline[1].split(",")
            if cleanline[1][0] != "":
                '''this huge spectacle removes the whitespaces that some names in the wished 
                company have in front of them. idk if this could've been done more efficiently'''
                new = []
                for member in cleanline[1]:
                    if member[0] == " ":
                        new.append(member[1:])  # ??
                    else:
                        new.append(member)
                cleanline.pop(1)
                cleanline.append(new)
            output.append(cleanline)
    output.pop(0)  # delete header fields
    output.sort(key=lambda a: len("".join(a[1])), reverse=True)
    return output


'''The names, wishes are sorted by descending wish length
On the delimiter: comma is the default delimiter the TKO-äly website uses, and as of now it's the
only one used 
'''


def filewrite(contents: list):
    dirname = os.path.dirname(__file__)
    savepath = os.path.join(dirname, "data", "testsave.csv")

    with open(savepath, "w") as file:
        for line in contents:
            string = ""
            for piece in line:
                string += str(piece) + ","
            string = string[:-1]
            file.write(string+"\n")
