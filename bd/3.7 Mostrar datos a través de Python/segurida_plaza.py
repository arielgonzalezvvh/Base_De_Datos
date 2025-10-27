# ==========================================
# menu_seguridad_completo.py
# CRUD completo con Procedimientos Almacenados (MySQL)
# Base de datos: seguridad_plazas
# Autor: Dany
# ==========================================

import mysql.connector

# ---------- CONFIGURACIÓN ----------
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "1234",  # Cambia tu contraseña
    "database": "seguridad_plazas"
}

# ---------- CONEXIÓN ----------
def conectar():
    return mysql.connector.connect(**DB_CONFIG)

# ---------- FUNCIONES GENÉRICAS ----------
def ejecutar_insertar(sp_name, args):
    cnx = cur = None
    try:
        cnx = conectar()
        cur = cnx.cursor()
        args.append(0)  # OUT param (nuevo ID)
        args = cur.callproc(sp_name, args)
        cnx.commit()
        print(f"✅ Registro insertado. Nuevo ID: {args[-1]}")
    except mysql.connector.Error as e:
        print("❌ Error en inserción:", e)
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()

def ejecutar_listar(sp_name):
    cnx = cur = None
    try:
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc(sp_name)
        for result in cur.stored_results():
            registros = result.fetchall()
            if not registros:
                print("No hay registros.")
            else:
                for fila in registros:
                    print(fila)
    except mysql.connector.Error as e:
        print("❌ Error:", e)
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()

def ejecutar_borrado_logico(sp_name, id_):
    try:
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc(sp_name, [id_])
        cnx.commit()
        print(f"🗑️ Registro ID {id_} marcado como eliminado.")
    except mysql.connector.Error as e:
        print("❌ Error:", e)
    finally:
        cur.close()
        cnx.close()

def ejecutar_restaurar(sp_name, id_):
    try:
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc(sp_name, [id_])
        cnx.commit()
        print(f"♻️ Registro ID {id_} restaurado correctamente.")
    except mysql.connector.Error as e:
        print("❌ Error:", e)
    finally:
        cur.close()
        cnx.close()

# ---------- MENÚS POR TABLA ----------
def menu_ciudades():
    while True:
        print("\n=== CIUDADES ===")
        print("1) Insertar\n2) Listar activos\n3) Listar todos\n4) Borrado lógico\n5) Restaurar\n0) Volver")
        op = input("Opción: ")
        if op == "1":
            nombre = input("Nombre ciudad: ")
            created_by = int(input("ID usuario creador: "))
            ejecutar_insertar("sp_insertar_ciudad", [nombre, created_by])
        elif op == "2":
            ejecutar_listar("sp_listar_ciudades_activos")
        elif op == "3":
            ejecutar_listar("sp_listar_ciudades_todos")
        elif op == "4":
            ejecutar_borrado_logico("sp_borrado_logico_ciudad", int(input("ID: ")))
        elif op == "5":
            ejecutar_restaurar("sp_restaurar_ciudad", int(input("ID: ")))
        elif op == "0":
            break

def menu_comunas():
    while True:
        print("\n=== COMUNAS ===")
        print("1) Insertar\n2) Listar activos\n3) Listar todos\n4) Borrado lógico\n5) Restaurar\n0) Volver")
        op = input("Opción: ")
        if op == "1":
            id_ciudad = int(input("ID ciudad: "))
            nombre = input("Nombre comuna: ")
            created_by = int(input("ID usuario creador: "))
            ejecutar_insertar("sp_insertar_comuna", [id_ciudad, nombre, created_by])
        elif op == "2":
            ejecutar_listar("sp_listar_comunas_activos")
        elif op == "3":
            ejecutar_listar("sp_listar_comunas_todos")
        elif op == "4":
            ejecutar_borrado_logico("sp_borrado_logico_comuna", int(input("ID: ")))
        elif op == "5":
            ejecutar_restaurar("sp_restaurar_comuna", int(input("ID: ")))
        elif op == "0":
            break

def menu_plazas():
    while True:
        print("\n=== PLAZAS ===")
        print("1) Insertar\n2) Listar activos\n3) Listar todos\n4) Borrado lógico\n5) Restaurar\n0) Volver")
        op = input("Opción: ")
        if op == "1":
            id_comuna = int(input("ID comuna: "))
            nombre = input("Nombre plaza: ")
            ubicacion = input("Ubicación: ")
            created_by = int(input("ID usuario creador: "))
            ejecutar_insertar("sp_insertar_plaza", [id_comuna, nombre, ubicacion, created_by])
        elif op == "2":
            ejecutar_listar("sp_listar_plazas_activos")
        elif op == "3":
            ejecutar_listar("sp_listar_plazas_todos")
        elif op == "4":
            ejecutar_borrado_logico("sp_borrado_logico_plaza", int(input("ID: ")))
        elif op == "5":
            ejecutar_restaurar("sp_restaurar_plaza", int(input("ID: ")))
        elif op == "0":
            break

