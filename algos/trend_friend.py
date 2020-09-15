
# скользящая средняя по n (иначе говоря ma(n)) - это среднее арифметическое по n последним значениям

# Суть:

# скользящая средняя 1 - средняя по n последним ценам
# скользящая средняя 2 - средняя по m последним ценам
# n<m
# Если скользящая средняя 1 больше скользящей средней 2, покупаем, иначе продаем
# При смене знака меняем позицию



# псевдокод:

# получить m цен
# сохранить их в истории
# посчитать ma1,ma2

# итерация:
# 	получить цену
# 	добавить цену в историю, удалить самую старую цену (история хранит последние m цен)
# 	посчитать ma1,ma2

# 	если ma1<ma2:
# 		тренд = вверх
# 	иначе:
# 	 	тренд = вниз

# 	если тренд = вверх:
# 		если позиция<0:
# 			купить
# 	иначе:
# 		если позиция>0:
# 			продать



class Trend_Friend:

	_ma_short_frame=0
	_ma_long_frame=0
	_last_values=[]
	_uptrend=False
	_pos=0
	# _ma_short,_ma_long=0


	def __init__(self, ma_long=100, ma_short=5):
		self._ma_short_frame=ma_short
		self._ma_long_frame=ma_long
		for i in range(max(ma_long,ma_short)):
			self._last_values.append(0)


	def iter(self, row):

		price=row[2]
		self._last_values.append(price)
		# if len(self._last_values)>self.ma_long:
		self._last_values.pop(0)
		ma_short=self.__ma(self._ma_short_frame)
		ma_long=self.__ma(self._ma_long_frame)

		# print(ma_long)
		# print(ma_short)

		if ma_short>ma_long:
			self._uptrend=True
		else:
			self._uptrend=False

		if self._pos>=0 and self._uptrend==False:
			self._pos-=1
			return "SELL"
		elif self._pos<=0 and self._uptrend==True:
			self._pos+=1
			return "BUY"
		else:
			return None
			

	def __ma(self,n):
		value = 0
		for price in self._last_values[-n:]:
			value+=price
		return value/n


