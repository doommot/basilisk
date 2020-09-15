import csv
# ['030119', '11:00:00', '186.3700000', '188.9500000', '186.0000000', '188.5200000', '7183730']
# [03/07/20, 10:00:00, 195.650000000, 10]

buy_action = "BUY"
sell_action = "SELL"

# logfile = "log.csv"


class Test:


	_history = []
	_counter = 1
	_result = 0
	_position = 0
	_timeframe = None
	# _max_pos = 10
	_init_money = 0
	logfile = "log.csv"


	def __init__(self, filename, timeframe = None, init_money = None, logfile="log.csv"):
		with open(filename) as csvfile:
			self._history=[]
			reader = csv.reader(csvfile)
			for row in reader:
				self._history.append(row)
		for row in self._history[1:]:
			row[2]=float(row[2])
			row[3]=float(row[3])
			# row[4]=float(row[4])
			# row[5]=float(row[5])
			# row[6]=float(row[6])
		self._timeframe = timeframe
		# self._max_pos = max_pos
		if init_money:
			self._init_money = init_money
		else:
			self._init_money = 10*self._history[1][2]
		self.logfile="log.csv"
		# with open 


	def get_row(self):
		# try:
		return self._history[self._counter]
		# except IndexError:
		# 	return None


	def send_action(self, action=None, n=1):
		if action:
			cost=self.get_row()[2]
			if action == buy_action:
				# print("buy at", cost)
				if self._init_money+self._result-cost*n > 0:
					self._position+=n
					self._result-=cost*n
				else:
					raise Exception("overbought")

			elif action == sell_action:
				# print("sell at", cost)
				if self._init_money+2*(self._position-n)*cost+self._result > 0:
					self._position-=n
					self._result+=cost*n
				else:
					raise Exception("oversold")
			else:
				raise ValueError("Unknown type of action")

		# print("buycheck:",str(self._init_money+self._result-cost*n))
		# print("sellcheck:",str(self._init_money+2*(self._position-n)*cost+self._result))
		self.__log()
		self.__skip()


	def __skip(self):
		# vol=0
		if self._timeframe:
			pass
		else:
			if self._history[self._counter][2]==self._history[self._counter+1][2]:
				while self._history[self._counter][2]==self._history[self._counter+1][2]:
					# vol+=self.get_row()[3]
					self._counter+=1
				# vol+=self.get_row()[3]
				# self._history[self._counter][3]+=vol
		self._counter+=1
		# print(self.get_row())
			

	def finish(self):
		self._result=self.__count_value()
		self._position=0
		return self._result


	def __count_value(self):
		value = self._result + self._position*self.get_row()[2]
		per_init = value/self._init_money*100
		return round(value,2),round(per_init,2)


	def __log(self):
		with open (self.logfile,'a+') as csvfile:
			logger = csv.writer(csvfile)
			row=self.get_row()[0:3]
			row.append(self._position)
			row.append(self.__count_value())
			logger.writerow(row)
			# print(row)

