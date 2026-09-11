#code_challenge3

print("============================ITEM DETAILS============================")

item_type = input("Type of Item:")
weight = float(input("Weight (kg): ")) 
is_Fragile = input("Is the item fragile or not?:")
 
print("==============================SHIPPING==============================")

sender_name = input("Sender Name:") 
distance = float(input("Distance (km): ")) 
is_Express = input("Is the item express or not?:")
is_International = input("Is the item international or not?:") 

print("==============================COMPUTATION==============================")


base_cost = (weight*2.50) + (distance*0.15) 

if weight <= 2.0 and distance <= 100 and not is_Express and not is_International:
          total = 0.00

elif is_International and is_Express:
          total = (base_cost*1.40) + 50

elif is_Express or (is_International and weight > 20):
          total = (base_cost*1.20) + 25

elif weight > 30 or distance > 1000:
          total = base_cost + 30

else:
          total = base_cost


print("What is your name?:", sender_name)
print("What is your purchased item?:", item_type)
print("Is your item fragile?:", is_Fragile)
print("How heavy is your purchased item?:", weight)
print("How far is your location?:", distance)
print("Is your item need express?:", is_Express)
print("Is your item international?:", is_International)
print("Total price of purchased items: Php", total)