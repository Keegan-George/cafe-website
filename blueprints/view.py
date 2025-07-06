from flask import Blueprint, render_template
from models import db, Cafe

view_bp = Blueprint("view", __name__)


@view_bp.route("/")
def home():
    return render_template("index.html")


@view_bp.route("/cafes")
def cafes_list():
    cafes = db.session.execute(db.select(Cafe).order_by(Cafe.id.desc())).scalars()
    return render_template("cafes.html", cafes=cafes)


@view_bp.route("/cafe/<int:id>")
def view_cafe(id):
    cafe: Cafe = db.get_or_404(entity=Cafe, ident=id)
    return render_template("cafe.html", cafe=cafe)
