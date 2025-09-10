# Blog de Recetas (Django • MVT)

Aplicación web estilo blog hecha con **Django** siguiendo el patrón **MVT**.  
Incluye herencia de templates, autenticación, perfiles, editor enriquecido (CKEditor), subida de imágenes, buscador y **mensajería** entre usuarios.

---

## 🎥 Video de demostración
➡️ https://TU-ENLACE-DE-VIDEO-AQUI 

---

## ✅ Funcionalidades
- Navbar con **Inicio, About, Pages, Perfil, Mensajes, Login/Logout**.
- **Pages**:
  - Campos: `title`, `subtitle`, `body`, `image`, `author`.
  - **Listado** con búsqueda (título, subtítulo, cuerpo) y paginación.
  - **Crear/Editar/Borrar** restringido a usuario logueado (**autor** o **staff**).
- **Mensajería**:
  - Enviar a otro usuario, ver bandeja de entrada y detalle (marca como leído).
- **Herencia de templates**

---

## 🚀 Instalación (Windows • PowerShell)

```bash
py -m venv .venv
.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver