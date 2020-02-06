from bs4 import BeautifulSoup
import requests
import pandas as pd
dataNama = []
dataJumlah = []
obj = []
hasil = {}
def getContent():
    page = requests.get("https://stackoverflow.com/tags")
    soup = BeautifulSoup(page.content, 'html.parser')
    detail = soup.find_all('div',class_="tag-cell")

    for x in detail:
        nama = x.find('a', class_="post-tag")
        jumlah = x.find('span', class_="item-multiplier-count")
        temp = {"Bahasa Pemrograman":nama.text,"Jumlah Pertanyaan":jumlah.text}
        obj.append(temp)
        hasil.update(temp)
        dataNama.append(nama.text)
        dataJumlah.append(jumlah.text)

    #data = {'Bahasa Pemrograman': dataNama, 'Jumlah Pertanyaan': dataJumlah}
    #df = pd.DataFrame(data)
    #print(df)
    return obj