# AI Ticket Auto-Triage System with Webhook Integration

This project demonstrates an AI-powered automation system that classifies, assigns, and prioritizes customer support tickets. It also sends tickets as webhook events to a backend server for further processing.

## ✨ Features

🔍 Automatic Ticket Classification → Bug, Billing, Feature Request, Other
👥 Team Assignment → Routes tickets to Engineering, Finance, Product, or Support
⚡ Priority Detection → High, Medium, Low
📂 CSV Storage → Saves tickets for history & dashboarding
📊 Interactive Dashboard → Visualize tickets per category & priority in Streamlit
🌐 Webhook Integration → Sends ticket data to a local Flask server

## 📂 Project Structure
```bash
ticket-auto-triage/
│
├── streamlit_app.py        # Streamlit frontend (ticket triage + dashboard)
├── webhook_receiver.py     # Flask backend to receive webhook calls
├── requirements.txt        # Python dependencies
├── .gitignore              # Ignore cache and CSV
├── README.md               # Project documentation
└── tickets.csv             # Auto-generated (not committed)
---
...
## 1.Install dependencies

python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt

## 2.Start the Webhook Receiver

python webhook_receiver.py

## 3.Run the Streamlit App

streamlit run streamlit_app.py

## 4.Submit Tickets

Enter a customer ticket description.
The system will classify, assign, and prioritize automatically.
Tickets are saved into tickets.csv and sent via webhook.

## Dashboard

The dashboard displays:

✅ Last 10 tickets
📌 Tickets per Category
⚡ Tickets per Priority

## Tech Stack

Frontend: Streamlit
Backend: Flask
AI Model: LangChain + Ollama (Gemma/Llama)
Data: CSV with Pandas

## Contributing

1. Fork the repository
2. Create a new branch (feature/my-feature)
3. Commit your changes
4. Push and open a Pull Request



