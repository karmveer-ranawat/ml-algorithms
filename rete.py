class Fact:
    def __init__(self, **kwargs):
        self.data = kwargs

class Production:
    def __init__(self, condition, action):
        self.condition = condition
        self.action = action

    def evaluate(self, fact):
        return self.condition(fact)

# Example facts
patient1 = Fact(symptoms=["fever", "cough"])
patient2 = Fact(symptoms=["fatigue", "headache"])

# Example production rules
def influenza_rule(fact):
    return "fever" in fact["symptoms"] and "cough" in fact["symptoms"]

def migraine_rule(fact):
    return "fatigue" in fact["symptoms"] and "headache" in fact["symptoms"]

# Create production rules
production1 = Production(condition=influenza_rule, action="Diagnose Influenza")
production2 = Production(condition=migraine_rule, action="Diagnose Migraine")

# Rete network (simplified)
network = [production1, production2]

# Evaluate facts
for patient in [patient1, patient2]:
    for production in network:
        if production.evaluate(patient.data):
            print(f"Patient diagnosed: {production.action}")
