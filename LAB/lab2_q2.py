# ye function naye use ke liye hai

print('%0.2f'%(4/3))
# result is:1.33              (yaha result me character ke taraf se bound nahi hai)
print('%10.2f'%(4/3))
# result is:      1.33        (yaha result me 10 character hai) 
print('%0.2f'%(4/3))
# result is:1.33              (yaha result me decimal ke bad 2 digit hai)
print('%0.4f'%(4/3))
# result is:1.3333            (yaha result me decimal ke bad 4 digit hai)



# use of format
print('the number is {}'.format(4))
# result is: the number is 4
print('the number is {},{},{},{},{},{},{},{}'.format(4,5,1,2,3,4,5,5))
# result is:the number is 4,5,1,2,3,4,5,5

# yahi kam f-string bhi karta hai 
print(f'the number is {7}')
# result is:the number is 7

# import calendar
# cal = calendar.Calendar()
# for x in cal.itermonthdays2(2023, 2):
#   print(x)
#   print(type(x[1]))

# try:
#   1/0
# # try:
# #   2/0
# except:
#   print(3)    

print(hash((1,2,3)))

l= []
l.append(2,)
print(l)


print('%0.0f'%(1234.5))