import requests as bengak
print("Pilih Bahasa Asal")
print("1. Indonesia | 2. English")
starting = int(input("Pilih Menu = "))
content = input("Input your text = ")
result = None
if starting == 1:
    link = "https://translate.google.co.id/?hl=id&sl=id&tl=en&text=" + content + "&op=translate"
    result = bengak.get(link)
else :
    link = "https://translate.google.co.id/?hl=id&sl=en&tl=id&text=" + content + "&op=translate"
    result = bengak.get(link)
print(result.text)
print(result.status_code)