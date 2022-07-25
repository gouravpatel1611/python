from tkinter import *

#----------------------------------------------
Start_point = (0,0)
end_point = (9,9)
sp = Start_point
box = 10
big_ls = []
f = []
path_dict = {}
value_dict = {}

def clear_screen():
    global big_ls,f,path_dict,value_dict
    big_ls = []
    f = []
    path_dict = {}
    value_dict = {}
#---------------------------------------------

for i in range(box):
    for j in range(box):
        value_dict[(i,j)] = 1



# text_update function
def text_updation(box):
    print(int(box[1]),int(box[3]))
    if value_dict_tk[box] == 1:
        button_dict[box].configure(bg='red') 
        value_dict_tk[box] = 0
        value_dict[(int(box[1]),int(box[3]))] = 0
    else:
        button_dict[box].configure(bg='#0052cc') 
        value_dict_tk[box] = 1
        value_dict[(int(box[1]),int(box[3]))] = 1


# maker ----------------------------
def make_path(s_point):
    path_dict[s_point] = []
    if s_point[0] -1 >=0 and value_dict[(s_point[0]-1,s_point[1])] ==1 :
        path_dict[s_point].append((s_point[0]-1,s_point[1]))

    if s_point[1] +1 <box  and value_dict[(s_point[0],s_point[1]+1)] ==1 :
        path_dict[s_point].append((s_point[0],s_point[1]+1))

    if s_point[0] +1 <box and value_dict[(s_point[0]+1,s_point[1])] == 1:
        path_dict[s_point].append((s_point[0]+1,s_point[1]))

    if s_point[1] -1 >=0 and value_dict[(s_point[0],s_point[1]-1)]==1:
        path_dict[s_point].append((s_point[0],s_point[1]-1))


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

def tr(pnt):
    snp = []
    if len(big_ls) >1:
        big_ls.pop()
        for i in big_ls[-1]:
            if pnt in path_dict[i]:
                snp.append(i)
                print(i)
                snp.sort()
        f.append(snp[0])
        me()
    else:
        print("done..........")
        print(pnt)
def me():
    tr(f[-1])


def run_app():
    for i in range(box):
        for j in range(box):
            make_path((i,j))
    big_ls.append(path_dict[end_point])
    check(path_dict[end_point])
    tr(sp)
    print((2,2),f,sp)
    button_dict[f'({sp[0]},{sp[1]})'].configure(bg='green')
    for i in f:
        button_dict[f'({i[0]},{i[1]})'].configure(bg='green')
    button_dict[f'({end_point[0]},{end_point[1]})'].configure(bg='green')
        

    


























# create root window
win = Tk()
  
# root window title and dimension
win.title("GeekForGeeks")
  
# Set geometry (widthxheight)

my_menu = LabelFrame(win , text='Mwnu')
my_menu.grid(row=0,column=0)

btn = Button(my_menu, text="Run", command= run_app)
btn.grid(row=0,column=0)

  

root = LabelFrame(win, text="daigram")
root.grid(row=1,column=0)
  
# create buttons
button_dict = {}
value_dict_tk = {}
# words = ["Py", "Java", "R", "JavaScript"]
words = []
for i in range(box):
    for j in range(box):
        words.append(f'({str(i)},{str(j)})')
        
for lang in words: 
    # pass each button's text to a function
    def action(x = lang): 
        return text_updation(x)
        
    # create the buttons 
    button_dict[lang] = Button(root, text = lang,command = action)
    button_dict[lang].grid(row=int(lang[1]),column=int(lang[3]),padx=2,pady=2) 
    button_dict[lang].configure(height = 3,width = 6,bg='#0052cc', fg='#ffffff') 
    value_dict_tk[lang] = 1
  
# Execute Tkinter
win.mainloop()