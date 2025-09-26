import random

# Base sentences to use as templates
sentences = [
    "The patient presented with acute chest pain and was admitted for evaluation.",
    "Dual antiplatelet therapy was started immediately after stent placement.",
    "Follow-up echocardiogram showed normal left ventricular function.",
    "Blood pressure remained within normal limits during the hospital stay.",
    "The patient denied dizziness or fainting during exertion.",
    "Laboratory results revealed mild elevation of troponin levels.",
    "Stent implantation was performed successfully with no complications.",
    "Aspirin and clopidogrel were prescribed upon discharge.",
    "Regular monitoring of lipid profile was recommended.",
    "The patient was advised to avoid strenuous physical activity initially.",
    "Coronary angiography confirmed significant blockage in the LAD artery.",
    "Smoking cessation counseling was provided before discharge.",
    "Dietary advice focused on reducing saturated fats and cholesterol.",
    "Blood glucose levels were elevated and required further management.",
    "The patient tolerated the procedure well without adverse effects.",
    "Electrocardiogram demonstrated ST segment normalization post intervention.",
    "The patient was enrolled in a cardiac rehabilitation program.",
    "Chest X-ray was clear with no pulmonary congestion.",
    "Antihypertensive medications were adjusted to maintain stable blood pressure.",
    "The patient reported mild headache after taking aspirin.",
    "No allergic reactions were observed following medication administration.",
    "Discharge summary emphasized adherence to prescribed therapy.",
    "Regular follow-up visits were scheduled every three months.",
    "The patient experienced mild fatigue during daily activities.",
    "Ejection fraction was preserved according to echocardiographic findings.",
    "No bleeding complications were reported during hospitalization.",
    "Body mass index indicated overweight, and lifestyle modifications were advised.",
    "Serum creatinine levels remained stable post procedure.",
    "Clopidogrel resistance testing was not required in this case.",
    "The patient expressed understanding of all discharge instructions.",
    "Physical examination revealed normal heart sounds and clear lungs.",
    "The stent was deployed using a drug-eluting platform.",
    "Family history of cardiovascular disease was noted in the record.",
    "The patient was encouraged to maintain a walking routine daily.",
    "Aspirin dosage was adjusted to minimize risk of bleeding.",
    "Cholesterol-lowering therapy with statins was initiated.",
    "Patient education materials were provided in written format.",
    "The care team emphasized the importance of medication compliance.",
    "Subsequent visits will assess overall cardiovascular risk reduction."
]

# Generate 1000 lines by randomly selecting templates
output_lines = [random.choice(sentences) for _ in range(10000)]

# Save to file
with open("synthetic_medical_dataset.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(output_lines))

print("1000-line synthetic dataset saved as 'synthetic_medical_dataset.txt'")
