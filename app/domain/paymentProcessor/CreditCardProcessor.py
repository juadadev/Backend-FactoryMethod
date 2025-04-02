from .PaymentProcessor import PaymentProcessor


class CreditCardProcessor(PaymentProcessor):
    def process(self, amount: float) -> float:
        commission_rate = 0.03
        final_mount = amount + (amount * commission_rate)

        if amount > 1000:
            final_mount += 10  # Cargo adicional

        return final_mount
