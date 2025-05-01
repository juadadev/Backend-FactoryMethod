from typing import Annotated

from fastapi import APIRouter, Query

from app.service.service import Service

from ..models.PaymentMethod import PaymentMethod

router_pay_method = APIRouter(tags=['Pay'])
service = Service()


@router_pay_method.get('/pay')
def pay(pay_method: Annotated[PaymentMethod, Query()], amount: float):
    """
    Realiza el pago seleccionando el método de pago de preferencia,
    automáticamente calcula el monto y lo retorna
    """
    response = service.payAndNotify(payment_type=pay_method.value, amount=amount)
    return response
