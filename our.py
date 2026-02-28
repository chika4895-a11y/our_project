import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("📊 Sales Dashboard (2024 vs 2025)")

# Create sample monthly sales data
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

sales_2024 = np.random.randint(80, 150, 12)
sales_2025 = sales_2024 + np.random.randint(-10, 30, 12)

df = pd.DataFrame({
    "Month": months,
    "2024": sales_2024,
    "2025": sales_2025
})

# --- Bar Chart (Monthly Comparison) ---
st.subheader("📈 Monthly Sales Comparison")

fig1, ax1 = plt.subplots()
x = np.arange(len(months))

ax1.bar(x - 0.2, df["2024"], width=0.4, label="2024")
ax1.bar(x + 0.2, df["2025"], width=0.4, label="2025")

ax1.set_xticks(x)
ax1.set_xticklabels(months)
ax1.set_ylabel("Sales")
ax1.set_title("Monthly Sales (2024 vs 2025)")
ax1.legend()

st.pyplot(fig1)

# --- Growth % Chart ---
st.subheader("📊 Monthly Growth % (2025 vs 2024)")

growth = ((df["2025"] - df["2024"]) / df["2024"]) * 100

fig2, ax2 = plt.subplots()
bars = ax2.bar(months, growth)

ax2.set_ylabel("Growth %")
ax2.set_title("Monthly Growth Percentage")

st.pyplot(fig2)

# --- Quarterly Distribution ---
def get_quarterly_sales(data):
    return [
        sum(data[0:3]),   # Q1
        sum(data[3:6]),   # Q2
        sum(data[6:9]),   # Q3
        sum(data[9:12])   # Q4
    ]

q_2024 = get_quarterly_sales(df["2024"])
q_2025 = get_quarterly_sales(df["2025"])

labels = ["Q1", "Q2", "Q3", "Q4"]

# --- Pie Charts ---
st.subheader("🍩 Sales Distribution by Quarter")

col1, col2 = st.columns(2)

with col1:
    st.write("### 2024")
    fig3, ax3 = plt.subplots()
    ax3.pie(q_2024, labels=labels, autopct='%1.1f%%')
    ax3.set_title("2024 Quarterly Distribution")
    st.pyplot(fig3)

with col2:
    st.write("### 2025")
    fig4, ax4 = plt.subplots()
    ax4.pie(q_2025, labels=labels, autopct='%1.1f%%')
    ax4.set_title("2025 Quarterly Distribution")
    st.pyplot(fig4)

# --- Final Insights ---
st.subheader("📌 Final Insights")

total_2024 = sum(df["2024"])
total_2025 = sum(df["2025"])

best_year = "2024" if total_2024 > total_2025 else "2025"
best_month = df.loc[df["2025"].idxmax(), "Month"]

st.success(f"Highest Sales Year: {best_year}")
st.success(f"Best Performing Month (2025): {best_month}")
from google import genai
 
client = genai.Client(api_key="AIzaSyBcFX9BMiimytaC3cpzIOsgMbaLr1zbmh4")
 
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain MERN in simple terms"
)
 
print(response. Text)