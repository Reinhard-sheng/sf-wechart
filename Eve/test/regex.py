import re

regex_private = re.compile(r'^(_.*|init)$')

print regex_private.match('init').group()