import numpy as np

class SubspaceIDS:
    def __init__(self, coefficients):
        """
        Inicializa el sistema de detección definiendo el 'subespacio normal'
        a través de los coeficientes de la ecuación lineal (ej: [2, -3, 1] para 2x - 3y + z = 0)
        """
        self.coeffs = np.array(coefficients)

    def evaluar_trafico(self, vector_trafico, umbral=0.1):
        """
        Evalúa si un paquete/vector de red pertenece al subespacio seguro.
        Aplica la regla del cero (producto punto / evaluación de la ecuación).
        """
        # Multiplicamos el vector de tráfico por los coeficientes del subespacio
        resultado = np.dot(vector_trafico, self.coeffs)
        
        # Verificamos si el resultado es prácticamente cero (considerando tolerancia flotante)
        if abs(resultado) <= umbral:
            return "NORMAL (Dentro del subespacio)"
        else:
            return f"¡ANOMALÍA DETECTADA! (Desviación del origen: {resultado:.2f})"

# ==========================================
# SIMULACIÓN EN TIEMPO REAL
# ==========================================

# Definimos nuestro subespacio seguro con la regla: 2(Bytes_Enviados) - 3(Bytes_Recibidos) + 1(Conexiones) = 0
# Representado como vector de coeficientes: [2, -3, 1]
ids = SubspaceIDS(coefficients=[2, -3, 1])

# Simulamos paquetes de tráfico que llegan a la red [Bytes_Enviados, Bytes_Recibidos, Conexiones]
paquetes_entrantes = [
    [15, 10, 0],   # Paquete 1: 2(15) - 3(10) + 1(0) = 30 - 30 + 0 = 0 (Pasa exacto)
    [30, 20, 0],   # Paquete 2: 2(30) - 3(20) + 1(0) = 60 - 60 + 0 = 0 (Pasa exacto)
    [100, 10, 5],  # Paquete 3: 2(100) - 3(10) + 1(5) = 200 - 30 + 5 = 175 (¡Se disparó!)
    [6, 4, 0],     # Paquete 4: 2(6) - 3(4) + 1(0) = 12 - 12 + 0 = 0 (Pasa exacto)
    [500, 500, 1]  # Paquete 5: 2(500) - 3(500) + 1(1) = 1000 - 1500 + 1 = -499 (¡Anomalía masiva!)
]

print("--- INICIANDO ESCANERO DE SEGURIDAD BASADO EN SUBESPACIOS ---\n")

for i, paquete in enumerate(paquetes_entrantes, 1):
    estado = ids.evaluar_trafico(paquete)
    print(f"Paquete #{i} {paquetes_entrantes[i-1]} --> {estado}")