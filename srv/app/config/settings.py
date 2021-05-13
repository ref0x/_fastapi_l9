from pydantic import BaseSettings

API_V1_STR = "/api/v1"


# class Database(BaseSettings):
	# url = "postgres://fastapi_dev:fastapi_dev@127.0.0.1:5432/fastapi_dev"
	# url = "sqlite://db3.sqlite"


class AppModels(BaseSettings):
	app_models = [
		"app.text.models",
	]


# database = Database()
app_models = AppModels()
