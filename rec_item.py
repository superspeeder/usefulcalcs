class Item(object):
  def __init__(self, name):
    self.name = name
    self.recipe = None
  
  def handshake(self, recipe):
    self.recipe = recipe
    
  def __repr__(self):
    return "<Item: {}>".format(self.name)
    
  


class Recipe(object):
  def __init__(self, output, inputs):
    self.out_item = output
    self.out_item.handshake(self)
    self.inputs = inputs
    
  def __repr__(self):
    return '\n'.join(self.inputs)
