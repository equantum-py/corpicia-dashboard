# Despliegue en Streamlit Cloud (Producción)

Sigue estos pasos para que José y el resto de la gerencia puedan acceder al dashboard desde cualquier celular o notebook mediante una URL pública gratuita.

## Paso 1: Crear Repositorio en GitHub
1. Ingresa a [GitHub](https://github.com/) y crea una cuenta si no tienes una.
2. Haz clic en **"New repository"** (Nuevo repositorio).
3. Nómbralo (ej. `corpicia-dashboard`).
4. Márcalo como **Privado** (recomendado para proteger tus datos de Excel) o **Público**.
5. Haz clic en **Create repository**.

## Paso 2: Subir el Proyecto
Arrastra o sube los siguientes archivos desde tu carpeta `informe ejecutivo corpicia` al repositorio de GitHub:
- `app.py`
- `data_loader.py`
- `PROSPECTOS_CORPICIA.xlsx`
- `requirements.txt`
- La carpeta `.streamlit/` completa (con su `config.toml`)
- La carpeta `pages/` completa

## Paso 3: Conectar a Streamlit Cloud
1. Ingresa a [Streamlit Community Cloud](https://share.streamlit.io/) e inicia sesión vinculando tu cuenta de GitHub.
2. Haz clic en **"New app"** y selecciona **"Deploy a public app from GitHub"**.
3. En el formulario, selecciona:
   - **Repository:** `tu-usuario/corpicia-dashboard`
   - **Branch:** `main` (o la rama que hayas usado).
   - **Main file path:** `app.py`
4. En "Advanced settings", asegúrate de usar Python 3.10 o superior. No se requieren *Secrets* adicionales a menos que conectes una API externa luego.
5. Haz clic en **Deploy**.

## Paso 4: ¡Listo para compartir!
Streamlit instalará todas las librerías listadas en tu `requirements.txt`.
En unos 2 o 3 minutos, tu aplicación estará en vivo. Streamlit te asignará una URL parecida a:
`https://corpicia-dashboard.streamlit.app`

Envíale este link a José por WhatsApp. ¡No necesita instalar nada!

---
> **Actualizaciones Futuras:** Si modificas el Excel `PROSPECTOS_CORPICIA.xlsx` con nuevas ventas, simplemente súbelo de nuevo a GitHub. Streamlit detectará el cambio y actualizará el Dashboard automáticamente en vivo.
