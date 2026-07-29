# Dashboards DDV

Hub de accesos a dashboards DDV hecho con Streamlit.

## Archivos del repo

- `app.py`: aplicacion principal.
- `requirements.txt`: dependencias para Streamlit Cloud.
- `.streamlit/config.toml`: colores base del sitio.

## Como publicarlo en Streamlit Community Cloud

1. Crear un repo nuevo en GitHub, por ejemplo `dashboards-ddv`.
2. Subir estos archivos al repo.
3. Entrar a https://share.streamlit.io/.
4. Elegir `New app`.
5. Seleccionar el repo.
6. En `Main file path`, usar `app.py`.
7. Publicar.

Una vez publicado, Streamlit va a entregar una URL del estilo:

```text
https://dashboards-ddv.streamlit.app/
```

Esa URL se puede compartir con cualquier persona si la app queda publica.
