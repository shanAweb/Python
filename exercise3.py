payment=1000000
good_credit=True
if good_credit:
    down_payment=(10/100)*payment
else:
    down_payment=(20/100)*payment
print(f'Down payment is: {down_payment}')
