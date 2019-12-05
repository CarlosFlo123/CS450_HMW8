'''--------------------------------------------------------------------------
Author: Carlos Flores Valero
Northwestern Polytechnic University, Fremont, CA
Date: 12/01/2019
Subject: Some OOP performing
---------------------------------------------------------------------------'''


#1_______________________________________________
class People():
  def __init__(self, name):         
    self.name = name
    self.sth = "I am reading lecture handout!" 
  def say(self, sth):
    self.sth = sth   
    return sth 
  def ask(self, sth):         
    return self.say("Would you please " + sth) 
  def greet(self):         
    return self.say("Hi, this is " + self.name) 
  def reiterate(self):
    return self.say(self.sth)
  def ask(self, sth):
    return self.say("Would you please " + sth)

michael = People("Michael")
michael.reiterate()
michael.say("Python")
michael.reiterate()
michael.greet()
michael.reiterate()
michael.ask('discuss about Python programming')
michael.reiterate()

#2_______________________________________________
class Twice(People):
  def __init__ (self, name):
    People.__init__(self, name)
  def say(self, sth):
    return People.say(self, sth + " " + sth)

michael = Twice("Michael")
michael.say("hi")

# The one that uses reiterate() generates a type of recursion 
# that end in a forever loop.

# The second one works but the return statement doesnt follow 
# the OOP style making the implementation non-escalable.

#3_______________________________________________
class VndMchn():
  def __init__(self, item, price):
    self.item = item
    self.price = price
    self.stock = 0
    self.cash = 0
  def vending(self):
    if self.stock > 0:
      if self.cash < self.price:
        return str("Need to deposit $" + str(self.price - self.cash) + " more.")
      elif self.cash == self.price:
        self.cash = 0
        self.stock -= 1
        return "Take your soda"
      else:
        tmp = self.cash - self.price
        self.cash = 0
        self.stock -= 1
        return "Take your soda and $" + str(tmp) + " change."
    else:
      return "Out of stock currently"
  def adding(self, x):
    self.stock += x
    return "Current " + self.item + " stock: " + str(self.stock)
  def deposit(self, x):
    if self.stock > 0:
      self.cash += x
      return "Current balance : $" + str(self.cash)
    else:
      return "Out of stock. Returning to you: $" + str(x)

a = VndMchn('soda', 3.5)
a.vending()
a.adding(2)
a.vending()
a.deposit(1.5)
a.vending()
a.deposit(5)
a.vending()
a.deposit(3.5)
a.vending()
a.deposit(10)


#4_______________________________________________
class Keypad():
  def __init__(self, *args):
    self.bttns = {}
    for ar in args:
      self.bttns[ar.pos] = ar

  def prs(self, info):
    try:
      self.bttns[info].pressed += 1
      return self.bttns[info].key
    except:
      print('Dude!, Bttn doesnt exist')
      pass
  def type(self, type_ip):
    try:
      res = ""
      for i in type_ip:
        self.bttns[i].pressed += 1
        res += self.bttns[i].key
      return res
    except:
      print('Bttn doesnt exist')
      pass
class Bttn(): # Button class
  def __init__(self, pstn, ky):
    self.pos = pstn
    self.key = ky
    self.pressed = 0

a1 = Bttn(0, 'H')
a2 = Bttn(1, 'I')
ky = Keypad(a1, a2)
ky.bttns[0].key
ky.prs(1)
ky.type([0, 1])
ky.type([1, 0])
a1.pressed
a2.pressed
