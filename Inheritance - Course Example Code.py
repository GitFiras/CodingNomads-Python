class Ingredient:
  """Models an Ingredient."""
  def __init__(self, name, amount):
    self.name = name
    self.amount = amount

  def expire(self):
    """Expires the ingredient item."""
    print(f"whoops, these {self.name} went bad...")
    self.name = "expired " + self.name

  def __str__(self):
   return f"You have {self.amount} {self.name}."

# we can define new classes that take over all their superclasses' variables and methods:
class Spice(Ingredient):  # means it inherits from the Ingredient class

# test of Class
# p = Ingredient('peas', 12)
# print(p)
# s = Spice('salt', 200)
# print(s)  # no need to define __str__() again - it works!

  # let's give Spice a method that its superclass doesn't have!
  def grind(self):
    print(f"You have now {self.amount} of ground {self.name}.")

c = Ingredient('carrots', 3)
p = Spice('pepper', 20)
print(c, p)
p.grind()
# c.grind()  # produces an error

class Spice(Ingredient):
  # we override this inherited method
  def expire(self):
    if self.name == 'salt':
      print(f"{self.name} never expires! ask the sea!")
    else:
      print(f"eh... sorry but that {self.name} actually got bad!")
      self.name = "expired " + self.name

c = Ingredient('carrots', 3)
p = Spice('pepper', 20)
s = Spice('salt', 200)
print(c, p, s)
p.expire()
print(p)
# try calling expire() with the c and s objects!
