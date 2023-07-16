import Ranjan_a1
old=input('Enter original currency: ')
new=input('Enter desired currency: ')
amt=float(input('Enter original amount: '))

# if the source currency is not valid, quit
if(not(Ranjan_a1.is_currency(old))):
	print(old," is not a valid currency")
	quit()
# if the target currency is not valid, quit
if(not(Ranjan_a1.is_currency(new))):
	print(new," is not a valid currency")
	quit()
else:
	print('You can exchange',amt,old,'for',Ranjan_a1.exchange(old,new,amt),new)
