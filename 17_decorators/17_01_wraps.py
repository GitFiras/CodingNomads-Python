'''
Write a decorator function that wraps text passed to it in a html <p> tag.

'''

def text(name):
   return "Hello, {0}".format(name)

def p_decorate(func):
   def wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return wrapper

greeting_text = p_decorate(text)

print(greeting_text("John"))
