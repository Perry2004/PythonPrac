import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['figure.figsize'] = (20.0, 10.0)

data_cco = pd.read_excel('./datasets/sila/0728.HK.xlsx')
data_cdi = pd.read_excel('./datasets/sila/0941.HK.xlsx')

cco_mcr = data_cco.iloc[:, 8]
cdi_mcr = data_cdi.iloc[:, 8]
cco_date = data_cco.iloc[:, 0]
cdi_date = data_cdi.iloc[:, 0]

print("\t\t0728\t\t\t0941")
print("Mean\t", end="")
print(cco_mcr.mean(), "\t", end="")
print(cdi_mcr.mean())

print("SD\t", end="")
print(cco_mcr.std(), "\t", end="")
print(cdi_mcr.std())

print("Median\t", end="")
print(cco_mcr.median(), "\t", end="")
print(cdi_mcr.median())

print("Quartiles\t", end="")
print(cco_mcr.quantile(q=0.25), cco_mcr.quantile(q=0.5), cco_mcr.quantile(q=0.75), "\t", sep="  ", end="")
print(cdi_mcr.quantile(q=0.25), cdi_mcr.quantile(q=0.5), cdi_mcr.quantile(q=0.75), sep="  ")

print("IQR\t\t", end="")
print(cco_mcr.quantile(q=0.75) - cco_mcr.quantile(q=0.25), "\t", end="")
print(cco_mcr.quantile(q=0.75) - cco_mcr.quantile(q=0.25))

# plt.bar(cdi_date, cdi_mcr, width=20.0)
# plt.boxplot(x=cdi_mcr, vert=False)
