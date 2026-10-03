"""Regenerate the portfolio CV PDFs while preserving the existing visual system."""

from __future__ import annotations

import os
from pathlib import Path

from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "assets" / "docs"
PHOTO = ROOT / "assets" / "images" / "profilepicrmvbg.png"
PAGE_W, PAGE_H = A4
SIDEBAR_W = 166
CONTENT_X = 193
CONTENT_RIGHT = PAGE_W - 25
CONTENT_W = CONTENT_RIGHT - CONTENT_X

NAVY = HexColor("#102A43")
NAVY_ACCENT = HexColor("#173F5F")
BLUE = HexColor("#1D66A8")
LIGHT_BLUE = HexColor("#60A9D8")
BODY = HexColor("#243E5A")
MUTED = HexColor("#52677D")
PALE = HexColor("#F7FBFF")
PILL = HexColor("#214E70")


def register_fonts() -> tuple[str, str]:
    fonts_dir = Path(os.environ.get("WINDIR", r"C:\Windows")) / "Fonts"
    regular_path = fonts_dir / "arial.ttf"
    bold_path = fonts_dir / "arialbd.ttf"
    if regular_path.exists() and bold_path.exists():
        pdfmetrics.registerFont(TTFont("PortfolioArial", str(regular_path)))
        pdfmetrics.registerFont(TTFont("PortfolioArial-Bold", str(bold_path)))
        return "PortfolioArial", "PortfolioArial-Bold"
    return "Helvetica", "Helvetica-Bold"


REGULAR, BOLD = register_fonts()


PROJECTS = [
    {
        "title": "FinSightAI",
        "description": {
            "en": "AI-powered financial analysis platform for market and financial data insights.",
            "sq": "Platformë financiare e fuqizuar nga AI për analiza të tregut dhe të dhënave financiare.",
        },
        "github": "https://github.com/adimemetii/finsightai",
        "live": "https://finsightai-3ea6.onrender.com/",
    },
    {
        "title": "MS Doors and Windows",
        "description": {
            "en": "Responsive corporate website focused on product presentation and UI/UX.",
            "sq": "Faqe web korporative responsive me fokus në prezantimin e produkteve dhe UI/UX.",
        },
        "github": "https://github.com/adimemetii/MS-DOORS-WINDOWS",
        "live": "https://msdoorsandwindows.netlify.app",
    },
    {
        "title": "BioPackKos",
        "description": {
            "en": "Modern corporate web presence promoting eco-friendly packaging solutions.",
            "sq": "Prezencë moderne web që promovon zgjidhje ekologjike për paketim.",
        },
        "github": "https://github.com/adimemetii/BioPackKos",
        "live": "https://biopackkos.com",
    },
    {
        "title": "CryptoVison",
        "description": {
            "en": "Completed AI project with a live demo and public GitHub repository.",
            "sq": "Projekt i përfunduar i AI me demo live dhe repository publik në GitHub.",
        },
        "github": "https://github.com/adimemetii/cryptovision",
        "live": "https://cryptovision-235t.onrender.com",
    },
    {
        "title": "TEB-Banking-Financial-Analytics",
        "description": {
            "en": "Interactive Streamlit dashboard for TEB Bank financial performance, built with open UP Datasphere data and KPI/visual analytics.",
            "sq": "Dashboard interaktiv në Streamlit për performancën financiare të TEB Bank, me të dhëna të hapura nga UP Datasphere dhe analiza KPI/vizuale.",
        },
        "github": "https://github.com/adimemetii/TEB-Banking-Financial-Analytics-Dashboard",
        "live": "https://tebbanking.streamlit.app/",
        "data": "https://datasphere.uni-pr.edu/per-kosove/",
    },
]


