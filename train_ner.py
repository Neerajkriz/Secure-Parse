import spacy
import random
import json
from spacy.training.example import Example
from spacy.util import minibatch

# Load dataset
dataset_path = "final_improved_new.json"
with open(dataset_path, "r") as file:
    raw_data = json.load(file)

# Shuffle the dataset
random.shuffle(raw_data)

# Convert dataset to spaCy format: (text, {"entities": [...]})
formatted_data = []
for entry in raw_data:
    sentence = entry["sentence"]
    entities = entry["entities"]
    formatted_data.append((sentence, {"entities": entities}))

# Initialize a blank English model
nlp = spacy.blank("en")

# Add NER pipeline
if "ner" not in nlp.pipe_names:
    ner = nlp.add_pipe("ner", last=True)
else:
    ner = nlp.get_pipe("ner")

# Add labels to the NER component
for _, annotations in formatted_data:
    for start, end, label in annotations["entities"]:
        ner.add_label(label)

# Disable other pipelines for training
other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]

# Training
with nlp.disable_pipes(*other_pipes):
    optimizer = nlp.begin_training()
    for iteration in range(40):  # You can adjust this
        random.shuffle(formatted_data)
        losses = {}
        batches = minibatch(formatted_data, size=4)
        for batch in batches:
            examples = []
            for text, annotations in batch:
                doc = nlp.make_doc(text)
                example = Example.from_dict(doc, annotations)
                examples.append(example)
            nlp.update(examples, drop=0.3, losses=losses)
        print(f"Iteration {iteration + 1} Losses:", losses)

# Save model
nlp.to_disk("custom_pii_ner")
print("Custom PII NER model trained and saved successfully!")
