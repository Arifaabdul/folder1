
# 1.Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20
def summ():
    sum1=8+2+3+0+7
    return sum1
summ()




# 2. Write a function for below scenario. 
# Param has 1000 rupees, ramu contains 5 chocolates, param give 500 rupees to ramu,
# ramu contains 10 chocolates, param give 700 rupees to ramu, 
# ramu contains no chocolates param give 1000 rupees to ramu.

# 3.Write a function for below scenario 
# Big billon festival in amazon, bill amount on cloths more than 1000 rupees i will get 25% discount on bill.
# bill amount on cloths less than 500 rupess i will get 5% discount on bill.
# bill amount on cloths between 500  to 1000 rupess i will get 20% discount on bill
def amazon_offer(amount):
    if amount >1000:
        offer=amount*.25
        return offer
    elif amount <500:
        offer=amount*.5
        return offer
    elif amount >=500 or amount <=1000:
        offer=amount*.20
        return offer
    else:
        print("no offers availible")
amazon_offer(1100)

   

# 3.Write a function for below scenario 
# Big billon festival in amazon, the single formal shirt value is 1500,
# two shirts together buy(1+1 offer) shirts value is 1200
# bulk shirts together buy(1+2 offer) shirts vlaue is 1000
def formal_shirt(shirt):
    if shirt==1:
        print("shirt value is 1500")
    elif shirt==2:
        print("1+1 offer and shirt value is 1200")
    elif shirt>2:
        print("1+2 offer and shirt value is 1000")
    else:
        print("no offers available")
formal_shirt(2)




# 4.Write a Python program to reverse a string. 
# Sample String : "ramu"
# Expected Output : "umar"
ramu="ramu"[::-1]
print(ramu)




# 5. Write a Python function that takes a list and returns a new list with unique elements of the first list. 
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]
def myfunction():
    lst=[1,2,3,3,3,3,4,5]
    convt=set(lst)
    unq_vls=list(convt)    
    return unq_vls
myfunction()
    

