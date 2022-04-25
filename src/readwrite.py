'''functions for reading and writing files'''
from pathlib import Path


def fileread(filepath: str):
    '''Read a file into a list
    Args:
        filepath: path to the file which will be read
    Returns:
        output: a list containing the file's contents'''
    output = []
    with open(filepath, encoding="UTF-8") as file:
        for line in file:
            line = line.replace("\n", "")
            cleanline = line.split(",", maxsplit=1)
            cleanline[1] = cleanline[1].replace('"', "")
            cleanline[1] = cleanline[1].split(",")
        # this huge spectacle removes the whitespaces that some names in the wished
        # company have in front of them, due to punctuation.
        # idk if this could've been done more efficiently
            new = []
            for member in cleanline[1]:
                if member == "":
                    break
                if member[0] == " ":
                    new.append(member[1:])
                else:
                    new.append(member)
                cleanline.pop(1)
                cleanline.append(new)
            output.append(cleanline)
    output.pop(0)  # delete header fields
    output.sort(key=lambda a: len("".join(a[1])), reverse=True)
    return output

# The names, wishes are sorted by descending wish length


def filewrite(placement: list, filepath):
    '''Write a file
    Args:
        filecontents: a list containing lines to be written. List has sublists which have sublists
        filepath: the desired path and filename
    '''
    filecontents = []
    for index, row in enumerate(placement):
        filecontents.append(row)
        if index % 2 == 1:
            filecontents.append([])

    Path(filepath).touch()

    with open(filepath, "w", encoding="UTF-8") as file:
        for line in filecontents:
            string = ""
            for piece in line:
                string += str(piece) + ","
            string = string[:-1]
            file.write(string+"\n")
