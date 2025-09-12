# Blog de Recetas — Proyecto Final (Django + MVT)

Proyecto final del curso: una app web en **Django 5** siguiendo el patrón **MVT**.  
Incluye páginas con contenido enriquecido, autenticación, perfil de usuario con edición y cambio de contraseña, y mensajería interna.

---

## 🧰 Stack & librerías

- **Python** 3.13
- **Django** 5.2
- **SQLite** (desarrollo)
- **Pillow** (imágenes)
- **django-ckeditor** (texto enriquecido)
- Archivos **static** y **media**

---

## 🎥 Video de demostración
https://drive.google.com/file/d/1jV7-_GdK4VJ9s9yK40oN9fIydBxywLzQ/view?usp=drive_link

---

## ✨ Funcionalidades

- Home con listado y buscador.
- Sección **Pages**:
  - Listado con **paginación** y **buscador** (`q`).
  - Detalle de página.
  - **CRUD** (crear/editar/borrar) para usuarios autenticados.
  - Editor enriquecido con CKEditor.
- **Autenticación**: registro, login, logout.
- **Perfil de usuario**:
  - Ver perfil con avatar, nombre, email, web, bio y cumpleaños.
  - **Editar perfil**.
  - **Cambiar contraseña**.
- **Mensajería interna** (inbox).

---

## 🚀 Instalación (Windows • PowerShell)

```bash
py -m venv .venv
.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver