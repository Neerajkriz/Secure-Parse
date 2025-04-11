import spacy
import json
from spacy.scorer import Scorer
from spacy.training.example import Example

# Load trained spaCy model
nlp = spacy.load("custom_pii_ner")

# Load test data
with open("cleaned_bank_aligned.json", "r") as file:
    test_data = json.load(file)

examples = []

# Create Examples for evaluation
for entry in test_data:
    text = entry["content"]
    entities = [(ent["start"], ent["end"], ent["label"]) for ent in entry["entity_labels"]]
    doc = nlp.make_doc(text)
    example = Example.from_dict(doc, {"entities": entities})
    examples.append(example)

# Evaluate the model
scorer = Scorer()
scores = scorer.score(examples)

# Print evaluation scores
print("\n🔍 Evaluation Results:")
for metric, value in scores["ents_p"].items() if isinstance(scores["ents_p"], dict) else scores.items():
    print(f"{metric}: {value}")

# Or print full scores dictionary
print("\n📊 Full Score Summary:")
print(json.dumps(scores, indent=2))
