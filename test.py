# import algo_idle_param
import backtest
import trend_friend
from datetime import datetime

# for sell_num in [3,5,7]:
# 	for buy_num in [4,6,8]:
# 		tester = backtest.Test("SBER_190101_191231_hr.csv")
# 		alg = algo_idle_param.chaotic(sell_num,buy_num)
# 		while 1:
# 			try:
# 				tester.send_action(alg.iter(tester.get_row()))
# 			except IndexError:
# 				break
# 			except Exception as e:
# 				if e.args[0]=="overbought":
# 					tester.send_action("SELL")
# 				elif e.args[0]=="oversold":
# 					tester.send_action("BUY")
# 				else:
# 					raise Exception(e)
# 		result = tester.finish()
# 		print("\nbuy_num={0},sell_num={1},result:{2}, change:{3}%".format(buy_num,sell_num,result[0],result[1]))

# tester = backtest.Test("SBER_190101_191231_hr.csv")
# tester.send_action("BUY")
# for i in range(100):
# 	print(tester.get_row())
# 	act = input()
# 	if act:
# 		tester.send_action(act)
# 	else:
# 		tester.send_action()
	# print(tester.)

# for ma1 in [15,20,30,50,75,100]:
# 	for ma2 in [1,3,5,7,9,12]:

# for ma1 in [1,3,5,7,9,12]:
# 	for ma2 in [15,20,30,50,75,100]:
for ma1 in [5,7,9]:
	for ma2 in [15,30,50]:
		start_time=datetime.now()
		tester = backtest.Test("SBER_190101_191231_hr.csv")
		alg = trend_friend.Trend_Friend(ma2,ma1)
		while True:
			try:
				tester.send_action(alg.iter(tester.get_row()))
			except IndexError:
				print("ma_long={0}, ma_short={1}, result (rub,%):".format(ma2,ma1))
				print(tester.finish())
				break
			except Exception:
				print("ma_long={0}, ma_short={1}, FAIL".format(ma2,ma1))
				break
		print("time:")
		print(datetime.now()-start_time)
		print()

		

# tester = backtest.Test("SBER_190101_191231_hr.csv")
# alg = algo_idle_param.chaotic()
# for i in range(30):
# 	for j in range(50):
# 		tester.send_action()
# 	tester.send_action(alg.iter(tester.get_row()))
# 	print(tester.count_value())
# print("\nresult:")
# print(tester.finish())