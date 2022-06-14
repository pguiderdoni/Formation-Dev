from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import User, Note
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

auth = Blueprint("auth", __name__)


@auth.route("/", methods=["GET", "POST"])
@login_required
def notes():
    if request.method == "POST":
        titre = request.form.get("titre")
        check_note = Note.query.filter_by(titre=titre).first()
        if check_note:
            flash("Ce titre existe déjà,", category="fail")
            return redirect(url_for("auth.notes"))
        else:
            corps = request.form.get("")
            new_note = Note(titre=titre, corps="", user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
    return render_template("home.html", user=current_user)


@auth.route("/delete-note/<champ>")
@login_required
def delete_note(champ):
    note = Note.query.filter_by(id=champ).first()
    if note:
        db.session.delete(note)
        db.session.commit()
        flash("Note supprimée!", category="success")
        return redirect(url_for("auth.notes"))
    else:
        flash("Une erreur est survenue,", category="fail")
        return render_template("home.html", user=current_user)


@auth.route("//<value>", methods=["GET", "POST"])
@login_required
def edit_note(value):
    if request.method == "GET":
        note = Note.query.get(value)
        return render_template("home.html", user=current_user, id=value, note=note)
    elif request.method == "POST":
        note = Note.query.filter_by(id=value).first()
        if note:
            corps = request.form.get("note")
            note.corps = corps
            db.session.commit()
            flash("Note éditée!", category="success")
            return redirect(url_for("auth.notes"))
        else:
            flash("Une erreur est survenue,", category="fail")
    return render_template("home.html", user=current_user)


@auth.route("/inscription", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("views.home"))
    if request.method == "POST":
        nom = request.form.get("nom")
        email = request.form.get("email")
        adresse = request.form.get("adresse")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        question_sec = request.form.get("question")
        reponse_sec = request.form.get("reponse")
        print(f"{nom},{email}")
        user = User.query.filter_by(email=email).first()
        if user:
            flash("Compte non créé, cet utilisateur existe déjà", category="fail")
            return render_template("signup.html", user={})
        else:
            if password == password2:
                new_user = User(nom=nom, email=email, adresse=adresse,
                                password=generate_password_hash(password, method="sha256"),
                                question_secrete=question_sec, reponse_secrete=reponse_sec)
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user)
                flash("Votre compte est créé!", category="success")
                return redirect(url_for("views.home"))
            else:
                flash("Compte non créé, vérifiez vos mots de passe", category="fail")
                return render_template("signup.html", user={})
    return render_template("signup.html", user=current_user)


@auth.route("/modifs/<champ>", methods=["GET", "POST"])
@login_required
def modification(champ):
    if request.method == "POST":
        old_password = request.form.get("old_password")
        new_password = request.form.get("new_password")
        new_password2 = request.form.get("new_password2")
        new_nom = request.form.get("new_nom")
        new_email = request.form.get("new_email")
        new_adresse = request.form.get("new_adresse")
        user = User.query.filter_by(email=current_user.email).first()
        if champ == "nom":
            user.nom = new_nom
            db.session.commit()
            flash('Nom modifié avec succès!', 'success')
            return redirect(url_for("views.compte"))
        if champ == "email":
            user_db = User.query.filter_by(email=new_email).first()
            if not user_db:
                user.email = new_email
                db.session.commit()
                flash('E-mail modifié avec succès!', 'success')
                return redirect(url_for("views.compte"))
            else:
                flash("Cet E-mail est déjà enregistré,", category="fail")
                return render_template("modifs.html", user=current_user, champ=champ)
        if champ == "adresse":
            user.adresse = new_adresse
            db.session.commit()
            flash('Adresse modifiée avec succès!', 'success')
            return redirect(url_for("views.compte"))
        if champ == "password":
            if check_password_hash(user.password, old_password):
                if new_password == new_password2:
                    user.password = generate_password_hash(new_password, method="sha256")
                    db.session.commit()
                    flash('Mot de passe modifié avec succès!', 'success')
                    return redirect(url_for("views.compte"))
                else:
                    flash("Les 2 mots de passe ne correspondent pas,", category="fail")
                    return render_template("modifs.html", user=current_user, champ=champ)
            else:
                flash("Mot de passe actuel incorrect,", category="fail")
                return render_template("modifs.html", user=current_user, champ=champ)
    return render_template("account.html", user=current_user)


@auth.route("/pass-recov", methods=["GET", "POST"])
def pass_recov():
    if request.method == "POST":
        email = request.form.get("email")
        email2 = request.form.get("email2")
        email3 = request.form.get("email3")
        reponse = request.form.get("reponse_secrete")
        password2 = request.form.get("password2")
        password3 = request.form.get("password3")
        if email:
            user = User.query.filter_by(email=email).first()
            if user:
                return render_template("pass_recov.html", user=current_user, email=email,
                                       question_secrete=user.question_secrete)
            else:
                flash("Utilisateur inconnu,", category="fail")
                return redirect(url_for("auth.login"))
        if email2:
            user = User.query.filter_by(email=email2).first()
            if user:
                if reponse == user.reponse_secrete:
                    return render_template("pass_reset.html", user=current_user, email=email2)
                else:
                    flash("Réponse incorrecte,", category="fail")
                    return render_template("pass_recov.html", user=current_user)
        if email3:
            user = User.query.filter_by(email=email3).first()
            print(f"{email}")
            if password2 == password3:
                user.password = generate_password_hash(password2, method="sha256")
                db.session.commit()
                flash('Mot de passe modifié avec succès!', 'success')
                return redirect(url_for("auth.login"))
            else:
                flash('Les mots de passe sont différents,', 'fail')
                return render_template("pass_reset.html", user=current_user, email=email2)
        else:
            flash("Utilisateur inconnu,", category="fail")
            return render_template("login.html", user=current_user)
    return render_template("login.html", user=current_user)


@auth.route("/identification", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("views.home"))
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        print(f"{email}")
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                flash("Vous êtes connecté!", category="success")
                return redirect(url_for("views.compte"))
            else:
                flash("Mot de passe incorrect,", category="fail")
                return render_template("login.html", user={})
        else:
            flash("Cet utilisateur est inconnu!", category="fail")
            return render_template("login.html", user={})
    return render_template("login.html", user=current_user)


@auth.route("/deconnection")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
