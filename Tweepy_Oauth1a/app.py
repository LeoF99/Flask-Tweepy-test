from flask import Flask, render_template, request
import tweepy

app = Flask(__name__)

@app.route('/')
def index():
	
	
	auth = tweepy.OAuthHandler(API_key, API_secret_key)
	auth.set_access_token(Access_token, Access_token_secret)
	api = tweepy.API(auth)
	
	procura = request.args.get('q')
	
	tweetsPublicos = api.user_timeline(procura)

	return render_template('home.html', tweets=tweetsPublicos)

if __name__=='__main__':
	app.run(debug=True)