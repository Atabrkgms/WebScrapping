import requests
import pandas as pd

url = "https://zagorapi.yemek.com/search/recipe"

res = []
y = 0 
for x in range(1,100):

    querystring = {"Start":f"{x}","Rows":"100"}

    headers = {
    "cookie": "__cf_bm=J4CepJ1U.cj3eivpAmUi5eIgI.tfN8cKPLCSUHK9C0A-1699453039-0-AVODtiOe4a%2F4pQ6QXld7wPaWJrzNdttwjZDzRdsdwvfqkpLYQmYqQuzAc5tfSZHawBoDcEFH2drbnGD%2FaIJbwv4%3D",
    "authority": "zagorapi.yemek.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7,fr;q=0.6",
    "origin": "https://yemek.com",
    "referer": "https://yemek.com/",
    "sec-ch-ua": "Google Chrome;v=119, Chromium;v=119, Not?A_Brand;v=24",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "macOS",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
    y+=1
    print(y)
    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()

    for p in data['Data']['Posts']:
        res.append(p)


df = pd.json_normalize(res)

df.to_csv('firstResults.csv')