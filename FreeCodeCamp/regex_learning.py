import re

def getMail (msg ,dollar):
  m = re.findall(r'\@+(\S*\.\S+)', msg)
  d = re.findall(r'$99+\S', dollar)
  ls = [m,d]
  return ls

str1 = "pedro@carneiro and pedro@carneiro.com and pedro@carneiro.com.br and pedro.e.carneiro@hotmail.com"
str2 = "This banana costs $ 2.99, while this apple costs $ 4.00"
data = getMail(str1,str2)

print(data)
