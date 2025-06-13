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

4. **Run the LLM model using Ollama(Before that download Ollama)**
   ```bash
   ollama run gemma:2b
   ```

6. **Launch the Streamlit web app**
   ```bash
   streamlit run web/app.py
   ```

---

## 💡 Sample Task

```
Build a chatbot for booking train tickets.
```

**🧠 Final Output Example:**
🧠 Final Output
Reflected on result: Executed: ## Breaking down the task into smaller subtasks:

1. User Input and Validation:

Collect user input regarding:
Destination
Travel dates
Number of passengers
Preferred travel class
Any special requirements (e.g., wheelchair access)
Validate the user input to ensure valid entries and prevent invalid bookings.
2. Ticket Search and Price Calculation:

Use an API or open-source database to search for available train tickets based on user input.
Calculate the total cost of the ticket based on selected travel class and other factors.
Display the total cost to the user for confirmation.
3. Payment Gateway Integration:

Integrate with a secure payment gateway to allow users to make online payments for their tickets.
Ensure the payment process is smooth and secure for both the user and the chatbot.
4. Ticket Booking and Confirmation:

Send a confirmation email and/or push notification to the user acknowledging their booking.
Provide a dashboard for the user to track their booked tickets, including itinerary details, seat selection, and payment history.
5. Chatbot Functionality:

Develop a conversational interface that allows users to interact with the chatbot 24/7.
Respond to user queries, answer frequently asked questions, and provide assistance with booking changes or cancellations.
Be available to answer follow-up questions and provide additional information.
Additional Subtasks:

Data management: Store and manage booking data securely, including user preferences, travel history, and payment details.
Integrations: Integrate with existing systems like calendars, airlines, and payment gateways to provide a comprehensive booking experience.
Testing and Quality Assurance: Implement automated tests and manual testing to ensure the chatbot function properly and meets user expectations.

---

## 📷 Demo Screenshot

![Screenshot (120)](https://github.com/user-attachments/assets/49cde8f6-49c6-487d-9071-95e3d86b4276)
![Screenshot (121)](https://github.com/user-attachments/assets/d5c82205-0853-4984-887f-4639780acf0a)
![Screenshot (122)](https://github.com/user-attachments/assets/bed7ad83-0096-4dff-bf73-dfc39ed8fbc8)



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
