import sys
import re

def main():
    args = sys.argv[1]
    print(args)
    html = ["<html>","<body>"]
    with open(args, 'r') as file:
        lines = file.readlines()
        for line in lines:
            html.append(regex_to_html(line))
        if flag_ul:
            html.append('</ul>')
    html.append("</body>")
    html.append("</html>")
    with open('output.html', 'w') as file:
        file.writelines(html)

def regex_to_html(line):
    global flag_ul
    regex_for_heading = r'^(#+)\s(.*)'
    regex_for_bold = r'(\*\*|__)(.*?)\1'
    regex_for_italic = r'(\*|_)(.*?)\1'
    regex_for_li = r'^\d.*$'
    regex_for_a = r'\[(.*?)\]\((.*?)\)'
    
    match = re.match(regex_for_heading, line)
    if match:
        line = f'<h{len(match.group(1))}>{match.group(2)}</h{len(match.group(1))}>'
    
    match = re.match(regex_for_bold, line)
    if match:
        prefix = match.group(2)
        line2 = line.replace(prefix, '').removeprefix(' ')
        line = f'<strong>{match.group(2)}</strong>{line2}'
    
    match = re.match(regex_for_italic, line)
    if match:
        prefix = match.group(2)
        line2 = line.replace(prefix, '').removeprefix(' ')
        line = f'<em>{match.group(2)}</em>{line2}'
    
    match = re.match(regex_for_a, line)
    if match:
        line = line.replace(match.group(0), f'<a href="{match.group(2)}">{match.group(1)}</a>')
    
    match = re.match(regex_for_li, line)
    if match:
        pattern = r'\b\d+\.\s*(.*)'
        line = line.replace("*", '')
        if not flag_ul:
            flag_ul = True
            line = f'<ul><li>{match.group(0)}</li>'
        else:
            line = f'<li>{match.group(1)}</li>'
    
    return line

if __name__ == "__main__":
    flag_ul = False
    main()
    
