import streamlit as st
import pandas as pd
import os
from langchain_community.chat_models import ChatOllama
import requests

# Initialize LLM (Ollama)
llm = ChatOllama(model="gemma3:latest")  # or llama2, gemma, etc.

# CSV file to store tickets
csv_file = "tickets.csv"

# Create CSV if it doesn't exist
if not os.path.exists(csv_file):
    df_init = pd.DataFrame(columns=["Ticket", "Category", "Assigned Team", "Priority"])
    df_init.to_csv(csv_file, index=False)

st.title("🎫 AI Ticket Auto-Triage System with Priority & Dashboard")

# --- Input Ticket ---
ticket_text = st.text_area("Enter customer ticket:")

if st.button("Classify Ticket"):
    if ticket_text.strip() == "":
        st.warning("Please enter a ticket description first.")
    else:
        # --- Classify Category ---
        category_prompt = f"""
        You are a support ticket classifier.
        Categories: [Bug, Billing, Feature Request, Other]

        Ticket: "{ticket_text}"

        Classify the ticket into exactly one category. Respond only with the category name.
        """
        category = llm.predict(category_prompt).strip()

        # --- Assign Team ---
        team_map = {
            "Bug": "Engineering",
            "Billing": "Finance",
            "Feature Request": "Product",
            "Other": "Support"
        }
        assigned_team = team_map.get(category, "Support")

        # --- Determine Priority ---
        priority_prompt = f"""
        You are a support ticket triage assistant.
        Ticket: "{ticket_text}"

        Based on urgency, classify the ticket into one of: High, Medium, Low.
        Respond only with the priority.
        """
        priority = llm.predict(priority_prompt).strip()

        # --- Save to CSV ---
        df = pd.read_csv(csv_file)
        df = pd.concat([df, pd.DataFrame([{
            "Ticket": ticket_text,
            "Category": category,
            "Assigned Team": assigned_team,
            "Priority": priority
        }])], ignore_index=True)
        df.to_csv(csv_file, index=False)

        # --- Display Results ---
        st.success(f"📌 Category: {category}")
        st.info(f"✅ Assigned Team: {assigned_team}")
        st.warning(f"⚡ Priority: {priority}")

        # --- Send Webhook ---
        webhook_url = "http://localhost:5001/webhook"
        payload = {
            "ticket": ticket_text,
            "category": category,
            "assigned_team": assigned_team,
            "priority": priority
        }

        try:
            response = requests.post(webhook_url, json=payload)
            if response.status_code == 200:
                st.success("Webhook sent successfully!")
            else:
                st.error(f"Webhook failed with status {response.status_code}")
        except Exception as e:
            st.error(f"Error sending webhook: {e}")

# --- Dashboard ---
st.subheader("📊 Dashboard")
if st.button("Show Dashboard"):
    df = pd.read_csv(csv_file)
    st.write("Last 10 tickets:")
    st.write(df.tail(10))

    # Tickets per category
    st.write("Tickets per Category:")
    st.bar_chart(df['Category'].value_counts())

    # Tickets per priority
    st.write("Tickets per Priority:")
    st.bar_chart(df['Priority'].value_counts())
