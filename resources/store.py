import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores
from schemas import StoresSchema

blp = Blueprint("Stores", __name__, description="Operations on stores")

@blp.route("/store/<string:store_id>")
class Store(MethodView):

    @blp.response(200, StoresSchema)
    def get(self, store_id):
        try:
            return stores[store_id]
        except:
            abort(404, message="Store not found")

    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message": "Store deleted."}
        except KeyError:
            abort(404, message="Store not found.")

@blp.route("/store")
class StoreList(MethodView):

    @blp.response(200, StoresSchema(many=True))
    def get(self):
        return stores.values()
    
    @blp.arguments(StoresSchema)
    @blp.response(200, StoresSchema)
    def post(self, store_data):
        store_data = request.get_json()

        '''if "name" not in store_data:
            abort(
                400,
                message="Bad request. Ensure 'name' is included in the JSON payload.",
            )'''

        for store in stores.values():
            if store_data["name"] == store["name"]:
                abort(404, message="Item already exists.") 
                
        store_id = uuid.uuid4().hex
        store = {**store_data, "id": store_id}
        stores[store_id]= store
        
        return store    
