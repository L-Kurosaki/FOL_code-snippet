knowledge_base = {
    "flu": {"fever", "cough", "sore throat"},
    "common cold": {"sneezing", "runny nose", "mild fever"},
    "malaria": {"fever", "chills", "sweating", "headache"},
    "covid19": {"fever", "cough", "shortness of breath", "loss of taste"},
    "strep throat": {"sore throat", "swollen lymph nodes", "fever"}
}

advice_base = {
    "flu": "Drink fluids, rest, and consult a doctor if symptoms worsen.",
    "common cold": "Rest, stay warm, and drink clear fluids.",
    "malaria": "Seek immediate medical treatment; antimalarial medications are required.",
    "covid19": "Isolate yourself, wear a mask, and seek medical advice.",
    "strep throat": "Visit a doctor for antibiotics and avoid sharing utensils."
}


def get_user_symptoms():
    print(" Welcome to HealthBot! ")
    print(" Enter your symptoms (comma-separated): ")
    user_input = input("Symptoms: ").lower()
    
    # TODO: Clean and split the input
    symptoms = {sym.strip() for sym in user_input.split(',')}  # replace with actual logic
    return symptoms


def infer_disease(user_symptoms):
    possible_diseases = []

    # TODO: Loop through the knowledge base and apply FOL-style rule:
    # if all symptoms of the disease exist in the user input
    # add the disease to the list
    for disease, symptoms in knowledge_base.items():
        if symptoms.issubset(user_symptoms):
            possible_diseases.append(disease)
    return possible_diseases


def run_chatbot():
    user_symptoms = get_user_symptoms()
    diseases = infer_disease(user_symptoms)

    if diseases:
        print("\n Based on your symptoms, you might have:")
        for disease in diseases:
            print(f"- {disease.title()}")
            print(f"  Advice: {advice_base.get(disease, 'Please consult a doctor.')}")

    else:
        print("\n No matching disease found.")
        print(" Please consult a healthcare professional.")

run_chatbot()