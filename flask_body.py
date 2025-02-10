from flask import Flask,render_template,request
import pyshorteners
class Flask_body:
    app=Flask(__name__)
    @app.route("/",methods=['POST','GET'])
    def home():
        if request.method=='POST':
            url_rec=request.form["url"]
            short_url=pyshorteners.Shortener().tinyurl.short(url_rec)
            return render_template("form.html",new_url=short_url,old_url=url_rec)
        else:
            return render_template("form.html")

