# class for Mouse control

import win32gui
import win32api
import win32con
import ctypes

class Mouse(object):
	# It simulates the mouse
	MOUSEEVENTF_MOVE = 0x0001	# mouse move
	MOUSEEVENTF_LEFTDOWN = 0x0002	# left button down
	MOUSEEVENTF_LEFTUP = 0x0004	# left button up
	MOUSEEVENTF_RIGHTDOWN = 0x0008	# right button down
	MOUSEEVENTF_RIGHTUP = 0x0010	# right button up
	MOUSEEVENTF_MIDDLEDOWN = 0x0020	# middle button down
	MOUSEEVENTF_MIDDLEUP = 0x0040	# middle button up
	MOUSEEVENTF_WHEEL = 0x0800	# wheel button rolled
	MOUSEEVENTF_ABSOLUTE = 0x8000	# absolute move
	SM_CXSCREEN = 0
	SM_CYSCREEN = 1
	
	def _do_event(self, flags, x_pos, y_pos, data, extra_info):
		# generate a mouse event
		x_calc = 65536L * x_pos / ctypes.windll.user32.GetSystemMetrics(self.SM_CXSCREEN) + 1
		y_calc = 65536L * y_pos / ctypes.windll.user32.GetSystemMetrics(self.SM_CYSCREEN) + 1
		return ctypes.windll.user32.mouse_event(flags, x_calc, y_calc, data, extra_info)

	def _get_button_value(self, button_name, button_up=False):
		# convert the name of the button into the corresponding value
		buttons = 0
		if button_name.find("right") >= 0:
			buttons = self.MOUSEEVENTF_RIGHTDOWN
		if button_name.find("left") >= 0:
			buttons = buttons + self.MOUSEEVENTF_LEFTDOWN
		if button_name.find("middle") >= 0:
			buttons = buttons + self.MOUSEEVENTF_MIDDLEDOWN
		if button_up:
			buttons = buttons << 1
		return buttons

	def move_mouse(self, pos):
		# move the mouse to the specified coordinates
		(x, y) = pos
		old_pos = self.get_position()
		x = x if (x != -1) else old_pos[0]
		y = y if (y != -1) else old_pos[1]
		self._do_event(self.MOUSEEVENTF_MOVE + self.MOUSEEVENTF_ABSOLUTE, x, y, 0, 0)
	
	def press_button(self, pos=(-1, -1), button_name="left", button_up=False):
		# push a button of the mouse
		self.move_mouse(pos)
		self._do_event(self.get_button_value(button_name, button_up), 0, 0, 0, 0)
	
	def click(self, pos=(-1, -1), button_name="left"):
		# click at the specified place
		self.move_mouse(pos)
		self._do_event(self._get_button_value(button_name, False) + self._get_button_value(button_name, True), 0, 0, 0, 0)
	
	def double_click(self, pos=(-1, -1), button_name="left"):
		# double click at the specified place
		self.click(pos, button_name)	# 1st click
		self.click(pos, button_name)	# 2nd click
	
	def get_position(self):
		# get mouse position
		return win32api.GetCursorPos()

#-----------------------------------------------------------------------------------------
#Added functions
#-----------------------------------------------------------------------------------------

	def invisible_click(self, pos=(-1, -1), button_name="left"):
		# click in specified place without moving mouse
		xcur, ycur = win32gui.GetCursorPos()
		ctypes.windll.user32.SetCursorPos(pos[0], pos[1])
		self.click(pos, button_name)
		ctypes.windll.user32.SetCursorPos(xcur, ycur)
	
	def invisible_click_rel(self, handle, pos, button_name="left"):
		# click without moving mouse in window coordinates as opposed to general screen coordinates
		xleft, ytop, xright, ybottom = win32gui.GetWindowRect(handle)	#get window dimension
		
		xcur, ycur = win32gui.GetCursorPos()
		
		ctypes.windll.user32.SetCursorPos(pos[0]+xleft, pos[1]+ytop)
		self.click((pos[0]+xleft, pos[1]+ytop), button_name)
		ctypes.windll.user32.SetCursorPos(xcur, ycur)

if __name__ == '__main__':
	p = (210, 260)
	print win32gui.GetForegroundWindow()
	mouse = Mouse()
	mouse.invisible_click_rel(win32gui.GetForegroundWindow(), p)
