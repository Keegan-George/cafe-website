from os import urandom
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, Boolean
from cafe_form import CafeForm


class Base(DeclarativeBase):
    pass


# create database
db = SQLAlchemy(model_class=Base)

# create flask app
app = Flask(__name__)

# configure SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"

# set secret key for csrf protection in flask form
app.config["SECRET_KEY"] = urandom(32)

# initialize the app with the extension
db.init_app(app)


class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    map_url: Mapped[str] = mapped_column(String(150), nullable=False)
    img_url: Mapped[str] = mapped_column(String(150))
    location: Mapped[str] = mapped_column(String(150), nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    seats: Mapped[str] = mapped_column(String(150), nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(150), nullable=False)


# create table schema in the database
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/cafes")
def cafes_list():
    cafes = db.session.execute(db.select(Cafe).order_by(Cafe.id.desc())).scalars()
    return render_template("cafes.html", cafes=cafes)


@app.route("/cafe/<int:id>")
def view_cafe(id):
    cafe: Cafe = db.get_or_404(entity=Cafe, ident=id)
    return render_template("cafe.html", cafe=cafe)


@app.route("/cafes/add", methods=["GET", "POST"])
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


@app.route("/edit/<int:id>", methods=["GET", "POST"])
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


@app.route("/delete/<int:id>")
def delete_cafe(id):
    cafe_to_delete: Cafe = db.get_or_404(entity=Cafe, ident=id)
    db.session.delete(cafe_to_delete)
    db.session.commit()
    return redirect(url_for("cafes_list"))


if __name__ == "__main__":
    app.run(debug=True)
