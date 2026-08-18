# Subspace-IDS

Prototype of an Intrusion Detection System (IDS) using vector and matrix subspace filtering in Python.

---

## Descripción del Proyecto
Este repositorio contiene un script experimental diseñado para la detección de anomalías y tráfico malicioso en redes. El enfoque principal del sistema es aplicar conceptos avanzados de **álgebra lineal (matrices, vectores y subespacios)** para modelar el comportamiento normal de la red y filtrar posibles intrusiones de manera eficiente y limpia.

---

##  Base Teórica y Matemática
A diferencia de los sistemas tradicionales basados únicamente en firmas estáticas, este prototipo utiliza un enfoque geométrico:
* **Modelado de tráfico:** Las características de las conexiones de red se representan como vectores dentro de un espacio vectorial multidimensional.
* **Subespacio de normalidad:** Se define una matriz base que genera un subespacio representativo del comportamiento legítimo o seguro.
* **Proyección y Filtrado:** El tráfico entrante se evalúa proyectándolo sobre el subespacio; desviaciones significativas fuera de este umbral algebraico se identifican y marcan como potenciales anomalías o intrusiones.

---

##  Tecnologías Utilizadas
* **Python** (Lógica principal del script)
* **Librerías de cálculo matricial** (Estructuras de vectores y matrices)

---

##  Estructura del Repositorio
* `subespacios_ciberseguridad.py` -> Script principal optimizado y autocontenido.
* `LICENSE` -> Licencia MIT para la gestión abierta y transparente del proyecto.

---

##  Uso y Ejecución
Para probar o revisar el funcionamiento del script en tu entorno local:

```bash
git clone [https://github.com/brianabcd2023-sketch/subspace-ids.git](https://github.com/brianabcd2023-sketch/subspace-ids.git)
cd subspace-ids
python subespacios_ciberseguridad.py
