import random
import numpy as np
import math
from datetime import datetime

luckyNumber = random.uniform(1, 100)

numbersArray = np.array([luckyNumber])

roundedLuckyNumber = math.ceil(numbersArray[0])

todayDate = datetime.now().strftime("%Y-%m-%d")

print("Lucky Day Generator")
print(f"Today's date: {todayDate}")
print(f"Your lucky number is: {roundedLuckyNumber}")