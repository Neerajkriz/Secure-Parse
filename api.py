import spacy
import requests
import json
from presidio_analyzer import AnalyzerEngine
from presidio_analyzer.nlp_engine import SpacyNlpEngine
from presidio_analyzer.predefined_recognizers import SpacyRecognizer
from presidio_anonymizer import AnonymizerEngine

# Load your trained spaCy NER model
custom_nlp = spacy.load("custom_pii_ner")

# Initialize Spacy NLP Engine with the custom model
nlp_engine = SpacyNlpEngine(
    models=[{"lang_code": "en", "model_name": "custom_pii_ner"}]
)

# Load the models
nlp_engine.load()

# Initialize Presidio Analyzer with the NLP engine
analyzer = AnalyzerEngine(nlp_engine=nlp_engine)

# Register spaCy recognizer for custom NER model
custom_spacy_recognizer = SpacyRecognizer(
    supported_language="en",
    supported_entities=custom_nlp.pipe_labels["ner"]
)
analyzer.registry.add_recognizer(custom_spacy_recognizer)

# Initialize Presidio Anonymizer
anonymizer = AnonymizerEngine()

# ✅ Function to send anonymized text to Gemini API
def send_to_gemini(anonymized_text):
    GEMINI_API_KEY = "AIzaSyDiYWwgGGku8ZrUDB5u8qOuO54XI7wdtwo"  # 🔹 Replace with your actual API key

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
    
    headers = {"Content-Type": "application/json"}

    payload = {
        "contents": [{"parts": [{"text": anonymized_text}]}]
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        response_data = response.json()
        return response_data  # ✅ Return the Gemini response
    else:
        print("\n❌ Error calling Gemini API:", response.status_code, response.text)
        return None

# ✅ Function to analyze, anonymize, and restore original PII
def process_text():
    text = input("\nEnter text to analyze for PII: ")

    # ✅ Detect PII using Presidio
    results = analyzer.analyze(text=text, language="en")

    # ✅ Store PII entity mappings for de-anonymization
    pii_mapping = {}

    # ✅ Replace PII entities with placeholders and store mapping
    anonymized_text = text
    for result in results:
        pii_entity = text[result.start:result.end]
        entity_type = result.entity_type
        placeholder = f"[{entity_type}]"
        
        # Store mapping for de-anonymization
        pii_mapping[placeholder] = pii_entity
        
        # Replace original PII in the text
        anonymized_text = anonymized_text.replace(pii_entity, placeholder)

    # ✅ Print anonymized text
    print("\n🔒 Anonymized Text:")
    print(anonymized_text)

    # ✅ Send anonymized text to Gemini API
    gemini_response = send_to_gemini(anonymized_text)

    if gemini_response:
        # ✅ Extract response text from Gemini
        response_text = gemini_response.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")

        # ✅ Restore original PII in Gemini’s response
        de_anonymized_text = response_text
        for placeholder, original_pii in pii_mapping.items():
            de_anonymized_text = de_anonymized_text.replace(placeholder, original_pii)

        # ✅ Print both anonymized and de-anonymized outputs
        print("\n📌 Gemini API Response (Anonymized):")
        print(response_text)

        print("\n🔓 Gemini API Response (De-Anonymized - Original Data Restored):")
        print(de_anonymized_text)

# ✅ Run the function
if __name__ == "__main__":
    process_text()
