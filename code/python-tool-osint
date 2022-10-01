import requests
import trio
import httpx
from ignorant.modules.social_media.instagram import instagram
from ignorant.modules.shopping.amazon import amazon

phone__number = int(input("Enter the phone number: "))
url = "https://accounts.snapchat.com/accounts/validate_phone_number"
cookies = {
   "xsrf_token":'BtpZ6sL9OenEJJYbQXFEsg'
 }
headers = {
 "accept": "*/*",
 "accept-encoding": "gzip, deflate, br",
 "accept-language": "ar,en;q=0.9,en-US;q=0.8",
 "content-type": "application/x-www-form-urlencoded; charset=utf-8",
 "sec-fetch-dest": "empty",
 "sec-fetch-mode": "same-origin",
 "sec-fetch-site": "same-origin",
 "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Mobile Safari/537.36"
 }
data = {"phone_country_code":"IN","phone_number":phone__number,"xsrf_token":"BtpZ6sL9OenEJJYbQXFEsg"}
req = requests.post(url,data=data,headers=headers,cookies=cookies).json()
text = str(req)
 #print(text)
if text.find('OK')>=0:
    print(f"{phone__number}==> Not Exist In Snapchat")
else:
    print(f"{phone__number}==> Exist In Snapchat")
email = phone__number
x = requests.Session()

h={"origin": "https://www.facebook.com","referer":"https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0","sec-fetch-dest": "empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin","sec-gpc": "1","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36"}
r = x.get("https://m.facebook.com/login",headers=h)
a = r.text.split('type="hidden" name="jazoest" value="', 1)[1]
jaz = a.split('"', 1)[0]
b = r.text.split('<input type="hidden" name="lsd" value="', 1)[1]
isd = b.split('"',1)[0]
c = r.text.split('"dtsg_ag":{"token":"', 1)[1]
token=c.split('"',1)[0]
d = r.text.split('"__spin_r":',1)[1]
spin_r = d.split(',', 1)[0]
e = r.text.split('"__spin_t":', 1)[1]
spin_t = e.split(',', 1)[0]
f = r.text.split('"hsi":"', 1)[1]
hsi = f.split('",', 1)[0]

data = f"jazoest={jaz}&lsd={isd}&email={email}&did_submit=1&user=0&a=1&dyn=7xe6Fo4OQ1PyWwHBWo5O12wAxu13wqovzEdEc8uw9-3K4o1j8hwem0nCq1ewcG0KEswaq0yE7i0n2US1kyE1oU884y0Mo2swdK0D83mwaS0zE&csr=&req=6&beoa=0&pc=PHASED%3ADEFAULT&dpr=1&ccg=EXCELLENT&rev={spin_r}&s=70zg4m%3Ae3atk5%3A42buqc&hsi={hsi}&comet_req=0&spin_r={spin_r}&spin_b=trunk&__spin_t={spin_t}"

h = {"content-type":"application/x-www-form-urlencoded",
"origin":"https://www.facebook.com",
"referer":"https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0",
"sec-fetch-dest":"empty",
"sec-fetch-mode":"cors",
"sec-fetch-site":"same-origin",
"sec-gpc":"1",
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36",
"x-fb-lsd": isd}

r2 = x.post("https://www.facebook.com/ajax/login/help/identify.php?ctx=recover" , data=data, headers=h)
c = r2.cookies
dic = c.get_dict()

if "sfiu" in dic.keys():
  print(f"{email}==> Exist In Facebook")
else:
  print(f"{email}==> Not Exist In Facebook")
async def main():
    phone=phone__number
    country_code="91"
    client = httpx.AsyncClient()
    out = []
    await instagram(phone, country_code, client, out)
    y=str(out)
    if "True" in y:
        print(f"{email}==>> Exist In  Instagram")
    else : 
     print(f"{email}==>> Not Exist In Instagram")
    # print(y)
    await amazon(phone, country_code, client, out)
    z=str(out)
    if "True" in z:
        print(f"{email}==>> Exist In Amazon")
    else : 
     print(f"{email}==>> Not Exist To Amazon")
    await client.aclose()
trio.run(main)
