import urllib.request
import json
from datetime import datetime

def fiyat_getir():
    # Güncel döviz kurlarını çeken ücretsiz API
    doviz_url = "https://open.er-api.com/v6/latest/USD"
    # Bitcoin fiyatını çeken ücretsiz API
    crypto_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

    req = urllib.request.Request(doviz_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        doviz_data = json.loads(response.read().decode())
        usd_try = doviz_data["rates"]["TRY"]
        eur_usd = doviz_data["rates"]["EUR"]
        eur_try = usd_try / eur_usd

    req_crypto = urllib.request.Request(crypto_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req_crypto) as response:
        crypto_data = json.loads(response.read().decode())
        btc_usd = crypto_data["bitcoin"]["usd"]

    tarih = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    rapor = f"""
======================================
 FİYAT RAPORU - {tarih}
======================================
 USD / TRY : {usd_try:.2f} TL
 EUR / TRY : {eur_try:.2f} TL
 Bitcoin   : ${btc_usd:,.2f}
======================================
"""
    return rapor

def rapora_kaydet(metin):
    with open("fiyat_raporu.txt", "a", encoding="utf-8") as dosya:
        dosya.write(metin + "\n")
    print("✓ Rapor 'fiyat_raporu.txt' dosyasına başarıyla kaydedildi!")

if __name__ == "__main__":
    print("Veriler çekiliyor, lütfen bekleyin...")
    try:
        sonuc = fiyat_getir()
        print(sonuc)
        rapora_kaydet(sonuc)
    except Exception as e:
        print("Bir hata oluştu:", e)
      
