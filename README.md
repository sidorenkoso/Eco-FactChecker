Eco-Factchecker AI: Multimodal Verification Dashboard

An interactive web application developed for a UNESCO Hackathon to cross-reference corporate ecological claims against scientific literature, specifically assessing avian biodiversity risks.

UI/UX & Dashboard Design:

Designed with a focus on explainability, visual clarity, and low cognitive load.

Key Features:

Human-in-the-Loop Interface: Prioritizes usability heuristics to allow researchers to easily verify AI-generated insights.

Generative AI Integration: Uses REST APIs (Gemini API) to summarize unstructured corporate reports.

Certainty Visualization: Dynamically calculates and visualizes certainty scores for ecological claims based on cross-referenced scientific literature.

NLP Processing: Extracts and analyzes key environmental claims related to avian biodiversity.

Tech Stack:

Frontend/UI: Streamlit (Python)

Backend: Python, REST APIs

AI/NLP: Gemini API, Natural Language Processing

Design: Figma (Wireframing & Prototyping)

How to Run Locally:

Clone the repository: git clone https://github.com/sidorenkoso/eco-factchecker-ai.git

Install dependencies: pip install -r requirements.txt

Set your Gemini API key in a .env file.

Run the Streamlit app: streamlit run app.py
