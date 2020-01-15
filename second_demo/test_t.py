import datetime
from datetime import datetime
# datetime.strptime('Jun 1 2005', '%b %d %Y').date() == date(2005, 6, 1)
a = "2020-01-01"
# c = datetime.strptime("2020-01-01", '%Y-%m-%d ')
b = datetime.fromisoformat("2020-01-01")
# b =datetime.utcfromtimestamp(a//1000)
print(b)