import random

# Original labeled dataset
lines = [
    "High fever and persistent cough\tinfection",
    "Sharp headache with sensitivity to light\tmigraine",
    "Shortness of breath during exertion\tasthma",
    "Severe chest pain during exercise\tangina",
    "Elevated blood sugar and frequent urination\tdiabetes",
    "Recurring sore throat with swollen glands\tinfection",
    "Sudden onset of intense headache\tmigraine",
    "Wheezing and coughing at night\tasthma",
    "Pain in chest radiating to left arm\tangina",
    "Persistent high glucose readings\tdiabetes",
    "Skin rash with itching\tallergy",
    "Stomach cramps and diarrhea\tinfection",
    "Blurry vision and high glucose levels\tdiabetes",
    "Chronic sneezing and watery eyes\tallergy",
    "Pressure in the chest during stress\tangina",
    "Severe throbbing headache\tmigraine",
    "Cough with yellow sputum\tinfection",
    "Difficulty breathing during sleep\tasthma",
    "Frequent urination and thirst\tdiabetes",
    "Shortness of breath while climbing stairs\tasthma",
    "Sudden loss of consciousness with chest pain\tangina",
    "Runny nose and sneezing in spring\tallergy",
    "Intense headache after bright light exposure\tmigraine",
    "Fever with sore throat\tinfection",
    "Severe chest discomfort after heavy meal\tangina",
    "Persistent cough lasting over three weeks\tinfection",
    "Wheezing triggered by cold weather\tasthma",
    "Vision problems and numbness in feet\tdiabetes",
    "Headache relieved by dark room rest\tmigraine",
    "Chest tightness during exercise\tangina",
    "Itchy skin after eating peanuts\tallergy",
    "Difficulty breathing in dusty environments\tasthma",
    "Abnormally high fasting glucose level\tdiabetes",
    "Recurring migraine attacks\tmigraine",
    "Painful urination with fever\tinfection",
    "Chest pressure spreading to the jaw\tangina",
    "Watery eyes and nasal congestion\tallergy",
    "Shortness of breath at rest\tasthma",
    "Frequent hunger and weight loss\tdiabetes"
]

# Expand to 1000 lines (random sampling with replacement)
expanded_lines = [random.choice(lines) for _ in range(10000)]

# Save to file
with open("expanded_labeled_dataset.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(expanded_lines))

print("1000-line labeled dataset saved as 'expanded_labeled_dataset.txt'")
