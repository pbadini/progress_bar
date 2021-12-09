import time
import sys
import random


class ProgressBar:
  def __init__(self, 
              num_of_bars = 1, 
              size = 50, 
              fill = '█',
              fill_color = 'reset', 
              background = '▒',
              background_color = 'reset',
              process = 'Process {}  '):
    self.size = size
    self.bars = num_of_bars
    self.has_space = False
    self.process = process
    self.current_bar = 0
    self.RESET_COLOR = '\u001b[0m'
    self.FILL = self.__get_color(fill_color) + fill + self.RESET_COLOR
    self.BACKGROUND = self.__get_color(background_color) + background + self.RESET_COLOR
    self.LINE_UP = '\u001b[{}F'
    self.LINE_DOWN = '\u001b[{}E'
    self.HIDE_CURSOR = '\u001b[?25l'
    self.SHOW_CURSOR = '\u001b[?25h'
    self.END_OF_LINE = '\u001b[0K'
    return

  def __len__(self):
    return self.bars

  def __iter__(self):
    return self

  def __next__(self):
    if self.current_bar >= self.bars:
      self.current_bar = 0
      raise StopIteration
    
    self.current_bar += 1
    return self

  def __get_color(self, color):
    color = color.lower()
    if color == 'black':
      color_num = 30
    elif color == 'red':
      color_num = 31
    elif color == 'green':
      color_num = 32
    elif color == 'yellow':
      color_num = 33
    elif color == 'blue':
      color_num = 34
    elif color == 'magenta':
      color_num = 35
    elif color == 'cyan':
      color_num = 36
    elif color == 'white':
      color_num = 37
    else:
      color_num = 0
    
    return '\u001b[0;{}m'.format(color_num)

  def __create_space(self):
    if not self.has_space:
      self.has_space = True
      sys.stdout.write('\n' * self.bars * 2)
      sys.stdout.flush()

    return

  def __mov_cursor_up(self, lines):
    sys.stdout.write(self.HIDE_CURSOR)
    sys.stdout.write(self.LINE_UP.format(lines))
    sys.stdout.flush()
    return

  def __mov_cursor_down(self, lines):
    sys.stdout.write(self.LINE_DOWN.format(lines))
    sys.stdout.write(self.SHOW_CURSOR)
    sys.stdout.flush()
    return
  
  def __go_to_pos(self, bar):
    self.__mov_cursor_up((self.bars - bar) * 2)
    return

  def __go_to_end(self, bar):
    self.__mov_cursor_down((self.bars - bar) * 2)
    return

  def __get_process_string(self, bar):
    return self.process.format(bar)
  
  def __get_bar_string(self, percent):
    num_of_complete = int(percent  * self.size / 100)

    return self.FILL * num_of_complete  + self.BACKGROUND * (self.size - num_of_complete)

  def __get_percent_string(self, percent):
    return ' {:.2f}%'.format(percent)

  def show(self, percent, bar = -1):
    if bar < 0:
      bar = self.current_bar - 1

    if percent > 100: percent = 100
    self.__create_space()
    self.__go_to_pos(bar)
    sys.stdout.write(self.__get_process_string(bar) + self.__get_bar_string(percent) + self.__get_percent_string(percent) + self.END_OF_LINE)
    sys.stdout.flush()
    self.__go_to_end(bar)
    return

  def show_error(self, error_msg, bar = -1, color = 'red'):
    if bar < 0:
      bar = self.current_bar - 1

    self.__create_space()
    self.__go_to_pos(bar)
    sys.stdout.write(self.__get_process_string(bar) + self.__get_color(color) + error_msg + self.RESET_COLOR + self.END_OF_LINE)
    sys.stdout.flush()
    self.__go_to_end(bar)
    return
  
  def show_success(self, error_msg, bar = -1, color = 'green'):
    if bar < 0:
      bar = self.current_bar - 1

    self.__create_space()
    self.__go_to_pos(bar)
    sys.stdout.write(self.__get_process_string(bar) + self.__get_color(color) + error_msg + self.RESET_COLOR + self.END_OF_LINE)
    sys.stdout.flush()
    self.__go_to_end(bar)
    return



if __name__ ==  '__main__':
  num_bars = 5
  bars = ProgressBar(num_bars, fill_color = 'green')
  percent = 0
  while True:
    for bar in bars:
      percent += random.random()
      bars.show(percent)
      time.sleep(0.01)








