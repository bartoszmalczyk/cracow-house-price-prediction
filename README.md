# Cracow House Price Prediction

Welcome to the **Cracow House Price Prediction** project! This repository contains a complete, end-to-end Machine Learning pipeline designed to estimate real estate prices (apartments and houses) in Kraków, Poland - https://cracow-house-price-prediction.streamlit.app. 

The project covers everything from data collection (web scraping) and data processing, to model training, and finally serving price predictions via a Command Line Interface (CLI) and a web application.

## App Preview
Here is the usage of the web version:
![App giff](images/app_preview.gif)

## Important Disclaimer: Training Data Sources

**Please note that the machine learning model in this project was trained exclusively using *selling offers* (listings scraped from property portals like Otodom), NOT actual residential transaction data.**

### Why does this matter?
- **Expectation vs. Reality:** Asking prices in real estate listings represent the *sellers' expectations*. They do not account for the final negotiations that take place before a transaction is closed.
- **Overestimation:** On average, final transaction prices might be lower than the listed prices by a few percent depending on the market conditions.
- **Market Sentiment:** The model perfectly captures the current listed market trends, sentiment, and the premium placed on specific features (e.g., location, air conditioning, parking), but it should be treated as an estimation of the *listing price*, rather than a guaranteed *sale price*.



## Key Features

1. **Custom Web Scraper (`scraper/`)**: Automated scripts to collect thousands of real estate listings, extracting features like square footage, number of rooms, floor, district, and additional information (balcony, air conditioning, parking).
2. **Data Cleaning & Model Training (`model/`)**: A comprehensive Jupyter Notebook detailing the Exploratory Data Analysis (EDA), handling missing values, encoding categorical variables, and training machine learning models.
3. **Interactive CLI (`main.py`)**: A terminal-based program that asks the user step-by-step questions about a property and instantly returns a predicted price.
4. **Web App (`app.py`)**: A graphical interface for more user-friendly interaction with the model.


##  Project Structure

```text
cracow-house-price-prediction/
│
├── README.md                   # Project documentation
├── requirements.txt            # Python dependencies
├── main.py                     # Main runnable script for terminal predictions
├── app.py                      # Web application
├── district_cords.py           # Stores coordinates for Kraków's districts
│
├── model/                      # ML resources
│   ├── data_cleaning_and_model_training.ipynb  # ML pipeline & EDA
│   └── house_prediction_in_cracow.pkl          # Trained model (scikit-learn)
│
└── scraper/                    # Data acquisition tools
    ├── scraper.py              # Main scraping engine
    ├── otodom_parser.py        # Parser specific to Otodom HTML structure
    ├── last_page.txt           # Utility to track scraper progress
    └── otodom_scraped_data.csv # Raw dataset collected by the scraper

```

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/cracow-house-price-prediction.git
   cd cracow-house-price-prediction
   ```
2. **Create a virtual environment (optional but recommended):**
   ```bash
    python3 -m venv venv
    source venv/bin/activate
   ```
3. **Install the required dependencies:**
   ```bash
    pip install -r requirements.txt
   ```

## Usage
1. Predicting Prices via CLI
To quickly get an estimate for a property, run the main interactive script:
   ```bash
    python3 main.py
   ```
2. Using the Web App
If you prefer a graphical UI, you can launch the app locally or simply visit the site: https://cracow-house-price-prediction.streamlit.app:
    ```bash
    streamlit run app.py
    ```
   
