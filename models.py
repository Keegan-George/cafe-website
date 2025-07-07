from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from extensions import db


MAX_STRING_LENGTH = 150


class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(MAX_STRING_LENGTH), nullable=False)
    map_url: Mapped[str] = mapped_column(String(MAX_STRING_LENGTH), nullable=False)
    img_url: Mapped[str] = mapped_column(String(MAX_STRING_LENGTH), nullable=True)
    location: Mapped[str] = mapped_column(String(MAX_STRING_LENGTH), nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    seats: Mapped[str] = mapped_column(String(MAX_STRING_LENGTH), nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(MAX_STRING_LENGTH), nullable=False)
