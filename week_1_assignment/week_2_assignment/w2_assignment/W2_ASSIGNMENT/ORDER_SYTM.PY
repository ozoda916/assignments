


customer_name = input('Enter you Customer name: ')
dish_1_name = 'lavash'
dish_1_price = 20000
dish_1_quantity = 3



dish_2_name = 'gamburg'
dish_2_price = 8000
dish_2_quantity = 2


dish_3_name = 'cola'
dish_3_price = 12000
dish_3_quantity = 1

has_student_ID = 'yes'
order_time = 12

subtotal = (dish_1_price * dish_1_quantity) + (dish_2_price * dish_2_quantity) + (dish_3_price * dish_3_quantity)
student_discount_eligibility = has_student_ID == 'yes' # True if 'yes', False if 'no'
student_discount = student_discount_eligibility * subtotal * 15 / 100
student_discount_amount = subtotal*0.15 == 'yes'
happy_hour_discount = subtotal*0.20
large_order_discount = subtotal*0.05
subtotal_after_discount = student_discount + happy_hour_discount + large_order_discount

main_discount = student_discount * (student_discount >= happy_hour_discount) + happy_hour_discount * (happy_hour_discount > student_discount)

service_charge = subtotal*0.1
delivery = (subtotal >= 100000) * 15000
final_total = subtotal_after_discount + delivery + service_charge
total_amound_saved = {subtotal} - {subtotal_after_discount}
total_discount = 15 +20 + 5
print("==========================================")
print("                 RECEIPT               ")
print("==========================================")

print(f' costumer name: {customer_name} ')
print(f'has student id: {has_student_ID} ')
print(f'Order time: {order_time}: ')

print('-- Ordered Items --')

print(f' All 3 orders: {dish_1_name} ; {dish_2_name} ; {dish_3_name} ')
print(f'subtotal before discounts: {subtotal} ')
print(f'{has_student_ID == "yes"} {student_discount} ')
print(f'{14<=order_time<=17} {happy_hour_discount} ')
print(f'{subtotal>=150000} {large_order_discount} ')
print(f'total discount: {total_discount} ')
print(f'subtotal after discount: {subtotal_after_discount} ')
print(f'service charge amount: {service_charge} ')
print(f'{subtotal < 100000 }', '0', {delivery} )
print(f"final total: {final_total}")
print(f'total amount saved: {total_amound_saved} ')

print(f'Thank you 😊' )




