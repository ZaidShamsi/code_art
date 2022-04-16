from matplotlib import pyplot as plt

fh=open('plot.txt')

count=0
variable_values_dict={}

for line in fh:
    count=count+1
    if count==1:
        variable_names_lst=line.split()
        for name in variable_names_lst:
            variable_values_dict[name]=[]
    else:
        key_count=0
        for key in variable_values_dict.keys():
            variable_values_dict[key].append(line.split()[key_count])
            key_count=key_count+1

plot_dict=variable_values_dict
print(list((plot_dict.keys())))

plt.xlabel('Coefficient of drag (Cd)')
plt.ylabel('Coefficient of lift (Cl)')
plt.xlim(.004,.040)
plt.ylim(-.2,1.4)
plt.plot(plot_dict[list(plot_dict.keys())[1]],plot_dict[list(plot_dict.keys())[0]],'b^',label='Jenkins')
#plt.plot(var3,var2,'g^',label='solver')
plt.legend()

plt.show()
