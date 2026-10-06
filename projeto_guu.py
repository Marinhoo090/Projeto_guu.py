import os
import streamlit as st

# =====================================================
# ✏️ EDITE AQUI SEUS DADOS
# =====================================================
NOME = "Gustavo Marinho"
IDADE = 16
CIDADE = "Santana de Parnaíba, SP"
O_QUE_FAZ = O_QUE_FAZ = "Estudante 1° ano Ensino Médio | Desenvolvedor Python | Vibe Coder"
SOBRE_MIM = (
    "SOBRE MIM: Meu nome é Gustavo, tenho 16 anos e estou no 1º ano do ensino médio. Já concluí o PROJOV, onde aprendi bastante sobre o mercado de trabalho, como me comportar em um ambiente profissional e também tive contato com ferramentas como Excel, PowerPoint e Word. Além disso, fiz um curso de Python na Fábrica de Programadores, onde comecei a me interessar ainda mais por programação. Atualmente, continuo estudando Python, praticando e aprendendo coisas novas para melhorar cada vez mais meus conhecimentos na área de tecnologia."
    "Meu objetivo no momento é conseguir meu primeiro emprego, adquirir experiência profissional e aprender cada vez mais. Quero continuar estudando programação, principalmente Python, e desenvolver meus conhecimentos na área de tecnologia. Mais para frente, pretendo conseguir uma oportunidade como desenvolvedor em uma empresa e seguir construindo minha carreira na área de programação."

)

# Habilidades: "nome": nível de 0 a 100
HABILIDADES = {
    "Python": 60,
    "Streamlit": 50,
    "Excel": 40,
    "Lógica de programação": 65,
    "Comunicação": 75,
    "Vontade de aprender": 100
}

PROJETOS = [
    {
        "titulo": "Meu primeiro projeto",
        "descricao": "Meu primeiro projeto foi o GoldenBoyz Car, um sistema de aluguel de carros desenvolvido em Python utilizando Streamlit. Nele, o usuário pode escolher um carro, informar por quantos dias ficou com ele e quantos quilômetros percorreu. O sistema identifica o valor da diária de cada carro e, ao clicar em 'Calcular', calcula o preço total do aluguel, considerando tanto os dias alugados quanto os quilômetros rodados. Esse projeto foi importante para mim porque foi uma das primeiras vezes que desenvolvi uma aplicação com uma interface, colocando em prática conceitos de Python como listas, condições, variáveis, entrada de dados e cálculos.",
        "tecnologias": ["Python", "Streamlit"],
        "link": "https://github.com/Marinhoo090",
    },
    # copie o bloco acima para adicionar mais projetos
]


STATUS = "🟢 Disponível para freelas"
FOTO = "foto.png"  # coloque sua foto na mesma pasta (opcional)

EMAIL = "gustavomarinho829@gmail.com"
GITHUB = "https://github.com/Marinhoo090"
LINKEDIN = "https://linkedin.com/in/seu-usuario"
# =====================================================

