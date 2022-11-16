# Q1: What is the output of the following code?
# var = "James" * 2  * 3
var = "James" * 2  * 3
var


# Q2: Create a list (month_lst) with month names and print values  as "this is month of January" 
lst=["january","febraury","march","april","may","june","july","august","september","october","november","december"]
for months in lst:
    var="this is month of "+months
    print(var)
    
    

# Q3: Create a tuple (year_tup) with years from 19470 to 2022
years=[1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990]
lst1=[]
for year in years:
    lst1.append(year)
    print(lst1)
    tup=tuple(lst1)    
tup 


   

# Q3: Create a set (flowers_set) with Colors names at least 5 colors names
colours=["red","pink","yellow","maroon","blue","green","brown"]
set_lst=[]
for colour in colours:
    set_lst.append(colour)
    print(set_lst)
    sett=set(set_lst)
sett


# Q4: create a dict with your friends names and his/her quality like (funny, intelligent, smart etc)
# ex:ex:  {"friend_name": "Thirish" , "Quality": "Smart"}
dictt={"friend_name":"keerthi" , "Quality":"Smart" , "friend_name":"padmavathi" , "Quality":"intelligent", "friend_name":"sweety" , "Quality":"intelligent" , "friend_name":"pravallika" , "Quality":"smart"}
dictt["friend_name"]


# Q5: Create a dict with family members names and relations
# ex:  {"family_member": "venkatrao" , "relation": "Father"}
dicct={"family_member": "abdul samad" , "relation": "Father","family_member": "aktharunnisa" , "relation": "Mother", "family_member": "abdul anwar" , "relation": "Brother"}
dicct["family_member"]




