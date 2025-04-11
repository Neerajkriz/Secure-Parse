import json
import spacy
from spacy.training import offsets_to_biluo_tags

def find_correct_offsets(text, label_text):
    """Find the correct offset of a substring within a text."""
    start = text.find(label_text)
    if start == -1:
        return None
    end = start + len(label_text)
    return (start, end)

def align_entities(text, entity_list, nlp):
    doc = nlp.make_doc(text)
    valid_entities = []
    for start, end, label in entity_list:
        entity_text = text[start:end]
        try:
            tags = offsets_to_biluo_tags(doc, [(start, end, label)])
            if '-' not in tags:
                valid_entities.append((start, end, label))
            else:
                # Try to auto-correct the entity span
                corrected = find_correct_offsets(text, entity_text)
                if corrected:
                    new_start, new_end = corrected
                    tags = offsets_to_biluo_tags(doc, [(new_start, new_end, label)])
                    if '-' not in tags:
                        valid_entities.append((new_start, new_end, label))
        except Exception as e:
            continue
    return valid_entities

# Load spaCy model
nlp = spacy.blank("en")

# Load your dataset
with open("new.json", "r", encoding="utf-8") as f:
    data = json.load(f)

cleaned_data = []

# Validate and auto-correct entity spans
for text, annotations in data:
    entities = annotations.get("entities", [])
    valid_entities = align_entities(text, entities, nlp)
    cleaned_data.append((text, {"entities": valid_entities}))

# Save the corrected version
with open("cleaned_new_autofixed.json", "w", encoding="utf-8") as f:
    json.dump(cleaned_data, f, indent=2)

print("Auto-fix complete. Saved to 'cleaned_new_autofixed.json'.")
