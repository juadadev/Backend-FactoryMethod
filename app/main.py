from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes.PayMethod import router_pay_method

app = FastAPI()

app.include_router(router_pay_method)

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
