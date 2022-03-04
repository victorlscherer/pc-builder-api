from flask import Blueprint

from app.controllers.product_controllers import (create_product,
                                                 get_all_products,
                                                 get_product_by_id)

bp = Blueprint("products", __name__, url_prefix="/products")


def update_product():
    ...


def delete_product():
    ...


bp.post("")(create_product)
bp.get("")(get_all_products)
bp.get("<int:id>")(get_product_by_id)
bp.patch("<int:id>")(update_product)
bp.delete("<int:id>")(delete_product)
