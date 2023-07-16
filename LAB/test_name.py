""" This script tests the module name"""

import name		# The module we want to test
import introcs 	 	# Includes the test procedures


# First test case
result = name.last_name_first('Sitare University')
introcs.assert_equals('University, Sitare', result)
    
# Second test case
result = name.last_name_first('Sitare            University')        
introcs.assert_equals('University, Sitare', result)

print('Module name is working correctly')
