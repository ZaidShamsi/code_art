from file_read_backwards import FileReadBackwards
from matplotlib import pyplot as plt
fh='cd-1-history'
count=0
cd=list()
itr=list()
itrlast=1000000
with FileReadBackwards(fh,encoding='utf-8') as cd_file:
    for line in cd_file:
        if float(line.split()[0])>itrlast:
            break
        if count==1001:
            break
        count=count+1
        if float(line.split()[0])==itrlast:
            count=count-1
        cd.append(float(line.split()[1]))
        itr.append(float(line.split()[0]))
        itrlast=float(line.split()[0])
itr.reverse(), cd.reverse()
plt.plot(itr,cd,label='cd')
avg_cd=sum(cd)/len(cd)
plt.plot([itr[0],itr[-1]],[avg_cd,avg_cd])
print('Cd avg over last',count,'iteration:', avg_cd)
plt.show()
