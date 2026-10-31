import streamlit as st
from pathlib import Path

# ==========================================================
# CONFIGURACIÓN
# ==========================================================
st.set_page_config(
    page_title="Portafolio | Diseño Interactivo",
    page_icon="🧡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE_DIR = Path(__file__).parent
IMAGE_DIR = BASE_DIR / "imagenes"

# ==========================================================
# PROYECTOS
# Las imágenes se guardan en la carpeta "imagenes".
# Los enlaces llevan a las aplicaciones publicadas.
# ==========================================================
PROJECTS = [
    {
        "title": "Mi primera app",
        "category": "Primeros pasos",
        "description": "Una primera exploración en la creación de aplicaciones interactivas con Streamlit.",
        "image": "mi_primera_app.jpg",
        "url": "https://mi-primera-app-acnkbmdru6hrq23we4wn5n5.streamlit.app/",
    },
    {
        "title": "De texto a voz",
        "category": "Audio · Accesibilidad",
        "description": "Convierte texto escrito en audio para escuchar el contenido de una manera diferente.",
        "image": "de_texto_a_voz.jpg",
        "url": "https://ndup8uh9tkma6edutrs3ye.streamlit.app/",
    },
    {
        "title": "Traductor",
        "category": "Lenguaje",
        "description": "Una herramienta para traducir y revisar textos entre idiomas.",
        "image": "traductor.jpg",
        "url": "https://traductor-ywqrsn66bqruhszpjx2kmb.streamlit.app/#2-revisa-tu-texto",
    },
    {
        "title": "OCR",
        "category": "Visión por computador",
        "description": "Explora el reconocimiento óptico de caracteres para extraer texto de imágenes.",
        "image": "ocr.jpg",
        "url": "https://9keavblldsdbcnqysmtnwx.streamlit.app/",
    },
    {
        "title": "Imágenes, texto, traducciones y audio",
        "category": "Multimodal",
        "description": "Integra diferentes formas de procesar contenido: imágenes, texto, traducciones y audio.",
        "image": "ocr_traducciones_audio.jpg",
        "url": "https://ocr-audio-jnqxs2tbgefvasrt59qxtc.streamlit.app/",
    },
    {
        "title": "WordCloud Studio",
        "category": "Visualización de texto",
        "description": "Representa visualmente las palabras más frecuentes de un texto mediante nubes de palabras.",
        "image": "wordcloud_studio.jpg",
        "url": "https://wordcloud0-cxswtkbvvgaum8hpflggpc.streamlit.app/",
    },
    {
        "title": "Escuchadero EAFIT",
        "category": "Análisis de sentimiento",
        "description": "Un proyecto para explorar el análisis de sentimientos y la interpretación de textos.",
        "image": "escuchadero_eafit.jpg",
        "url": "https://sentimenta-ed68e57e5fcjbnsqf8rvd5.streamlit.app/",
    },
    {
        "title": "EAFITRESPONDE",
        "category": "Búsqueda inteligente · PLN",
        "description": "Busca el documento más relacionado con una pregunta usando TF-IDF y similitud coseno.",
        "image": "eafitresponde.jpg",
        "url": "https://tfidfeafit-tkk866c5gyuhh6h4qgd3eh.streamlit.app/",
    },
    {
        "title": "Detección de objetos en imágenes",
        "category": "Visión por computador",
        "description": "Experimenta con técnicas de inteligencia artificial para reconocer objetos en imágenes.",
        "image": "deteccion_objetos.jpg",
        "url": "https://clase9-7uln6n6sftuutrisciaafa.streamlit.app/",
    },
    {
        "title": "Detección de movimientos",
        "category": "Interacción · Movimiento",
        "description": "Explora la detección de movimientos como entrada para experiencias interactivas.",
        "image": "deteccion_movimientos.jpg",
        "url": "https://miappclase9-vi2ssx6gwgyvclpfctunyd.streamlit.app/",
    },
    {
        "title": "Detección de dígitos escritos a mano",
        "category": "Visión por computador · Machine learning",
        "description": "Dibuja un número y prueba un modelo entrenado para reconocer dígitos escritos a mano.",
        "image": "deteccion_digitos.jpg",
        "url": "https://mnistpred-main-clase12.streamlit.app/",
    },
    {
        "title": "Reconocimiento usando modelos de visión",
        "category": "Visión por computador",
        "description": "Experimenta con un modelo de visión que interpreta dibujos o imágenes para reconocer lo representado.",
        "image": "reconocimiento_modelos_vision.jpg",
        "url": "https://drawrecog-main-clase12.streamlit.app/",
    },
    {
        "title": "Tablero inteligente",
        "category": "Interacción · Visión por computador",
        "description": "Explora una experiencia de tablero interactivo que combina trazos y reconocimiento mediante tecnología.",
        "image": "tablero_inteligente.jpg",
        "url": "https://histinf-main-clase12.streamlit.app/",
    },
    {
        "title": "Lector de sensor MQTT",
        "category": "IoT · Sistemas ciberfísicos",
        "description": "Consulta datos publicados por sensores mediante MQTT y explora la comunicación entre dispositivos.",
        "image": "lector_sensor_mqtt.jpg",
        "url": "https://recepmqtt-main-clase.streamlit.app/",
    },
    {
        "title": "Control por voz",
        "category": "Interacción · Voz",
        "description": "Prueba una interfaz que utiliza comandos de voz como forma de interacción y control.",
        "image": "control_por_voz.jpg",
        "url": "https://ctrlvoice-main-clase.streamlit.app/",
    },
    {
        "title": "Cerradura inteligente",
        "category": "IoT · Sistemas ciberfísicos",
        "description": "Explora una cerradura inteligente que integra gestos y mecanismos de interacción física.",
        "image": "cerradura_inteligente.jpg",
        "url": "https://cerraduragestosfinal-14.streamlit.app/",
    },
]

# ==========================================================
# ESTILOS
# ==========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Roboto+Slab:wght@700;800;900&display=swap');

:root {
    --peach: #FFC8AA;
    --peach-light: #FFF1E8;
    --ink: #15100E;
    --muted: #5D4A40;
    --white: #FFFDFB;
    --line: #E7A987;
}
.stApp {
    background: var(--peach);
    color: var(--ink);
    font-family: 'DM Sans', sans-serif;
}
[data-testid="stHeader"] {
    background: rgba(255, 200, 170, 0.92);
}
.block-container {
    max-width: 1240px;
    padding-top: 2.3rem;
    padding-bottom: 2rem;
}
.hero-kicker {
    text-transform: uppercase;
    letter-spacing: .18em;
    font-size: .78rem;
    font-weight: 800;
    color: var(--muted);
    margin-bottom: 1rem;
}
.hero-title {
    font-family: 'Roboto Slab', Georgia, serif;
    font-size: clamp(3.2rem, 8vw, 7.4rem);
    font-weight: 900;
    letter-spacing: -.065em;
    line-height: .92;
    color: var(--ink);
    margin: 0;
}
.hero-title span {
    display: block;
    color: var(--white);
    -webkit-text-stroke: 1.5px var(--ink);
}
.hero-copy {
    font-size: 1.08rem;
    line-height: 1.7;
    max-width: 650px;
    color: var(--muted);
    margin-top: 1.5rem;
}
.hero-pill {
    display: inline-block;
    border: 1px solid var(--ink);
    border-radius: 999px;
    padding: .45rem .8rem;
    font-size: .8rem;
    font-weight: 700;
    margin: .25rem .25rem .25rem 0;
}
.section-heading {
    font-family: 'Roboto Slab', Georgia, serif;
    font-weight: 900;
    font-size: clamp(2rem, 4vw, 3.6rem);
    letter-spacing: -.045em;
    margin: 0;
    color: var(--ink);
}
.section-note {
    color: var(--muted);
    font-size: 1rem;
    line-height: 1.6;
    margin: .5rem 0 1.4rem 0;
}
.project-card {
    background: var(--white);
    border: 1.5px solid var(--ink);
    border-radius: 18px;
    overflow: hidden;
    height: 100%;
    box-shadow: 5px 5px 0 var(--ink);
    transition: transform .18s ease, box-shadow .18s ease;
}
.project-card:hover {
    transform: translate(-2px, -3px);
    box-shadow: 8px 8px 0 var(--ink);
}
.project-card img {
    width: 100%;
    aspect-ratio: 4 / 5;
    object-fit: cover;
    display: block;
    border-bottom: 1.5px solid var(--ink);
}
.project-content {
    padding: 1.1rem 1.1rem 1.25rem 1.1rem;
}
.project-category {
    font-size: .72rem;
    font-weight: 800;
    letter-spacing: .09em;
    text-transform: uppercase;
    color: #8A4B2C;
    margin-bottom: .55rem;
}
.project-title {
    font-family: 'Roboto Slab', Georgia, serif;
    font-size: 1.28rem;
    line-height: 1.15;
    font-weight: 900;
    margin: 0 0 .65rem 0;
}
.project-description {
    font-size: .92rem;
    line-height: 1.55;
    color: #5D4A40;
    min-height: 4.4rem;
}
a.project-link {
    display: inline-block;
    margin-top: .75rem;
    padding: .65rem .9rem;
    background: var(--ink);
    color: white !important;
    border-radius: 999px;
    font-size: .86rem;
    font-weight: 700;
    text-decoration: none !important;
}
a.project-link:hover {
    background: #8A4B2C;
}
.about-panel {
    background: var(--peach-light);
    border: 1.5px solid var(--ink);
    border-radius: 18px;
    padding: clamp(1.2rem, 3vw, 2rem);
}
.footer {
    border-top: 1px solid var(--ink);
    margin-top: 3rem;
    padding: 1.3rem 0 .5rem 0;
    display: flex;
    justify-content: space-between;
    gap: 1rem;
    flex-wrap: wrap;
    color: var(--muted);
    font-size: .85rem;
}
div[data-testid="stMarkdownContainer"] a:not(.project-link) {
    color: var(--ink);
}
@media (max-width: 640px) {
    .block-container { padding-left: 1rem; padding-right: 1rem; }
    .hero-title { font-size: 3.35rem; }
}
</style>
""", unsafe_allow_html=True)

# ==========================================================
# PORTADA
# ==========================================================
st.markdown("""
<div class="hero-kicker">PORTAFOLIO DIGITAL · PROYECTOS INTERACTIVOS</div>
<div class="hero-title">IDEAS QUE<br><span>SE VUELVEN</span> EXPERIENCIAS.</div>
<div class="hero-copy">
Un recorrido por mis primeras aplicaciones y experimentos con tecnología,
procesamiento de lenguaje natural, visión por computador y experiencias interactivas.
Cada proyecto es una oportunidad para aprender, explorar y convertir una idea en algo que se pueda probar.
</div>
<div style="margin-top:1rem">
    <span class="hero-pill">Diseño interactivo</span>
    <span class="hero-pill">Python · Streamlit</span>
    <span class="hero-pill">Inteligencia artificial</span>
    <span class="hero-pill">Prototipado</span>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# ==========================================================
# PROYECTOS
# ==========================================================
st.markdown('<div class="section-heading">Proyectos seleccionados<span style="color:#fff">.</span></div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-note">Dieciséis aplicaciones para explorar. Selecciona “Abrir proyecto” '
    'para visitar cada experiencia en vivo.</div>',
    unsafe_allow_html=True
)

# Filtro por categoría
categories = ["Todos"] + sorted({p["category"] for p in PROJECTS})
selected_category = st.selectbox("Filtrar proyectos por categoría", categories, label_visibility="collapsed")
visible_projects = PROJECTS if selected_category == "Todos" else [
    p for p in PROJECTS if p["category"] == selected_category
]

cols_per_row = 3
for start in range(0, len(visible_projects), cols_per_row):
    row_projects = visible_projects[start:start + cols_per_row]
    cols = st.columns(cols_per_row, gap="large")
    for col, project in zip(cols, row_projects):
        image_path = IMAGE_DIR / project["image"]
        with col:
            # Las tarjetas usan HTML para mantener el estilo de la identidad visual.
            from html import escape
            image_html = ""
            if image_path.exists():
                import base64
                mime = "image/jpeg"
                encoded = base64.b64encode(image_path.read_bytes()).decode("utf-8")
                image_html = f'<img src="data:{mime};base64,{encoded}" alt="{escape(project["title"])}">'
            else:
                image_html = '<div style="aspect-ratio:4/5;background:#FFE0CE;display:grid;place-items:center;font-size:3rem">✦</div>'

            st.markdown(f"""
            <div class="project-card">
                {image_html}
                <div class="project-content">
                    <div class="project-category">{escape(project["category"])}</div>
                    <div class="project-title">{escape(project["title"])}</div>
                    <div class="project-description">{escape(project["description"])}</div>
                    <a class="project-link" href="{escape(project["url"], quote=True)}" target="_blank" rel="noopener noreferrer">Abrir proyecto ↗</a>
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.write("")

# ==========================================================
# SOBRE ESTE PORTAFOLIO
# ==========================================================
st.write("")
st.markdown("""
<div class="about-panel">
    <div class="hero-kicker">UN PROCESO EN CONSTRUCCIÓN</div>
    <div class="section-heading" style="font-size:clamp(1.8rem,3vw,2.7rem)">Aprender haciendo.</div>
    <p style="font-size:1rem;line-height:1.75;color:#5D4A40;margin-bottom:0">
    Este portafolio reúne ejercicios y aplicaciones desarrolladas durante mi proceso de aprendizaje.
    En ellos exploro distintas formas de conectar personas, información y tecnología.
    Las descripciones son breves y pueden ampliarse con el objetivo, el proceso, las herramientas
    utilizadas y los aprendizajes de cada proyecto.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    <span><strong>PORTAFOLIO DIGITAL</strong> · Diseño Interactivo</span>
    <span>Hecho con curiosidad, código y creatividad 🧡</span>
</div>
""", unsafe_allow_html=True)
