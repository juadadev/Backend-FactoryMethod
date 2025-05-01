"""Módulo de notificaciones.

Define la interfaz base para las notificaciones.
"""

from abc import ABC, abstractmethod


class Notification(ABC):
    """Interface de notificación.

    Define los métodos que deben ser implementados por las clases que implementan esta interfaz.
    """

    @abstractmethod
    def send_amount(self, amount: float) -> dict[str, float]:
        """Envía un monto y retorna un diccionario con el resultado.

        Args:
            amount (float): Cantidad a enviar.

        Returns:
            dict[str, float]: Respuesta del envío.
            ejemplo: {"monto": 354.0}
        """
        pass
