# foo = [2,18,9,22,17,24,8,12,27]
# print filter(lambda x:x%3 == 0,foo)

# print map(lambda x:x*2+10,foo)

# print reduce(lambda x,y:x+y,foo)

# for i in range(10):
# 	print i

import api

@api.onchange('a')
def func():
	print '1'

# func()

# def func(param):
# 	if param > 1 and param % 1 != 0:
# 		print 'error'
# print '2.5'
# func(2.5)
# print '2'
# func(2)
# print '0.5'
# func(0.5)
# from datetime import datetime
# import datetime as dt

# # print date.today()

# # print date('2015-6-1')

# print 8/7*7

# date_obj = datetime(2016,1,2)
# print date_obj.weekday()

# print date_obj+dt.timedelta(days=-date_obj.weekday())
# print dt.datetime.utcnow()
# print dt.datetime.now()


# import re  
# inputStr="hello python,ni hao c,zai jian python"  
# replaceStr=re.sub(r"hello (\w+),ni hao (\w+),zai jian \1","PHP",inputStr)  
# print replaceStr  

# @api.onchange('hello')
# def func():
# 	print 'do something'

# import collections
# print 'Regular dictionary:'
# d = {}
# d['a'] = 'A'
# d['b'] = 'B'
# d['c'] = 'C'
# d['d'] = 'D'
# d['a1'] = 'A1'
# d['b1'] = 'B1'
# d['c1'] = 'C1'
# d['d1'] = 'D1'
# for k, v in d.items():
#   print k, v
# print '\nOrderDict:'
# d = collections.OrderedDict()
# d['a'] = 'A'
# d['b'] = 'B'
# d['c'] = 'C'
# d['d'] = 'D'
# for k, v in d.items():
#   print k, v

class A():
	pass

	@staticmethod
	def check(cls,*args):
		print cls,args

func = A().check

print func

func(1,2,3)
