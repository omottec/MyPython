import re

r_file = "/Users/qbb/Bt/repalce_res/R.txt"
with open(r_file) as file_object:
    r_contents = file_object.read()

origin_file = '/Users/qbb/Bt/repalce_res/all_origin'
white_lines = []
black_lines = []
with open(origin_file) as file_object:
    for line in file_object:
        print(line.strip())
        key = re.search(r'^\s*<string name="(.+)">.*</string>$', line).group(1)
        print(key.strip())
        if r_contents.__contains__(key):
            white_lines.append(line)
        else:
            black_lines.append(line)

filter_file = "/Users/qbb/Bt/repalce_res/all_filter"
with open(filter_file, 'w') as file_object:
    for l in white_lines:
        file_object.write(l)

black_file = "/Users/qbb/Bt/repalce_res/all_black"
with open(black_file, 'w') as file_object:
    for l in black_lines:
        file_object.write(l)