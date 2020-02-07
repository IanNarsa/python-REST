from bs4 import BeautifulSoup
import requests
import pandas as pd
dataNama = []
dataJumlah = []
obj = []
hasil = {}
def getContent():
    print("masuk")
    page = requests.get("https://stackoverflow.com/tags")
    soup = BeautifulSoup(page.content, 'html.parser')
    detail = soup.find_all('div',class_="js-tag-cell")
    for x in detail:
        nama = x.find('a', class_="post-tag")
        #print(nama)
        n = x.find('div', class_="mt-auto")
        jumlah = n.find('div', class_="grid--cell")
        #print(jumlah)
        temp = {"Bahasa Pemrograman":nama.text,"Jumlah Pertanyaan":jumlah.text}
        #print(temp)
        obj.append(temp)
        hasil.update(temp)
        dataNama.append(nama.text)
        dataJumlah.append(jumlah.text)

    #data = {'Bahasa Pemrograman': dataNama, 'Jumlah Pertanyaan': dataJumlah}
    #df = pd.DataFrame(data)
    #print(obj)
    return obj
#getContent()