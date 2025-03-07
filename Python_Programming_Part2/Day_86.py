"""
Requests Module in Python
    It is the HTTP library that enables developers to send HTTP requests in python.
    It is the external module.
    It is mainly used for web scraping.

    There mainly two requests
    1)get request
    2)post request
"""
#get Requests
import requests
response=requests.get("https://www.google.com/search?q=code+with+harry&sca_esv=efe6d24389f8b041&rlz=1C1GCEB_enIN1042IN1042&sxsrf=ADLYWIL1sMrIxj3vaU-uNqxH_u7o_qSiRw%3A1735835074716&ei=wr12Z8-xK8movr0P5tm1mQY&ved=0ahUKEwjPmpHIudeKAxVJlK8BHeZsLWMQ4dUDCBA&uact=5&oq=code+with+harry&gs_lp=Egxnd3Mtd2l6LXNlcnAiD2NvZGUgd2l0aCBoYXJyeTIHECMYJxjqAjIHECMYJxjqAjIHECMYJxjqAjIHECMYJxjqAjIHECMYJxjqAjINEC4Y0QMYxwEYJxjqAjINEC4Y0QMYxwEYJxjqAjIHECMYJxjqAjIHECMYJxjqAjINEC4Y0QMYxwEYJxjqAkj9dFCTOFjscXABeAGQAQCYAQCgAQCqAQC4AQPIAQD4AQGYAgGgAg-oAgqYAw_xBV8KMoQDAWRckgcBMaAHAA&sclient=gws-wiz-serp")
print(response.text)
print(response.status_code)

#Post Requests
import requests
url="https://api.example.com/login"
headers={"User Agent":"Mozilla/5.0(Windows NT 10.0 )"
        ,"Content Type":"application/json"}
data={"username":"myusername",
      "Password":"mypassword"}

response=requests.post(url,headers=headers,json=data)

print(response.text)
