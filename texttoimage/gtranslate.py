import requests

api_url = r"https://translation.googleapis.com/language/translate/v2?key=AIzaSyAa5TXeL8kKbAaViyby-IrNocK3Jwltp_o"

data = {
    "q": "default",
    "source": "en",
    "target": "de",
    "format": "text"
}


def translate(text):
    data["q"] = text
    response = requests.post(api_url, json=data)
    print(response)
    return response.json()["data"]["translations"][0]["translatedText"]


with open("tempdata/REVhpsentences.txt", "r") as inf:
    with open("tempdata/gtranslated.txt", "w+") as outf:
        outf.writelines(translate(t) for t in inf.readlines())
