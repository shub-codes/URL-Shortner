from flask import Flask,render_template,request
from qrcode import QRCode
# QR code generation depends on pillow library and QRcode library
import pyshorteners
class Flask_body:
    app=Flask(__name__)
    @app.route("/",methods=["POST","GET"])
    def home():
        if request.method=="POST":
            url_rec=request.form["url"]
            short_url=pyshorteners.Shortener().tinyurl.short(url_rec)
            qr = QRCode(version=1, box_size="3", border="1")
            qr.add_data(url_rec)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            qr_path="static/QRcode.png"
            img.save(qr_path)
            return render_template("form.html",new_url=short_url,old_url=url_rec,qr_path=qr_path)
        else:
            return render_template("form.html")

