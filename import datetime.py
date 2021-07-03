import datetime
import numpy as np

given_date = datetime.date.today()
start = given_date.replace(day=1)
end = datetime.date.today()

BDday= np.busday_count( start, end )
print(BDday)