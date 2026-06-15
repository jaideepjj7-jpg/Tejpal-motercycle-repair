from flask import Flask,render_template,request,redirect
app = Flask(__name__)
import requests
BOT_TOKEN="8064805834:AAFH2zdpZeI5K900YwxrmWKLlyoBQTTY3Ro"
CHAT_ID="8622911486"

def send_telegram_message(name,phone,date, service):
    message=f"""Appointment Booked
    Name: {name}
    Phone:{phone}
    Date:{date}
    Service:{service}
    """
    url=f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url,data={
        "chat_id":CHAT_ID,
        "text":message
    })

@app.route('/')
def home():
    return render_template("home.html")
    
@app.route('/about')
def about ():
    return render_template("about.html")
    
@app.route('/appointment', methods=["GET","POST"])
def appointment():
    if request.method== "POST" :
        name=request.form.get("name")
        phone=request.form.get("phone")
        date=request.form.get("date")
        service=request.form.get("service")
        print(name)
        print(phone)
        print(date)
        print(service)
        send_telegram_message(name,phone,date, service)
        return render_template('success.html',name=name)
    return render_template('appointment.html')

@app.route('/success')
def success():
    return render_template('success.html',name=name)

if __name__ == '__main__':
    app.run(debug=True)