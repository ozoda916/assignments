
# Collect: Dish name, price, and quantity for 3 dishes
# Get customer information: Name, has_student_id (yes/no),
# order_time (hour in 24-hour format, e.g., 14 for 2 PM)
customer_name = ('Enter you Customer_name: ')
dish_1_name = 'lavash'
dish_1_price = 20000
dish_1_quantity = 3



dish_2_name = 'gamburg'
dish_2_price = 8000
dish_2_quantity = 2


dish_3_name = 'cola'
dish_3_price = 12000
dish_3_quantity = 1




# has_student_ID = input('Enter has_student_ID: ')
has_student_ID = 'yes'

# order_time (hour in 24-hour format, e.g., 14 for 2 PM)
order_time = 18

subtotal = dish_1_price * dish_1_quantity + dish_2_price * dish_2_quantity + dish_3_price * dish_3_quantity

student_discount_eligibility = has_student_ID == 'yes' # True if 'yes', False if 'no'
student_discount_amount = student_discount_eligibility * subtotal * 15 / 100

subtotal_after_student_discount = subtotal - student_discount_amount 



happy_hour_discount_eligibility =  order_time >=14 and order_time <=17
happy_hour_discount_amount = happy_hour_discount_eligibility * subtotal * 0.2

happy_hour_discount = subtotal* 20 / 100 == order_time >=14 , order_time <=17
student_discount_amount = subtotal*0.15 == 'yes'
student_discount_amount = subtotal*0.15 == 'NO'


large_order_eligible = subtotal >=150000

# subtotal = subtotal*0.20 - student_discount_amount == order_time >= 14 , order_time <= 17

large_order_discount = 0.05*subtotal
large_order_eligible = subtotal >=150000

applied_discount =student_discount_amount + happy_hour_discount_amount + large_order_discount
student_discount = 0.15*subtotal
main_discount = student_discount * (student_discount_amount >= happy_hour_discount) +  (happy_hour_discount)

service_charge = subtotal*0.1
delivery = (subtotal >= 100000) * 15000
if subtotal < 100000:
    delivery_free = 0
    free_delivery = True
else: 
    delivery_free = 15000
    free_delivery = False

final_total = subtotal_after_student_discount + service_charge + delivery_free
total_discounts = main_discount + large_order_discount
total_saved = total_discounts


# ------------------------------------------------
# Output
# ----------------------------------------------
print("==========================================")
print("                 RECEIPT               ")
print("==========================================")
print(f' costumer name: {customer_name} ')
print(f'has student id: {has_student_ID} ')
print(f'Order time: {order_time}: ')

print('-- Ordered Items --')

print(f' All 3 orders: {dish_1_name} ; {dish_2_name} ; {dish_3_name} ')
      

print(f"\nSubtotal (before discounts): {subtotal: ,}')sum\n")
print("--- Discounts ---")
print(f'student discount eligible: {student_discount_eligibility} | Amount: {student_discount_amount: ,.0f}sum')
print(f'Happy hour eligible: {happy_hour_discount_eligibility} | Amount: {main_discount:,.0f}sum')

print(f'applied main discount: {applied_discount}')
print (f'total discounts: {subtotal:,.0f}')

print('---   charges ---')

print(f'subtotal after discounts: {subtotal_after_student_discount:, }')
print(f'service charge (10%): {service_charge:,.0f} sum')
print(f'Delivery free:{delivery:,.0f} sum')

print(f'final total: {final_total:,.0f} sum')
      
print(f'total amount saved; {total_saved:,.0f} sum')
print('==========================================')
