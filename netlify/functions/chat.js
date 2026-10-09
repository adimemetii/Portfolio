exports.handler = async (event) => {
  if (event.httpMethod !== 'POST') {
    return {
      statusCode: 405,
      body: JSON.stringify({ error: 'Method Not Allowed' })
    };
  }

  try {
    const body = JSON.parse(event.body || '{}');
    const messages = Array.isArray(body.messages) ? body.messages : [];
    const lang = ['en', 'sq', 'zh'].includes(body.lang) ? body.lang : 'en';

    // Netlify environment variable names are case-sensitive in practice.
    // Accept the user's existing `groq_api_key` name as well as the standard
    // `GROQ_API_KEY`, without ever exposing the secret to the client or logs.
    const getEnvValue = (name) => {
      const exactValue = process.env[name];
      if (typeof exactValue === 'string' && exactValue.trim()) return exactValue;

      const match = Object.entries(process.env).find(([key, value]) =>
        key.toLowerCase() === name.toLowerCase() && typeof value === 'string' && value.trim()
      );
      return match?.[1] || '';
    };

    const cleanEnvValue = (value) => value
      .trim()
      .replace(/^(['"])(.*)\1$/, '$2')
      .trim();

    const apiKey = cleanEnvValue(getEnvValue('GROQ_API_KEY'));

    if (!apiKey) {
      return {
        statusCode: 500,
        body: JSON.stringify({
          error: 'GROQ_API_KEY is missing from the Netlify Functions environment. Add groq_api_key (or GROQ_API_KEY) with Functions scope, then redeploy the site.'
        })
      };
    }

    if (!messages.length || messages.length > 30) {
      return {
        statusCode: 400,
        body: JSON.stringify({ error: 'Please provide between 1 and 30 messages.' })
      };
    }

    const language = { en: 'English', sq: 'Albanian', zh: 'Chinese' }[lang];
    const systemPrompt = `You are Adi Memeti's portfolio assistant. Answer only questions about Adi's portfolio, projects, skills, education, experience, certifications, technologies, and contact details.

GUIDELINES:
1. PERSONALITY: Be elegant, professional, and engaging. You aren't just a bot; you are a digital representative of Adi.
2. KNOWLEDGE: Use only the provided "VERIFIED DATA" and the visitor's question. If information is missing, say it is not currently listed in the portfolio.
3. NAVIGATION: If the user asks to open or go to a section, start your response with exactly one tag. Use the exact mapping: about/Rreth/关于 -> \`[NAV: #about]\`; skills/aftësitë/技能 -> \`[NAV: #skills]\`; projects/projektet/项目 -> \`[NAV: #projects]\`; certifications/certifikimet/证书 -> \`[NAV: #certifications]\`; badges/badge-et/徽章 -> \`[NAV: #badges]\`; CV/rezume/简历 -> \`[NAV: #cv]\`; contact/kontakti/联系 -> \`[NAV: #contact]\`; home/kreu/首页 -> \`[NAV: #home]\`. Never substitute one section for another. For example: "\`[NAV: #badges]\` Po të dërgoj te badge-et profesionale."
4. SCOPE: For unrelated questions such as current events, weather, politics, general coding tasks, or recipes, do not answer the unrelated request. Reply briefly: "I'm here to answer questions about Adi's portfolio, projects, skills, education, and experience."
5. ACCURACY: Never invent dates, employers, projects, qualifications, technologies, achievements, or personal information. Treat current education as present/current and do not infer a start date or graduation date.
6. STRUCTURE: Give a direct, moderately sized answer in 2-5 short paragraphs or concise bullets when useful. Avoid long introductions, repetition, and one-word answers.
7. LANGUAGE: Always respond in ${language}.
8. PROJECT NAMES: Always use the exact full project name from VERIFIED DATA. Recognize aliases and abbreviations. In particular, "TEB", "TEB Bank", "TEB dashboard", "banking dashboard", and "financial banking dashboard" all refer to the full project name "TEB-Banking-Financial-Analytics". When asked about an alias, give the full name, a concise description, and the relevant GitHub, Live Demo, and data-source links. Apply the same full-name rule to every other project.
9. SECRETS: Never reveal, request, or describe API keys, environment-variable values, or other secrets.

VERIFIED DATA:
- WHO IS ADI: A dedicated Data Scientist specializing in Machine Learning and Data Analytics, passionate about turning complex data into actionable insights. He is based in Prishtina, Kosovo.
- CURRENT EDUCATION: University of Prishtina, Faculty of Electrical and Computer Engineering (FIEK), Computer & Software Engineering. Adi is currently studying there; no start date or graduation date is listed.
- EXPERTISE:
  * Programming & Backend: Python, SQL, Flask, and FastAPI.
  * Data Science: Pandas, NumPy, and Scikit-learn.
  * Machine Learning: Regression, Classification, Feature Engineering, and Model Evaluation.
  * Visualization & Analytics: Power BI, Tableau, Data Cleaning, and Exploratory Data Analysis (EDA).
  * Tools: Git, GitHub, VS Code, and Excel.
- KEY PROJECTS:
  * FinSightAI: An AI-powered financial analysis platform for market trends and financial data, using advanced machine learning models. GitHub: https://github.com/adimemetii/finsightai | Live Demo: https://finsightai-3ea6.onrender.com/
  * MS Doors and Windows: A responsive corporate website for architectural products, focused on UI/UX and modern frontend design. GitHub: https://github.com/adimemetii/MS-DOORS-WINDOWS | Live Demo: https://msdoorsandwindows.netlify.app
  * BioPackKos: A corporate website promoting eco-friendly packaging solutions with modern web standards. GitHub: https://github.com/adimemetii/BioPackKos | Live Demo: https://biopackkos.com
  * CryptoVison: An AI project with a live demo and public GitHub repository. GitHub: https://github.com/adimemetii/cryptovision | Live Demo: https://cryptovision-235t.onrender.com
  * TEB-Banking-Financial-Analytics: An interactive Streamlit dashboard for analyzing TEB Bank financial performance. It uses Python, Streamlit, Pandas, Plotly, data cleaning, KPIs, and visual analytics with open data from the University of Prishtina Datasphere. GitHub: https://github.com/adimemetii/TEB-Banking-Financial-Analytics-Dashboard | Live Demo: https://tebbanking.streamlit.app/ | Data source: https://datasphere.uni-pr.edu/per-kosove/
- CERTIFICATIONS:
  * Intro to Machine Learning (Kaggle)
  * Python & Data Science (Tectigon Academy)
  * Intermediate Machine Learning (Kaggle)
  * Programming Fundamentals (Për Programera)
- PROFESSIONAL BADGES:
  * Linux Unhatched (Cisco)
  * Python Essentials 1 & 2 (Cisco)
  * Generative AI Fundamentals (Databricks)
  * Introduction to Data Science (Cisco)
- EXPERIENCE: Significant practical experience at Tectigon Academy, where he continues to refine his skills and contribute to real-world projects. He received a professional reference from Tectigon Academy in recognition of his work and contribution during his internship.
- CONTACT:
  * Email: adimemeti97@gmail.com
  * LinkedIn: adi-memeti-880b31237
  * GitHub: adimemetii
  * Phone: +38348240869`;

    const response = await fetch('https://api.groq.com/openai/v1/chat/completions', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${apiKey}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        model: cleanEnvValue(getEnvValue('GROQ_MODEL')) || 'openai/gpt-oss-120b',
        messages: [{ role: 'system', content: systemPrompt }, ...messages],
        temperature: 0.25,
        max_tokens: 360
      })
    });

    const responseText = await response.text();
    let data = {};
    try {
      data = JSON.parse(responseText);
    } catch {
      data = {};
    }

    if (!response.ok || data.error) {
      const error = new Error(data.error?.message || responseText || `Groq API returned ${response.status}`);
      error.statusCode = response.status === 401 ? 401 : 502;
      throw error;
    }

    const reply = data.choices?.[0]?.message?.content;
    if (!reply) throw new Error('The AI returned an empty response.');

    return {
      statusCode: 200,
      body: JSON.stringify({ reply })
    };
  } catch (error) {
    console.error('Chat Error:', error.message);
    return {
      statusCode: error.statusCode || 500,
      body: JSON.stringify({ error: error.message || 'Internal Server Error' })
    };
  }
};