st.set_page_config(page_title=f"{NOME} | Portfólio", page_icon="💻", layout="wide",
                   initial_sidebar_state="expanded")

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"], .stApp {
    font-family: 'Poppins', sans-serif;
}
.stApp {
    background: linear-gradient(160deg, #E3F2FF 0%, #CFE8FF 50%, #BFE0FF 100%);
}
#MainMenu, footer, [data-testid="stToolbar"] {visibility: hidden;}
header {background: transparent !important;}

/* tudo alinhado à esquerda */
.block-container {
    max-width: 1100px;
    margin-left: 0;
    padding: 3rem 3rem 4rem 4rem;
}

/* HERO */
.hero {
    background: linear-gradient(135deg, #1E6FD9 0%, #4DA3FF 100%);
    border-radius: 24px;
    padding: 44px 48px;
    margin-bottom: 28px;
    box-shadow: 0 12px 30px rgba(30, 111, 217, 0.30);
}
.hero .oi { color: #D6EBFF; font-size: 1.2rem; font-weight: 500; margin: 0; }
.hero .nome { color: #FFFFFF; font-size: 3.6rem; font-weight: 800; line-height: 1.1; margin: 4px 0 8px 0; }
.hero .cargo { color: #FFFFFF; font-size: 1.5rem; font-weight: 600; margin: 0 0 8px 0; }
.hero .frase { color: #E6F2FF; font-size: 1.15rem; margin: 0 0 22px 0; }
.chip {
    display: inline-block;
    background: rgba(255,255,255,0.22);
    color: #FFFFFF;
    padding: 8px 18px;
    border-radius: 999px;
    font-size: 1rem;
    font-weight: 500;
    margin: 0 10px 8px 0;
}

/* ABAS */
.stTabs [data-baseweb="tab-list"] { gap: 10px; border-bottom: none; }
.stTabs [data-baseweb="tab-highlight"], .stTabs [data-baseweb="tab-border"] { display: none; }
.stTabs [data-baseweb="tab"] {
    background: #FFFFFF;
    border-radius: 999px;
    padding: 10px 26px;
    height: auto;
    box-shadow: 0 2px 8px rgba(30,111,217,0.12);
}
.stTabs [data-baseweb="tab"] p { font-size: 1.1rem; font-weight: 600; color: #1E6FD9; }
.stTabs [aria-selected="true"] { background: #1E6FD9; }
.stTabs [aria-selected="true"] p { color: #FFFFFF !important; }

/* CARDS */
.titulo-secao { color: #0A2540; font-size: 2rem; font-weight: 700; margin: 24px 0 14px 0; }
.texto { color: #1B3A5C; font-size: 1.2rem; line-height: 1.8; }
.card {
    background: #FFFFFF;
    border-radius: 18px;
    padding: 24px 28px;
    margin-bottom: 18px;
    box-shadow: 0 6px 18px rgba(30,111,217,0.12);
    border-left: 6px solid #1E6FD9;
    transition: transform .2s ease, box-shadow .2s ease;
}
.card:hover { transform: translateY(-4px); box-shadow: 0 12px 26px rgba(30,111,217,0.22); }
.card h3 { color: #0A2540; font-size: 1.5rem; font-weight: 700; margin: 0 0 8px 0; }
.card p { color: #1B3A5C; font-size: 1.1rem; margin: 0 0 12px 0; }
.tag {
    display: inline-block;
    background: #E3F2FF;
    color: #1E6FD9;
    padding: 4px 14px;
    border-radius: 999px;
    font-size: .9rem;
    font-weight: 600;
    margin: 0 8px 6px 0;
}
.botao {
    display: inline-block;
    background: #1E6FD9;
    color: #FFFFFF !important;
    padding: 10px 24px;
    border-radius: 12px;
    font-weight: 600;
    text-decoration: none;
    margin: 6px 10px 6px 0;
}
.botao:hover { background: #1558B0; }

/* BARRAS DE HABILIDADE */
/* SIDEBAR */
[data-testid="stSidebar"] { background: linear-gradient(180deg, #1E6FD9 0%, #4DA3FF 100%); }
[data-testid="stSidebar"] * { color: #FFFFFF; }
[data-testid="stSidebar"] .avatar {
    width: 110px; height: 110px; border-radius: 50%;
    background: #FFFFFF; color: #1E6FD9 !important;
    font-size: 3rem; font-weight: 800;
    display: flex; align-items: center; justify-content: center;
    margin: 10px 0 16px 0;
}
[data-testid="stSidebar"] img { border-radius: 50%; margin-bottom: 12px; }
.side-nome { font-size: 1.8rem; font-weight: 700; margin: 0; }
.side-cargo { font-size: 1.05rem; margin: 0 0 14px 0; opacity: .95; }
.side-info { font-size: 1rem; margin: 0 0 6px 0; }
.side-status {
    display: inline-block; background: rgba(255,255,255,0.22);
    padding: 6px 14px; border-radius: 999px; font-size: .9rem; font-weight: 600; margin: 10px 0 18px 0;
}
.side-btn {
    display: block; background: rgba(255,255,255,0.2);
    padding: 10px 16px; border-radius: 12px; margin-bottom: 10px;
    text-decoration: none; font-weight: 600;
}
.side-btn:hover { background: rgba(255,255,255,0.35); }

.skill-topo { display: flex; justify-content: space-between; color: #0A2540; font-size: 1.15rem; font-weight: 600; }
.barra { background: #D6EBFF; border-radius: 999px; height: 12px; margin-top: 8px; }
.barra-cheia { background: linear-gradient(90deg, #1E6FD9, #4DA3FF); height: 12px; border-radius: 999px; }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# ---------- SIDEBAR ----------
with st.sidebar:
    if os.path.exists(FOTO):
        st.image(FOTO)
    else:
        st.markdown(f"<div class='avatar'>{NOME[0].upper()}</div>", unsafe_allow_html=True)

    st.markdown(
        f"<p class='side-nome'>{NOME}</p>"
        f"<p class='side-cargo'>{O_QUE_FAZ}</p>"
        f"<p class='side-info'> {IDADE} anos</p>"
        f"<p class='side-info'>📍 {CIDADE}</p>"
        f"<span class='side-status'>{STATUS}</span>",
        unsafe_allow_html=True,
    )

    pagina = st.radio(
        "Navegue pelo portfólio:",
        ["👤 Sobre mim", "⚡ Habilidades", "🚀 Projetos", "📬 Contato"],
    )

    st.markdown(
        "<br>"
        f"<a class='side-btn' href='mailto:{EMAIL}'>📧 Email</a>"
        f"<a class='side-btn' href='{GITHUB}' target='_blank'>🐙 GitHub</a>"
        f"<a class='side-btn' href='{LINKEDIN}' target='_blank'>💼 LinkedIn</a>",
        unsafe_allow_html=True,
    )

# ---------- HERO ----------
hero = (
    "<div class='hero'>"
    "<p class='oi'>👋 Olá, eu sou</p>"
    f"<p class='nome'>{NOME}</p>"
    f"<p class='cargo'>{O_QUE_FAZ}</p>"
    f"<span class='chip'> {IDADE} anos</span>"
    f"<span class='chip'>📍 {CIDADE}</span>"
    "</div>"
)
st.markdown(hero, unsafe_allow_html=True)

# ---------- CORPO (muda conforme a escolha na sidebar) ----------
if pagina == "👤 Sobre mim":
    st.markdown("<p class='titulo-secao'>Sobre mim</p>", unsafe_allow_html=True)
    st.markdown(f"<p class='texto'>{SOBRE_MIM}</p>", unsafe_allow_html=True)

elif pagina == "⚡ Habilidades":
    st.markdown("<p class='titulo-secao'>Habilidades</p>", unsafe_allow_html=True)
    for nome, nivel in HABILIDADES.items():
        st.markdown(
            "<div class='card'>"
            f"<div class='skill-topo'><span>{nome}</span><span>{nivel}%</span></div>"
            f"<div class='barra'><div class='barra-cheia' style='width:{nivel}%'></div></div>"
            "</div>",
            unsafe_allow_html=True,
        )

elif pagina == "🚀 Projetos":
    st.markdown("<p class='titulo-secao'>Projetos</p>", unsafe_allow_html=True)
    for p in PROJETOS:
        tags = "".join(f"<span class='tag'>{t}</span>" for t in p["tecnologias"])
        st.markdown(
            "<div class='card'>"
            f"<h3>{p['titulo']}</h3>"
            f"<p>{p['descricao']}</p>"
            f"{tags}<br>"
            f"<a class='botao' href='{p['link']}' target='_blank'>Ver projeto →</a>"
            "</div>",
            unsafe_allow_html=True,
        )

elif pagina == "📬 Contato":
    st.markdown("<p class='titulo-secao'>Vamos conversar?</p>", unsafe_allow_html=True)
    st.markdown(
        "<div class='card'>"
        f"<a class='botao' href='mailto:{EMAIL}'>📧 {EMAIL}</a>"
        f"<a class='botao' href='{GITHUB}' target='_blank'>🐙 GitHub</a>"
        f"<a class='botao' href='{LINKEDIN}' target='_blank'>💼 LinkedIn</a>"
        "</div>",
        unsafe_allow_html=True,
    )
