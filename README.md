# Event Management System

## 📌 Project Description

The Event Management System is a Python-based project designed to manage and analyze event-related data.

The system stores information such as Event ID, Event Name, Number of Participants, Budget, Duration, Rating, and Event Status.

It uses Python libraries such as NumPy, Pandas, SciPy, Matplotlib, and Bokeh to perform data analysis, statistical calculations, and data visualization.

---

## 🎯 Objectives

- To manage event details using Python.
- To analyze the number of participants in each event.
- To calculate total and average event budgets.
- To analyze event ratings.
- To calculate cost per participant.
- To identify completed and upcoming events.
- To perform statistical analysis using SciPy.
- To find the correlation between participants and budget.
- To visualize event data using Matplotlib and Bokeh.

---

## 🛠️ Technologies Used

- Python
- NumPy
- Pandas
- SciPy
- Matplotlib
- Bokeh

---

## 📚 Python Libraries Used

### 1. NumPy
Used for numerical calculations such as:
- Total participants
- Average participants
- Maximum participants
- Minimum participants
- Total budget
- Average budget
- Average rating

### 2. Pandas
Used for:
- Creating the event DataFrame
- Displaying event details
- Filtering completed and upcoming events
- Calculating cost per participant

### 3. SciPy
Used for statistical analysis:
- One-sample T-test
- Pearson correlation

### 4. Matplotlib
Used to create:
- Event participants bar graph
- Event ratings line graph

### 5. Bokeh
Used to create an interactive graph showing participants in each event.

---

## 📊 Event Data

The system contains 8 events:

| Event ID | Event Name | Participants | Budget | Duration | Rating | Status |
|----------|------------|--------------|--------|----------|--------|--------|
| E101 | Tech Fest | 250 | ₹80,000 | 8 hrs | 4.5 | Completed |
| E102 | Cultural Fest | 400 | ₹1,00,000 | 10 hrs | 4.2 | Completed |
| E103 | Sports Day | 350 | ₹75,000 | 7 hrs | 4.0 | Completed |
| E104 | Workshop | 120 | ₹40,000 | 5 hrs | 4.6 | Completed |
| E105 | Hackathon | 200 | ₹90,000 | 12 hrs | 4.8 | Completed |
| E106 | Annual Function | 500 | ₹1,20,000 | 6 hrs | 4.3 | Upcoming |
| E107 | Music Night | 300 | ₹70,000 | 5 hrs | 4.1 | Upcoming |
| E108 | Career Fair | 275 | ₹85,000 | 8 hrs | 4.4 | Upcoming |

---

## 🔍 Main Features

### Event Details
Displays complete information about all events.

### NumPy Analysis
Calculates:
- Total events
- Total participants
- Average participants
- Maximum participants
- Minimum participants
- Total event budget
- Average event budget
- Average event rating

### Pandas Analysis
Separates events into:
- Completed Events
- Upcoming Events

### Cost Per Participant
The system calculates the cost of organizing an event for each participant.

Formula:

Cost Per Participant = Event Budget / Number of Participants

### SciPy Statistical Analysis

A one-sample T-test is performed to check whether the average event rating is significantly different from 4.

Pearson correlation is also calculated between:
- Number of Participants
- Event Budget

### Data Visualization

The project generates:

1. **Bar Graph** – Participants in each event
2. **Line Graph** – Event ratings
3. **Interactive Bokeh Graph** – Event participants

---

## 📈 Final Analysis

The system provides a final summary containing:

- Total number of events
- Number of completed events
- Number of upcoming events
- Total participants
- Total event budget
- Average event rating
- Most participated event
- Highest rated event

---
