# Streamlit BMI Calculator Web App

A user-friendly, interactive web application built with **Python** and **Streamlit** that calculates Body Mass Index (BMI) and categorizes results using official **World Health Organization (WHO)** clinical standards.

---

## Features

* **Interactive Web Interface:** Clean UI built using Streamlit for instant visual updates.
* **Comprehensive WHO Classifications:** Categorizes scores into detailed health ranges:
  * 🔵 **Underweight:** $< 18.5$
  * 🟢 **Normal weight:** $18.5 - 24.9$
  * 🟡 **Overweight:** $25.0 - 29.9$
  * 🔴 **Obesity Class 1 (Moderate):** $30.0 - 34.9$
  * 🔴 **Obesity Class 2 (Severe):** $35.0 - 39.9$
  * 🔴 **Obesity Class 3 (Very Severe / High Risk):** $\ge 40.0$
* **Input Validation & Error Prevention:** Handled zero and missing values to prevent runtime app crashes.

---

## Tech Stack

* **Language:** Python 3.x
* **Framework:** Streamlit

---

## Repository Structure

```text
BMI_CALCULATOR/
├── app.py              # Main Streamlit application code
├── requirements.txt    # Required Python libraries
└── README.md           # Project documentation