CONTENT = {
    "en": {
        "subtitle": "DATA SCIENCE INTERN",
        "location": "Pristina, Kosovo  |  Data Science and Software Engineering",
        "profile_title": "PROFILE",
        "profile": "Computer & Software Engineering student focused on Data Science, Machine Learning, and Generative AI. Completed practical training in Python, data analysis, ML modeling, and modern AI technologies, with a strong focus on practical and data-driven solutions. Since August 2026, I have been part of Tectigon Academy as a Data Science Intern.",
        "experience": "EXPERIENCE",
        "role": "DATA SCIENCE INTERN, TECTIGON ACADEMY | August 2026 - Present",
        "experience_bullets": [
            "Practical work with Python, Pandas, SQL, and data analysis.",
            "Application of Machine Learning concepts, data preparation, and model evaluation.",
            "Use of Tableau and Microsoft Power BI for visualization and reporting.",
            "Exploration of Generative AI, LLMs, RAG, and Responsible AI principles.",
            "Received a professional reference from Tectigon Academy in recognition of my work and contribution during my internship.",
        ],
        "education": "EDUCATION",
        "university": "University of Prishtina - Faculty of Electrical and Computer Engineering (FIEK)",
        "program": "Program: Computer & Software Engineering",
        "current": "CURRENT EDUCATION | Currently studying",
        "course": "Për Programera - Full Stack Web Development | Course / Training",
        "projects": "SELECTED PROJECTS",
        "certifications": "CERTIFICATIONS & TRAINING",
        "certification_items": [
            "Intermediate Machine Learning - Kaggle",
            "Generative AI Fundamentals - Databricks",
            "Introduction to Machine Learning - Kaggle",
            "Python & Data Science - Tectigon Academy",
            "Introduction to Data Science - Cisco",
            "PCAP: Programming Essentials in Python - Cisco / NDG",
            "Linux Unhatched - Cisco / NDG",
            "Për Programera - Full Stack Web Development",
        ],
        "skills": "TECHNICAL SKILLS",
        "skill_groups": [
            ("Programming", "Python, SQL, Git, GitHub, Flask, FastAPI, VS Code"),
            ("Data Science", "Pandas, NumPy, Scikit-Learn, Data Analysis, Data Management, Data Preparation"),
            ("Machine Learning", "XGBoost, Gradient Boosting, Regression, Classification, Linear Regression, Decision Trees"),
            ("Modeling", "Cross-Validation, Pipelines, Feature Engineering, Categorical Encoding, Model Evaluation"),
            ("BI & Visualization", "Tableau, Microsoft Power BI, Excel"),
            ("Data & Analytics", "Data Cleaning, Exploratory Data Analysis (EDA)"),
            ("Generative AI", "LLM, RAG, AI Agents, Responsible AI"),
        ],
        "portfolio_links": "PORTFOLIO LINKS",
        "data_source": "Data source: UP Datasphere",
        "contact": "CONTACT",
        "languages": "LANGUAGES",
        "core": "CORE STRENGTHS",
        "language_items": [("Albanian", "Native / Excellent proficiency"), ("English", "Fluent / Excellent proficiency")],
        "core_items": ["Python", "SQL", "Pandas", "ML", "Power BI", "Tableau", "Git", "Excel", "LLM / RAG"],
        "footer": "Adi Memeti  |  DATA SCIENCE INTERN",
    },
    "sq": {
        "subtitle": "PRAKTIKANT I DATA SCIENCE",
        "location": "Prishtinë, Kosovë  |  Data Science dhe Inxhinieri Softuerike",
        "profile_title": "PROFILI",
        "profile": "Student i Inxhinierisë Kompjuterike dhe Softuerike me fokus në Data Science, Machine Learning dhe Generative AI. Kam përfunduar trajnime praktike në Python, analizë të të dhënave, modelim ML dhe teknologji moderne të AI, me fokus të fortë në zgjidhje praktike dhe të bazuara në të dhëna. Nga gushti 2026 jam pjesë e Tectigon Academy si Data Science Intern.",
        "experience": "PËRVOJA",
        "role": "DATA SCIENCE INTERN, TECTIGON ACADEMY | Gusht 2026 - Tani",
        "experience_bullets": [
            "Punë praktike me Python, Pandas, SQL dhe analizë të të dhënave.",
            "Aplikim i koncepteve të Machine Learning, përgatitjes së të dhënave dhe vlerësimit të modeleve.",
            "Përdorim i Tableau dhe Microsoft Power BI për vizualizim dhe raportim.",
            "Eksplorim i Generative AI, LLM-ve, RAG dhe parimeve të Responsible AI.",
            "Mora një referencë profesionale nga Tectigon Academy në njohje të punës dhe kontributit tim gjatë internshipit.",
        ],
        "education": "ARSIMI",
        "university": "Universiteti i Prishtinës - Fakulteti i Inxhinierisë Elektrike dhe Kompjuterike (FIEK)",
        "program": "Programi: Inxhinieri Kompjuterike dhe Softuerike",
        "current": "ARSIMI AKTUAL | Aktualisht duke studiuar",
        "course": "Për Programera - Full Stack Web Development | Kurs / Trajnim",
        "projects": "PROJEKTET E ZGJEDHURA",
        "certifications": "CERTIFIKIME & TRAJNIME",
        "certification_items": [
            "Intermediate Machine Learning - Kaggle",
            "Generative AI Fundamentals - Databricks",
            "Introduction to Machine Learning - Kaggle",
            "Python & Data Science - Tectigon Academy",
            "Introduction to Data Science - Cisco",
            "PCAP: Programming Essentials in Python - Cisco / NDG",
            "Linux Unhatched - Cisco / NDG",
            "Për Programera - Full Stack Web Development",
        ],
        "skills": "AFTËSITË TEKNIKE",
        "skill_groups": [
            ("Programim", "Python, SQL, Git, GitHub, Flask, FastAPI, VS Code"),
            ("Shkencë e të Dhënave", "Pandas, NumPy, Scikit-Learn, Data Analysis, Data Management, Data Preparation"),
            ("Machine Learning", "XGBoost, Gradient Boosting, Regression, Classification, Linear Regression, Decision Trees"),
            ("Modelim", "Cross-Validation, Pipelines, Feature Engineering, Categorical Encoding, Model Evaluation"),
            ("BI & Vizualizim", "Tableau, Microsoft Power BI, Excel"),
            ("Të Dhëna & Analitikë", "Data Cleaning, Analiza Eksploruese e të Dhënave (EDA)"),
            ("AI Gjenerative", "LLM, RAG, AI Agents, Responsible AI"),
        ],
        "portfolio_links": "LIDHJET E PORTFOLIOS",
        "data_source": "Burimi i të dhënave: UP Datasphere",
        "contact": "KONTAKTI",
        "languages": "GJUHËT",
        "core": "PIKAT KRYESORE",
        "language_items": [("Shqip", "Gjuhë amtare / Njohuri të shkëlqyera"), ("Anglisht", "Rrjedhshëm / Njohuri të shkëlqyera")],
        "core_items": ["Python", "SQL", "Pandas", "ML", "Power BI", "Tableau", "Git", "Excel", "LLM / RAG"],
        "footer": "Adi Memeti  |  PRAKTIKANT I DATA SCIENCE",
    },
}


