from flask import Flask
from flask import request
import requests
import json

app = Flask(__name__)


@app.route("/")
def index():
    name = request.args.get("name")
    author = request.args.get("author")
    url = "https://api.zhuishushenqi.com/book/fuzzy-search?query=" + name
    r = json.loads(requests.get(url).text)
    if r:
        for i in r["books"]:
            if i["author"] == author:
                book_id = i["_id"]
    if book_id:
        return book_id
    else:
        return "err"

if __name__ == "__main__":
    app.run()
