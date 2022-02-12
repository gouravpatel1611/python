table_list = [{'Station': 'A', 'BS': 2.665, 'IS': ' ', 'FS': ' ', 'HI': ' ', 'RISE': ' ', 'FALL': ' ', 'RL': 240.0, 'Remark': 'BM'}, {'Station': 'B', 'BS': ' ', 'IS': 3.225, 'FS': ' ', 'HI': ' ', 'RISE': ' ', 'FALL': ' ', 'RL': ' ', 'Remark': ' '}, {'Station': 'C', 'BS': 1.85, 'IS': ' ', 'FS': 2.905, 'HI': ' ', 'RISE': ' ', 'FALL': ' ', 'RL': ' ', 'Remark': 'CP'}, {'Station': 'D', 'BS': ' ', 'IS': 0.98, 'FS': ' ', 'HI': ' ', 'RISE': ' ', 'FALL': ' ', 'RL': ' ', 'Remark': ' '}, {'Station': 'E', 'BS': 1.585, 'IS': ' ', 'FS': 2.62, 'HI': ' ', 'RISE': ' ', 'FALL': ' ', 'RL': ' ', 'Remark': 'CP'}, {'Station': 'F', 'BS': ' ', 'IS': 0.96, 'FS': ' ', 'HI': ' ', 'RISE': ' ', 'FALL': ' ', 'RL': ' ', 'Remark': ' '}, {'Station': 'G', 'BS': ' ', 'IS': ' ', 'FS': 0.425, 'HI': ' ', 'RISE': ' ', 'FALL': ' ', 'RL': ' ', 'Remark': ' '}]
set_list = [[2.665, 3.225, 2.905], [1.85, 0.98, 2.62], [1.585, 0.96, 0.425]]
RL = 240

value_of_HI = 0;
pre_item = ""
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

temp_for_itm = 0
temp_num = 1
for itm in set_list:
    t_n_c = 0
    for point in itm:
        if t_n_c != 0:
            r_f = round(temp_for_itm-point,3)
            if r_f < 0:
                table_list[temp_num]['FALL'] = r_f*-1
            else:
                table_list[temp_num]['RISE'] = r_f
                
            temp_num += 1
        t_n_c += 1
        temp_for_itm = point


            
print("\n")