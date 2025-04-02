from typing_extensions import Annotated
from fastapi import APIRouter, Query

from app.service.service import Service
from ..models.PaymentMethod import PaymentMethod

router_pay_method = APIRouter(tags=["Pay"])
service = Service()


@router_pay_method.get("/pay")
def pay(pay_method: Annotated[PaymentMethod, Query()], amount: float):
    response = service.payAndNotify(payment_type=pay_method.value, amount=amount)
    return response
