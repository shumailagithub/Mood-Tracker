import streamlit as st  # For creating web interface
import pandas as pd     # For data manipulation
import datetime         # For handling dates
import csv              # For reading and writing CSV files
import os  # Operating system ,  For file Operations

# Define the file name for starting mood data
MOOD_FILE = "mood_log.csv" 

# Function to read name for storing mood data
def load_mood_data():
    # Check if the file exists
    if not os.path.exists(MOOD_FILE):
        # If no file, create empty DataFrame with columns
        return pd.DataFrame(columns=["Date", "Mood"])
    # Read and return existing mood data
    return pd.read_csv(MOOD_FILE)


# Function to add new mood entry to CSV file
def save_mood_data(date, mood):
    # Open file in append mode
    with open(MOOD_FILE, "a") as file:
        
        # Create CSV writer 
        writer = csv.writer(file)
        
        # Add new mood entry
        writer.writerow([date, mood])
    
# Streamlit app Title    
st.title("😀😔😡😐😇Mood Tracker")

# Get todays date
today = datetime.date.today()

# Create subheader for mood input
st.subheader("How are your feeling?  ")

# Create dropdown for mood selection
mood = st.selectbox("Select your mood", ["Happy", "Sad", "Angry", "Neutral"])

# Create button to save mood
if st.button("Log Mood"):
    
    # Save mood when the button is clicked
    save_mood_data(today, mood)
    
    # Show Success message
    st.success("Mood Logged Successfully! ")
    
# Load existing mood data  
data = load_mood_data()

# if there is data to display
if not data.empty:
    
    # Create section for Visualization
    st.subheader("Mood Trends Over Time")
    
    # Convert date string to datetime Objects
    data["Date"] = pd.to_datetime(data["Date"])
    
    #  Count Frequency of mood frequencies
    mood_counts = data.groupby("Mood").count()["Date"]
    
    # Display bar chart of mood frequencies
    st.bar_chart(mood_counts)
    
    st.write("Build with 💗 by [Shumaila Gulfam] (https://github.com/shumailagithub)")