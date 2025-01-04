# Simulador de Inventario para Tienda ElectroPlus 🛒

## Descripción 📖
Este es un simulador de inventario diseñado para gestionar productos, controlar stock y registrar ventas en una tienda de electrodomésticos. Utiliza **Python** con una interfaz gráfica en **wxPython** y **SQLite** como base de datos para garantizar almacenamiento seguro y eficiente.

---

## Características 🛠️
- **Agregar, editar y eliminar productos** del inventario.
- **Controlar el stock** de productos en tiempo real.
- **Registrar ventas** y actualizar automáticamente el inventario.
- **Reposición automática** configurable según el nivel mínimo de stock.
- **Interfaz gráfica intuitiva** con `wxPython`.
- **Base de datos local** SQLite para persistencia de datos.

---

## Tecnologías 🚀
- **Python** 3.8+
- **wxPython** 4.2.1
- **SQLite** como base de datos local.
- Diseño siguiendo el patrón **Modelo-Vista-Controlador (MVC)**.

---

## Instalación 💻

1. Clona este repositorio:
   ```bash
   git clone https://github.com/mamomeri/tu-repositorio.git
   cd tu-repositorio
   ```

2. Instala las dependencias necesarias:
   ```bash
   pip install wxPython
   ```

3. Ejecuta el programa:
   ```bash
   python src/main.py
   ```

---

## Uso 📋
1. Inicia el programa con `src/main.py`.
2. Agrega nuevos productos al inventario desde la interfaz.
3. Realiza ventas y observa cómo el stock se actualiza automáticamente.
4. Configura niveles mínimos de stock para reposición automática.
5. Consulta y exporta reportes de inventario y ventas.

---

## Estructura del Proyecto 📂

```
ElectroPlus/
│
├── assets/             # Recursos visuales
│   └── images/         # Logos e imágenes
├── docs/               # Documentación del proyecto
│   ├── DBDesign/       # Diseños y diagramas de base de datos
│   └── Reports/        # Reportes técnicos
├── src/                # Código fuente principal
│   ├── DataBase/       # Scripts y datos de la base de datos
│   ├── MVC/            # Implementación del modelo-vista-controlador
│   ├── Utils/          # Funciones auxiliares y logger
│   └── Test/           # Pruebas unitarias
├── logs/               # Archivos de registro
└── temp/               # Archivos temporales
```

---

## Próximas Funcionalidades ✨
- Exportar reportes a formatos **PDF/Excel**.
- Implementar autenticación de usuarios.
- Añadir gráficos estadísticos para visualizar ventas.
- Gestión avanzada de usuarios y permisos.

---

## Contribuciones 🤝
¡Contribuciones son bienvenidas! Si deseas mejorar este proyecto, abre un **pull request** o inicia una **discusión**.

---

## Licencia 📄
Este proyecto está bajo la licencia **MIT**.

---

## Capturas de Pantalla 🖼️
> *(Aquí puedes añadir imágenes del programa en funcionamiento, como la interfaz gráfica o reportes generados).*

---

## Contacto 📧
Si tienes alguna pregunta o sugerencia, contáctame en:
- **GitHub:** [mamomeri](https://github.com/mamomeri)
