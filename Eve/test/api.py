def onchange(*args):
	print attrsetter('_onchange',args)
	return attrsetter('_onchange',args)

def attrsetter(attr,value):
	print 'attr',attr
	print 'value',value
	return lambda method: method
	return lambda method: setattr(method,attr,value) or method
