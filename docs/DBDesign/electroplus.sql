-- Crear la base de datos
CREATE DATABASE ElectroPlusDB;
USE ElectroPlusDB;

-- Tabla CLIENTE
CREATE TABLE Cliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    contacto VARCHAR(100),
    direccion VARCHAR(255)
);

-- Tabla TRABAJADOR
CREATE TABLE Trabajador (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    tipo ENUM('empleado', 'administrador') NOT NULL,
    contraseña VARCHAR(100) NOT NULL
);

-- Tabla PRODUCTO
CREATE TABLE Producto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    categoria VARCHAR(100),
    descripcion TEXT,
    modelo VARCHAR(100),
    precio_al_por_menor DECIMAL(10,2),
    stock INT NOT NULL,
    detalles_tecnicos TEXT
);

-- Tabla PROVEEDOR
CREATE TABLE Proveedor (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    contacto VARCHAR(100)
);

-- Tabla MOVIMIENTO_INVENTARIO
CREATE TABLE Movimiento_Inventario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_producto INT NOT NULL,
    id_trabajador INT NOT NULL,
    cantidad INT NOT NULL,
    fecha DATE NOT NULL,
    FOREIGN KEY (id_producto) REFERENCES Producto(id),
    FOREIGN KEY (id_trabajador) REFERENCES Trabajador(id)
);

-- Tabla VENTA
CREATE TABLE Venta (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    id_trabajador INT NOT NULL,
    fecha DATE NOT NULL,
    metodo_pago VARCHAR(50),
    observaciones TEXT,
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id),
    FOREIGN KEY (id_trabajador) REFERENCES Trabajador(id)
);

-- Tabla DETALLE_VENTA
CREATE TABLE Detalle_Venta (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_venta INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (id_venta) REFERENCES Venta(id),
    FOREIGN KEY (id_producto) REFERENCES Producto(id)
);

-- Tabla RELACIÓN PROVEEDOR-PRODUCTO (Suministra)
CREATE TABLE Suministra (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_proveedor INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL,
    fecha DATE NOT NULL,
    precio_al_por_mayor DECIMAL(10,2),
    FOREIGN KEY (id_proveedor) REFERENCES Proveedor(id),
    FOREIGN KEY (id_producto) REFERENCES Producto(id)
);


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

-- Insertar datos en la tabla MOVIMIENTO_INVENTARIO
INSERT INTO Movimiento_Inventario (id_producto, id_trabajador, cantidad, fecha) VALUES
(1, 1, 10, '2024-12-01'),
(2, 2, 5, '2024-12-02'),
(3, 1, 3, '2024-12-03');

-- Insertar datos en la tabla VENTA
INSERT INTO Venta (id_cliente, id_trabajador, fecha, metodo_pago, observaciones) VALUES
(1, 1, '2024-12-10', 'Efectivo', 'Cliente pidió entrega inmediata'),
(2, 2, '2024-12-11', 'Tarjeta', 'Cliente utilizó tarjeta de crédito'),
(3, 3, '2024-12-12', 'Efectivo', NULL);

-- Insertar datos en la tabla DETALLE_VENTA
INSERT INTO Detalle_Venta (id_venta, id_producto, cantidad, precio_unitario) VALUES
(1, 1, 1, 500.00),
(1, 2, 2, 300.00),
(2, 3, 1, 700.00),
(3, 1, 2, 500.00);

-- Insertar datos en la tabla SUMINISTRA
INSERT INTO Suministra (id_proveedor, id_producto, cantidad, fecha, precio_al_por_mayor) VALUES
(1, 1, 10, '2024-11-01', 450.00),
(2, 2, 5, '2024-11-02', 280.00),
(3, 3, 8, '2024-11-03', 650.00);

-- Consultas adicionales para análisis y visualización

-- Ver todos los clientes
SELECT * FROM Cliente;

-- Ver todos los trabajadores
SELECT * FROM Trabajador;

-- Ver todos los productos
SELECT * FROM Producto;

-- Ver el inventario actual de todos los productos
SELECT id, nombre, stock FROM Producto;

-- Ver movimientos de inventario por producto
SELECT mi.id, p.nombre AS producto, mi.cantidad, mi.fecha, t.nombre AS trabajador
FROM Movimiento_Inventario mi
JOIN Producto p ON mi.id_producto = p.id
JOIN Trabajador t ON mi.id_trabajador = t.id
ORDER BY mi.fecha;

-- Ver todas las ventas realizadas
SELECT v.id, c.nombre AS cliente, t.nombre AS trabajador, v.fecha, v.metodo_pago, v.observaciones
FROM Venta v
JOIN Cliente c ON v.id_cliente = c.id
JOIN Trabajador t ON v.id_trabajador = t.id
ORDER BY v.fecha;

-- Ver los detalles de una venta específica
SELECT dv.id, p.nombre AS producto, dv.cantidad, dv.precio_unitario, (dv.cantidad * dv.precio_unitario) AS subtotal
FROM Detalle_Venta dv
JOIN Producto p ON dv.id_producto = p.id
WHERE dv.id_venta = 1;

-- Ver el suministro de productos por proveedor
SELECT s.id, pr.nombre AS proveedor, p.nombre AS producto, s.cantidad, s.fecha, s.precio_al_por_mayor
FROM Suministra s
JOIN Proveedor pr ON s.id_proveedor = pr.id
JOIN Producto p ON s.id_producto = p.id
ORDER BY s.fecha;

-- Ver el total de ventas por cliente
SELECT c.nombre AS cliente, SUM(dv.cantidad * dv.precio_unitario) AS total_ventas
FROM Venta v
JOIN Cliente c ON v.id_cliente = c.id
JOIN Detalle_Venta dv ON v.id = dv.id_venta
GROUP BY c.nombre
ORDER BY total_ventas DESC;

-- Ver los productos más vendidos
SELECT p.nombre AS producto, SUM(dv.cantidad) AS total_vendido
FROM Detalle_Venta dv
JOIN Producto p ON dv.id_producto = p.id
GROUP BY p.nombre
ORDER BY total_vendido DESC;

