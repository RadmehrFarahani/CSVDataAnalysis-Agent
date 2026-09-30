# 📊 CSV Data Analysis Agent

An AI-powered CSV data analysis tool built with **Python, Streamlit, LangChain, Ollama, and Pandas**.

The application allows users to upload a CSV file and ask questions about their data using natural language. A LangChain Pandas DataFrame Agent analyzes the data and generates the answer using **Llama 3.2** locally through Ollama.

## ✨ Features

* 📁 Upload CSV files
* 💬 Ask questions using natural language
* 📊 Analyze data with Pandas
* 🤖 AI-powered analysis with Llama 3.2
* 🦙 Local LLM using Ollama
* 🔗 LangChain DataFrame Agent
* 🖥️ Simple Streamlit interface

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* Ollama
* Llama 3.2
* Pandas

## 🧠 How It Works

```text
Upload CSV
    ↓
Load Data with Pandas
    ↓
Create Pandas DataFrame Agent
    ↓
User Query
    ↓
Llama 3.2 + LangChain
    ↓
Data Analysis & Response
```

The agent can interpret the user's question and perform operations on the uploaded DataFrame to generate an answer.

## 🚀 Run Locally

Install the dependencies:

```bash
pip install -r requirements.txt
```

Download the Llama 3.2 model:

```bash
ollama pull llama3.2
```

Run the application:

```bash
streamlit run app.py
```

## 💡 Example

Upload a CSV file and ask:

```text
What is the average credit score?
```

or:

```text
Show me the top 10 customers by total spending.
```

## 📚 Concepts

This project demonstrates:

* LLM-powered Data Analysis
* LangChain Agents
* Pandas DataFrame Agent
* Natural Language → Data Analysis
* Local LLMs with Ollama
* Streamlit

## 👨‍💻 Author

**Radmehr Farahani**

Backend Developer | AI & LLM Enthusiast

📧 [radmehrfarahani82@gmail.com](mailto:radmehrfarahani82@gmail.com)
