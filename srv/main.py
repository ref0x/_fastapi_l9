from fastapi import FastAPI
# from tortoise.contrib.fastapi import register_tortoise

from app import routers
from app.config import settings

app = FastAPI(title="~ R2D2 API ~", debug=False)

app.include_router(routers.api_router, prefix=settings.API_V1_STR)

# register_tortoise(
#     app,
#     db_url=settings.database.url,
#     modules={"models": ['models']},
#     generate_schemas=True,
#     add_exception_handlers=True,
# )
