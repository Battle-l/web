import functools
def log(func=''): 
	def decorator(fn):
		@functools.wraps(fn)
		def wrapper(*args, **kw):
			print('begin %s' % func)
			f = fn(*args, **kw)
			print('end %s' % func)
			return f
		return wrapper
	return decorator

@log()
def a():
    print('hello')
 
@log('execute')
def b():
    print('hello,g')

a()
b()