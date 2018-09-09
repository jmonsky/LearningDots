from math import atan2, cos, sin

class PVector(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def __add__(self, otherV):
		if isinstance(otherV, PVector):
			return PVector(self.x+otherV.x, self.y+otherV.y)

	def mag(self):
		return ((self.x)**2+(self.y)**2)**0.5

	def angle(self):
		return atan2(self.y, self.x)

	def limit(self, mag):
		if self.mag() > mag:
			ang = self.angle()
			self.x = cos(ang)*mag
			self.y = sin(ang)*mag

	def copy(self):
		return PVector(self.x, self.y)

	def __str__(self):
		return str((self.x, self.y))

	def __getitem__(self, x):
		if x == 0:
			return self.x
		elif x == 1:
			return self.y
		else:
			return 0