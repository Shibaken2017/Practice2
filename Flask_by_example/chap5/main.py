import datetime
from flask import make_response

import feedparser
from flask import Flask
from flask import render_template
from flask import request

app=Flask(__name__)

RSS_FEEDS={"bbc":"http://feeds.bbci.co.uk/news/rss.xml","cnn":"http://rss.cnn.com/rss/edition.rss"
           ,"fox":"http://feeds.foxnews.com/foxnews/latest"}


@app.route("/")
def get_news():
    query=request.args.get("publication")

    if request.cookies.get("initial_access"):
        print("cokkieがあります")

        init_date=request.cookies.get("initial_access")
        print(request.cookies.get("initial_access"))
    else:
        print("cokkieがありませｎ")

        init_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if not query or query.lower() not in RSS_FEEDS:
        publication="bbc"
    else:
        publication=query.lower()




    feed=feedparser.parse(RSS_FEEDS[publication])

    #return render_template("home.html",articles=feed["entries"])
    response=make_response(render_template("home.html",articles=feed["entries"]))



    expires=datetime.datetime.now()+datetime.timedelta(days=365)
    response.set_cookie("initial_access",init_date,expires=expires)

    return response


if __name__=="__main__":
    app.run(port=5000,debug=True)
