# Colleen is turning N years old! Therefore, she has N candles of various heights on her cake, and candle I has height I.
# Because the taller candles tower over the shorter ones, Colleen can only blow out the tallest candles.
# Given the height I for each individual candle, find and print the number of candles she can successfully blow out.
from collections import Counter

# Method 1
def birthdayCakeBlownCandles1(n, height_arr):
    return height_arr.count(max(height_arr))

# Method 2
def birthdayCakeBlownCandles2(n, height_arr):
    return max(Counter(height_arr).items())[1]

print("**What is Colleen's Age**")
n = int(input().strip())
print("**Enter the height of the candles**")
height_arr = [int(x) for x in input().strip().split(' ')]

result = birthdayCakeBlownCandles1(n, height_arr)
print(result)

result = birthdayCakeBlownCandles2(n, height_arr)
print(result)
