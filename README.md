The advancement of artificial intelligence (AI) in healthcare has led to the development of various diagnostic tools designed to assist in preliminary medical assessments. One such application is HealthBot, a diagnostic chatbot that utilizes First-Order Logic (FOL) to infer possible diseases based on user-reported symptoms. By structuring medical knowledge in a logical rule-based system, HealthBot demonstrates how computational reasoning can support symptom analysis and disease hypothesis generation.

Unlike large language model (LLM)-based chatbots, which rely on statistical patterns in training data, HealthBot employs a knowledge-driven approach, where medical relationships are explicitly encoded as logical rules. This method enhances transparency, as diagnostic reasoning follows predefined pathways that can be audited and refined by medical experts. While not a replacement for professional diagnosis, tools like HealthBot can help users understand potential conditions and encourage timely medical consultation.

This report outlines the design, implementation, and testing of HealthBot, emphasizing its rule-based reasoning system, implemented using Python dictionaries and condition matching. The findings contribute to ongoing discussions on AI-assisted diagnostics, particularly in resource-limited settings where access to healthcare professionals may be constrained (Topol, 2019; Jiang et al., 2021).
##2. Knowledge Base Conversion (FOL to English)
The following FOL rules have been converted into English statements:
•	1. Flu: If the patient has symptoms of fever, cough, and sore throat, they might have flu.
•	2. Common Cold: If the patient has sneezing, runny nose, and mild fever, they might have common cold.
•	3. Malaria: If the patient has fever, chills, sweating, and headache, they might have malaria.
•	4. Covid-19: If the patient has fever, cough, shortness of breath, and loss of taste, they might have covid-19.
•	5. Strep Throat: If the patient has sore throat, swollen lymph nodes, and fever, they might have strep throat.

###3. Advice Base
The advice_base dictionary maps each disease to basic advice:

advice_base = {
    "flu": "Drink fluids, rest, and consult a doctor if symptoms worsen.",
    "common_cold": "Stay warm, rest, and use over-the-counter medicine.",
    "malaria": "Seek immediate medical help and avoid mosquito bites.",
    "covid19": "Isolate yourself, wear a mask, and get tested.",
    "strep_throat": "Take antibiotics if prescribed and avoid sharing utensils."
}
