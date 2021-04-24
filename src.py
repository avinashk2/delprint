import re, sys


files = sys.argv[1:]
for file in files:
    print(f'-----processing {file}---------')
    with open(file) as f:
        with open(file+'clean', 'a') as cleanf:
            for line in f.readlines():
                if re.search(r'[\s*#]*print\(.*?\)', line):
                    print('removed line ===>', line)
                    continue
                else:
                    cleanf.write(line)
