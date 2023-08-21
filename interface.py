import scratchattach as scr
from flask import Flask, render_template, abort
app = Flask(__name__)

def user_load(username):
	user=scr.get_user(username)
	user.year = user.join_date.split("-")[0]
	user.month = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}[int(user.join_date.split("-")[1][1:] if len(user.join_date.split("-")[1]) == 1 else user.join_date.split("-")[1])]
	user.day = user.join_date.split("-")[2].split("T")[0]
	user.time = user.join_date.split("T")[1].split("Z")[0].split(".")[0]
	user.all_followers = []
	result = ["temp"]
	offset = 0
	while result != []:
		result = user.followers(offset=offset)
		user.all_followers += result
		offset += 40
	user.follower_count = user.stats()["followers"]
	result = ["temp"]
	user.all_following = []
	offset = 0
	while result != []:
		result = user.following(offset=offset)
		user.all_following += result
		offset += 40
	user.following_count = user.stats()["following"]
	try:
		user.comment_count = len(user.comments())
	except:
		abort(404)
	result = ["temp"]
	user.all_projects = []
	offset = 0
	while result != []:
		result = user.projects(offset=offset)
		user.all_projects += result
		offset += 40
	user.project_count = len(user.all_projects)
	return user

def project_load(id):
	project=scr.get_project(str(id))
	project.comment_count = len(project.comments())
	return project

@app.route("/")
def root():
	return render_template("root.html")

@app.route("/users/<username>")
def user(username):
	user=user_load(username)
	return render_template("user.html", user=user, len=len)

@app.route("/users/<username>/followers")
def user_followers(username):
	user=user_load(username)
	return render_template("user_followers.html", user=user)

@app.route("/users/<username>/following")
def user_following(username):
	user=user_load(username)
	return render_template("user_following.html", user=user)

@app.route("/users/<username>/projects")
def user_projects(username):
	user=user_load(username)
	return render_template("user_projects.html", user=user)

@app.route("/projects/<id>")
def project(id):
	project = project_load(id)
	return render_template("project.html", project=project)


if __name__ == "__main__":
  app.run(debug=True)
