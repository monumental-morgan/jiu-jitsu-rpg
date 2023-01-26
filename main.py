class TopPins:
  def __init__(self):
    pass

  def side_control(self): # submit, mount, north south
    decision = input("\nYou are in side control. What do you do?\nA. Submit\nB. Go to Mount\nC. Go to North-South\nD. Take opponent's back\n")
    if decision == 'a':
      print('You attempt submit your opponent.')
      pinner.submit() #add some wait time before moving into next function
    elif decision == 'b':
      print('You attempt to mount your opponent.')
      print('You successfully mount your opponent!')
      pinner.mount() #add some wait time before moving into next function
    elif decision == 'c':
      print('You attempt to move into North-South.')
      pinner.north_south() #add some wait time before moving into next function
    elif decision == 'd':
      print("You attempt to take your opponent's back")
      pinner.rear_mount()
      
  def mount(self):  #submit, side control, north-south
    decision = input("\nYou have top mount. What do you do?\nA. Submit\nB. Go to side control\nC. Take opponent's back\nD. Go to knee on belly\n")
    if decision == 'a':
      print('You attempt submit your opponent.')
      pinner.submit() #add some wait time before moving into next function
    elif decision == 'b':
      print('You attempt to move into side control.')
      pinner.side_control() #add some wait time before moving into next function
    elif decision == 'c':
      print("You attempt to take your opponent's back.")
      pinner.rear_mount() #add some wait time before moving into next function
    elif decision == 'd':
      print('You attempt to move into knee on belly')
      pinner.knee_on_belly()
  
  def rear_mount(self): #submit, mount
    decision = input("\nYou have rear mount. What do you do?\nA. Submit\nB. Go to mount\n")
    if decision == 'a':
      print('You attempt submit your opponent.')
      pinner.submit() #add some wait time before moving into next function
    elif decision == 'b':
      print('You attempt to move into top mount.')
      pinner.mount() #add some wait time before moving into next function
  
  def north_south(self): # submit, side control, knee on belly
    decision = input("\nYou are in top North-South. What do you do?\nA. Submit\nB. Go to side control\nC. Go to knee-on-belly\n")
    if decision == 'a':
      print('You attempt submit your opponent.')
      pinner.submit() #add some wait time before moving into next function
    elif decision == 'b':
      print('You attempt to move into side control.')
      pinner.side_control() #add some wait time before moving into next function
    elif decision == 'c':
      print('You attempt to move to knee-on-belly')
      pinner.knee_on_belly() #add some wait time before moving into next function
      
  def knee_on_belly(self): # submit, side control, mount
    decision = input("\nYou are have knee-on-belly. What do you do?\nA. Submit\nB. Go to side control\nC. Go to mount\n")
    if decision == 'a':
      print('You attempt submit your opponent.')
      pinner.submit() #add some wait time before moving into next function
    elif decision == 'b':
      print('You attempt to move into side control.')
      pinner.side_control() #add some wait time before moving into next function
    elif decision == 'c':
      print('You successfully mount your opponent!')
      pinner.mount() #add some wait time before moving into next function
  
  def submit(self):
    print("You have successfully submitted your opponent!")

class BottomPins:
  def __init__(self):
    pass

  def b_side_control(self): # submit, mount, north south
    decision = input("\nYour opponent has you in side control. What do you do?\nA. Submit (Buggy Choke, etc)\nB. Escape to guard\n)
    if decision == 'a':
      print('You attempt submit your opponent.')
      pinner.submit() #add some wait time before moving into next function
    elif decision == 'b':
      print('You attempt to mount your opponent.')
      print('You successfully mount your opponent!')
      pinner.b_mount() #add some wait time before moving into next function
      
  def b_mount(self):  #submit, side control, north-south
    decision = input("\nYour opponent is mounted on top of you. What do you do?\nA. Submit\nB. Go to side control\nC. Take opponent's back\nD. Go to knee on belly\n")
    if decision == 'a':
      print('You attempt submit your opponent.')
      pinner.submit() #add some wait time before moving into next function
    elif decision == 'b':
      print('You attempt to move into side control.')
      pinner.b_side_control() #add some wait time before moving into next function
    elif decision == 'c':
      print('You attempt to move into North-South.')
      pinner.b_rear_mount() #add some wait time before moving into next function
    elif decision == 'd':
      print('You attempt to move into knee on belly')
      pinner.knee_on_belly()
  
  def b_rear_mount(self): #submit, mount
    decision = input("\nYou have rear mount. What do you do?\nA. Submit\nB. Go to mount\n")
    if decision == 'a':
      print('You attempt submit your opponent.')
      pinner.submit() #add some wait time before moving into next function
    elif decision == 'b':
      print('You attempt to move into top mount.')
      pinner.b_mount() #add some wait time before moving into next function
  
  def north_south(self): # submit, side control, knee on belly
    decision = input("\nYou are in top North-South. What do you do?\nA. Submit\nB. Go to side control\nC. Go to knee-on-belly\n")
    if decision == 'a':
      print('You attempt submit your opponent.')
      pinner.submit() #add some wait time before moving into next function
    elif decision == 'b':
      print('You attempt to move into side control.')
      pinner.b_side_control() #add some wait time before moving into next function
    elif decision == 'c':
      print('You attempt to move to knee-on-belly')
      pinner.b_knee_on_belly() #add some wait time before moving into next function
      
  def b_knee_on_belly(self): # submit, side control, mount
    decision = input("\nYou are have knee-on-belly. What do you do?\nA. Submit\nB. Go to side control\nC. Go to mount\n")
    if decision == 'a':
      print('You attempt submit your opponent.')
      pinner.submit() #add some wait time before moving into next function
    elif decision == 'b':
      print('You attempt to move into side control.')
      pinner.b_side_control() #add some wait time before moving into next function
    elif decision == 'c':
      print('You successfully mount your opponent!')
      pinner.b_mount() #add some wait time before moving into next function
  
  def submit(self):
    print("You have successfully submitted your opponent!")

pinner = TopPins()
pinned = BottomPins()

pinned.side_control()

def play_again():
  play_again = input('Would you like to play again? ')
  if play_again == 'y':
    pinner.side_control()

play_again()