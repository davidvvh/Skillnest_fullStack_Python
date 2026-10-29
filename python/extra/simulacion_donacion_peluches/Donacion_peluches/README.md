# Donación de Peluches

Proyecto sencillo hecho con Flask, Python y MySQL.

## Para instalar

Instala las librerías necesarias:

```bash
pip install flask mysql-connector-python python-dotenv
```

## Base de datos

Ejecuta el archivo `db_peluches.sql` en MySQL Workbench o phpMyAdmin.

## Configuración

Edita el archivo `.env` y escribe los datos de tu MySQL. No compartas ese archivo con contraseñas reales.

## Ejecutar

Desde esta carpeta ejecuta:

```bash
python server.py
```

Después abre http://localhost:5000/

## Funciones

- Registro e inicio de sesión.
- Crear donaciones de peluches.
- Ver, editar y borrar las donaciones propias.
- Adoptar peluches.
- Ver quién donó y quién adoptó cada peluche.
- Contar las visitas de cada peluche.
