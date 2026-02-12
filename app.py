from flask import Flask, render_template, request
from news import *

app = Flask(__name__)
app.config["SECRET_KEY"] = "code636"

@app.route("/",methods =["POST","GET"])
def homePage():

    try:
        type(data)
    except NameError:
        data = getnews(category="general")

    title = "General"
    if request.method == "POST":
        query = request.form.get("search")
        category = request.form.get("category")
        index = request.form.get("card")

        title = query
        if query!=None: 
            data = getnews(q=query.strip().lower() )
        elif index!=None:
            news = data[int(index)]
            return render_template("news.html",news=news,title=news["title"])
        else:   
            title = category
            data = getnews(category=category)
            
    return render_template("index.html",data=data,title=title,len=len, range=range)

@app.route("/health")
def health():
    return "Status OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
