'''
Problem
Given four integers. Determine if there exists a binary string having  0's and  1's
such that the total number of subsequences equal to the sequence "01" in it is a and
the total number of subsequences equal to the sequence "10" in it is b.

A binary string is a string made of the characters '0' and '1' only.

A sequence  is a subsequence of a sequence  if  can be obtained from  by deletion of several (possibly, zero or all) elements.

Input Format

The first line contains a single integer  (), denoting the number of test cases.

Each of the next  lines contains four integers , ,  and  ((, ()), as described in the problem.

Output Format

For each test case, output "Yes'' (without quotes) if a string with given conditions exists and "No'' (without quotes) otherwise.

Sample Input       Sample Output
3 2 4 2               Yes
3 3 6 3               Yes
3 3 4 3               No

Explanation
When x, y, a and b are 3, 2, 4 and 2 respectively, string 00110 is a valid string. So answer is Yes

When x, y, a and b are 3, 3, 4 and 3 respectively, we can't find any valid string. So answer is No.
'''
def bin_str(x, y, a, b):
	'''
	here we have to search a times '01' in string also after deleting some elements b/w them
	and we have to search b times '10' in string also after deleting some elements b/w them
	'''
	string = '0'*x+'1'*y

