import re

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')

matchObject = phoneNumRegex.search('My number is 415-555-4242.')

matchObject	# <re.Match object; span=(13, 25), match='415-555-4242'>

re.match.group()	# '415-555-4242'

print(f"Phone Number found: {re.match.group()}")	# Phone Number found: 415-555-4242