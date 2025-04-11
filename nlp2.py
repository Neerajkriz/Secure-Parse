import spacy

# Load your trained NER model
nlp = spacy.load("custom_pii_ner")  # Adjust path if needed

# Test case covering most PII types
test_text = """
John Doe applied for a loan with ID LN-98765-2026 using his credit card 1111-2222-3333-4444.
His SSN is 987-65-4321, and his email is johndoe@email.com.
John's bank account number is 112233445566, and the routing number is 021000021.
He provided his IBAN GB33BUKB20201555555555 for an international transaction.
His mortgage ID is MRTG-33456-2026, and his IFSC code is HDFC0001234.
John's phone number is (555) 123-4567, and his SWIFT code is BOFAUS3NXXX.
"""

# Process the text with the trained model
doc = nlp(test_text)

# Print detected entities
print("Entities detected:")
for ent in doc.ents:
    print(f" - Text: {ent.text}, Label: {ent.label_}")
