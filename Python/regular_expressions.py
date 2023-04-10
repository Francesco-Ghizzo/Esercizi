import re

'''
Compiling Regular Expressions

Regular expressions are compiled into pattern objects, which have methods for various operations such as searching for pattern matches or performing string substitutions.
'''

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')

matchObject = phoneNumRegex.search('My number is 415-555-4242.')

matchObject	# Out: <re.Match object; span=(13, 25), match='415-555-4242'>

'''
You can query the match object for information about the matching string. Match object instances also have several methods and attributes:
'''

re.match.group()	# Out: '415-555-4242'

'''
group() returns the substring that was matched by the RE.
'''

print(f"Phone Number found: {re.match.group()}")	# Out: Phone Number found: 415-555-4242

'''
Matching Multiple Groups with the Pipe

The | character is called a pipe. You can use it anywhere you want to match one of many expressions. For example, the regular expression r'Batman|Tina Fey' will match either 'Batman' or 'Tina Fey'.
When both Batman and Tina Fey occur in the searched string, the first occurrence of matching text will be returned as the Match object.
'''

regex = re.compile (r'Batman|Superman')

matchObject = regex.search('Batman and Superman')

matchObject.group()	# Out: 'Batman'

matchObject = regex.search('Superman and Batman')

matchObject.group()	# Out: 'Superman'

'''
You can find all matching occurrences with the findall() method:
'''

matchObject = regex.findall('Superman and Batman')

matchObject	# Out: ['Superman', 'Batman']

'''
Optional Matching with the Question Mark

Sometimes there is a pattern that you want to match only optionally. That is, the regex should find a match regardless of whether that bit of text is there. The ? character flags the group that precedes it as an optional part of the pattern:
'''

regex = re.compile(r'Bat(wo)?man')

matchObject = regex.search('The Adventures of Batman')

matchObject.group()	# Out: 'Batman'

matchObject = regex.search('The Adventures of Batwoman')

matchObject.group()	# Out: 'Batwoman'

'''
Matching Zero or More with the Star

The * (called the star or asterisk) means “match zero or more”—the group that precedes the star can occur any number of times in the text. It can be completely absent or repeated over and over again.
'''

regex = re.compile(r'Bat(wo)*man')

matchObject = regex.search('The Adventures of Batman')

matchObject.group()	# Out: 'Batman'

matchObject = regex.search('The Adventures of Batwoman')

matchObject.group()	# Out: 'Batwoman'

matchObject = regex.search('The Adventures of Batwowoman')

matchObject.group()	# Out: 'Batwowoman'

'''
Matching One or More with the Plus

While * means “match zero or more,” the + (or plus) means “match one or more.” Unlike the star, which does not require its group to appear in the matched string, the group preceding a plus must appear at least once.
'''
