from datetime import datetime
import json
import scratchattach as scr
from flask import Flask, render_template, request
app = Flask(__name__)

def with_offset(function):
	offset = 0
	result = []
	while True:
		returned = function(offset=offset)
		if not returned:
			return result
		result.extend(returned)
		offset += 40

class SettingsManager:
	def __init__(self):
		self.settings_json = json.load(open("settings.json", "r"))

	def refresh_settings(self):
		self.settings_json = json.load(open("settings.json", "r"))

settings_manager = SettingsManager()

def user_load(username):
	user = scr.get_user(username)
	return user, {
		"join_date" : datetime.fromisoformat(user.join_date).strftime("%Y %B %d at %m:%S"),
		"all_followers" : with_offset(user.followers),
		"all_following" : with_offset(user.following),
		"comment_count" : len(user.comments()),
		"all_projects" : with_offset(user.projects)
	}

def project_load(id):
	project=scr.get_project(str(id))
	return project, len(project.comments())

@app.route("/")
def root():
	return render_template("root.html", featured_projects=scr.featured_projects(), dark_mode=settings_manager.settings_json["dark-mode"])

@app.route("/users/<username>")
def user(username):
	user, info = user_load(username)
	return render_template("user.html", user=user, info=info, len=len, dark_mode=settings_manager.settings_json["dark-mode"])

@app.route("/users/<username>/followers")
def user_followers(username):
	user, info = user_load(username)
	return render_template("user_followers.html", user=user, info=info, dark_mode=settings_manager.settings_json["dark-mode"])

@app.route("/users/<username>/following")
def user_following(username):
	user, info = user_load(username)
	return render_template("user_following.html", user=user, info=info, dark_mode=settings_manager.settings_json["dark-mode"])

@app.route("/users/<username>/projects")
def user_projects(username):
	user, info = user_load(username)
	return render_template("user_projects.html", user=user, info=info, dark_mode=settings_manager.settings_json["dark-mode"])

@app.route("/projects/<id>")
def project(id):
	project, comment_count = project_load(id)
	return render_template("project.html", project=project, comment_count=comment_count, dark_mode=settings_manager.settings_json["dark-mode"], turbowarp=settings_manager.settings_json["turbowarp-embed"])

@app.route("/settings", methods=["POST", "GET"])
def settings():
	if request.method == "POST":
		turbowarp_embed = request.form.get('turbowarp-embed')
		dark_mode = request.form.get('dark-mode')
		settings_newjson = json.load(open("settings.json", "r"))
		settings_newjson["turbowarp-embed"] = True if turbowarp_embed == "on" else False
		settings_newjson["dark-mode"] = True if dark_mode == "on" else False
		json.dump(settings_newjson, open("settings.json", "w"), indent=4)
		settings_manager.refresh_settings()
		return render_template("settings.html", success=True, dark_mode=settings_manager.settings_json["dark-mode"])
	else:
		return render_template("settings.html", success=False, dark_mode=settings_manager.settings_json["dark-mode"])

if __name__ == "__main__":
  app.run(debug=True)
