import curses
from global_settings import *

class Text:
  def __init__(self, string):
    self.string=string
    self.column_string=""
    if len(string) > (SETTINGS.COLUMN_TEXT_WIDTH - 2):
      self.column_string=string[:(SETTINGS.COLUMN_TEXT_WIDTH - 5)]+"...  "
    else:
      self.column_string=string+" "*(SETTINGS.COLUMN_TEXT_WIDTH - len(string))

  def Redefine(self):
    if len(self.string) > (SETTINGS.COLUMN_TEXT_WIDTH - 2):
      self.column_string=self.string[:(SETTINGS.COLUMN_TEXT_WIDTH - 5)]+"...  "
    else:
      self.column_string=self.string+" "*(SETTINGS.COLUMN_TEXT_WIDTH - len(self.string))

  def RawText(self):
    return self.string

  def ColumnText(self):          ## According to COLUMN_TEXT_WIDTH
    return self.column_string

class Line:
  def __init__(self, x, y, text, screen):
    self.x = x                              # X co-ordinate of starting point
    self.y = y                              # Y co-ordinate of starting point
    self.text = Text(text)                        # Text to be outputted
    self.highlighted=0                      # For toggling the highlighting
    self.screen=screen

  def Display(self):
    self.screen.Display(self.text.ColumnText(), self.x, self.y)

  def DisplayBold(self):
    self.screen.DisplayBold(self.text.ColumnText(), self.x, self.y)

  def Highlight(self):
    self.screen.Highlight(self.text.ColumnText(), self.x, self.y)

  def Toggle(self):
    if self.highlighted==0:
      self.highlighted=1
      self.Highlight()
    else:
      self.highlighted=0
      self.Display()