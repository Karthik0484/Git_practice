import random

otp = random.randint(100000, 999999)

print("Your OTP is:", otp)

from datetime import datetime

date1 = datetime(2024, 1, 1)
date2 = datetime(2024, 2, 1)

difference = date2 - date1

print("Days between dates:", difference.days)