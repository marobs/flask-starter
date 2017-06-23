from flask import *
import helpers

@main.route('/')
def main_route():
	templateVar = helpers.helperFunction()
	return render_template("main.html", templatevar=templateVar)
