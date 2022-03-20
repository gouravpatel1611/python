
# ------------USER INPUT -------------------------------------------------


print('\t~~ Welcome B.C.E. Project ~~')
point = int(input(("Enter the Total Number of Given Point :- ")))
changing_point = int(input(("Enter the Total Changing Point :- ")))
RL = float(input("Enter Your R.L. :- "))
# ~~~~~~~~~~~~~~ END ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ------------ MAKING SET ARRY-------------------------------------------------
changing_point_list = []
point_list = []

print("\n")
print("\t ~~ Enter Point ~~")
for i in range(1,point+1):
    temp = float(input(f"Enter point no.{i} :- "))
    point_list.append(temp)

print("\n")
print("\t ~~ Enter Changing Point ~~")

for i in range(1,changing_point+1):
    temp = int(input(f"Enter Changing point no.{i} :- "))
    changing_point_list.append(temp)
changing_point_list.append(len(point_list))

set_list = []
start_point = 0
for i in changing_point_list:
    set_list.append(point_list[start_point:i])
    start_point=i
    
print(set_list)
# ~~~~~~~~~~~~~~ END ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ------------ MAKING TABLE LIST -------------------------------------------------
table_list = []
st = [ "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","AA","BB","CC","DD","EE","FF","II"]
st_num = 0
temp = 0
temp_value = None
for item in set_list:
    for i in item:
        if temp_value == i:
            continue
        demo = {
            'Station': " ",
            'BS' : " ",
            'IS' : " ",
            'FS' : " ",
            'HI' : " ",
            'RL' : " ",
            'Remark' : " "
        }
        if st_num == 0:
            demo['Station'] = st[st_num]
            demo['BS'] = i
            demo['Remark'] = "BM"
            demo['RL'] = RL
            
        elif i == item[-1]:
            if set_list[-1][-1] == i:
                demo['Station'] = st[st_num]
                demo['FS'] = i
            else:
                demo['Station'] = st[st_num]
                demo['FS'] = i
                demo['BS'] = set_list[temp+1][0]
                demo['Remark'] = "CP"
                temp_value = set_list[temp+1][0]
                
        else:
            demo['Station'] = st[st_num]
            demo['IS'] = i
        st_num += 1
        table_list.append(demo)
        # 2nd loop end 
    temp += 1
# ~~~~~~~~~~~~~~ END ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    
    
# ------------ Calculate TABLE LIST -------------------------------------------------
value_of_HI = 0;
for item in table_list:
    if item['Remark'] == "BM":
        if item['BS'] != " " and item['RL'] != " ":
            item['HI'] = item['BS']+ item['RL']
            value_of_HI = item['BS']+ item['RL']
    else:
        if item['IS'] != " ":
            item['RL'] = value_of_HI - item['IS']
            
        elif item['FS'] != " ":
            item['RL'] = value_of_HI - item['FS']
            
        if item['BS'] != " " and item['RL'] != " ":
            item['HI'] = item['BS']+ item['RL']
            value_of_HI = item['BS']+ item['RL']
    # Loop End
    
# ~~~~~~~~~~~~~~ END ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# ------------ PRINTING  TABLE  -------------------------------------------------   
print("\n") 
print("---------|---------|---------|---------|---------|---------|--------|")
print ("{:<8} | {:<7} | {:<7} | {:<7} | {:<7} | {:<7} | {:<7}|".format("Station","BS","IS","FS","HI","RL","Remark"))   
print("---------|---------|---------|---------|---------|---------|--------|")


for item in table_list:
    station   = str(item['Station'])
    table_bs  = str(item['BS'] )[0:6]
    table_is  = str(item['IS'] )[0:6]
    table_fs  = str(item['FS'] )[0:6]
    table_hi  = str(item['HI'] )[0:6]
    table_rl  = str(item['RL'] )[0:7]
    table_rm  = str(item['Remark'])
    
    print ("{:<8} | {:<7} | {:<7} | {:<7} | {:<7} | {:<7} | {:<7}|".format(station,table_bs,table_is,table_fs,table_hi,table_rl,table_rm))
    print("---------|---------|---------|---------|---------|---------|--------|")
    
    
print("\n")
print("Value = ","{:.2f}".format(table_list[-1]['RL']-table_list[0]['RL']))
# ~~~~~~~~~~~~~~ END ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
