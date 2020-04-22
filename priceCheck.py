import requests
from bs4 import BeautifulSoup
import smtplib

def checkPrice():
  url ="https://www.saturn.de/de/product/_sony-playstation-4-pro-1tb-jet-black-standalone-2495539.html"

  dictionary ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0"}

  page = requests.get(url,headers=dictionary)

  soup = BeautifulSoup(page.content,"html.parser")
   
  title = soup.find("h1",itemprop="name").get_text()
  price = soup.find(class_="price-details").get_text()

  
  print(title.strip())
  print(price.strip())

  priceAsFloat = float(price[3:6])

  if(priceAsFloat<385.0):
     send_mail()
     print("Email was sent!")
  else:
     print("Nothing changed.")
   
  



def send_mail():
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()


    password = input("Please type in the server password:")
    server.login("timo.schessl@gmail.com",password)

    subject="PS4 pro price Saturn"
    body ="PS4 is now cheaper at Saturn!"

    message= f"Subject: {subject}\n\n{body}"

    server.sendmail(
      "timo.schessl@gmail.com",
      "timo.schessl@gmail.com",
       message)

    
checkPrice()









