#!/usr/bin/env python
from flask import Flask, flash, redirect, render_template, request, session, \
abort, url_for
from lxml import html 
import requests
from twilio.rest import Client

app = Flask(__name__)

# Your Account SID from twilio.com/console
account_sid = "AC1c04fe37d935a15562607e929cff7b85"
# Your Auth Token from twilio.com/console
auth_token  = "c7cd4c8ed7c57061b3f03ac839b146b9"
client = Client(account_sid, auth_token)

@app.route("/")
def hello():

	
   		return render_template('main.html')

@app.route("/sendSms", methods=["POST", "GET"])
def hi():
	if request.method == "POST":
		print(request.form["tel"])
		print(request.form["body"])
		print(request.form["recipient"])
   		return redirect(url_for('modal', message_body=request.form["body"], phone=request.form["tel"], name=request.form["recipient"]))
	else:
		f = open('data.txt', 'r')
		names = []
		messages = []
		isMessage = 0
		cursor = f.readline()
		while (cursor != ""):
			if (isMessage):
				print("New message: " + cursor)
				messages.append(cursor)
			
			else :
				
				if (cursor == "&&&\n"):
					isMessage = 1

				else:
					names.append(cursor)

			cursor = f.readline()

	
   		return render_template('index.html', messages=messages, names=names)

@app.route("/sms/<message_body>")
def sms(message_body):

	message = client.messages.create(
	    to="9292849804",
	    from_="8448538277",
	    body="Message from: " +  message_body)
	return "Message Sent! Here is the body: " + message.body

@app.route("/modal")
def modal():
	phone =  request.args['phone']
	name = request.args['name']
	message_body = request.args['message_body']

	message = client.messages.create(
	    to=phone,
	    from_="8448538277",
	    body="What's up " + name + "? Here is the crazy news: " +  message_body)

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
	f.write('\n'.join(recipients));
	f.write('\n&&&\n')
	f.write('\n'.join(messages))

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




if __name__ == "__main__":
    # Change the host and port name if you want. The default config is port 
    # 5000 on localhost, which you can access by pointing your browser to
    # `localhost:5000`, `127.0.0.1:5000`, or `0.0.0.0:5000`.
    app.run(host='0.0.0.0', port=5000)
