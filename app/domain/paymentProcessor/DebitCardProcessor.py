from .PaymentProcessor import PaymentProcessor


class DebitCardProcessor(PaymentProcessor):
    def process(self, amount: float) -> float:
        commission_rate = 0.01
        final_mount = amount + (amount * commission_rate)

        if amount > 500:
            final_mount += 5  # Cargo adicional

        return final_mount
