from flask import Flask, render_template, request
import tweepy

app = Flask(__name__)

@app.route('/')
def index():
	
	
	auth = tweepy.AppAuthHandler(API_key, API_secret_key)
	api = tweepy.API(auth)

	procura = request.args.get('q')
	
	tweetsPublicos = api.search(procura, lang='pt', count=20, result_type="recent")

	return render_template('home.html', tweets=tweetsPublicos)

if __name__=='__main__':
	app.run(debug=True)