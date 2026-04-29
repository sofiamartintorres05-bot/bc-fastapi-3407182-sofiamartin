from fastapi import FastAPI

# ============================================
# CREAR LA API
# ============================================

# Aquí iniciamos la aplicación de FastAPI
app = FastAPI(
    title="Mercado Campesino API",
    description="API para gestionar vendedores, productos, ventas y clientes",
    version="1.0.0"
)

# ============================================
# DATOS SIMULADOS (como si fuera una BD)
# ============================================

# Listas básicas para probar la API
vendors = ["Don Pedro", "Finca La Esperanza"]
products = ["Papa", "Tomate", "Cebolla"]
customers = ["Ana", "Carlos"]

# Ejemplo de ventas
sales = [
    {"product": "Papa", "customer": "Ana", "quantity": 2},
    {"product": "Tomate", "customer": "Carlos", "quantity": 5}
]

# ============================================
# 1. ENDPOINT PRINCIPAL (/)
# ============================================

@app.get("/")
async def root():
    """
    Este endpoint muestra información general de la API.
    Es lo primero que se ve cuando entras.
    """
    return {
        "name": "Mercado Campesino API",
        "version": "1.0.0",
        "entities": ["vendors", "products", "sales", "customers"],
        "docs": "/docs"
    }

# ============================================
# 2. CONSULTAR UN PRODUCTO
# ============================================

@app.get("/products/{product_name}")
async def get_product(
    product_name: str,
    detail: bool = False
):
    """
    Busca un producto por su nombre.

    product_name → viene en la URL (path)
    detail → viene como ?detail=true (query)
    """

    # Validamos si el producto existe
    if product_name not in products:
        return {"error": "Producto no encontrado"}

    # Si el usuario pide detalle
    if detail:
        return {
            "product": product_name,
            "price": 3000,
            "stock": 50,
            "message": f"Producto {product_name} disponible en el mercado campesino"
        }

    # Respuesta simple
    return {
        "product": product_name,
        "message": f"{product_name} disponible"
    }

# ============================================
# 3. MENSAJE FORMAL PARA CLIENTES
# ============================================

@app.get("/customers/{name}/formal")
async def customer_formal(
    name: str,
    role: str = "Cliente"
):
    """
    Genera un mensaje formal.

    name → nombre del cliente o vendedor
    role → tipo de persona (Cliente, Vendedor, etc.)
    """

    message = f"Estimado/a {role} {name}, gracias por apoyar el mercado campesino."

    return {
        "message": message,
        "name": name,
        "role": role
    }

# ============================================
# 4. FUNCIÓN PARA SABER LA HORA DEL DÍA
# ============================================

def get_day_period(hour: int):
    """
    Esta función NO es un endpoint.
    Solo ayuda a saber si es mañana, tarde o noche.
    """

    if 5 <= hour < 12:
        return ("Buenos días", "morning")
    elif 12 <= hour < 18:
        return ("Buenas tardes", "afternoon")
    else:
        return ("Buenas noches", "night")

# ============================================
# 5. MENSAJE EN UNA VENTA SEGÚN LA HORA
# ============================================

@app.get("/sales/{customer_name}/time-based")
async def sales_time_based(
    customer_name: str,
    hour: int
):
    """
    Simula una venta con saludo según la hora.

    customer_name → nombre del cliente
    hour → hora del día (0 a 23)
    """

    # Validamos que la hora sea correcta
    if hour < 0 or hour > 23:
        return {"error": "Hora inválida"}

    # Usamos la función auxiliar
    greeting, period = get_day_period(hour)

    return {
        "message": f"{greeting}, {customer_name}. Gracias por tu compra.",
        "hour": hour,
        "period": period
    }

# ============================================
# 6. ESTADO DE LA API
# ============================================

@app.get("/health")
async def health_check():
    """
    Sirve para verificar que la API está funcionando bien.
    """
    return {
        "status": "healthy",
        "service": "mercado-campesino-api",
        "version": "1.0.0"
    }