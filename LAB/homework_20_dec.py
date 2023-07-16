# # homework_20_dec

# # 1. Given 3 numbers, check if they add up to 21.
# def check_to_21(a,b,c):
# 	return a+b+c == 21


# # 2. Given input as day of week “Monday” etc, write a function that returns true if this is a weekday.

# def weekday(s):
# 	return not s.lower()=='wednesday'

# # print(weekday('sunday'))	
# # Now write another function that returns alarm time 7 AM for weekday and 9 AM for weekend
# def alarm(s):
# 	return '7 AM' if weekday(s) else '9 AM'

# # print(alarm('sunday'))	

# # 3. The number 6 is a truly great number. Given two int values, a and b,
# # return True if either one is 6. Or if their sum or difference is 6.
# # Note: the function abs(num) computes the absolute value of a number.
# # love6(6, 4) → True
# # love6(4, 5) → False
# # love6(1, 5) → True

# def love6(a,b):
# 	return a == 6 or b == 6 or a+b == 6 or abs(a-b) == 6
# # print(love6(5, 1))

# # 4. Given 2 numbers, radius1 and radius2, calculate the area of two circles.
# # If area of circle 1 + area of circle 2 : greater than 100 return "HIGH"
# # less than or equal to 100 and greater than 50 return "MEDIUM"
# # less than or equal to 50 return "LOW"
# import math
# def area_sum(radius1,radius2):
# 	total_area=math.pi*(radius1**2)+math.pi*(radius2**2)
# 	if total_area > 100:
# 		return 'HIGH'
# 	elif total_area > 50:
# 		return 'MEDIUM'
# 	else:
# 		return 'LOW'
# print(area_sum(3,4))


# # 5. Given 3 angles of a triangle as input, print if the triangle is “Acute”, “Obtuse”, “Right-Angled”, “Invalid”
# def triangle(a,b,c):
# 	M=max(a,b,c)
# 	if a+b+c == 180
# 		if a <= 0 or a <= 0 or a <= 0:
# 			print('invalid')
# 		elif M > 90:
# 			print('obtuse')
# 		elif M == 90:
# 			print('Right-Angled')
			
# 		else:
# 			print('Acute')
# 	else:
# 		print('invalid')		
# print(triangle(60,30,90))
