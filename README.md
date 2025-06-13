# 🤖 Agentic Workflow with LangGraph & Ollama

This project demonstrates an agentic AI workflow using [LangGraph](https://github.com/langchain-ai/langgraph) and runs on a **local language model** via [Ollama](https://ollama.com), with a **Streamlit web UI**.

---

## 🚀 Features

- 🔄 Agentic pipeline: **Plan → Tool → Reflect**
- 🧠 Uses **Gemma 2B** model locally via Ollama
- 🌐 Interactive UI using **Streamlit**
- 🐍 Built with **Python 3.11+**
- ✅ No OpenAI API needed, runs fully offline!

---

## 📁 Project Structure

```
agentic-workflow-langgraph/
├── src/
│   ├── agents/
│   ├── models/
│   ├── workflow/
│   └── main.py
├── web/
│   ├── app.py
│   ├── templates/
│   └── static/
├── requirements.txt
└── README.md
```

---

## ⚙️ How to Run

### 🔧 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/HimaShin/agentic-workflow-langgraph.git
   cd agentic-workflow-langgraph
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate    # for Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the LLM model using Ollama**
   ```bash
   ollama run gemma:2b
   ```

5. **Launch the Streamlit web app**
   ```bash
   streamlit run web/app.py
   ```

---

## 💡 Sample Task

```
Build a chatbot for booking train tickets.
```

**🧠 Final Output Example:**
> Reflected on result: Executed: - Gather input → Find trains → Book → Confirm ticket

---

## 📷 Demo Screenshot

_Add a screenshot of your Streamlit app here if available._

---

## 👨‍💻 Developer

**Himakar Pendlimarri**  
[GitHub - HimaShin](https://github.com/HimaShin)  
[LinkedIn](https://linkedin.com/in/pendlimarri-himakar-2a6177230)

---

## 📝 License

MIT License. Free to use and modify!

---

### ✅ Bonus Ideas

- 📄 Download output as PDF
- 🎙️ Add chatbot voice support
- ☁️ Deploy to Streamlit Cloud
