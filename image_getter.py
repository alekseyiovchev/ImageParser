import re
import requests

def getType(url):
    return re.search("(\.png|\.jpg|\.svg)", url)



res = requests.get(input('Вставьте URL: '))
match = re.findall("[A-z/\-0-9=:\.]+\.png|[A-z/\-0-9=:\.]+\.jpg|[A-z/\-0-9=:\.]+\.svg", res.text)

print(match)

for i in range(0, len(match)):
    try:
        image = requests.get(match[i])
        type = getType(match[i])

        if image and type:
            file = open(r"D:\imgs\img{}{}".format(i, type.group(0)), "wb")
            file.write(image.content)
            file.close()
    except Exception as e:
        print("Link {} is incorrect".format(match[i]))
