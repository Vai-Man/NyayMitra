import re
import streamlit as st
import requests
import PyPDF2
import io

IK_API_TOKEN = "YOUR_INDIAN_KANOON_API_KEY"
IK_API_URL = "https://api.indiankanoon.org/search/"
IK_HEADERS = {
    "Authorization": f"Token {IK_API_TOKEN}",
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
}

GPT_API_KEY = "YOUR_GPT_API_KEY"
GPT_API_URL = "https://api.openai.com/v1/models"
GPT_MODEL = "gpt-3.5-turbo"

GPT_HEADERS = {
    "Authorization": f"Bearer {GPT_API_KEY}",
    "Content-Type": "application/json"
}

# function to clean HTML tags
def clean_tags(text):
    return re.sub(r"<.*?>", "", text)

def chat(user_message, context=""):
    data = {
        "model": GPT_MODEL,
        "messages": [
            {
                "role": "system",
                "content": "You are NyayMitra, an AI legal assistant specializing in Indian law. Your responses must be **direct, professional, and informative**. \
                    - If a user asks about any legal issue, follow this approach: \
                        1️. **Cite similar cases and legal precedents** at any cost. \
                        2️. **Explain relevant laws** (e.g., Indian Penal Code, Civil Procedure Code, etc.). \
                        3️. **Outline a clear action plan**, including filing complaints, legal notices, or court procedures. \
                    - Do **not** provide legal representation or opinions—only **factual guidance**. \
                    - If a question is **unclear**, ask for clarification. \
                    - If a query is **unrelated to law**, state that you cannot assist. \
                    - If using a custom document, **answer ONLY from its content**. \
                    - Follow this **writing style**: \
                        - Avoid **buzzwords**, using **plain English** instead. \
                        - Use **legal jargon where relevant**. \
                        - Maintain a **neutral, confident, and professional** tone."
            },
            {"role": "user", "content": f"Context: {context}\n\nUser: {user_message}"}
        ],
        "max_tokens": 500,
        "temperature": 0.5
    }

    response = requests.post(GPT_API_URL, headers=GPT_HEADERS, json=data)
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].strip()
    else:
        return f"❌ Error: {response.status_code} - {response.text}"  

def extract_text(uploaded_file):
    if uploaded_file.type == "text/plain":
        return uploaded_file.read().decode("utf-8")
    elif uploaded_file.type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = "\n".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
        return text
    else:
        return None

st.title("Indian Kanoon Chatbot")
st.write("Search legal cases, discuss legal topics, or chat based on a custom document.")

option = st.sidebar.radio("Select Mode:", ["Search Cases (Indian Kanoon)", "Chat with NyayMitra", "Chat with Custom Document"])

if option == "Search Cases (Indian Kanoon)":
    st.subheader("🔍 Search Cases on Indian Kanoon")
    query = st.text_input("Enter your legal query:")

    if query:
        st.write("🔄 Searching...")
        data = {"formInput": query, "pagenum": 0}
        response = requests.post(IK_API_URL, headers=IK_HEADERS, data=data)

        if response.status_code == 200:
            try:
                data = response.json()
                if "docs" in data and data["docs"]:
                    st.write("### 🔹 Top 5 Results")
                    for result in data["docs"][:5]:  # Show top 5 results
                        title = clean_tags(result.get("title", "No Title"))
                        doc_id = result.get("id", "")
                        if doc_id:
                            url = f"https://indiankanoon.org/doc/{doc_id}/"
                            st.markdown(f"🔹 **[{title}]({url})**")
                        else:
                            st.markdown(f"🔹 **{title}**")
                else:
                    st.write("❌ No relevant results found.")
            except Exception as e:
                st.error(f"❌ Error parsing response: {str(e)}")
        else:
            st.error(f"❌ API Error {response.status_code}: {response.text}")

elif option == "Chat with NyayMitra":
    st.subheader("💬 Chat about Laws & Cases")
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input("Ask about a legal topic or discuss a case...")

    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        ai_response = chat(user_input)
        st.session_state.chat_history.append({"role": "assistant", "content": ai_response})
        with st.chat_message("assistant"):
            st.markdown(ai_response)

elif option == "Chat with Custom Document":
    st.subheader("📄 Upload a Document for Legal Q&A")
    
    uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])
    
    if uploaded_file:
        document_text = extract_text(uploaded_file)
        
        if document_text:
            st.session_state["document_context"] = document_text
            st.success("✅ Document uploaded successfully! Ask questions based on this document.")
        else:
            st.error("❌ Unable to extract text. Please upload a valid PDF or TXT file.")

    if "document_context" in st.session_state:
        user_input = st.chat_input("Ask something from your document...")

        if user_input:
            with st.chat_message("user"):
                st.markdown(user_input)

            ai_response = chat(user_input, context=st.session_state["document_context"])
            with st.chat_message("assistant"):
                st.markdown(ai_response)
