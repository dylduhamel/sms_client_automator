class clientInfo:
     def __init__(self, bookID, name, balance):
          self.bookID = bookID
          self.name = name
          self.balance = balance

     def messageFormat(self):
          return "Hello " + self.bookID + " Your balance on action23.com for this past week is $" + str(self.balance)
     