
from Exception.Exception import PaymentFailedException


class PaymentProcessor:
    def process_payment(self, order):
        try:
            raise PaymentFailedException("Payment declined.")
        except PaymentFailedException as e:
            print(f"Payment Error: {e}")
            order.update_order_status("Payment Failed")