import numpy as np
'''
class CurveGenerator(object):

	@staticmethod
	def PointSlope(minLevel, maxLevel, startValue, inflation):
		array = np.zeros(maxLevel + 1)
		for i in xrange(minLevel, maxLevel + 1):
			array[i] = startValue + (inflation * i)
		return array

	@staticmethod
	def EarlyLateCurve(minLevel, maxLevel, minValue, maxValue, e=1.0, l=1.0):
		array = np.zeros(maxLevel + 1)
		for i in xrange(minLevel, maxLevel + 1):
			array[i] = CurveGenerator.CalculateValue(i, float(minLevel), 
				float(maxLevel), float(minValue), float(maxValue), float(e), float(l))
		return array

	@staticmethod
	def LateCurve(level, minLevel, maxLevel, minValue, maxValue):
		diff = minLevel - maxLevel
		stat = minValue - maxValue
		num = stat * level ** 2 - 2 * minLevel * stat * level + minLevel ** 2 * maxValue - 2 * minLevel * maxLevel * minValue + minValue * minLevel ** 2
		denom = diff ** 2
		return num / denom

	@staticmethod
	def EarlyCurve(level, minLevel, maxLevel, minValue, maxValue):
		diff = maxLevel - minLevel
		stat = maxValue - minValue
		num = -stat * level ** 2 + 2 * maxLevel * stat * level + minLevel ** 2 * maxValue - 2 * minLevel * maxLevel * maxValue + minValue * maxLevel ** 2
		denom = diff ** 2
		return num / denom

	@staticmethod
	def SteadyCurve(level, minLevel, maxLevel, minValue, maxValue):
		chLevel = maxLevel - minLevel
		chStat = maxValue - minValue
		base1 = chStat / chLevel * level
		mod = maxValue * minLevel - minValue * maxLevel
		base2 = mod / chLevel
		return base1 - base2

	@staticmethod
	def CalculateValue(level, minLevel, maxLevel, minValue, maxValue, e, l):
		if level < minLevel:
			return minValue
		if level > maxLevel:
			return maxValue
		if e == l:
			stat = CurveGenerator.SteadyCurve(level, minLevel, maxLevel, minValue, maxValue)
		else:
			early = CurveGenerator.EarlyCurve(level, minLevel, maxLevel, minValue, maxValue)
			late = CurveGenerator.LateCurve(level, minLevel, maxLevel, minValue, maxValue)
			stat = (e * early + l * late) / (e + l)
		return min(maxValue, max(minValue, stat))
'''

class CurveGenerator(object):

	def __init__(self, *args):
		if len(args) >= 6:
			self.SetValues(*args)

	def SetValues(self, mnV, mdV, mxV, mnL, mdL, mxL, e=0, l=0, s=0, c1=0, c2=0, i=True):
		"""Sets the values used for curve calculation
		
		Arguments:
		mnV --
		mdV --
		mxV --
		
		
		"""
		# Set attribute values
		self._minV, self._midV, self._maxV = mnV, mdV, mxV
		self._minL, self._midL, self._maxL = mnL, mdL, mxL
		self._early, self._late, self._steady = e, l, s
		self._curve1, self._curve2, self._integer = c1, c2, i
		# Calculate constant values
		self._inmi = (self._midV - self._minV) / (self._midL - self._minL)
		self._infi = (self._maxV - self._minV) / (self._maxL - self._minL)
		self._infimi = (self._infi - self._inmi) / (self._maxL - self._midL)

	def Generate(self):
		array = np.zeros(self._maxL + 1)
		for lvl in xrange(self._minL, self._maxL):
			array[lvl] = self.GetValue(lvl)
		return array

	def GetValue(self, level):
		if level <= self._minL:
			if self._integer: return int(self._minV)
			return self._minV
		if level >= self._maxL:
			if self._integer: return int(self._maxV)
			return self._maxV
		total = 0
		if self._early  > 0: total += self._early  * self._earlyCurve(level)
		if self._late   > 0: total += self._late   * self._lateCurve(level)
		if self._steady > 0: total += self._steady * self._steadyCurve(level)
		if self._curve1 > 0: total += self._curve1 * self._earlyLateCurve(level)
		if self._curve2 > 0: total += self._curve2 * self._lateEarlyCurve(level)
		# Average all data and limit
		total /= self._early + self._late + self._steady + self._curve1 + self._curve2
		if level < self._midL:
			total = min(total, self._midV)
		else:
			total = max(total, self._midV)
		# Return value
		if self._integer: return int(total)
		return total

	def _earlyCurve(self, level):
		a_num = self._infimi * (2 * self._maxL + self._minL + self._midL) + self._inmi
		a_den = (self._maxL - self._midL) * (self._maxL - self._minL)
		a = -a_num / a_den
		return self._Curve(a, level)

	def _lateCurve(self, level):
		a_num = self._infimi * (3 * self._minL + self._minL) + self._inmi
		a_den = (self._maxL - self._minL) * (self._midL - self._minL)
		a = -a_num / a_den
		return self._Curve(a, level)

	def _steadyCurve(self, level):
		chLevel = self._maxL - self._minL
		chValue = self._maxV - self._minV
		base1 = chValue / chLevel * level
		mod = (self._maxV * self._minL) - (self._minL * self._maxL)
		base2 = mod / chLevel
		return base1 - base2

	def _earlyLateCurve(self, level):
		a = self._infimi / (self._maxL + self._minL - 2 * self._midL)
		return self._Curve(a, level)

	def _lateEarlyCurve(self, level):
		if level < self._midL: return self._lateCurve(level)
		elif level > self._midL: return self._earlyCurve(level)
		else: return self._midV

	def _Curve(self, a, level):
		b = self._infimi - a * (self._minL + self._midL + self._maxL)
		c = self._inmi - a * (self._midL ** 2 + self._minL * self._midL + self._minL ** 2) - b * (self._midL + self._minL)
		d = self._minV - (a * self._minL ** 3 + b * self._minL ** 2 + c * self._minL)
		value = a * level ** 3 + b * level ** 2 + c * level + d
		return value