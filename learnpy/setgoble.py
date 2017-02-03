import sys
ddir = 'C:\\Python\\Python35\\Lib\\test\\test_decimal.py'
sys.path.append(ddir)
import decimal
a = decimal.Decimal(1)/decimal.Decimal(7)
print(a)