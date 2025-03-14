# **NyayMitra: AI-Powered Legal Assistant**  

## **Overview**  
NyayMitra is an AI-driven legal assistant designed to help users navigate Indian law. This project integrates the **Indian Kanoon API** for legal case searches and an **AI-powered chatbot** for legal discussions. Additionally, users can upload documents to receive context-aware responses based on their content.  

## **Features**  
- **Indian Kanoon Search:** Retrieve relevant case laws and legal documents.  
- **AI Chatbot:** Engage in legal discussions powered by an AI model specialized in Indian law.  
- **Custom Document Chat:** Upload legal documents (PDF/TXT) and ask questions based on their content.  

## **Technical Details**  
Initially, we explored implementing our own models using frameworks like Hugging Face. However, after evaluating performance, accuracy, and scalability, we strategically integrated APIs. This allows for:  
- **Reliable and up-to-date legal information** via Indian Kanoon.  
- **Scalable AI interactions** without the need for large-scale computational resources.  
- **Simplified deployment and accessibility** for a wider audience.  

The current implementation ensures efficiency while leaving room for future in-house model development.  

## **Installation**  
To set up the project locally:  

1. **Clone this repository:**  
   ```bash
   git clone https://github.com/Vai-Man/NyayMitra.git
   cd nyaymitra
   ```  
2. **Install dependencies:**  
   ```bash
   pip install -r requirements.txt
   ```  
3. Replace `YOUR_INDIAN_KANOON_API_KEY` and `YOUR_GPT_API_KEY` in `app.py` with your actual API keys.  

## **Usage**  
Run the application with:  
```bash
streamlit run app.py
```  

## **Disclaimer**  
NyayMitra provides AI-generated responses based on available legal information. It does not offer legal representation or definitive legal advice. Users should consult a professional lawyer for legal matters.  