def menu_estado_camaras():
    while True:
        print("\n=== ESTADO CAMARAS ===")
        print("1) Insertar\n2) Listar activos\n3) Listar todos\n4) Borrado lógico\n5) Restaurar\n0) Volver")
        op = input("Opción: ")
        if op == "1":
            nombre = input("Nombre estado: ")
            created_by = int(input("ID creador: "))
            ejecutar_insertar("sp_insertar_estado_camara", [nombre, created_by])
        elif op == "2":
            ejecutar_listar("sp_listar_estado_camaras_activos")
        elif op == "3":
            ejecutar_listar("sp_listar_estado_camaras_todos")
        elif op == "4":
            ejecutar_borrado_logico("sp_borrado_logico_estado_camara", int(input("ID: ")))
        elif op == "5":
            ejecutar_restaurar("sp_restaurar_estado_camara", int(input("ID: ")))
        elif op == "0":
            break

def menu_camaras():
    while True:
        print("\n=== CAMARAS ===")
        print("1) Insertar\n2) Listar activos\n3) Listar todos\n4) Borrado lógico\n5) Restaurar\n0) Volver")
        op = input("Opción: ")
        if op == "1":
            id_plaza = int(input("ID plaza: "))
            id_estado = int(input("ID estado: "))
            modelo = input("Modelo: ")
            created_by = int(input("ID creador: "))
            ejecutar_insertar("sp_insertar_camara", [id_plaza, id_estado, modelo, created_by])
        elif op == "2":
            ejecutar_listar("sp_listar_camaras_activos")
        elif op == "3":
            ejecutar_listar("sp_listar_camaras_todos")
        elif op == "4":
            ejecutar_borrado_logico("sp_borrado_logico_camara", int(input("ID: ")))
        elif op == "5":
            ejecutar_restaurar("sp_restaurar_camara", int(input("ID: ")))
        elif op == "0":
            break

def menu_juntas_vecinos():
    while True:
        print("\n=== JUNTAS DE VECINOS ===")
        print("1) Insertar\n2) Listar activos\n3) Listar todos\n4) Borrado lógico\n5) Restaurar\n0) Volver")
        op = input("Opción: ")
        if op == "1":
            nombre = input("Nombre junta: ")
            direccion = input("Dirección: ")
            created_by = int(input("ID creador: "))
            ejecutar_insertar("sp_insertar_junta_vecinos", [nombre, direccion, created_by])
        elif op == "2":
            ejecutar_listar("sp_listar_juntas_vecinos_activos")
        elif op == "3":
            ejecutar_listar("sp_listar_juntas_vecinos_todos")
        elif op == "4":
            ejecutar_borrado_logico("sp_borrado_logico_junta_vecinos", int(input("ID: ")))
        elif op == "5":
            ejecutar_restaurar("sp_restaurar_junta_vecinos", int(input("ID: ")))
        elif op == "0":
            break

def menu_usuarios():
    while True:
        print("\n=== USUARIOS ===")
        print("1) Insertar\n2) Listar activos\n3) Listar todos\n4) Borrado lógico\n5) Restaurar\n0) Volver")
        op = input("Opción: ")
        if op == "1":
            nombre = input("Nombre usuario: ")
            id_tipo = int(input("ID tipo usuario: "))
            created_by = int(input("ID creador: "))
            ejecutar_insertar("sp_insertar_usuario", [nombre, id_tipo, created_by])
        elif op == "2":
            ejecutar_listar("sp_listar_usuarios_activos")
        elif op == "3":
            ejecutar_listar("sp_listar_usuarios_todos")
        elif op == "4":
            ejecutar_borrado_logico("sp_borrado_logico_usuario", int(input("ID: ")))
        elif op == "5":
            ejecutar_restaurar("sp_restaurar_usuario", int(input("ID: ")))
        elif op == "0":
            break

def menu_reportes():
    while True:
        print("\n=== REPORTES ===")
        print("1) Insertar\n2) Listar activos\n3) Listar todos\n4) Borrado lógico\n5) Restaurar\n0) Volver")
        op = input("Opción: ")
        if op == "1":
            id_usuario = int(input("ID usuario: "))
            id_tipo = int(input("ID tipo reporte: "))
            descripcion = input("Descripción: ")
            created_by = int(input("ID creador: "))
            ejecutar_insertar("sp_insertar_reporte", [id_usuario, id_tipo, descripcion, created_by])
        elif op == "2":
            ejecutar_listar("sp_listar_reportes_activos")
        elif op == "3":
            ejecutar_listar("sp_listar_reportes_todos")
        elif op == "4":
            ejecutar_borrado_logico("sp_borrado_logico_reporte", int(input("ID: ")))
        elif op == "5":
            ejecutar_restaurar("sp_restaurar_reporte", int(input("ID: ")))
        elif op == "0":
            break

# ---------- MENÚ PRINCIPAL ----------
def menu_principal():
    while True:
        print("\n=== MENÚ PRINCIPAL SEGURIDAD PLAZAS ===")
        print("1) Ciudades\n2) Comunas\n3) Plazas\n4) Estado Cámaras\n5) Cámaras")
        print("6) Juntas Vecinos\n7) Usuarios\n8) Reportes\n0) Salir")
        op = input("Selecciona: ")
        if op == "1": menu_ciudades()
        elif op == "2": menu_comunas()
        elif op == "3": menu_plazas()
        elif op == "4": menu_estado_camaras()
        elif op == "5": menu_camaras()
        elif op == "6": menu_juntas_vecinos()
        elif op == "7": menu_usuarios()
        elif op == "8": menu_reportes()
        elif op == "0":
            print("👋 Cerrando aplicación.")
            break
        else:
            print("❌ Opción no válida.")

# ---------- EJECUCIÓN ----------
if __name__ == "__main__":
    menu_principal()
