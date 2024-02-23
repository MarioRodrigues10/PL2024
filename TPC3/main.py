import sys
import re

def main():
    pattern = r'(on|off|=|\d+)'
    list = []
    for linha in sys.stdin:
        match = re.findall(pattern, linha)
        list.append(match)
    control = False
    sum = 0
    for list2 in list:
        for element in list2:
            if element.lower() == "on":
                control = True
            elif element.lower() == "off":
                control = False
            elif element.isdigit():
                if control:
                    sum += int(element)
            elif element.lower() == "=":
                print("Soma:", sum)

if __name__ == '__main__':
    main()