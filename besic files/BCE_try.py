

RL= 100

table_list = []
set_list = [[2.65, 1.745, 0.625, 0.26], [2.525, 2.16, 1.235, 0.87, 1.365], [0.625, 1.79, 2.535]]

st = [ "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
st_num = 0
temp = 0
temp_value = " "
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

    
    
    
    
    