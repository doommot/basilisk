import backtest
import trend_friend
from datetime import datetime

# ma2=9
# ma1=100

ma1=1
ma2=20

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