from .PaymentProcessor import PaymentProcessor


class PaypalProcessor(PaymentProcessor):
    def process(self, amount: float) -> float:
        commission_rate = 0.02
        final_mount = amount + (amount * commission_rate)

        if amount > 750:
            final_mount += 7  # Cargo adicional

        return final_mount
