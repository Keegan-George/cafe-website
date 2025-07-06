from flask import Blueprint, render_template, redirect, url_for
from models import db, Cafe
from cafe_form import CafeForm

add_bp = Blueprint("add", __name__)

@add_bp.route("/cafes/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()

    if form.validate_on_submit():
        name = form.name.data
        map_url = form.map_url.data
        img_url = form.img_url.data
        location = form.location.data
        has_sockets = form.has_sockets.data
        has_toilet = form.has_toilet.data
        has_wifi = form.has_wifi.data
        can_take_calls = form.can_take_calls.data
        seats = form.seats.data
        coffee_price = form.coffee_price.data

        new_cafe = Cafe(
            name=name,
            map_url=map_url,
            img_url=img_url,
            location=location,
            has_sockets=has_sockets,
            has_toilet=has_toilet,
            has_wifi=has_wifi,
            can_take_calls=can_take_calls,
            seats=seats,
            coffee_price=coffee_price,
        )

        db.session.add(new_cafe)
        db.session.commit()

        return redirect(url_for("cafes_list"))

    return render_template("add.html", form=form)


@add_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_cafe(id):
    cafe_to_edit: Cafe = db.get_or_404(entity=Cafe, ident=id)

    # display current data in the form
    form = CafeForm(
        name=cafe_to_edit.name,
        map_url=cafe_to_edit.map_url,
        img_url=cafe_to_edit.img_url,
        location=cafe_to_edit.location,
        has_sockets=cafe_to_edit.has_sockets,
        has_toilet=cafe_to_edit.has_toilet,
        has_wifi=cafe_to_edit.has_wifi,
        can_take_call=cafe_to_edit.can_take_calls,
        seats=cafe_to_edit.seats,
        coffee_price=cafe_to_edit.coffee_price,
    )

    if form.validate_on_submit():
        cafe_to_edit.name = form.name.data
        cafe_to_edit.map_url = form.map_url.data
        cafe_to_edit.img_url = form.img_url.data
        cafe_to_edit.location = form.location.data
        cafe_to_edit.has_sockets = form.has_sockets.data
        cafe_to_edit.has_toilet = form.has_toilet.data
        cafe_to_edit.has_wifi = form.has_wifi.data
        cafe_to_edit.can_take_calls = form.can_take_calls.data
        cafe_to_edit.seats = form.seats.data
        cafe_to_edit.coffee_price = form.coffee_price.data
        db.session.commit()
        return redirect(url_for("view_cafe", id=cafe_to_edit.id))

    return render_template("add.html", form=form, is_edit=True, cafe=cafe_to_edit)