import time

"""
Caesar-Cypher Program
"""
"""
Linked-List Implementation; Allows for mutation of objects
"""
class Link:
    """A linked list.

    >>> s = Link(3, Link(4, Link(5)))
    >>> len(s)
    3
    >>> s[2]
    5
    >>> s
    Link(3, Link(4, Link(5)))
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

    def __len__(self):
        return 1 + len(self.rest)

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(self.first, rest_str)

"""
String to Linked-List Implementation
"""

def converter(string):
	if not string:
		return Link.empty
	return Link(string[0], converter(string[1:]))

"""
Caesar-Cypher Encryptor; Transforms every letter in the linked-list by a set numerical value; Mutates the Linked-List
"""

def encryptor(link, value):
    if link is Link.empty:
        return
    link.first = chr(ord(link.first) + value)
    return encryptor(link.rest, value)

"""
Linked-List Implementation to String
"""

def deconverter(link):
    empty_string = ""
    def deconverter_helper(link):
        nonlocal empty_string
        while link is not Link.empty:
            empty_string = empty_string + link.first
            link = link.rest
        return empty_string
    return deconverter_helper(link)


"""
Ceasar-Cypher Decryptor; Transforms every letter in the linked-list back to the original set of letters
"""

def decryptor(link, value):
    if link is Link.empty:
        return
    link.first = chr(ord(link.first) - value)
    return decryptor(link.rest, value)

"""
Caesar-Cypher Program
"""


string = str(input('Enter your message:').replace(' ', ''))
value = int(input('Enter the value you want to shift by:'))


def caesar_cypher(string, value):
    try:
        converted_string = converter(string)
        encryptor(converted_string, value)
        converted_string = deconverter(converted_string)
        print("Here is your encoded message!")
        print("-->" + converted_string + "<--")
    except TypeError:
        print("Ensure that your value is an integer!")

    
caesar_cypher(string, value)















