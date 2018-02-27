from collections import defaultdict

# d = defaultdict(int)
# d = defaultdict(list)
# print d['k']

# class Missing(dict):
# 	def __missing__(self, key):
# 		self[key] = 'mis'
# 		return 'missing'


# d = Missing()
# d['a']
# print d

data = [('a', 1),('b', 2),('b', 3)]
d = defaultdict(int)
for k, v in data:
	print k, v 
	d[k] += 1

print d