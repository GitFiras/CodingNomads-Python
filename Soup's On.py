
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


''''Soup assigmnment '''
t= Ingredient('tomatoes',3)
p = Ingredient('potatoes',12)

soup = Soup([t,p])

soup.cook()
print(soup)
