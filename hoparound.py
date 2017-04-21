"""
    Copyright (C) 2009 Mike Major <ossfm@yahoo.com>
    
    This file is part of HopAround.

    Hop-A-Round is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    HopAround is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Hop-A-Round.  If not, see <http://www.gnu.org/licenses/>.
"""

from sugar.activity import activity
from view import Views
from data import LevelData
import gtk
import locale
import gobject

class HopaRoundActivity(activity.Activity):
  def __init__(self, handle):
    activity.Activity.__init__(self, handle)
    # make the toolbox
    toolbox = activity.ActivityToolbox(self)
    self.set_toolbox(toolbox)
    toolbox.show()
    self.data = LevelData()
    self.ui = Views()
    self.ui.clear(self.data)
    self.ui.slider_click.connect("clicked", self.submit_answer, self.ui.slider_tool)
    self.ui.mult_1.connect("clicked", self.submit_answer, self.ui.mult_1)
    self.ui.mult_2.connect("clicked", self.submit_answer, self.ui.mult_2)
    self.ui.mult_3.connect("clicked", self.submit_answer, self.ui.mult_3)
    self.ui.mult_4.connect("clicked", self.submit_answer, self.ui.mult_4)
    self.ui.entry_click.connect("clicked", self.submit_answer, self.ui.entry_tool)
    self.ui.entry_tool.connect("activate", self.submit_answer, self.ui.entry_tool)
    self.setup(self.data, self.ui)
    self.set_canvas(self.ui.get_user_interaction())
    self.show_all()
    self.ui.help.hide()
    
  def setup(self, data, ui):
    data.gen_random()
    ui.set_rounding_phrase(data)
    ui.set_choices(data.random_number, data.mult)
    ui.set_tab(data)

  def submit_answer(self, widget, answer):
    try: # for int answer because of entry field 
      if answer.get_name() == "GtkHScale":
        num = int(answer.get_value())
      elif answer.get_name() == "GtkButton":
        num = locale.atoi(answer.get_label())
      elif answer.get_name() == "GtkEntry":
        num = locale.atoi(answer.get_text())
    except:
      self.ui.answer_nan()
    else:
      if self.data.check_answer(num):
        self.ui.answer_correct(self.data)
      else:
        self.ui.answer_incorrect(self.data)
      gobject.timeout_add(2500, self.ui.clear, self.data)
      self.setup(self.data, self.ui)
      
