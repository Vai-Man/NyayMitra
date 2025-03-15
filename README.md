# **NyayMitra: AI-Powered Legal Assistant**  

## AI/ML & Data Analytics Team - Group 1

## **Team Members**  
- **Vaibhav Manihar**
- **Mainik Sil**
- **Akshat Goel**

## **Project Description**  
NyayMitra is an AI-driven legal assistant designed to help users navigate Indian law efficiently. It integrates:  
- **Indian Kanoon API** for retrieving relevant case laws.  
- **AI-powered chatbot** for legal discussions, leveraging state-of-the-art language models.  
- **Custom Document Processing**, allowing users to upload legal documents and get context-aware responses.  

Initially, we explored implementing our own models using frameworks like Hugging Face and trained them on a curated legal dataset. This dataset, which was used in our previous versions, has been included in the repository for reference. However, after evaluating performance, accuracy, and scalability, we strategically transitioned to an API-based approach. This allows for:  

- **Reliable and up-to-date legal information** via Indian Kanoon.  
- **Scalable AI interactions** without the need for large-scale computational resources.  
- **Simplified deployment and accessibility** for a wider audience.  

The current implementation prioritizes efficiency while keeping room for future in-house model development.  

## **Architectural Diagram**  
![NyayMitra Architecture](https://i.imgur.com/OqVbJUD.png)  

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
3. **Replace API keys**: Open `app.py` and replace:  
   - `YOUR_INDIAN_KANOON_API_KEY`  
   - `YOUR_GPT_API_KEY`  

## **Usage**  
Run the application with:  
```bash
streamlit run app.py
```  

## **References**  
- **Indian Kanoon API:** [https://www.indiankanoon.org/](https://www.indiankanoon.org/)  
- **OpenAI API Documentation:** [https://platform.openai.com/docs/](https://platform.openai.com/docs/)  
- **Streamlit Documentation:** [https://docs.streamlit.io/](https://docs.streamlit.io/)  

## **Disclaimer**  
NyayMitra provides AI-generated responses based on available legal information. It does not offer legal representation or definitive legal advice. Users should consult a professional lawyer for legal matters.  
