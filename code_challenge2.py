money = eval(input("Enter Money to DEPOSIT ---->>> ")) #int(), eval(), type() 
#print(type(money))
print("========================= PH BANK DENOMINATION ========================== ")
print("MONEY TO DEPOSIT ------------> ", money, "php")
 

#computation here

thous = money // 1000
money = money % 1000

f_hundred = money // 500
money = money % 500

t_hundred = money // 200
money = money % 200

fifty = money // 50
money = money % 50

five = money // 5
money = money % 5

one = money // 1
money = money % 1

print("1000  :", thous)
print("500   :", f_hundred)
print("200   :", t_hundred)
print("50    :", fifty)
print("5     :", five)
print("1     :", one)
