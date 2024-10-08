class Boleto:
    def __init__(self, numero_vagon, numero_silla, tipo):
        self._numero_vagon = numero_vagon
        self._numero_silla = numero_silla
        self._tipo = tipo
        self._precio = self._calcular_precio()

    def _calcular_precio(self):
        precios = {'A': 2000, 'B': 4000, 'C': 6000}
        return precios.get(self._tipo, 0)

    @property
    def precio(self):
        return self._precio

    def get_numero_asiento(self):
        return f"{self._numero_vagon}-{str(self._numero_silla).zfill(2)}"

    @property
    def numero_silla(self):
        return self._numero_silla
