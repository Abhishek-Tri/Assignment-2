#printing current date and time
from datetime import datetime,date

AajKiDate=date.today()
now = datetime.now()
AbhiKaTime = now.strftime("%H:%M %p")

print(AajKiDate,"and",AbhiKaTime)