def wrap_text(text: str, font: str, size: float, width: float) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if not current or pdfmetrics.stringWidth(candidate, font, size) <= width:
            current = candidate
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines or [""]


def draw_lines(c: canvas.Canvas, text: str, x: float, y_top: float, width: float, *, font: str = REGULAR, size: float = 8.35, leading: float = 11.4, color=BODY, bullet: str | None = None) -> float:
    lines = wrap_text(text, font, size, width - (10 if bullet else 0))
    c.setFont(font, size)
    c.setFillColor(color)
    y = y_top
    for index, line in enumerate(lines):
        prefix = f"{bullet} " if bullet and index == 0 else ("  " if bullet else "")
        c.drawString(x, PAGE_H - y - size, prefix + line)
        y += leading
    return y


def draw_section(c: canvas.Canvas, title: str, y_top: float) -> float:
    c.setFont(BOLD, 10.8)
    c.setFillColor(BLUE)
    c.drawString(CONTENT_X, PAGE_H - y_top - 10.8, title)
    c.setStrokeColor(BLUE)
    c.setLineWidth(0.8)
    c.line(CONTENT_X, PAGE_H - y_top - 20, CONTENT_RIGHT, PAGE_H - y_top - 20)
    return y_top + 30


def draw_sidebar(c: canvas.Canvas, data: dict[str, object]) -> None:
    c.setFillColor(NAVY)
    c.rect(0, 0, SIDEBAR_W, PAGE_H, fill=1, stroke=0)
    c.setFillColor(NAVY_ACCENT)
    c.rect(0, PAGE_H - 8, SIDEBAR_W, 8, fill=1, stroke=0)

    center_x = 83
    center_y = PAGE_H - 96
    c.setFillColor(PALE)
    c.circle(center_x, center_y, 56, fill=1, stroke=0)
    c.setStrokeColor(HexColor("#8CC8ED"))
    c.setLineWidth(1.5)
    c.circle(center_x, center_y, 56, fill=0, stroke=1)
    c.drawImage(ImageReader(str(PHOTO)), center_x - 56, center_y - 56, width=112, height=112, mask="auto", preserveAspectRatio=True)

    def side_section(title: str, top: float, content: list[tuple[str, str]] | list[str], pills: bool = False, simple: bool = False) -> None:
        c.setFont(BOLD, 8.6)
        c.setFillColor(PALE)
        c.drawString(20, PAGE_H - top - 8.6, title)
        c.setStrokeColor(LIGHT_BLUE)
        c.setLineWidth(0.6)
        c.line(20, PAGE_H - top - 18, 146, PAGE_H - top - 18)
        y = top + 29
        if pills:
            x = 20
            for item in content:
                label = str(item)
                pill_w = pdfmetrics.stringWidth(label, BOLD, 7.0) + 14
                if x + pill_w > 146:
                    x = 20
                    y += 23
                c.setFillColor(PILL)
                c.setStrokeColor(LIGHT_BLUE)
                c.roundRect(x, PAGE_H - y - 17, pill_w, 17, 4, fill=1, stroke=1)
                c.setFont(BOLD, 7.0)
                c.setFillColor(white)
                c.drawString(x + 7, PAGE_H - y - 12, label)
                x += pill_w + 5
            return
        if simple:
            for item in content:
                y = draw_lines(c, str(item), 20, y, 126, font=REGULAR, size=7.5, leading=10, color=PALE)
                y += 7
            return
        for heading, detail in content:
            c.setFont(BOLD, 8.0)
            c.setFillColor(PALE)
            c.drawString(20, PAGE_H - y - 8, heading)
            y += 14
            y = draw_lines(c, detail, 20, y, 126, font=REGULAR, size=7.5, leading=10, color=PALE)
            y += 10

    side_section(str(data["contact"]), 174, ["+383 48 240 869", "adimemeti97@gmail.com", "LinkedIn", "GitHub"], simple=True)
    # Add clickable sidebar contact links without changing the visual text.
    c.linkURL("mailto:adimemeti97@gmail.com", (20, PAGE_H - 231, 146, PAGE_H - 217), relative=0)
    c.linkURL("https://www.linkedin.com/in/adi-memeti-880b31237/", (20, PAGE_H - 248, 146, PAGE_H - 234), relative=0)
    c.linkURL("https://github.com/adimemetii", (20, PAGE_H - 265, 146, PAGE_H - 251), relative=0)
    side_section(str(data["languages"]), 282, data["language_items"])
    side_section(str(data["core"]), 390, data["core_items"], pills=True)

    c.setStrokeColor(LIGHT_BLUE)
    c.setLineWidth(0.6)
    c.line(20, 48, 146, 48)
    c.setFont(REGULAR, 7.2)
    c.setFillColor(PALE)
    c.drawString(20, 34, "Data Science  |  Software Engineering")


