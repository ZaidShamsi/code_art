from matplotlib import pyplot as plt

fh=open('project_twitter_data.txt')

count=0
var0=list()
var1=list()
#var2=list()
#var3=list()

for line in fh:
    try:
        float(line.split(',')[0])
    except:
        continue
    var0.append(float(line.split(',')[4].rstrip()))
    var1.append(float(line.split(',')[0]))
fh.close()
print(var0)
'''
var0=[x/0.228363965 for x in var0]
img=plt.imread('img_Cp_1point51.png')
plt.imshow(img,extent=[0,1,2,-3],aspect='auto')
plt.title('3D Simulation\nAoA 1.51\u00b0')
plt.xlabel('x/c')
plt.ylabel('Coefficient of pressure (Cp)')
plt.xlim(0,1)
plt.ylim(2,-3)
plt.plot(var0,var1,'go',ms=1.5,label='solver')
'''
plt.xlabel('Net Score')
plt.ylabel('Number of Retweets')
plt.title('Net Positive Score, \u2192 Many Retweets\u2191 ')
plt.plot(var0,var1,'bo',ms=3,label='Number of Retweets')
plt.legend()

plt.show()
