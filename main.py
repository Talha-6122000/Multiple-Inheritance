# Inheritancance is used to take on the properties of an exisiting class
# The inherited class is known as Base Class while the class who inherits is known as derived class
class User:
  def sign_in(self):
    print("Logged In")
class Wizard(User):
  def __init__(self,name,power):
    self.name=name
    self.power=power
  def attack(self):
    print(f"Attacking with the power of {self.power}")
class Archar(User):
  def __init__(self,name,num_arrows):
    self.name=name
    self.num_arrows=num_arrows
  def arrows(self):
    print(f'Player Name is {self.name}')
    print(f"Attacking with left arrows {self.num_arrows}")
# Multiple Inheritance
class HybridBorg(Wizard,Archar):
  def __init__(self,name,power,num_arrows):
    Wizard.__init__(self,name,power)
    Archar.__init__(self,name,num_arrows)


  pass
hb1=HybridBorg('Talha','8767',635)
print(hb1.attack())
print(hb1.arrows())