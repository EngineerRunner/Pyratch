from datetime import datetime
import scratchattach
from flask import Flask, render_template
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

def user_load(username):
	user = scratchattach.get_user(username)
	return user, {
		"join_date" : datetime.fromisoformat(user.join_date).strftime("%Y %B %d at %m:%S"),
		"all_followers" : with_offset(user.followers),
		"all_following" : with_offset(user.following),
		"comment_count" : len(user.comments()),
		"all_projects" : with_offset(user.projects)
	}

def project_load(id):
	project=scratchattach.get_project(str(id))
	return project, len(project.comments())

@app.route("/")
def root():
	return render_template("root.html")

@app.route("/users/<username>")
def user(username):
	user, info = user_load(username)
	return render_template("user.html", user=user, info=info, len=len)

@app.route("/users/<username>/followers")
def user_followers(username):
	user, info = user_load(username)
	return render_template("user_followers.html", user=user, info=info)

@app.route("/users/<username>/following")
def user_following(username):
	user, info = user_load(username)
	return render_template("user_following.html", user=user, info=info)

@app.route("/users/<username>/projects")
def user_projects(username):
	user, info = user_load(username)
	return render_template("user_projects.html", user=user, info=info)

@app.route("/projects/<id>")
def project(id):
	project, comment_count = project_load(id)
	return render_template("project.html", project=project, comment_count=comment_count)


if __name__ == "__main__":
  app.run(debug=True)
