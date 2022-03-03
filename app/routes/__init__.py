from flask import Blueprint, Flask

from app.routes.address_routes import bp_address
from app.routes.cart_routes import bp as bp_cart
from app.routes.category_routes import bp as bp_category
from app.routes.order_routes import bp as bp_order
from app.routes.product_routes import bp as bp_product
from app.routes.user_routes import bp as bp_user

blueprint = Blueprint("api", __name__, url_prefix="/")


def init_app(app: Flask):
    app.config["JSON_SORT_KEYS"] = False

    blueprint.register_blueprint(bp_order)
    blueprint.register_blueprint(bp_address)
    blueprint.register_blueprint(bp_cart)
    blueprint.register_blueprint(bp_user)
    blueprint.register_blueprint(bp_product)
    blueprint.register_blueprint(bp_category)

    app.register_blueprint(blueprint)
