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

import random
import math

class LevelData():
  def __init__(self):
    self.question_max = 3  # number of questions in each section (slider, multiple choice & entry)
    self.thresh_slider = 0  # if question count matches this number, change to this section
    self.thresh_mult = self.question_max  # if question count matches this number, change to this section
    self.thresh_entry = 2 * self.question_max  # if question count matches this number, change to this section
    self.min_level = 1  # minimum levels in the activity; also the exponent of the current level
    self.max_level = 5  # maximum levels in the activity; also the exponent of the current level
    self.current_level = 1  # starting and current level indicator
    self.question_count = 0  # number of questions asked on current level
    self.level_score = 0  # number of questions correct on current level
    self.thresh_up = 6  # level score at/above which the level will be increased
    self.thresh_down = 0  # level score at/below which the level will be reduced
    self.level_change = 0  # flag indicating a level change
    self.digits = []  # collection of digits to create the question from
    random.seed()

  def check_answer(self, response):
    if response == self.correct_answer:
      self.level_score += 1
    else:
      self.level_score -= 1
    if self.question_count == self.question_max * 3:
      if self.level_score >= self.thresh_up and self.current_level < self.max_level:
        self.level_change = 1
      elif self.level_score <= self.thresh_down and self.current_level > self.min_level:
        self.level_change = -1
      self.question_count = self.level_score = 0
    return self.correct_answer == response

  def increase_level(self):
    if self.current_level < self.max_level:
      self.current_level += 1
    self.answer_decade = int(10**self.current_level)
    self.level_change = 0

  def decrease_level(self):
    if self.current_level > self.min_level:
      self.current_level -= 1
    self.answer_decade = int(10**self.current_level)
    self.level_change = 0

  def gen_random(self):
    if self.level_change == 1:
      self.increase_level()
    elif self.level_change == -1:
      self.decrease_level()
    self.question_count += 1
    # generate a random number. don't use digits 0 or 9; 
    # they cause duplicates in the mult choice answer set.
    self.digits = range(1,9)
    random.shuffle(self.digits)
    str_num = ""
    for x in range(0, self.current_level + 2):
      str_num += str(random.choice(self.digits))
    self.random_number = int(str_num)
    self.answer_decade = int(math.pow(10, self.current_level))
    self.correct_answer = int(round(self.random_number/(self.answer_decade*1.0), 0) * self.answer_decade)
    # create the multiple choice possibilities
    self.mult=[]
    self.mult.append(int(math.floor(self.random_number/(self.answer_decade*1.0)) * self.answer_decade))
    self.mult.append(int(math.ceil(self.random_number/(self.answer_decade*1.0)) * self.answer_decade))
    if self.current_level == self.min_level:
      self.mult.append(int(math.floor(self.random_number/(self.answer_decade*10.0)) * self.answer_decade * 10.0))
      self.mult.append(int(math.ceil(self.random_number/(self.answer_decade*10.0)) * self.answer_decade * 10.0))
    elif self.current_level == self.max_level:
      self.mult.append(int(math.floor(self.random_number/(self.answer_decade*0.1)) * self.answer_decade * 0.1))
      self.mult.append(int(math.ceil(self.random_number/(self.answer_decade*0.1)) * self.answer_decade * 0.1))
    else:
      factor = random.choice([0.1,10.0])
      self.mult.append(int(math.floor(self.random_number/(self.answer_decade*factor)) * self.answer_decade * factor))
      self.mult.append(int(math.ceil(self.random_number/(self.answer_decade*factor)) * self.answer_decade * factor))

  def get_game_data(self):
    temp = "\n\nLevel: " + str(self.current_level)
    #temp += "\nRandom Number: " + str(self.random_number)
    #temp += "\nDecade: " + str(self.answer_decade)
    #temp += "\nCorrect Answer: " + str(self.correct_answer)
    #temp += "\nMult Choices: " + str(self.mult)
    temp += "\nScore: " + str(self.level_score)
    temp += "\nCount: " + str(self.question_count)
    return temp
