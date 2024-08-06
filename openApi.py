import random
import string

# 生成一个随机字母
random_letter = random.choice(string.ascii_letters)
print(f"随机字母: {random_letter}")

# 生成一个长度为 10 的随机字符串
random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=5000))
print(f"随机字符串: {random_string}")
