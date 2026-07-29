import base64
from pathlib import Path

import streamlit as st


BASE_DIR = Path(__file__).parent
LOGO_CANDIDATES = [
    BASE_DIR / "assets" / "logo-distribuidora-del-valle.png",
    BASE_DIR / "logo-distribuidora-del-valle.png",
]
LOGO_PATH = next((path for path in LOGO_CANDIDATES if path.exists()), None)


def image_data_uri(path):
    image_bytes = path.read_bytes()
    encoded = base64.b64encode(image_bytes).decode("utf-8")
    return f"data:image/png;base64,{encoded}"


st.set_page_config(
    page_title="Dashboards DDV",
    page_icon="📊",
    layout="wide",
)


DASHBOARDS = [
    {
        "name": "Tope Bultos",
        "description": "Control operativo de topes y volumen de bultos.",
        "url": "https://topebultos.streamlit.app/",
        "group": "Operaciones",
    },
    {
        "name": "Planificacion DDV",
        "description": "Planificacion diaria y seguimiento DDV.",
        "url": "https://planificacionddv.streamlit.app/",
        "group": "Planificacion",
    },
    {
        "name": "Repagos",
        "description": "Revision de repagos y estado de gestion.",
        "url": "https://repagos.streamlit.app/",
        "group": "Finanzas",
    },
    {
        "name": "KPIs Foco",
        "description": "Indicadores clave para seguimiento de foco.",
        "url": "https://kpisfoco.streamlit.app/",
        "group": "Indicadores",
    },
    {
        "name": "Planificacion IFEE",
        "description": "Planificacion y consulta del tablero IFEE.",
        "url": "https://planificacion-ifeevprb7is4zwjk6k5suo.streamlit.app/",
        "group": "Planificacion",
    },
    {
        "name": "NPS DDV",
        "description": "Analisis de satisfaccion y experiencia DDV.",
        "url": "https://npsddv.streamlit.app/",
        "group": "Experiencia",
    },
    {
        "name": "Reunion semanal ventas",
        "description": "Documento Loop para la reunion semanal.",
        "url": "https://loop.cloud.microsoft/p/eyJ3Ijp7InUiOiJodHRwczovL2dydXBvdmVuZXJvbmkuc2hhcmVwb2ludC5jb20vP25hdj1jejBsTWtZbVpEMWlJVXB6TTNWWU5GVmlNR3RYWlhSQ2JtdElkbkJWUXpSWWJqWnViakl5Tm1oSWRtVlRNVWhqZFU5Vk5ISnNhMUk0ZVRFMFRtaFVORkF4YmxKUE56VXdhSFltWmowd01USlpWakpQU0VFeVdrVXpOVUpHVFUxYVdrWkxSbFJSTWxkUVNVUlpTMGhZSm1NOUptWnNkV2xrUFRFJTNEIiwiciI6ZmFsc2V9LCJwIjp7InUiOiJodHRwczovL2dydXBvdmVuZXJvbmkuc2hhcmVwb2ludC5jb20vY29udGVudHN0b3JhZ2UvQ1NQXzVmZWVjZDI2LTFiODUtNDVkMi05ZWI0LTE5ZTQxZWZhNTQwYi9sYSUyMEJpYmxpb3RlY2ElMjBkZSUyMGRvY3VtZW50b3MvTG9vcEFwcERhdGEvUExBTlRJTExBJTIwJTIwUkVVTklPTiUyMFNFTUFOQUwlMjBERSUyMFZFTlRBUyUyMDEubG9vcD9uYXY9Y3owbE1rWmpiMjUwWlc1MGMzUnZjbUZuWlNVeVJrTlRVRjgxWm1WbFkyUXlOaTB4WWpnMUxUUTFaREl0T1dWaU5DMHhPV1UwTVdWbVlUVTBNR0ltWkQxaUlVcHpNM1ZZTkZWaU1HdFhaWFJDYm10SWRuQlZRelJZYmpadWJqSXlObWhJZG1WVE1VaGpkVTlWTkhKc2ExSTRlVEUwVG1oVU5GQXhibEpQTnpVd2FIWW1aajB3TVRKWlZqSlBTRVkzVjFoWFNrZENNMUJZTlVOS05GWkRVVTFQU2tSSVNWaE1KbU05SlRKR0ptWnNkV2xrUFRFJTNEIiwiciI6ZmFsc2V9LCJpIjp7ImkiOiJhNGMyY2M1My01YWE2LTRkNjMtODhmYS0yNDYyYzZmYzRlMWIifX0",
        "group": "Ventas",
    },
    {
        "name": "CxC DDV",
        "description": "Seguimiento de cuentas por cobrar DDV.",
        "url": "https://cxcddv.streamlit.app/",
        "group": "Finanzas",
    },
]


