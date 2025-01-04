import sqlite3
import os
from utils.config import DATABASE_PATH
# Ruta de la base de datos
DB_PATH = os.path.join(os.path.dirname(__file__), "../Data/ElectroPlusDB.db")


def check_database_exists():
    """Verifica si la base de datos ya existe."""
    if os.path.exists(DB_PATH):
        print("Base de datos ya creada.")
        return True
    return False


def create_database():
    """Crea la base de datos y las tablas."""
    print("Creando la base de datos...")
    # Asegurarse de que la carpeta exista
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    
    # Conectar a la base de datos
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    
    # Crear las tablas
    script_sql = """
    -- Tabla CLIENTE
    CREATE TABLE Cliente (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        contacto TEXT,
        direccion TEXT
    );

    -- Tabla TRABAJADOR
    CREATE TABLE Trabajador (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        tipo TEXT NOT NULL CHECK(tipo IN ('empleado', 'administrador')),
        contraseña TEXT NOT NULL
    );

    -- Tabla PRODUCTO
    CREATE TABLE Producto (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        categoria TEXT,
        descripcion TEXT,
        modelo TEXT,
        precio_al_por_menor REAL NOT NULL,
        stock INTEGER NOT NULL,
        detalles_tecnicos TEXT
    );

    -- Tabla PROVEEDOR
    CREATE TABLE Proveedor (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        contacto TEXT
    );

    -- Tabla MOVIMIENTO_INVENTARIO
    CREATE TABLE Movimiento_Inventario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_producto INTEGER NOT NULL,
        id_trabajador INTEGER NOT NULL,
        cantidad INTEGER NOT NULL,
        fecha TEXT NOT NULL,
        FOREIGN KEY (id_producto) REFERENCES Producto (id),
        FOREIGN KEY (id_trabajador) REFERENCES Trabajador (id)
    );

    -- Tabla VENTA
    CREATE TABLE Venta (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_cliente INTEGER NOT NULL,
        id_trabajador INTEGER NOT NULL,
        fecha TEXT NOT NULL,
        metodo_pago TEXT,
        observaciones TEXT,
        FOREIGN KEY (id_cliente) REFERENCES Cliente (id),
        FOREIGN KEY (id_trabajador) REFERENCES Trabajador (id)
    );

    -- Tabla DETALLE_VENTA
    CREATE TABLE Detalle_Venta (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_venta INTEGER NOT NULL,
        id_producto INTEGER NOT NULL,
        cantidad INTEGER NOT NULL,
        precio_unitario REAL NOT NULL,
        FOREIGN KEY (id_venta) REFERENCES Venta (id),
        FOREIGN KEY (id_producto) REFERENCES Producto (id)
    );

    -- Tabla SUMINISTRA
    CREATE TABLE Suministra (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_proveedor INTEGER NOT NULL,
        id_producto INTEGER NOT NULL,
        cantidad INTEGER NOT NULL,
        fecha TEXT NOT NULL,
        precio_al_por_mayor REAL,
        FOREIGN KEY (id_proveedor) REFERENCES Proveedor (id),
        FOREIGN KEY (id_producto) REFERENCES Producto (id)
    );
    """
    cursor.executescript(script_sql)
    conexion.commit()
    conexion.close()
    print("Base de datos y tablas creadas correctamente.")


def insert_initial_data():
    """Inserta datos iniciales en la base de datos."""
    print("Insertando datos iniciales...")
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    
    insert_data = """
    -- Insertar datos en la tabla CLIENTE
    INSERT INTO Cliente (nombre, contacto, direccion) VALUES
    ('Juan Pérez', '0987654321', 'Calle Falsa 123'),
    ('Ana López', '0998765432', 'Av. Siempre Viva 456'),
    ('Luis Gómez', '0976543210', 'Barrio Centro 789');

    -- Insertar datos en la tabla TRABAJADOR
    INSERT INTO Trabajador (nombre, tipo, contraseña) VALUES
    ('Carlos Ruiz', 'empleado', 'password123'),
    ('María Fernández', 'administrador', 'admin123'),
    ('Pedro Martínez', 'empleado', 'empleado123');

    -- Insertar datos en la tabla PRODUCTO
    INSERT INTO Producto (nombre, categoria, descripcion, modelo, precio_al_por_menor, stock, detalles_tecnicos) VALUES
    ('Televisor', 'Electrónica', 'Televisor LED de 50 pulgadas', 'Modelo-X', 500.00, 20, 'Resolución 4K, HDMI, USB'),
    ('Lavadora', 'Electrodomésticos', 'Lavadora automática de 15 kg', 'Modelo-Y', 300.00, 15, 'Carga superior, 5 modos de lavado'),
    ('Refrigerador', 'Electrodomésticos', 'Refrigerador de 300 litros', 'Modelo-Z', 700.00, 10, 'Eficiencia energética A+');

    -- Insertar datos en la tabla PROVEEDOR
    INSERT INTO Proveedor (nombre, contacto) VALUES
    ('ElectroPro', '0981234567'),
    ('HogarPerfecto', '0971234567'),
    ('TecnoGlobal', '0961234567');
    """
    cursor.executescript(insert_data)
    conexion.commit()
    conexion.close()
    print("Datos iniciales insertados correctamente.")


def initialize_db():
    """
    Verifica si la base de datos existe. Si no, la crea, inicializa las tablas y agrega datos iniciales.
    """
   

    # Verifica si el archivo de base de datos ya existe
    if os.path.exists(DATABASE_PATH):
        print(f"Base de datos ya creada en: {DATABASE_PATH}")
    else:
        print(f"Creando base de datos en: {DATABASE_PATH}")
        conexion = sqlite3.connect(DATABASE_PATH)
        cursor = conexion.cursor()

        # Crear tablas e insertar datos iniciales
        create_database(cursor)
        insert_initial_data(cursor)

        # Confirmar los cambios
        conexion.commit()
        print("Base de datos inicializada correctamente.")


