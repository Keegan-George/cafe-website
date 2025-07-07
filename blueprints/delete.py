from flask import Blueprint, redirect, url_for
from models import Cafe
from extensions import db


delete_bp = Blueprint("delete", __name__)


@delete_bp.route("/delete/<int:id>")
def delete_cafe(id):
    cafe_to_delete: Cafe = db.get_or_404(entity=Cafe, ident=id)
    db.session.delete(cafe_to_delete)
    db.session.commit()
    return redirect(url_for("view.cafes_list"))
