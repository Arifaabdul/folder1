# problem1: 
# create a list, value range 30-70

lst=[]
for s in range(30,71):
    print(s)
    lst.append(s)
    print(lst)
lst
    
# create a tuple,value range 70-120
lst2=[]
for s in range(70,121):
    print(s)
    lst2.append(s)
    print(lst2)
    tup= tuple(lst2)
    print(tup)
tup    
    
# create a set, value range 130-170
lst_set=[]
for s in range(130,171):
    print(s)
    lst_set.append(s)
    print(lst_set)
    set_new=lst_set
    sett=set(set_new)

sett

    
# problem2:
# create a list, values- month(january,feburary etc) name 

months='January',' February',' March',' April',' May',' June',' July',' August',' September',' October',' November',' December'
lst_months=[]
for s in months:
    print(s)
    lst_months.append(s)
    
lst_months    

#create a tuple,value with week(sunday,monday etc) names
weeks='Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'
lst4=[]
for s in weeks:
    print(s)
    lst4.append(s)
    print(lst4)
    weeks_tup=tuple(lst4)
    print(weeks_tup)

weeks_tup

#create a set, value with season(winter,summer etc) names
seasons='summer','rainy','winter'
set_lst=[]

for s in seasons:
    print(s)
    set_lst.append(s)
    print(set_lst)
    set_new1=set_lst
    sesn_set=set(set_new1)
sesn_set

# problem3: 
# create a list, values- India all state names
states='Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu Kashmir','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal'

states_lst=[]

for s in states:
    print(s)
    states_lst.append(s)

states_lst

#create a tuple,values- color names
colr_nms='red','green','yellow','blue','pink','white','maroon'
colr_lst=[]

for s in colr_nms:
    print(s)
    colr_lst.append(s)
    print(colr_lst)
    nms_tup=tuple(colr_lst)
    print(nms_tup)
nms_tup

#create a set, values- flower names
flowers='rose','jasmine','lotus','lily','sunflower'
flwr_lst=[]

for s in flowers:
    print(s)
    flwr_lst.append(s)
    print(flwr_lst)
    set_new=flwr_lst
    flwr_set=set(set_new)
    
flwr_set    
    
# problem4:
# P4Q1: 
# input=["Jan","Feb","Mar","Apr","Maye"]
# Maye replace with May
# output=["Jan","Feb","Mar","Apr","May"] 
   
prb4_lst=["Jan","Feb","Mar","Apr","Maye"]  

prb4_lst[4]="may"    
prb4_lst

# P4Q2: 
# input=["Jan","Feb","Mar","Apr","May"]
# output=["Jan","Feb"]

prb4_2=["Jan","Feb","Mar","Apr","May"]

prb4_2_new=prb4_2[0:2]
prb4_2_new

# P4Q3: 
# input=["Jan","Feb","Mar","Apr","May"]
# output=["Feb","Mar","Apr"]

prb4_3=["Jan","Feb","Mar","Apr","May"]

prb4_3_new= prb4_3[1:4]
prb4_3_new

# P4Q4: 
# input=["Jan","Feb","Mar","Apr","May"]
# output=["Apr"]

prb4_4=["Jan","Feb","Mar","Apr","May"]

prb4_4_new= prb4_4[3:4]
prb4_4_new

# P4Q5: 
# input=["Jan","Feb","Mar","Apr","May"]
# output=["Jan"]

prb4_5=["Jan","Feb","Mar","Apr","May"]

prb4_5_new= prb4_5[0:1]
prb4_5_new

# P4Q6: 
# input=["Jan","Feb","Mar","Apr","May"]
# output=["May"]

prb4_6=["Jan","Feb","Mar","Apr","May"]

prb4_6_new= prb4_6[4:5]
prb4_6_new

# problem5:
# P5Q1: 
# input=["Jan","Feb","Mar","Apr",Apr","Maye"]
# output=["Jan","Feb","Mar","Apr","Maye"]

prb5_1=["Jan","Feb","Mar","Apr","Apr","Maye"]

prb5_1_new=set(prb5_1)
prb5_1_new

# P5Q2: 
# input=["Jan","Feb","Feb","Feb","Mar","Apr","May"]
# output=["Jan","Feb"]

prb5_2=["Jan","Feb","Feb","Feb","Mar","Apr","May"]

prb5_2_new= prb5_2[0:2]
prb5_2_new

# P5Q3: 
# input=["Jan","Feb","Mar","Feb","Mar","Feb","Mar","Apr","May"]
# output=["Feb","Mar","Apr"]

prb5_3=["Jan","Feb","Mar","Feb","Mar","Feb","Mar","Apr","May"]

prb5_3_new= prb5_3[5:8]
prb5_3_new
