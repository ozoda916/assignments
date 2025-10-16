


customer_name = "Alex Johnson"
dish_1_name = 'lavash'
dish_1_price = 25000
dish_1_quantity = 2



dish_2_name = 'gamburg'
dish_2_price = 8000
dish_2_quantity = 1


dish_3_name = 'cola'
dish_3_price = 5000
dish_3_quantity = 3

has_student_ID = 'yes'
order_time = 16

subtotal = (dish_1_price * dish_1_quantity) + (dish_2_price * dish_2_quantity) + (dish_3_price * dish_3_quantity) 
happy_hour_eligible = 14 <= order_time <= 17
student_discount_eligibility = has_student_ID == 'yes' # True if 'yes', False if 'no'
student_discount = student_discount_eligibility * subtotal * 15 / 100
student_discount_amount =  student_discount_eligibility*subtotal*0.15 == 'yes'
happy_hour_discount = subtotal*0.20*happy_hour_eligible
large_order_eligible = subtotal >=150000
 # find out if it is eligible
large_order_discount =(subtotal > 150000) * subtotal * 0.05 

all_discounts = student_discount + happy_hour_discount + large_order_discount 


main_discount = student_discount * (student_discount >= happy_hour_discount) + happy_hour_discount * (happy_hour_discount > student_discount)
which_discount_applied = "student_discount" * (student_discount >= happy_hour_discount) + "happy_hour_discount" * (happy_hour_discount > student_discount)

total_discount = main_discount + large_order_discount
subtotal_after_discount = subtotal - total_discount

service_charge = subtotal_after_discount * 0.1        #fix
delivery_fee = (subtotal < 100000)*15000

final_total = subtotal_after_discount + delivery_fee + service_charge
total_amound_saved = total_discount
total_discount = main_discount + large_order_discount



 



print("==========================================")
print("                 RECEIPT               ")
print("==========================================")

print(f' costumer name: {customer_name} ')
print(f'has student id: {has_student_ID} ')
print(f'Order time: {order_time}: ')

print("==========================================")
print('-- Ordered Items --')
print("==========================================")

print(f' All 3 orders: {dish_1_name} ; {dish_2_name} ; {dish_3_name} ')
print(f'subtotal before discounts: {subtotal} ')
print(f'Student discount eligible: {has_student_ID == "yes"} {student_discount} ')
print(f'Happy hour eligible: {14<=order_time<=17} {happy_hour_discount} ')
print(f'Applied discount: {which_discount_applied} {main_discount}')
print(f'Large order eligible: {subtotal>=150000} {large_order_discount} ')
print(f'total discount: {total_discount} ')
print(f'subtotal after discount: {subtotal - total_discount} ')
print(f'service charge amount: {service_charge} ')
print(f'delivery fee: {delivery_fee} (fee delivery: {subtotal >=100000})')
print(f'{subtotal < 100000 }', '0', {delivery_fee} )
print(f"final total: {final_total}")
print(f'total amount saved:  {total_amound_saved}')

print(f'Thank you 😊' )




