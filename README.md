
# HealthBot: A Rule-Based Diagnostic Chatbot Using First-Order Logic (FOL)

## 1. Overview

**HealthBot** is an AI-assisted diagnostic chatbot designed to provide **preliminary medical assessments** by leveraging **First-Order Logic (FOL)** to analyze user-reported symptoms. Unlike Large Language Model (LLM)-based systems that rely on statistical inference, HealthBot adopts a **rule-based approach**, making its reasoning process **transparent, interpretable, and auditable** by medical professionals.

While not a substitute for certified diagnosis, HealthBot supports **symptom awareness** and encourages users to seek timely medical consultation—particularly valuable in **resource-limited environments**.

---

## 2. Key Features

* Uses **First-Order Logic** to infer likely diseases.
* Implements medical rules via **Python dictionaries** and **condition matching**.
* Provides **clear diagnostic paths** that experts can verify or modify.
* Offers **advice for each identified condition**.
* Designed with **accessibility and simplicity** in mind.

---

## 3. Disease Inference Rules (FOL to English)

The system uses the following logic-based rules to infer possible diseases:

1. **Flu**: If the patient has **fever**, **cough**, and **sore throat**, they might have flu.
2. **Common Cold**: If the patient has **sneezing**, **runny nose**, and **mild fever**, they might have common cold.
3. **Malaria**: If the patient has **fever**, **chills**, **sweating**, and **headache**, they might have malaria.
4. **Covid-19**: If the patient has **fever**, **cough**, **shortness of breath**, and **loss of taste**, they might have covid-19.
5. **Strep Throat**: If the patient has **sore throat**, **swollen lymph nodes**, and **fever**, they might have strep throat.

---

## 4. Advice Base

Each condition includes a simple advice message stored in the `advice_base` dictionary:

```python
advice_base = {
    "flu": "Drink fluids, rest, and consult a doctor if symptoms worsen.",
    "common_cold": "Stay warm, rest, and use over-the-counter medicine.",
    "malaria": "Seek immediate medical help and avoid mosquito bites.",
    "covid19": "Isolate yourself, wear a mask, and get tested.",
    "strep_throat": "Take antibiotics if prescribed and avoid sharing utensils."
}
```

---

## 5. Use Case

HealthBot is ideal for:

* **Educational tools** demonstrating AI in healthcare.
* **Preliminary self-assessment** before seeking medical attention.
* **Healthcare support in underserved regions** lacking immediate access to professionals.

---

## 6. References

* Topol, E. (2019). *Deep Medicine: How Artificial Intelligence Can Make Healthcare Human Again*.
* Jiang, F., Jiang, Y., Zhi, H., et al. (2021). Artificial intelligence in healthcare: past, present and future.

---


