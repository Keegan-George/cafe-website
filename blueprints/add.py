from flask import Blueprint, render_template, redirect, url_for
from models import Cafe
from cafe_form import CafeForm
from extensions import db

add_bp = Blueprint("add", __name__)


@add_bp.route("/cafes/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()

    if form.validate_on_submit():
        new_cafe = Cafe()
        form.populate_obj(new_cafe)

        db.session.add(new_cafe)
        db.session.commit()

        return redirect(url_for("view.cafes_list"))

    return render_template("add.html", form=form)


@add_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_cafe(id):
    cafe_to_edit: Cafe = db.get_or_404(entity=Cafe, ident=id)

    # display existing data in the form
    form = CafeForm(obj=cafe_to_edit)

    if form.validate_on_submit():
        form.populate_obj(cafe_to_edit)

        db.session.commit()
        
        return redirect(url_for("view.view_cafe", id=cafe_to_edit.id))

    return render_template("add.html", form=form, is_edit=True, cafe=cafe_to_edit)
