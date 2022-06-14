from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import User, Note

views = Blueprint("views", __name__)


@views.route("/")
@login_required
def home():
    return render_template("home.html", user=current_user)


@views.route("/account")
@login_required
def compte():
    return render_template("account.html", user=current_user)


@views.route("/pass-recov")
def pass_recov():
    return render_template("pass_recov.html", user=current_user)


@views.route("/pass-reinit")
def pass_reinit():
    return render_template("pass_reset.html", user=current_user)


@views.route("/modifs/<champ>")
@login_required
def modification(champ):
    return render_template("modifs.html", user=current_user, champ=champ)




