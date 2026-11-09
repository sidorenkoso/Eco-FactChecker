import streamlit as st
import google.generativeai as genai

API_KEY = "AQ.Ab8RN6LhuqtNnKlZdirRyC2DVfqZGfmcyfnO9j1kHS38r_wZ3A"

st.set_page_config(page_title="Eco-Factchecker AI", page_icon="🌍", layout="centered")

st.title("🌍 AI Ecological Fact-Checker")
st.markdown(
    "**UNESCO Hackathon Project**: Exposing greenwashing and analyzing cascading ecological risks for avian populations.")

st.markdown("---")
st.markdown("### Mandatory Evaluation Factors:")
st.markdown("- Direct Mortality & Collisions")
st.markdown("- Energetics & Fatigue")
st.markdown("- Habitat Degradation")
st.markdown("---")

st.subheader("Submit Corporate Statement for Analysis")
statement = st.text_area(
    "Input the infrastructure proposal or corporate claim:",
    height=150,
    placeholder="e.g., 'Our new glass architecture and wind turbine project is 100% eco-friendly and safe for local wildlife...'"
)

SYSTEM_PROMPT = """
You are an advanced Ecological Decision Support System (DSS) and Fact-Checking AI specialized in Ecology, Biology, Avian Biology, Metabolic Energetics, and Environmental Impact Assessment.
YOUR GOAL:
Critically evaluate promotional claims, corporate statements, and infrastructure proposals (wind farms, glass architecture, wetland drainage, deforestation) to detect greenwashing and expose hidden, cascading ecological risks.
MANDATORY ECOLOGICAL FACTORS TO EVALUATE:
1. DIRECT MORTALITY & COLLISION RISKS:
   * Avian collisions with wind turbine blades (especially during low visibility or migratory peaks).
   * Massive bird strikes against reflective, mirrored, or transparent glass structures (fatal Window Collisions).
2. ENERGETICS & PHYSIOLOGICAL FATIGUE:
   * Flight rerouting energetic costs (quantify estimated energy expenditure overhead, e.g., +15% to +40%).
   * Instinctive over-exertion: Birds often push through exhaustion until lethal physical collapse or mid-flight death occurs due to metabolic depletion.
3. HABITAT DEGRADATION & ANTHROPOGENIC IMPACTS:
   * Wind Turbines: Microclimate alteration, soil erosion, and vibration disruption around turbine foundations.
   * Wetland Drainage / Plant Construction: Destruction of critical stopover sites (Ramsar-level ecosystems), leading to mass starvation.
   * Deforestation: Forest canopy fragmentation, loss of nesting micro-habitats, edge effects.
OUTPUT FORMAT:
Your response MUST STRICTLY follow this structured format:
[VERDICT]
Option A: DECEPTIVE / GREENWASHING DETECTED (High Ecological Risk)
Option B: SEVERE ECOLOGICAL IMPACT (Irreversible Local Damage)
Option C: SCIENTIFICALLY SOUND (Low Impact)
[CASCADE RISK TREE]
Render a step-by-step logical causal chain using strictly text indentations:
* Step 1: Trigger (Human Action / Infrastructure Project)
* Step 2: Behavioral / Physical Interference
* Step 3: Physiological / Energetic Impact (% Energy Overhead / Metabolic Exhaustion)
* Step 4: Ecosystem Chain Reaction (Soil Erosion, Wetland Loss, Nesting Failure)
* Step 5: Final Population Outcome (Direct Mortality % / Regional Population Collapse)
[SCIENTIFIC JUSTIFICATION]
Provide a rigorous 3-4 sentence biological explanation citing specific ecological mechanisms.
[RECOMMENDED MITIGATION]
List 1-2 mandatory, science-backed requirements or explain why the project should be halted.
"""

if st.button("Run Ecological Assessment", type="primary"):
    if not statement:
        st.error("⚠️ Please provide a statement to analyze.")
    else:
        with st.spinner("Analyzing ecological impacts and metabolic energetics..."):
            try:
                genai.configure(api_key=API_KEY)

                model = genai.GenerativeModel(
                    model_name='gemini-3.6-flash',
                    system_instruction=SYSTEM_PROMPT
                )

                response = model.generate_content(statement)
                result_text = response.text

                st.markdown("---")
                st.subheader("📊 Assessment Results")

                parts = result_text.split("[")

                for part in parts:
                    if part.startswith("VERDICT]"):
                        verdict_text = part.replace("VERDICT]", "").strip()
                        if "DECEPTIVE" in verdict_text or "SEVERE" in verdict_text:
                            st.error(f"**VERDICT:** {verdict_text}")
                        else:
                            st.success(f"**VERDICT:** {verdict_text}")

                    elif part.startswith("CASCADE RISK TREE]"):
                        st.warning("**CASCADE RISK TREE:**")
                        tree_text = part.replace("CASCADE RISK TREE]", "").strip()
                        st.code(tree_text, language="markdown")

                    elif part.startswith("SCIENTIFIC JUSTIFICATION]"):
                        st.info("**SCIENTIFIC JUSTIFICATION:**")
                        st.write(part.replace("SCIENTIFIC JUSTIFICATION]", "").strip())

                    elif part.startswith("RECOMMENDED MITIGATION]"):
                        st.success("**RECOMMENDED MITIGATION:**")
                        st.write(part.replace("RECOMMENDED MITIGATION]", "").strip())

            except Exception as e:
                st.error(f"❌ Error during API call: {e}")