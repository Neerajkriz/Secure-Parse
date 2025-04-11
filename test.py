from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

# Initialize Presidio Analyzer and Anonymizer
analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

# Get input text from the user
text = input("Enter text with PII to check detection and anonymization: ")

# Analyze text for PII entities
results = analyzer.analyze(text=text, entities=[], language="en")

# Print detected PII entities
if not results:
    print("\n🔹 No PII detected.")
else:
    print("\n🔹 Detected PII:")
    for result in results:
        print(f"  - {result.entity_type}: {text[result.start:result.end]} (Score: {result.score:.2f})")

    # Anonymize detected PII
    anonymized_text = anonymizer.anonymize(text=text, analyzer_results=results)
    print("\n🔹 Anonymized Text:")
    print(f"  {anonymized_text.text}")
