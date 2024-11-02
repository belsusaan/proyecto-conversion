import streamlit as st

st.title("Conversor")
st.write("Escoge entre distintas categorías")

# Diccionario de categorías y unidades de conversión
categorias = {
    "Medida fisica": {
        "temperatura": ["Celsius", "Fahrenheit", "Kelvin"],
        "Longitud": ["Metros", "Pulgadas", "Pies", "Kilometros", "Millas", "Yardas"],
        "Peso/Masa": ["Gramos", "Kilogramos", "Libras", "Onzas", "Toneladas"],
        "Volumen": ["Litros", "Galones", "Mililitros", "Metros cubicos", "Pies cubicos"],
        "Superficie/Area": ["Metros cuadrados", "Hectareas", "Acres", "Kilometros cuadrados"],
        "Velocidad": ["Km/h", "m/s", "mph", "nudos"]
    },
    "Unidades de tiempo": {
        "Tiempo": ["Segundos", "Minutos", "Horas", "Días", "Semanas", "Meses", "Años", "Milisegundos", "Microsegundos"]
    },
    "Monedas": {
        "Moneda": ["Dolar", "Quetzal", "Euro", "Libra esterlina", "Franco suizo", "Yen japones", 
                   "Dolar canadiense", "Yuan chino", "Dolar australiano", "Real brasileño", "Rublo ruso", 
                   "Peso mexicano", "Peso uruguayo", "Peso chileno", "Nuevo dolar taiwanes"]
    }
}

# Temperatura
def convertir_temperatura(solicitud, primero, segundo):
    if primero == "Celsius" and segundo == "Fahrenheit":
        return solicitud * 9/5 + 32
    elif primero == "Fahrenheit" and segundo == "Celsius":
        return (solicitud - 32) * 5/9
    elif primero == "Celsius" and segundo == "Kelvin":
        return solicitud + 273.15
    elif primero == "Kelvin" and segundo == "Celsius":
        return solicitud - 273.15
    elif primero == "Fahrenheit" and segundo == "Kelvin":
        return ((solicitud - 32) * (5/9)) + 273.15
    elif primero == "Kelvin" and segundo == "Fahrenheit":
        return ((solicitud - 273.15) * 1.8) + 32
    return solicitud

# categoria principal
categoria = st.selectbox("Categoría", list(categorias.keys()), index=0)

# Minicategorias
tipo_unidad = st.selectbox("Tipo de unidad", list(categorias[categoria].keys()), index=0)
unidades = categorias[categoria][tipo_unidad]

# columnas para selección
col1, col2 = st.columns(2)
tipo_dato1 = col1.selectbox("De:", unidades, label_visibility="visible", index=0)
dato1 = col1.number_input("Cantidad:", label_visibility="visible")
tipo_dato2 = col2.selectbox("A:", unidades, label_visibility="visible", index=0)

# Botón para conversión
bot1, bot2 = st.columns(2)
if bot1.button("Convertir", type="primary"):
    if categoria == "Medida fisica" and tipo_unidad == "temperatura":
        resultado = convertir_temperatura(dato1, tipo_dato1, tipo_dato2)
    elif categoria == "Medida fisica" and tipo_unidad == "Longitud":
        resultado = "Estamos en construcción"
         # faltan minicategorías dentro de esta categoría

         #Otras categorías, falta implementar funciones
    elif categoria == "Monedas":
        resultado = "Estamos en construcción"
    else:
        resultado = "Estamos en construcción"
    # Mostrar el resultado
    col2.title(f"Resultado: {resultado}")

# Botón para resetear la aplicación
if bot2.button("Reset"):
    st.rerun()
