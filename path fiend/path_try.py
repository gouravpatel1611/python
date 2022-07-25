
Start_point = (0,0)
end_point = (2,2)



path_dict = {}
value_dict = {}
for i in range(5):
    for j in range(5):
        value_dict[(i,j)] = 1
print(value_dict)
# value_dict[(0,1)] = 0
# value_dict[(1,1)] = 0
# value_dict[(2,1)] = 0
# value_dict[(3,1)] = 0
def make_path(s_point):
    path_dict[s_point] = []
    if s_point[0] -1 >=0 and value_dict[(s_point[0]-1,s_point[1])] ==1 :
        path_dict[s_point].append((s_point[0]-1,s_point[1]))

    if s_point[1] +1 <5  and value_dict[(s_point[0],s_point[1]+1)] ==1 :
        path_dict[s_point].append((s_point[0],s_point[1]+1))

    if s_point[0] +1 <5 and value_dict[(s_point[0]+1,s_point[1])] == 1:
        path_dict[s_point].append((s_point[0]+1,s_point[1]))

    if s_point[1] -1 >=0 and value_dict[(s_point[0],s_point[1]-1)]==1:
        path_dict[s_point].append((s_point[0],s_point[1]-1))

for i in range(5):
    for j in range(5):
        make_path((i,j))

print(path_dict[(2,2)])

big_ls = []
sp = Start_point


def snd():
    check(big_ls[-1])

def check(lst):
    ls = []
    if sp in lst :
        print("yes",lst)
    else:
        for i in lst:
            print("-----------------> list",i)
            for k in path_dict[i]:
                ls.append(k)
            print("ls ==> ",list(set(ls)))
        big_ls.append(list(set(ls)))
        print('**************************')
        snd()

big_ls.append(path_dict[end_point])
check(path_dict[end_point])
print(big_ls)

f = []
def tr(pnt):
    snp = []
    if len(big_ls) >1:
        big_ls.pop()
        for i in big_ls[-1]:
            if pnt in path_dict[i]:
                snp.append(i)
                print(i)
        print("gourav",snp)
        f.append(snp[0])
        me()
    else:
        print("done..........")
        print(pnt)
def me():
    tr(f[-1])

tr(sp)
print((2,2),f,sp)