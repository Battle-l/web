class Chain(object):

	def __init__(self, path=''):
		self._path = path

	def __getattr__(self, path):
		return Chain('%s/%s' % (self._path, path))

	def __str__(self):
		return self._path

	#def __call__(self):
	#	return Chain()
	__call__ = __getattr__
	__repr__ = __str__
	
print('%s'%(Chain().status.user.timeline.list))
print('%s'%(Chain().users('michael').repos))