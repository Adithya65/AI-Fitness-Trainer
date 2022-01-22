from datetime import date
from datetime import datetime
today = date.today()
now = datetime.now()

text=str(now)
print(text[:16])