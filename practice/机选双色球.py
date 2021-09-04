import random  #导入random模块

#设置红蓝球范围
redballs = list(range(1, 34))
blueballs = list(range(1, 17))

#设置随机
redrand = random.sample (redballs, 6)
redrand.sort()
bluerand = random.sample (blueballs, 1)

#显示结果
print ('机选红球号码是{}'.format (redrand))
print ('机选蓝球号码是{}'.format (bluerand))
