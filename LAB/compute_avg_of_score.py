def b_s_sum(b1score,b2score):
	#this program is used for getting sum of two boys score
	
	return b1score+b2score

def g_s_sum(g1score,g2score):
	#this program is used for getting sum of two girls score
	return g1score+g2score

def avg_score(b1score,b2score,g1score,g2score):
	
 
	'''this program will give avg score 
	of sum obtained by previous two program
	a=score of first boy
	b=score of second boy
	c=score of first girl
	d=score of second girl'''

	return (b_s_sum(b1score,b2score)+g_s_sum(g1score,g2score))/4

print(avg_score(45,34,49,23))

