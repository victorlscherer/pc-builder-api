from http import HTTPStatus

from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.core.database import db
from app.models.address_model import AddressModel
from app.models.user_model import UserModel
from app.models.users_addresses_model import UserAddressModel


@jwt_required()
def create_address():
    current_user = get_jwt_identity()
    data = request.get_json()

    try:
        if type(data["cep"]) != str:
            return {"error": "CEP must be of String(str) type!"}, HTTPStatus.BAD_REQUEST

        if type(data["numero"]) != int:
            return {
                "error": "House number must be of Integer type!"
            }, HTTPStatus.BAD_REQUEST

        address_data_factory = {
            "zip_code": data["cep"],
            "state": data["estado"],
            "city": data["cidade"],
            "public_place": data["logradouro"],
            "number": data["numero"],
        }

        address = AddressModel(**address_data_factory)

        db.session.add(address)
        db.session.commit()

        users_addresses = UserAddressModel(
            user_id=current_user["user_id"], address_id=address.address_id
        )

        db.session.add(users_addresses)
        db.session.commit()

        return address_data_factory, HTTPStatus.CREATED
    except KeyError:
        return {
            "message": "Missing or invalid key(s)",
            "required Keys": ["zip_code", "state", "city", "public_place", "number"],
            "recieved": list(data.keys()),
        }, HTTPStatus.BAD_REQUEST


@jwt_required()
def get_address():
    current_user = get_jwt_identity()

    query = (
        db.session.query(AddressModel)
        .select_from(AddressModel)
        .join(UserAddressModel)
        .join(UserModel)
        .filter(UserAddressModel.user_id == current_user["user_id"])
        .first()
    )
    return jsonify(query), HTTPStatus.OK


def update_address():
    ...
