class nameReturner:
  def name(self, first_name):
    l_name = input("Hey, enter your last name for me: ")
    if l_name:
      print("Hello there, " + first_name + " " + l_name.title() + "!")
    else:
      print("Program terminated...")
name1 = nameReturner()
name1.name("Waleed")
