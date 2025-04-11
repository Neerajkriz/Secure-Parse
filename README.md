# 🔐 SecureParse

SecureParse is a privacy-focused Natural Language Processing (NLP) tool that automatically detects, evaluates, and redacts Personally Identifiable Information (PII) from documents and datasets.

---

## 🚀 Features

- 🔍 Custom Named Entity Recognition (NER) for detecting PII entities  
- 🛡️ Secure data redaction and masking  
- 📊 Model evaluation metrics and visualization (F1 score, precision, recall)  
- 📝 Auto-generation of clean DOCX reports  
- 📦 Easy integration with existing NLP pipelines  

---

## 📁 Project Structure

```
📦 SecureParse/
├── app.py                     # Main Flask app (if any)
├── api.py                     # REST API endpoints
├── train_ner.py               # Script to train custom NER model
├── evaluate.py                # Evaluation of NER performance
├── data/                      # Raw and cleaned datasets
├── custom_pii_ner/            # Custom spaCy/Presidio models
├── templates/                 # HTML templates (if web app)
├── graph/                     # Model outputs, logs, visualizations
└── README.md                  # Project documentation
```

---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/Neerajkriz/Secure-Parse.git
cd Secure-Parse

# (Optional) Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🧠 Tech Stack

- Python 3.x  
- spaCy / Presidio  
- Flask (for API)  
- Pandas / NumPy  
- Matplotlib / Seaborn (for graphs)  
- python-docx (for DOCX generation)  

---

## 🧪 How to Use

1. **Train your custom NER model**
   ```bash
   python train_ner.py
   ```

2. **Evaluate the model**
   ```bash
   python evaluate.py
   ```

3. **Use redaction and masking**
   ```bash
   python app.py  # or use API via api.py
   ```

4. **Generate DOCX reports**
   ```bash
   python generate_doc.py
   ```

---

## 📈 Sample Visualizations

- NER Model Performance Charts  
- Precision/Recall Graphs  
- Comparison with Presidio  

---

## 📃 License

This project is licensed under the MIT License. See `LICENSE` for more information.

---

## 🙋‍♂️ Author

**Neeraj Krishna**  
[GitHub](https://github.com/Neerajkriz)

---

## 🌟 Star this repo

If you found SecureParse useful, please give it a ⭐️ on GitHub. Your support helps!
