from flask import Flask
from flask_smorest import Api
from db import items, stores

from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint

app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Stores REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

api.register_blueprint(ItemBlueprint)
api.register_blueprint(StoreBlueprint)


#as a server the methods are switched
# POST - receive data
# GET - send data

# docker build -t flask-smorest-api .
# docker run -dp 5005:5000 -w /app -v "$(pwd):/app" flask-smorest-api  ## every changed code reflects on image
# in here must change as well on docker image and don't have to rebuilding and rerunning docker build and run everytime