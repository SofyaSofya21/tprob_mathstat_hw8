import numpy as np
import scipy.stats as stats

# 1 -----------------------
print("Task 1")

# 1) Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого 
# кредитного скоринга (ks):
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
# Найдите ковариацию этих двух величин с помощью элементарных действий, а затем с помощью функции 
# cov из numpy
# Полученные значения должны быть равны.
# Найдите коэффициент корреляции Пирсона с помощью ковариации и среднеквадратичных отклонений 
# двух признаков, а затем с использованием функций из библиотек numpy и pandas.

zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110]
ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]

# Ковариация
zp_ks = []
for i in range(len(zp)):
    zp_ks.append(zp[i]*ks[i])
print(zp_ks)
M_zp_ks = np.mean(zp_ks) # 81141.7 
M_zp = np.mean(zp) # 101.4
M_ks = np.mean(ks) #  709.9
print(M_zp_ks, M_zp, M_ks)
cov = M_zp_ks - M_zp * M_ks # 9157.84
print(cov)

print(np.cov(zp,ks)) # 10175.3778
print(np.cov(zp,ks,ddof=0)) # 9157.84

# Корреляция

sigma_zp = np.std(zp,ddof=0)
sigma_ks = np.std(ks,ddof=0)
print( sigma_zp, sigma_ks)
cov = np.cov(zp,ks,ddof=0)
r = cov/(sigma_ks*sigma_zp) # 0.8875
print(r)
print(np.corrcoef(zp,ks)) # 0.8875
df = pd.DataFrame({'zp':zp,'ks':ks})
print(df['zp'].corr(df['ks'])) # 0.8875