# bc-fastapi-3407182-sofiamartin
# 🌾 Mercado Campesino API

### 🧑‍🌾 Conectando productores y clientes

---

## ✨ Descripción

API REST desarrollada con **FastAPI** que simula el funcionamiento de un mercado campesino.
Permite consultar productos, generar mensajes para clientes y simular ventas.

Este proyecto hace parte del proceso de aprendizaje en desarrollo backend.

---

## 🚀 Tecnologías

* 🐍 Python
* ⚡ FastAPI
* 🚀 Uvicorn

---

## ⚙️ Cómo ejecutar el proyecto

### 1️⃣ Instalar dependencias

```bash
pip install fastapi uvicorn
```

### 2️⃣ Ejecutar el servidor

```bash
uvicorn main:app --reload
```

### 3️⃣ Abrir en el navegador

```
http://127.0.0.1:8000/docs
```

---

## 📊 Datos simulados

Actualmente la API trabaja sin base de datos:

| Entidad       | Datos                         |
| ------------- | ----------------------------- |
| 👨‍🌾 Vendors | Don Pedro, Finca La Esperanza |
| 🥔 Products   | Papa, Tomate, Cebolla         |
| 🧍 Customers  | Ana, Carlos                   |
| 💰 Sales      | Compras simuladas             |

---

## 🔗 Endpoints

### 🏠 Información general

**GET /**
Muestra datos básicos de la API.

---

### 🥕 Productos

**GET /products/{product_name}**

Consultar un producto por nombre.

🔹 Ejemplo:

```
/products/Papa
```

🔹 Con detalle:

```
/products/Papa?detail=true
```

---

### 🧍 Clientes (mensaje formal)

**GET /customers/{name}/formal**

Genera un mensaje formal.

🔹 Ejemplo:

```
/customers/Ana/formal
```

---

### ⏰ Ventas según la hora

**GET /sales/{customer_name}/time-based**

Genera un mensaje dependiendo de la hora.

🔹 Ejemplo:

```
/sales/Ana/time-based?hour=10
```

---

### ❤️ Estado de la API

**GET /health**

Verifica que todo esté funcionando correctamente.

---

## 🧠 Lo que aprendí

✔ Crear APIs con FastAPI
✔ Manejar rutas (endpoints)
✔ Usar parámetros (path y query)
✔ Retornar datos en JSON
✔ Usar documentación automática (`/docs`)

---

## ⚠️ Importante

* Este proyecto usa datos simulados
* No está conectado a base de datos
* Es la base para proyectos más avanzados

---

## 🔥 Próximos pasos

* 🔹 CRUD completo
* 🔹 Validaciones con Pydantic
* 🔹 Base de datos con SQLAlchemy

---

## 👩‍💻 Autor

Sofía Martin Torres
Estudiante en formación backend 🚀