st.markdown(
    """
    <style>
    .stApp {
        background: #f7f8fb;
        color: #18212f;
    }
    .block-container {
        padding-top: 2.2rem;
        padding-bottom: 2.2rem;
        max-width: 1160px;
    }
    .hero {
        background: #ffffff;
        border: 1px solid #d8dee8;
        border-radius: 10px;
        padding: 28px 30px;
        margin-bottom: 22px;
        box-shadow: 0 1px 2px rgba(16, 24, 39, 0.06);
    }
    .hero-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 28px;
    }
    .hero-copy {
        min-width: 0;
    }
    .hero-logo {
        width: min(380px, 34vw);
        height: auto;
        flex: 0 1 380px;
    }
    .eyebrow {
        color: #69748a;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        margin-bottom: 8px;
    }
    .hero h1 {
        margin: 0;
        font-size: clamp(2.1rem, 5vw, 3.8rem);
        line-height: 1.04;
        color: #101827;
    }
    .hero p {
        margin: 12px 0 0;
        max-width: 680px;
        color: #4f5c70;
        font-size: 1rem;
        line-height: 1.65;
    }
    @media (max-width: 820px) {
        .hero-header {
            align-items: flex-start;
            flex-direction: column-reverse;
        }
        .hero-logo {
            width: min(420px, 100%);
        }
    }
    .card {
        min-height: 292px;
        background: #ffffff;
        border: 1px solid #d8dee8;
        border-radius: 8px;
        padding: 18px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        box-shadow: 0 1px 2px rgba(16, 24, 39, 0.05);
    }
    .badge {
        display: inline-block;
        width: fit-content;
        border-radius: 6px;
        background: #edf2fb;
        color: #2454a6;
        padding: 5px 9px;
        font-size: 0.74rem;
        font-weight: 700;
        margin-bottom: 10px;
    }
    .card h2 {
        margin: 0 0 8px;
        font-size: 1.18rem;
        line-height: 1.25;
        color: #18212f;
        min-height: 3rem;
    }
    .card p {
        margin: 0;
        color: #59667a;
        font-size: 0.9rem;
        line-height: 1.48;
    }
    .card a {
        display: block;
        width: 100%;
        box-sizing: border-box;
        text-align: center;
        background: #18212f;
        color: #ffffff !important;
        padding: 11px 12px;
        border-radius: 6px;
        text-decoration: none;
        font-weight: 700;
        margin-top: 18px;
    }
    .card a:hover {
        background: #2454a6;
        text-decoration: none;
    }
    div[data-testid="column"] {
        margin-bottom: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    f"""
    <div class="hero">
        <div class="hero-header">
            <div class="hero-copy">
                <div class="eyebrow">Centro de accesos</div>
                <h1>Dashboards DDV</h1>
            </div>
            {f'<img class="hero-logo" src="{image_data_uri(LOGO_PATH)}" alt="Distribuidora del Valle">' if LOGO_PATH else ''}
        </div>
        <p>Acceso rapido a los tableros operativos, comerciales y financieros. Hay {len(DASHBOARDS)} accesos disponibles.</p>
    </div>
    """,
    unsafe_allow_html=True,
)


columns = st.columns(4)
for index, dashboard in enumerate(DASHBOARDS):
    with columns[index % 4]:
        st.markdown(
            f"""
            <div class="card">
                <div>
                    <span class="badge">{dashboard["group"]}</span>
                    <h2>{dashboard["name"]}</h2>
                    <p>{dashboard["description"]}</p>
                </div>
                <a href="{dashboard["url"]}" target="_blank" rel="noreferrer">Abrir tablero</a>
            </div>
            """,
            unsafe_allow_html=True,
        )