def draw_header(c: canvas.Canvas, data: dict[str, object]) -> float:
    c.setFont(BOLD, 25)
    c.setFillColor(BODY)
    c.drawString(CONTENT_X, PAGE_H - 20 - 25, "ADI MEMETI")
    c.setFont(BOLD, 11.5)
    c.setFillColor(BLUE)
    c.drawString(CONTENT_X, PAGE_H - 51 - 11.5, str(data["subtitle"]))
    c.setFont(REGULAR, 8.25)
    c.setFillColor(MUTED)
    c.drawString(CONTENT_X, PAGE_H - 75 - 8.25, str(data["location"]))
    c.setFont(REGULAR, 7.75)
    c.setFillColor(BLUE)
    c.drawString(CONTENT_X, PAGE_H - 93 - 7.75, "+383 48 240 869")
    c.drawString(CONTENT_X + 104, PAGE_H - 93 - 7.75, "adimemeti97@gmail.com")
    c.drawString(CONTENT_X + 250, PAGE_H - 93 - 7.75, "LinkedIn")
    c.drawString(CONTENT_X + 302, PAGE_H - 93 - 7.75, "GitHub")
    c.linkURL("mailto:adimemeti97@gmail.com", (CONTENT_X + 104, PAGE_H - 101, CONTENT_X + 220, PAGE_H - 90), relative=0)
    c.linkURL("https://www.linkedin.com/in/adi-memeti-880b31237/", (CONTENT_X + 250, PAGE_H - 101, CONTENT_X + 294, PAGE_H - 90), relative=0)
    c.linkURL("https://github.com/adimemetii", (CONTENT_X + 302, PAGE_H - 101, CONTENT_X + 345, PAGE_H - 90), relative=0)
    c.setStrokeColor(BLUE)
    c.setLineWidth(1.1)
    c.line(CONTENT_X, PAGE_H - 111, CONTENT_RIGHT, PAGE_H - 111)
    return 125


