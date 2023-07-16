def is_major(dob_d,dob_m,dob_y):

	'''this program will help the user to select the require 
	candidate from different qualities 
	dob_d=age in day
	dob_m=age in month
	dob_y=age in year



	is_major(9,7,2007)
	>>> false
	is_major(4,1,2007)
	>>>false
	is_major(9,7,2001)
	>>>true

	'''
	return dob_y < 2004 or dob_y == 2004 and (dob_m < 11 or dob_m == 11 and dob_d <= 4)


def is_eligible(dob_d,dob_m,dob_y,gender):
	''' this program checks eligibility of a person
	dob_d=age in day
	dob_m=age in month
	dob_y=age in year
	gender=gender of person


	is_eligible(9,7,2007''male')
	>>> true
	is_eligible(9,7,2007,'female')
	>>> false
	is_eligible(13,5,2001,'female')
	>>> true
	
	'''
	return gender == 'male' or is_major(dob_d,dob_m,dob_y)

is_eligible(20,8,2005,'male')
print(is_eligible(20,8,2005,'male'))
print(is_eligible(20,8,2005,'female'))



# def is_major(dob_d,dob_m,dob_y):

# 	'''this program will help the user to select the require 
# 	candidate from different qualities 
# 	dob_d=age in day
# 	dob_m=age in month
# 	dob_y=age in year'''
# 	return(dob_y<2004 or dob_y==2004 and (dob_m<11 or dob_m==11 and dob_d<=4))


# def is_eligible(dob_d,dob_m,dob_y,gender):
# 	''' this program checks eligibility of a person
# 	dob_d=age in day
# 	dob_m=age in month
# 	dob_y=age in year
# 	gender=gender of person '''
# 	return(gender=='male' or is_major(dob_d,dob_m,dob_y))

# is_eligible(20,8,2005,'male')
# print(is_eligible(20,8,2005,'male'))
# print(is_eligible(20,8,2005,'female'))
