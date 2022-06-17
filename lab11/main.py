import re
import os

if __name__ == '__main__':
    file = open("resources/access.log")
    regex = r".*(26/Mar/2009:(1[4-9]:(49:2[3-9]|5[0-9]:[0-5][0-9])|2[0-3]:[0-5][0-9]:[0-5][0-9])" \
            r"|(2[7-9]/Mar/2009:(1|0[0-9])|(2[0-3]):[0-5][0-9]:[0-5][0-9])" \
            r"|30/Mar/2009:(0[0-8]:[0-5][0-9]:[0-5][0-9]|(0[0-9]|1[0-7]):([0-2][0-9]|3[0-6]))" \
            r".*\"GET .*\"robots\.txt"

    count = 0
    lines = file.readlines()
    for line in lines:
        found_text = re.search(regex, line)
    if found_text is not None:
        print(found_text)
        count += 1

    print(count)