def draw_projects(c: canvas.Canvas, data: dict[str, object], y_top: float) -> float:
    y = draw_section(c, str(data["projects"]), y_top)
    col_gap = 22
    col_w = (CONTENT_W - col_gap) / 2
    row_height = 68
    for index, project in enumerate(PROJECTS):
        row, col = divmod(index, 2)
        x = CONTENT_X + col * (col_w + col_gap)
        top = y + row * row_height
        c.setFont(BOLD, 8.45)
        c.setFillColor(BODY)
        c.drawString(x, PAGE_H - top - 8.45, project["title"])
        desc_top = top + 13
        desc_end = draw_lines(c, project["description"]["en" if data["subtitle"].startswith("DATA") else "sq"], x, desc_top, col_w, size=7.7, leading=9.5)
        link_top = max(desc_end + 2, top + 39)
        c.setFont(BOLD, 6.9)
        c.setFillColor(BLUE)
        c.drawString(x, PAGE_H - link_top - 6.9, "GitHub  |  Live Demo")
        c.linkURL(project["github"], (x, PAGE_H - link_top - 8.5, x + 28, PAGE_H - link_top + 1.5), relative=0)
        c.linkURL(project["live"], (x + 40, PAGE_H - link_top - 8.5, x + 95, PAGE_H - link_top + 1.5), relative=0)
        if project.get("data"):
            c.setFont(REGULAR, 6.7)
            label = str(data["data_source"])
            c.drawString(x, PAGE_H - link_top - 17, label)
            c.linkURL(project["data"], (x, PAGE_H - link_top - 18.5, x + col_w, PAGE_H - link_top - 8), relative=0)
    return y + ((len(PROJECTS) + 1) // 2) * row_height + 4


def draw_page_one(c: canvas.Canvas, data: dict[str, object]) -> None:
    draw_sidebar(c, data)
    y = draw_header(c, data)
    y = draw_section(c, str(data["profile_title"]), y)
    y = draw_lines(c, str(data["profile"]), CONTENT_X, y, CONTENT_W, size=8.45, leading=11.4) + 8
    y = draw_section(c, str(data["experience"]), y)
    c.setFont(BOLD, 8.45)
    c.setFillColor(BODY)
    c.drawString(CONTENT_X, PAGE_H - y - 8.45, str(data["role"]))
    y += 17
    for bullet in data["experience_bullets"]:
        y = draw_lines(c, bullet, CONTENT_X, y, CONTENT_W, size=8.1, leading=11.5, bullet="-") + 3
    y += 5
    y = draw_section(c, str(data["education"]), y)
    c.setFont(BOLD, 8.2)
    c.setFillColor(BODY)
    y = draw_lines(c, str(data["university"]), CONTENT_X, y, CONTENT_W, font=BOLD, size=8.2, leading=11.2)
    y += 3
    y = draw_lines(c, str(data["program"]), CONTENT_X, y, CONTENT_W, size=8.2, leading=11.2)
    y += 3
    c.setFont(BOLD, 8.0)
    c.setFillColor(BLUE)
    c.drawString(CONTENT_X, PAGE_H - y - 8, str(data["current"]))
    y += 18
    y = draw_lines(c, str(data["course"]), CONTENT_X, y, CONTENT_W, font=REGULAR, size=8.0, leading=11.2) + 7
    draw_projects(c, data, y)
    draw_footer(c, data)


def draw_page_two(c: canvas.Canvas, data: dict[str, object]) -> None:
    draw_sidebar(c, data)
    y = 30
    y = draw_section(c, str(data["certifications"]), y)
    for item in data["certification_items"]:
        y = draw_lines(c, item, CONTENT_X, y, CONTENT_W, size=8.25, leading=14, bullet="-") + 1
    y += 14
    y = draw_section(c, str(data["skills"]), y)
    col_gap = 22
    col_w = (CONTENT_W - col_gap) / 2
    blocks = data["skill_groups"]
    row_y = y
    for index, (title, items) in enumerate(blocks):
        row, col = divmod(index, 2)
        if col == 0 and index > 0:
            row_y += 59
        x = CONTENT_X + col * (col_w + col_gap)
        top = row_y
        c.setFont(BOLD, 8.2)
        c.setFillColor(BLUE)
        c.drawString(x, PAGE_H - top - 8.2, title)
        draw_lines(c, items, x, top + 14, col_w, size=7.7, leading=9.8)
    y_after_skills = row_y + 59
    y = draw_section(c, str(data["portfolio_links"]), y_after_skills + 9)
    col_w = (CONTENT_W - col_gap) / 2
    for index, project in enumerate(PROJECTS):
        row, col = divmod(index, 2)
        x = CONTENT_X + col * (col_w + col_gap)
        top = y + row * 31
        c.setFont(BOLD, 7.7)
        c.setFillColor(BODY)
        c.drawString(x, PAGE_H - top - 7.7, project["title"])
        c.setFont(REGULAR, 6.8)
        c.setFillColor(BLUE)
        c.drawString(x, PAGE_H - top - 18, "GitHub  |  Live Demo")
        c.linkURL(project["github"], (x, PAGE_H - top - 19.5, x + 28, PAGE_H - top - 9), relative=0)
        c.linkURL(project["live"], (x + 40, PAGE_H - top - 19.5, x + 95, PAGE_H - top - 9), relative=0)
    draw_footer(c, data)


def draw_footer(c: canvas.Canvas, data: dict[str, object]) -> None:
    c.setStrokeColor(BLUE)
    c.setLineWidth(0.8)
    c.line(CONTENT_X, 25, CONTENT_RIGHT, 25)
    c.setFont(REGULAR, 7.2)
    c.setFillColor(MUTED)
    c.drawString(CONTENT_X, 12, str(data["footer"]))


def build_pdf(language: str, output_path: Path) -> None:
    data = CONTENT[language]
    pdf = canvas.Canvas(str(output_path), pagesize=A4, pageCompression=1)
    pdf.setTitle("Adi Memeti - English CV" if language == "en" else "Adi Memeti - CV Shqip")
    pdf.setAuthor("Adi Memeti")
    draw_page_one(pdf, data)
    pdf.showPage()
    draw_page_two(pdf, data)
    pdf.save()


if __name__ == "__main__":
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    build_pdf("en", OUTPUT_DIR / "Adi_Memeti_CV_English (1).pdf")
    build_pdf("sq", OUTPUT_DIR / "Adi_Memeti_CV_Shqip (1).pdf")
    print("Generated English and Shqip CV PDFs.")
