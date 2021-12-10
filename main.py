from quart import Quart ,render_template,redirect,url_for
from quart_discord import DiscordOAuth2Session,requires_authorization,Unauthorized

from nextcord.ext import ipc
import os,json

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "true"

settings_file = open("./config/settings.json")
configure = json.load(settings_file)

app = Quart(__name__)
discord = DiscordOAuth2Session(app)
app.secret_key = b'subthis'
app.config["DISCORD_CLIENT_ID"] =configure["client_id"]
app.config["DISCORD_CLIENT_SECRET"] = configure["client_secret"]
app.config["DISCORD_REDIRECT_URI"] = configure["discord_redirect_uri"]
app.config["DISCORD_BOT_TOKEN"] = configure["token"]


@app.route("/callback/")
async def callback():
	try:
		await discord.callback()
	except:
		return redirect(url_for("login"))
	return redirect(url_for("dashboard"))

@app.route("/login/")
async def home():
	return await discord.create_session()

@app.route("/")
async def index():
	return await render_template("index.html")
@app.route("/dashboard/")
async def dashboard():
	user = await discord.fetch_user()
	return await render_template("dashboard.html",user=user)	
if __name__ == "__main__":
	app.run(debug=True)
