import streamlit as st

st.set_page_config(
    page_title="Chika K Gangadharan | Portfolio",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Lato:wght@300;400;700&display=swap');

  :root {
    --bg:      #F0F4F1;
    --white:   #FFFFFF;
    --dark:    #1C2B1E;
    --green:   #3A6B45;
    --light-g: #7AAE85;
    --accent:  #C17B2A;
    --muted:   #7A8C7D;
    --border:  #C8D8CB;
  }

  html, body, [data-testid="stAppViewContainer"] {
    background: var(--bg) !important;
    color: var(--dark);
    font-family: 'Lato', sans-serif;
  }

  [data-testid="stHeader"] { background: transparent !important; }
  #MainMenu, footer, [data-testid="stToolbar"] { visibility: hidden; }

  h1, h2, h3 { font-family: 'Playfair Display', serif !important; }

  /* ── Hero ── */
  .hero {
    background: linear-gradient(135deg, var(--green) 0%, #2A4F32 100%);
    border-radius: 8px;
    padding: 3rem 2.5rem;
    color: white;
    margin-bottom: 2rem;
    display: flex;
    align-items: center;
    gap: 2rem;
  }
  .hero-text h1 {
    font-size: 2.8rem;
    color: white !important;
    margin: 0 0 0.3rem;
    line-height: 1.1;
  }
  .hero-text .italic { font-style: italic; color: #A8D4B0; }
  .hero-role {
    font-size: 0.85rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #A8D4B0;
    margin-bottom: 0.8rem;
  }
  .hero-bio {
    font-size: 0.9rem;
    color: rgba(255,255,255,0.85);
    line-height: 1.7;
    max-width: 560px;
  }
  .badge {
    display: inline-block;
    background: rgba(255,255,255,0.15);
    border: 1px solid rgba(255,255,255,0.3);
    border-radius: 20px;
    padding: 3px 12px;
    font-size: 0.7rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: white;
    margin-right: 6px;
    margin-top: 8px;
  }

  /* ── Section ── */
  .section-head {
    font-family: 'Playfair Display', serif;
    font-size: 1.4rem;
    color: var(--green);
    border-bottom: 2px solid var(--green);
    padding-bottom: 0.4rem;
    margin-bottom: 1.2rem;
  }
  .section-label {
    font-size: 0.65rem;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 0.5rem;
  }

  /* ── Cards ── */
  .card {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 1.3rem 1.5rem;
    margin-bottom: 1rem;
    border-left: 4px solid var(--green);
  }
  .card-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.05rem;
    color: var(--dark);
    margin-bottom: 0.2rem;
  }
  .card-sub {
    font-size: 0.78rem;
    color: var(--accent);
    font-weight: 700;
    letter-spacing: 0.05em;
    margin-bottom: 0.5rem;
  }
  .card-body {
    font-size: 0.82rem;
    color: var(--muted);
    line-height: 1.65;
  }

  /* ── Skill bars ── */
  .skill-row { margin-bottom: 0.9rem; }
  .skill-top {
    display: flex;
    justify-content: space-between;
    font-size: 0.78rem;
    margin-bottom: 3px;
    color: var(--dark);
  }
  .skill-track {
    height: 5px;
    background: var(--border);
    border-radius: 3px;
    overflow: hidden;
  }
  .skill-fill {
    height: 100%;
    background: linear-gradient(90deg, var(--green), var(--light-g));
    border-radius: 3px;
  }

  /* ── Pub card ── */
  .pub-card {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 1rem 1.3rem;
    margin-bottom: 0.8rem;
    position: relative;
  }
  .pub-card::before {
    content: '"';
    font-family: 'Playfair Display', serif;
    font-size: 3rem;
    color: var(--border);
    position: absolute;
    top: -8px;
    left: 10px;
    line-height: 1;
  }
  .pub-title {
    font-size: 0.82rem;
    font-weight: 700;
    color: var(--dark);
    margin-bottom: 0.3rem;
    padding-left: 1.5rem;
  }
  .pub-venue {
    font-size: 0.75rem;
    color: var(--muted);
    font-style: italic;
    padding-left: 1.5rem;
  }

  /* ── Stat blocks ── */
  .stat-card {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 1rem;
    text-align: center;
  }
  .stat-num {
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    color: var(--green);
    display: block;
  }
  .stat-lbl {
    font-size: 0.65rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--muted);
  }

  /* ── Contact ── */
  .contact-item {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 0.85rem;
    margin-bottom: 0.6rem;
    color: var(--dark);
  }
  .contact-icon {
    width: 28px;
    height: 28px;
    background: var(--green);
    color: white;
    border-radius: 50%;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 0.75rem;
    flex-shrink: 0;
  }

  [data-testid="column"] { padding: 0 0.5rem !important; }
</style>
""", unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-text">
    <div class="hero-role">Educator · Researcher · AI Enthusiast</div>
    <h1>Chika K<br><span class="italic">Gangadharan</span></h1>
    <p class="hero-bio">
      Dedicated educator with over 16 years of experience in Electronics.
      Proven expertise in curriculum development, event coordination,
      and fostering vibrant learning communities. Passionate about applying
      deep learning to plant disease detection for smarter, sustainable agriculture.
    </p>
    <div>
      <span class="badge">📍 Kerala, India</span>
      <span class="badge">🎓 PhD Candidate – AI</span>
      <span class="badge">📚 16+ Yrs Teaching</span>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Stats ─────────────────────────────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)
for col, (num, lbl) in zip(
    [c1, c2, c3, c4],
    [("16+", "Years of Teaching"), ("2", "Research Papers"), ("3", "Degrees"), ("∞", "Passion for AI")],
):
    with col:
        st.markdown(f"""
        <div class="stat-card">
          <span class="stat-num">{num}</span>
          <span class="stat-lbl">{lbl}</span>
        </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Tabs ──────────────────────────────────────────────────────────────────────
tabs = st.tabs(["🏛️  Experience", "🎓  Education", "🛠️  Skills", "📄  Research", "📬  Contact"])

# ── Tab 1: Experience ─────────────────────────────────────────────────────────
with tabs[0]:
    st.markdown('<div class="section-head">Work Experience</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
      <div class="card-title">Assistant Professor</div>
      <div class="card-sub">MES College Marampally &nbsp;|&nbsp; 2008 – Present</div>
      <div class="card-body">
        Teaching undergraduate and postgraduate students in Electronics and interdisciplinary domains for over 16 years.
        Published research papers in reputed journals; currently pursuing PhD in Artificial Intelligence.
        Successfully coordinated national-level workshops, technical quizzes, cultural events, and academic competitions.
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-head" style="margin-top:1.5rem">Resource Person</div>', unsafe_allow_html=True)

    resource_items = [
        ("Major Resource Person – AI Tools Workshop",
         "Center for Professional Development",
         "Familiarizing AI Tools for faculty and scholars of the institution."),
        ("Technical Session – Machine Intelligence",
         "THARANG 2K26 · IHRD, 8 Feb 2026",
         "Handled a session on Machine Intelligence at the technical fest organised by Institute of Human Resource Development."),
        ("Workshop – Neural Networks & ML",
         "MES Kallady College Mannarkkad",
         "Introduction to Neural Network and Machine Learning."),
    ]
    for title, sub, body in resource_items:
        st.markdown(f"""
        <div class="card">
          <div class="card-title">{title}</div>
          <div class="card-sub">{sub}</div>
          <div class="card-body">{body}</div>
        </div>""", unsafe_allow_html=True)

# ── Tab 2: Education ──────────────────────────────────────────────────────────
with tabs[1]:
    st.markdown('<div class="section-head">Education</div>', unsafe_allow_html=True)

    edu = [
        ("2025 – 2028", "PhD in Artificial Intelligence (Pursuing)", "Mahatma Gandhi University"),
        ("2011 – 2013", "MBA – Human Resource Management", "Bharatiar University"),
        ("2005 – 2007", "MSc Electronics", "MES College Marampally"),
    ]
    for years, degree, uni in edu:
        st.markdown(f"""
        <div class="card">
          <div class="card-sub">{years}</div>
          <div class="card-title">{degree}</div>
          <div class="card-body">{uni}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown('<div class="section-head" style="margin-top:1.5rem">Certifications & Memberships</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
      <div class="card-title">Certified Innovation Ambassador – Foundation Level</div>
      <div class="card-sub">MoE's Innovation Cell &nbsp;|&nbsp; 6 Aug 2025</div>
    </div>
    <div class="card">
      <div class="card-title">Member – Raman International Optronic Society</div>
      <div class="card-sub">Membership ID: RIOS/0295/2022 &nbsp;|&nbsp; 2022 – 2024</div>
    </div>
    """, unsafe_allow_html=True)

# ── Tab 3: Skills ─────────────────────────────────────────────────────────────
with tabs[2]:
    left, right = st.columns(2, gap="large")

    with left:
        st.markdown('<div class="section-head">Technical Skills</div>', unsafe_allow_html=True)
        skills = [
            ("Python", 88),
            ("C++", 72),
            ("TensorFlow / Keras", 80),
            ("Scikit-learn", 78),
            ("Matplotlib & Seaborn", 82),
            ("Deep Learning (LSTM, TL, XAI)", 85),
            ("Machine Learning", 87),
        ]
        for name, pct in skills:
            st.markdown(f"""
            <div class="skill-row">
              <div class="skill-top"><span>{name}</span><span>{pct}%</span></div>
              <div class="skill-track"><div class="skill-fill" style="width:{pct}%"></div></div>
            </div>""", unsafe_allow_html=True)

    with right:
        st.markdown('<div class="section-head">Domain Knowledge</div>', unsafe_allow_html=True)
        domains = [
            ("Analog Communication", 90),
            ("Power Electronics", 88),
            ("Digital Electronics", 88),
            ("Robotics", 75),
            ("Biomedical Instrumentation", 78),
            ("VLSI", 74),
        ]
        for name, pct in domains:
            st.markdown(f"""
            <div class="skill-row">
              <div class="skill-top"><span>{name}</span><span>{pct}%</span></div>
              <div class="skill-track"><div class="skill-fill" style="width:{pct}%"></div></div>
            </div>""", unsafe_allow_html=True)

        st.markdown('<div class="section-head" style="margin-top:1.5rem">Research AI Tools</div>', unsafe_allow_html=True)
        for tool in ["Scispace", "Notebook LM", "Logically", "Paperpal", "Research Rabbit"]:
            st.markdown(f"""
            <div style="display:inline-block;background:#E8F0EA;border:1px solid var(--border,#C8D8CB);
            border-radius:20px;padding:4px 14px;font-size:0.75rem;margin:4px 4px 0 0;color:#1C2B1E;">
            🌿 {tool}</div>""", unsafe_allow_html=True)

# ── Tab 4: Research ───────────────────────────────────────────────────────────
with tabs[3]:
    st.markdown('<div class="section-head">Research Publications</div>', unsafe_allow_html=True)

    pubs = [
        (
            "Churn Prediction – A Comparative Analysis with Supervised Machine Learning",
            "Advances and Applications in Mathematical Sciences, Vol. 20, Issue 12, Oct 2021, pp. 3049–3060",
        ),
        (
            "Feature Selection – A Performance Evaluation Using Objective Models of PCA and Gini Impurity",
            "4th International Conference on Recent Trends in Engineering Technology and Management | ISBN: 978-81-965908-7-1",
        ),
    ]
    for title, venue in pubs:
        st.markdown(f"""
        <div class="pub-card">
          <div class="pub-title">{title}</div>
          <div class="pub-venue">{venue}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown('<div class="section-head" style="margin-top:1.5rem">Research Interest</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
      <div class="card-title">🌱 Plant Disease Detection via Deep Learning</div>
      <div class="card-body">
        Deeply passionate about applying advanced deep learning techniques — including LSTM, Transfer Learning,
        and Explainable AI — to detect and manage plant diseases, contributing to smarter and more
        sustainable agricultural practices.
      </div>
    </div>
    """, unsafe_allow_html=True)

# ── Tab 5: Contact ────────────────────────────────────────────────────────────
with tabs[4]:
    left, right = st.columns([1, 1], gap="large")

    with left:
        st.markdown('<div class="section-head">Get in Touch</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="contact-item">
          <span class="contact-icon">📞</span>
          <span>+91-9846190713</span>
        </div>
        <div class="contact-item">
          <span class="contact-icon">✉</span>
          <span>kattchika35@gmail.com</span>
        </div>
        <div class="contact-item">
          <span class="contact-icon">📍</span>
          <span>Kerala, India</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="section-head" style="margin-top:1.8rem">References</div>', unsafe_allow_html=True)
        for name, role, phone, email in [
            ("Dr. Sabu M K", "Professor, Dept. of Computer Applications, CUSAT", "+919446128197", "sabumk@cusat.ac.in"),
            ("Dr. Jasmine P M", "Principal & Professor, MES Kallady College", "+919447050322", "jasmine@mesmarampally.org"),
        ]:
            st.markdown(f"""
            <div class="card">
              <div class="card-title">{name}</div>
              <div class="card-sub">{role}</div>
              <div class="card-body">📞 {phone}<br>✉ {email}</div>
            </div>""", unsafe_allow_html=True)

    with right:
        st.markdown('<div class="section-head">Send a Message</div>', unsafe_allow_html=True)
        name_in = st.text_input("Your Name")
        email_in = st.text_input("Your Email")
        subject  = st.selectbox("Subject", ["Collaboration", "Research Inquiry", "Workshop / Talk", "Other"])
        message  = st.text_area("Message", height=130)
        if st.button("📨  Send Message", use_container_width=True):
            if name_in and email_in and message:
                st.success(f"Thank you, {name_in}! Your message has been received.")
            else:
                st.warning("Please fill in all fields before sending.")

st.markdown("""
<hr style="border-color:#C8D8CB;margin:2.5rem 0 1rem">
<div style="text-align:center;font-size:0.7rem;color:#7A8C7D;letter-spacing:0.1em;">
  © 2026 Chika K Gangadharan &nbsp;·&nbsp; Assistant Professor & AI Researcher &nbsp;·&nbsp; Kerala, India
</div><br>
""", unsafe_allow_html=True)