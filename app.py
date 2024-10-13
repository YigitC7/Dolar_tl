from flask import Flask, render_template, request
import requests

url = "https://api.exchangerate-api.com/v4/latest/USD"
response = requests.get(url)
data = response.json()
dolar = data['rates']['TRY']

python_Flask_main=Flask(__name__)

@python_Flask_main.route("/")
def index():
	return render_template("/index.html",dolar = dolar)

@python_Flask_main.route("/hesapla",methods=["GET","POST"])
def hesapla():
	try:
		if request.method == "POST":
			girdi = request.form.get("girdi")
			girdi = float(girdi)
			return render_template("/hesapla.html",
				sonuc=girdi*dolar,
				dolar=dolar,
				girdi=girdi)
		else:
			return render_template("/hata.html",hata="Veri bulunamadı :/")
	except:
		return render_template("/hata.html",hata="Lütfen sadece rakamsal değer girin :/")

if __name__ == "__main__":
	python_Flask_main.run(debug = True)