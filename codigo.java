public class PaymentProcessor {
  public double processPayment(String paymentType, double amount) {
    double finalAmount = 0.0;

    if (paymentType.equals("CREDIT_CARD")) {
      // Lógica de procesamiento para la tarjeta de crédito
      double commissionRate = 0.03;
      finalAmount = amount + (amount * commissionRate);
      System.out.println("Procesando pago con tarjeta de crédito");

      // validaciones específicas
      if (amount > 1000) {
        finalAmount += 10; // cargo autonomi
      }
    } else if (paymentType.equals("DEBIT_CARD")) {
      // Lógica de procesamiento para la tarjeta de debito
      double commissionRate = 0.01;
      finalAmount = amount + (amount * commissionRate);
      System.out.println("Procesando pago con tarjeta de debito");

      // validaciones específicas
      if (amount > 500) {
        finalAmount += 5; // cargo adicional
      }
    } else if (paymentType.equals("PAYPAL")) {
      // Lógica de procesamiento para PayPal
      double commissionRate = 0.02;
      finalAmount = amount + (amount * commissionRate);
      System.out.println("Procesando pago con PayPal");

      // validaciones específicas
      if (amount > 750) {
        finalAmount += 7; // cargo autonomi
      }
    } else {
      throw new IllegalArgumentException("Método de pago no soportado");
    }
    return finalAmount;
  }
}
