import requests
from bs4 import BeautifulSoup

#----------------------------------------
#ZORLU SANAT SİTESİNDEN ETKİNLİK ADI VE TARİHİ ÇEKME KODU
#----------------------------------------

# Web sitesi URL'si
url = 'https://www.zorlupsm.com/'

# Sayfayı çekmek için requests kullanımı
response = requests.get(url)

# Sayfa içeriğini BeautifulSoup ile ayrıştırmak
soup = BeautifulSoup(response.text, 'html.parser')

# h2 ve b etiketleri içindeki classlara ait verileri alma
data = soup.find_all('h2',class_='font-size-m') #etkinlik adı
data2 = soup.find_all('b',class_='font-size-m') #etkinlik tarihi

# Bulunan verileri yazdır 
for item, date in zip(data, data2):
    print(f"Etkinlik Adı: {item.text}, Etkinlik Tarihi: {date.text}")
