from fastapi import FastAPI
from .routes.PayMethod import router_pay_method

app = FastAPI()
app.include_router(router_pay_method)
