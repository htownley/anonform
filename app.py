#!/usr/bin/env python
from flask import Flask, flash, redirect, render_template, request, session, \
abort, url_for
from lxml import html 
import requests
from twilio.rest import Client

app = Flask(__name__)

# Your Account SID from twilio.com/console
account_sid = "ACf211000f1e2bdf7ad833b9eaf541dc75"
# Your Auth Token from twilio.com/console
auth_token  = "5a6ab79b242b9d4fdc8a3ea22d3f4a7a"
client = Client(account_sid, auth_token)

@app.route("/", methods=["POST", "GET"])
def hello():
	if request.method == "POST":
   		return redirect(url_for('modal', message_body=request.form["msg"]))
	else:
   		return render_template('main.html')

@app.route("/sms/<message_body>")
def sms(message_body):

	message = client.messages.create(
	    to="+19292849804",
	    from_="+15005550006",
	    body=message_body)
	return "Message Sent! Here is the body: " + message.body

@app.route("/modal/<message_body>")
def modal(message_body):

	message = client.messages.create(
	    to="+19292849804",
	    from_="+15005550006",
	    body=message_body)

	return render_template('modal.html', message_body=message_body)

@app.route("/scrape")
def scrape():
	page = requests.get('http://echenran.pythonanywhere.com/c4gdata')
	tree = html.fromstring(page.content)
	#This will create a list of buyers:
	recipients = tree.xpath('//div[@title="recipient"]/text()')
	#This will create a list of prices
	messages = tree.xpath('//span[@class="message"]/text()')

	f = open('data.txt', 'w')
	f.write('Recipient: '.join(recipients))

	f.write('\n')
	return 'Recipients: '.join(recipients)


# Henry's page
@app.route("/henry")
def henry():

	return render_template('henry.html')

# Neha's page
@app.route("/neha")
def neha():

	return render_template('neha.html')


# Katherine's page
@app.route("/katherine")
def katherine():

	return render_template('katherine.html')

# William's page
@app.route("/william")
def william():
	return render_template('william.html')

@app.route("/tasha")
def tasha():
	
	return render_template('tasha.html')




if __name__ == "__main__":
    # Change the host and port name if you want. The default config is port 
    # 5000 on localhost, which you can access by pointing your browser to
    # `localhost:5000`, `127.0.0.1:5000`, or `0.0.0.0:5000`.
    app.run(host='0.0.0.0', port=5000)
