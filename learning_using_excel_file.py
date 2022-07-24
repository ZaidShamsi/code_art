import pandas

fh=pandas.read_excel('0714_Validation.xlsx')
count=0
for line in fh:
    count=count+1
    if count==1:
        print(line)
