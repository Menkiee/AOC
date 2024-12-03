import re

pt_1, pt_2 = 0, 0
enable = True

with open('input.txt') as input:
    for l in input:
        matches = re.findall(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)', l.strip())
        for match in matches:
            if 'do()' == match:
                enable = True
            elif 'don\'t()' == match:
                enable = False
            else:
                a, b = map(int, re.findall(r'\d+',match))
                if enable:
                    pt_2 += a * b

                pt_1 += a * b


print(pt_1, pt_2)






