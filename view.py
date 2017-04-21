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

import gtk
import random
import locale
import sugar.profile

class Views():
  def __init__(self):
    locale.setlocale(locale.LC_ALL,"")
    self.name = sugar.profile.get_nick_name()
    self.user_interaction = gtk.VBox()
    self.activity = gtk.Notebook()
    self.activity.set_show_tabs(False)
    self.activity.set_size_request(800, 600)
    self.user_interaction.pack_start(self.activity, False, False, 10)
    # navigation
    self.navigation = gtk.HButtonBox()
    self.user_interaction.pack_start(self.navigation, False, False, 10)
    self.navigation.pack_start(gtk.Label(), False, False, 10)
    self.play = gtk.Button("Play")
    self.navigation.pack_start(self.play, False, False, 10)
    self.play.connect("clicked", self.play_clicked)
    self.help = gtk.Button("Help")
    self.help.connect("clicked", self.help_clicked)
    self.navigation.pack_start(self.help, False, False, 10)
    self.back = gtk.Button("Back")
    self.back.connect("clicked", self.back_clicked)
    self.navigation.pack_start(self.back, False, False, 10)
    self.next = gtk.Button("Next")
    self.next.connect("clicked", self.next_clicked)
    self.navigation.pack_start(self.next, False, False, 10)
    self.navigation.pack_start(gtk.Label(), False, False, 10)
    #
    # create the intro tab
    self.intro_tab = gtk.VBox()
    self.activity.append_page(self.intro_tab)
    # intro - heading
    self.intro_heading = gtk.Label()
    self.intro_heading.set_markup("<big>Let's round numbers with Hoppy the Grasshopper</big>")
    self.intro_tab.pack_start(self.intro_heading, False, False, 10)
    # intro - intro area
    self.intro_area = gtk.HBox()
    self.intro_tab.pack_start(self.intro_area, False, False, 10)
    # intro - image
    self.image_intro = gtk.Image()
    self.intro_area.pack_start(self.image_intro, False, False, 10)
    self.image_intro.set_from_pixbuf(gtk.gdk.pixbuf_new_from_file("hoppy-title.svg"))
    # intro - text tabs
    self.introduction = gtk.Notebook()
    self.introduction.set_show_tabs(False)
    self.intro_area.pack_start(self.introduction, False, False, 10)
    self.intro_tab1 = gtk.Label()
    self.intro_tab1.set_line_wrap(True)
    self.intro_tab1.set_size_request(700, 300)
    self.intro_tab1.set_markup("<big>When Hoppy brags to his friends, he likes to tell them how many leaves he can eat in one day.\n\n\nWhen he doesn't know the <b>exact</b> number, he <b>estimates</b>.\n\n\nThis is called <b>rounding</b>.</big>")
    self.introduction.append_page(self.intro_tab1)
    self.intro_tab2 = gtk.Label()
    self.intro_tab2.set_line_wrap(True)
    self.intro_tab2.set_size_request(700, 300)
    self.intro_tab2.set_markup("<big><b>Hoppy says there are two rules for rounding numbers:</b>\n\n\n1.  If the number you are rounding is followed \n\tby <b>5, 6, 7, 8 or 9</b> round the number <b>up</b>.\n\n\tExample:  38 rounded to the nearest ten is 40.\n\n\n2.  If the number you are rounding is followed \n\tby <b>0, 1, 2, 3 or 4</b> round the number <b>down</b>.\n\n\tExample:  33 rounded to the nearest ten is 30.</big>")
    self.introduction.append_page(self.intro_tab2)
    self.intro_tab3 = gtk.Label()
    self.intro_tab3.set_line_wrap(True)
    self.intro_tab3.set_size_request(700, 300)
    self.intro_tab3.set_markup("<big><b>Look at the number 182,727:</b>\n\n\t182,727 rounded to the nearest <b>ten</b> is 182,730\n\t182,727 rounded to the nearest <b>hundred</b> is 182,700\n\t182,727 rounded to the nearest <b>thousand</b> is 183,000\n\t182,727 rounded to the nearest <b>ten thousand</b> is 180,000\n\t182,727 rounded to the nearest <b>hundred thousand</b> is 200,000\n\n\nAll the numbers to the right of the place that you are <b>rounding to</b> become zeros.\n\n\t34 rounded to the nearest <b>ten</b> is 30\n\t4,654 rounded to the nearest <b>hundred</b> is 4,700\n\t986 rounded to the nearest <b>thousand</b> is 1,000\n\t219,526 rounded to the nearest <b>ten thousand</b> is 220,000\n\t742,899 rounded to the nearest <b>hundred thousand</b> is 700,000</big>")
    self.introduction.append_page(self.intro_tab3)
    #
    # create the quiz tab
    self.quiz_tab = gtk.HBox()
    self.activity.append_page(self.quiz_tab)
    self.user_input = gtk.VBox()
    self.quiz_tab.pack_start(self.user_input, False, False, 10)
    self.rounding_phrase = gtk.Label("rounding phrase")
    self.user_input.pack_start(self.rounding_phrase, False, False, 10)
    # quiz - create the play notebook to show the widgets for playing
    self.tabber = gtk.Notebook()
    self.tabber.set_show_tabs(False)
    self.user_input.pack_start(self.tabber, False, False, 10)
    # quiz - create the slider tab
    self.slider_tab = gtk.VButtonBox()
    self.slider_instruction = gtk.Label()
    self.slider_instruction.set_markup("<big>Move the slider to choose the correct answer</big>")
    self.slider_tab.pack_start(self.slider_instruction, False, False, 10)
    self.slider_adjustment = gtk.Adjustment()
    self.slider_tool = gtk.HScale(self.slider_adjustment)
    self.slider_tool.set_digits(0)
    self.slider_tab.pack_start(self.slider_tool, False, False, 10)
    self.slider_click = gtk.Button("OK")
    self.slider_tab.pack_start(self.slider_click, False, False, 10)
    self.tabber.append_page(self.slider_tab)
    # quiz - create the multiple choice tab
    self.mult_tab = gtk.VBox()
    self.mult_instruction = gtk.Label()
    self.mult_instruction.set_markup("<big>Choose one of the answers below</big>")
    self.mult_tab.pack_start(self.mult_instruction, False, False, 10)
    self.mult_1 = gtk.Button()
    self.mult_1.unset_flags(gtk.CAN_FOCUS)  
    self.mult_tab.pack_start(self.mult_1, False, False, 10)
    self.mult_2 = gtk.Button()
    self.mult_2.unset_flags(gtk.CAN_FOCUS)  
    self.mult_tab.pack_start(self.mult_2, False, False, 10)
    self.mult_3 = gtk.Button()
    self.mult_3.unset_flags(gtk.CAN_FOCUS)  
    self.mult_tab.pack_start(self.mult_3, False, False, 10)
    self.mult_4 = gtk.Button()
    self.mult_4.unset_flags(gtk.CAN_FOCUS)  
    self.mult_tab.pack_start(self.mult_4, False, False, 10)
    self.tabber.append_page(self.mult_tab)
    # quiz - create the entry tab
    self.entry_tab = gtk.VButtonBox()
    self.entry_instruction = gtk.Label()
    self.entry_instruction.set_markup("<big>Type your answer below and click 'OK'</big>")
    self.entry_tab.pack_start(self.entry_instruction, False, False, 10)
    self.entry_tool = gtk.Entry()
    self.entry_tab.pack_start(self.entry_tool, False, False, 10)
    self.entry_click = gtk.Button("OK")
    self.entry_tab.pack_start(self.entry_click, False, False, 10)
    self.tabber.append_page(self.entry_tab)
    # quiz - create the output
    self.user_output = gtk.VBox()
    self.quiz_tab.pack_start(self.user_output, False, False, 10)
    self.output = gtk.Label("")
    self.output.set_alignment(0.1, 0.5)
    self.user_output.pack_start(self.output, False, False, 10)
    self.image_output = gtk.Image()
    self.user_output.pack_start(self.image_output, False, False, 10)
    self.image_correct_answer = gtk.gdk.pixbuf_new_from_file("hoppy-right.svg")
    self.image_incorrect_answer = gtk.gdk.pixbuf_new_from_file("hoppy-wrong.svg")

  def get_user_interaction(self):
    return self.user_interaction

  def set_rounding_phrase(self, data):
    text = "<big>Round the number <b>"
    text += self.locl(data.random_number)
    text += "</b> to the nearest <b>" 
    text += self.locl(data.answer_decade) + "</b></big>"
    self.rounding_phrase.set_markup(text)

  def set_choices(self, number, choices):
    self.slider_adjustment.set_all(number, choices[0], choices[1], 1)
    # shuffle around the possibilities
    random.shuffle(choices)
    self.mult_1.set_label(self.locl(choices[0]))
    self.mult_2.set_label(self.locl(choices[1]))
    self.mult_3.set_label(self.locl(choices[2]))
    self.mult_4.set_label(self.locl(choices[3]))
    self.entry_tool.set_text("")

  def answer_correct(self, data):
    text = "<big><span foreground=\"dark green\"><b>That's Right, "
    text += self.name + "!!! =8-) </b></span> \n\n"
    text += self.locl(data.random_number) + " rounded to the nearest "
    text += self.locl(data.answer_decade) + " is " + self.locl(data.correct_answer)
    if data.level_change:
      text += "\n\n<span foreground=\"dark green\"><b>You made it to the next level! =8^P</b></span>"
    text += "</big>"
    self.output.set_markup(text)
    self.image_output.set_from_pixbuf(self.image_correct_answer)

  def answer_incorrect(self, data):
    text = "<big><span foreground=\"red\"><b>Sorry " + self.name + ". >:( </b></span> \n\n"
    text += self.locl(data.random_number) + " rounded to the nearest "
    text += self.locl(data.answer_decade) + " is " + self.locl(data.correct_answer)
    if data.level_change:
      text += "\n\n<span foreground=\"red\"><b>You dropped a level. Concentrate! >8^|</b></span>"
    text += "</big>"
    self.output.set_markup(text)
    self.image_output.set_from_pixbuf(self.image_incorrect_answer)

  def clear(self, data):
    self.output.set_markup("<big>" + data.get_game_data() + "</big>")
    self.image_output.clear()
    return False

  def answer_nan(self):
    text = "<big><span foreground=\"blue\"><b>Please enter only numbers.</b></span> \n\n</big>"
    self.output.set_markup(text)
  
  def set_tab(self, data):
    if data.question_count > data.thresh_entry:
      self.tabber.set_current_page(2)
      self.entry_tool.grab_focus()
    elif data.question_count > data.thresh_mult:
      self.tabber.set_current_page(1)
    elif data.question_count > data.thresh_slider:
      self.tabber.set_current_page(0)
      self.slider_tool.grab_focus()

  def play_clicked(self, widget):
    self.help.show()
    self.back.hide()
    self.next.hide()
    self.play.hide()
    self.activity.set_current_page(1)

  def help_clicked(self, widget):
    self.help.hide()
    self.back.show()
    self.next.show()
    self.play.show()
    self.activity.set_current_page(0)

  def back_clicked(self, widget):
    self.introduction.prev_page()

  def next_clicked(self, widget):
    self.introduction.next_page()

  def locl(self, characters):
    return str(locale.format("%d", characters, True))
