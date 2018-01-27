import functools

def log(a=''):
    def dec(fn):
        @functools.wraps(fn)
        def wra(*args,**kw):
            print('%s begin call:%s'%(a,fn.__name__))
            f=fn(*args,**kw)
            print ('end call')
            return f
        return wra        
    return dec
    
@log
def f():
    print('I am function f')
    
@log('check!')
def g():
    print('I am function g')
f()
g()