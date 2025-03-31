# Proyecto 2 - Análisis y Diseño de Algoritmos  
**Subset Sum Problem - Técnicas: Divide and Conquer y Programación Dinámica**  
Sección 20 - Gabriel Brolo  
Autores: Joaquin Campos (22155), Hansel López (19026)  

---

## 🧠 Descripción del problema

Dado un conjunto de números enteros positivos y un valor objetivo `T`, el problema consiste en determinar si existe un subconjunto del arreglo cuya suma sea exactamente igual a `T`.

Este es un problema clásico conocido como **Subset Sum**. Su complejidad lo hace ideal para comparar las estrategias de solución **Divide and Conquer** (DaC) y **Programación Dinámica** (DP).

---

## 📌 Enfoques implementados

### 1. **Divide and Conquer (DaC)**

- **Lógica**: En cada paso se divide el problema en dos ramas:
  - Tomar el elemento actual y restarlo del objetivo.
  - Ignorar el elemento actual.
- **Ventajas**: Fácil de implementar, muestra claramente la estructura de árbol de decisiones.
- **Desventajas**: Ineficiente para entradas grandes debido a la recomputación de subproblemas.

### 2. **Programación Dinámica (DP con memoización)**

- **Lógica**: Usa un diccionario (`memo`) para almacenar resultados de subproblemas previamente resueltos.
- **Ventajas**: Muy eficiente en comparación al enfoque DaC.
- **Aplicación**: Se usaron pruebas con múltiples arreglos y con valores `T` variables para comparar el rendimiento.

---

## 🧪 Pruebas realizadas

### ✅ 30 arreglos diferentes con `T = 195`
- Script: `programacionDin/PrograDin30ARR.py`
- Script: `DivideAndConq/DaC30ARR.py`

### ✅ 30 valores de `T` con arreglo fijo
- Script: `programacionDin/prograDin30T.py`
- Script: `DivideAndConq/DaC30T.py`

Cada caso genera una gráfica con los tiempos de ejecución, en milisegundos, comparando la eficiencia práctica de ambas técnicas.

---

## 📊 Análisis comparativo

- **Teórico**:  
  - DaC: Complejidad exponencial `O(2^n)`  
  - DP: Complejidad pseudo-polynomial `O(n*T)`  
- **Empírico**:  
  - DP muestra una mejora significativa gracias al uso de memoización.
  - DaC se vuelve lento conforme aumenta el número de combinaciones posibles.

---

## ⚙️ Cómo ejecutar el proyecto

### 1. Crear y activar entorno virtual

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```
### 3. Ejecutar scripts

```bash
python programacionDin/PrograDin30ARR.py
python programacionDin/prograDin30T.py
python DivideAndConq/DaC30ARR.py
python DivideAndConq/DaC30T.py
```