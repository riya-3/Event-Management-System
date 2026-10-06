import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource

# --------------------------------------------------
# ANSI COLOR CONSTANTS
# --------------------------------------------------
RESET   = "\033[0m"
BOLD    = "\033[1m"
CYAN    = "\033[96m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
BLUE    = "\033[94m"
MAGENTA = "\033[95m"
WHITE   = "\033[97m"

def print_header(title, color=CYAN):
    """Utility to print bold section headers"""
    print(f"\n{color}{BOLD}{'=' * 70}{RESET}")
    print(f"{color}{BOLD}  {title.center(66)}{RESET}")
    print(f"{color}{BOLD}{'=' * 70}{RESET}")

def print_subheader(title, color=BLUE):
    """Utility to print subheaders"""
    print(f"\n{color}{BOLD}{title}{RESET}")
    print(f"{color}{'-' * 70}{RESET}")

# Header Banner
print_header("EVENT MANAGEMENT SYSTEM", CYAN)

# --------------------------------------------------
# 1. EVENT DATA USING PANDAS
# --------------------------------------------------
event_data = {
    "Event_ID": [
        "E101", "E102", "E103", "E104", "E105",
        "E106", "E107", "E108"
    ],
    "Event_Name": [
        "Tech Fest",
        "Cultural Fest",
        "Sports Day",
        "Workshop",
        "Hackathon",
        "Annual Function",
        "Music Night",
        "Career Fair"
    ],
    "Participants": [
        250, 400, 350, 120, 200, 500, 300, 275
    ],
    "Budget": [
        80000, 100000, 75000, 40000,
        90000, 120000, 70000, 85000
    ],
    "Duration_Hours": [
        8, 10, 7, 5, 12, 6, 5, 8
    ],
    "Rating": [
        4.5, 4.2, 4.0, 4.6,
        4.8, 4.3, 4.1, 4.4
    ],
    "Status": [
        "Completed",
        "Completed",
        "Completed",
        "Completed",
        "Completed",
        "Upcoming",
        "Upcoming",
        "Upcoming"
    ]
}

events = pd.DataFrame(event_data)

print_subheader("1. EVENT DETAILS", BLUE)
print(events.to_string(index=False))

# --------------------------------------------------
# 2. NUMPY ANALYSIS
# --------------------------------------------------
participants = np.array(events["Participants"])
budget = np.array(events["Budget"])
rating = np.array(events["Rating"])

print_subheader("2. NUMPY STATISTICS", MAGENTA)

print(f"Total Events:                    {BOLD}{len(events)}{RESET}")
print(f"Total Participants:              {BOLD}{np.sum(participants)}{RESET}")
print(f"Average Participants per Event:  {BOLD}{round(np.mean(participants), 2)}{RESET}")
print(f"Maximum Participants:            {BOLD}{np.max(participants)}{RESET}")
print(f"Minimum Participants:            {BOLD}{np.min(participants)}{RESET}")
print(f"Total Event Budget:              {GREEN}{BOLD}₹ {np.sum(budget):,}{RESET}")
print(f"Average Event Budget:            {GREEN}{BOLD}₹ {round(np.mean(budget), 2):,}{RESET}")
print(f"Average Event Rating:            {YELLOW}{BOLD}{round(np.mean(rating), 2)} / 5.0{RESET}")

# --------------------------------------------------
# 3. PANDAS ANALYSIS
# --------------------------------------------------
print_subheader("3. PANDAS ANALYSIS", BLUE)

print(f"\n{BOLD}{GREEN}Completed Events:{RESET}")
print(
    events[events["Status"] == "Completed"][
        ["Event_Name", "Participants", "Rating"]
    ].to_string(index=False)
)

print(f"\n{BOLD}{YELLOW}Upcoming Events:{RESET}")
print(
    events[events["Status"] == "Upcoming"][
        ["Event_Name", "Participants", "Budget"]
    ].to_string(index=False)
)

# --------------------------------------------------
# 4. COST PER PARTICIPANT
# --------------------------------------------------
events["Cost_Per_Participant"] = events["Budget"] / events["Participants"]

print_subheader("4. COST PER PARTICIPANT", GREEN)

# Formatting output to show currency clearly
df_display = events[["Event_Name", "Participants", "Budget", "Cost_Per_Participant"]].copy()
df_display["Budget"] = df_display["Budget"].apply(lambda x: f"₹ {x:,}")
df_display["Cost_Per_Participant"] = df_display["Cost_Per_Participant"].apply(lambda x: f"₹ {x:.2f}")

print(df_display.to_string(index=False))

# --------------------------------------------------
# 5. SCIPY STATISTICAL ANALYSIS
# --------------------------------------------------
print_subheader("5. SCIPY STATISTICAL ANALYSIS (One-Sample T-Test)", MAGENTA)

# Testing whether average rating is significantly different from 4
t_statistic, p_value = stats.ttest_1samp(rating, 4)

print(f"T-Statistic: {BOLD}{round(t_statistic, 4)}{RESET}")
print(f"P-Value:     {BOLD}{round(p_value, 4)}{RESET}")

if p_value < 0.05:
    print(f"Result:      {GREEN}{BOLD}Average event rating is significantly different from 4.{RESET}")
else:
    print(f"Result:      {YELLOW}{BOLD}No significant difference from rating 4.{RESET}")

# --------------------------------------------------
# 6. SCIPY CORRELATION
# --------------------------------------------------
correlation, correlation_p = stats.pearsonr(participants, budget)

print_subheader("6. SCIPY CORRELATION ANALYSIS", MAGENTA)
print(f"Correlation (Participants vs Budget): {BOLD}{round(correlation, 4)}{RESET}")
print(f"P-Value:                            {BOLD}{round(correlation_p, 4)}{RESET}")

# --------------------------------------------------
# 7. MATPLOTLIB BAR GRAPH
# --------------------------------------------------
plt.figure(figsize=(10, 6))
bars = plt.bar(events["Event_Name"], events["Participants"], color="#3498db", edgecolor="#2980b9")

plt.title("Participants in Each Event", fontsize=14, fontweight="bold", pad=15)
plt.xlabel("Events", fontsize=11, fontweight="bold")
plt.ylabel("Number of Participants", fontsize=11, fontweight="bold")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

# --------------------------------------------------
# 8. MATPLOTLIB LINE GRAPH
# --------------------------------------------------
plt.figure(figsize=(10, 6))
plt.plot(
    events["Event_Name"],
    events["Rating"],
    marker="o",
    color="#e74c3c",
    linewidth=2,
    markersize=8
)

plt.title("Event Ratings Overview", fontsize=14, fontweight="bold", pad=15)
plt.xlabel("Events", fontsize=11, fontweight="bold")
plt.ylabel("Rating (Out of 5)", fontsize=11, fontweight="bold")
plt.xticks(rotation=45)
plt.ylim(3.5, 5.0)
plt.grid(True, linestyle="--", alpha=0.6)

plt.tight_layout()
plt.show()

# --------------------------------------------------
# 9. BOKEH INTERACTIVE GRAPH
# --------------------------------------------------
source = ColumnDataSource(events)

bokeh_plot = figure(
    x_range=events["Event_Name"].tolist(),
    title="Event Participants - Interactive Bokeh Graph",
    x_axis_label="Events",
    y_axis_label="Participants",
    width=900,
    height=500
)

bokeh_plot.vbar(
    x="Event_Name",
    top="Participants",
    width=0.6,
    source=source,
    color="#2ecc71"
)

bokeh_plot.xaxis.major_label_orientation = 0.8

show(bokeh_plot)

# --------------------------------------------------
# 10. FINAL SUMMARY
# --------------------------------------------------
completed = events[events["Status"] == "Completed"]
upcoming = events[events["Status"] == "Upcoming"]

most_participated = events.loc[events["Participants"].idxmax(), "Event_Name"]
highest_rated = events.loc[events["Rating"].idxmax(), "Event_Name"]

print_header("FINAL EVENT SUMMARY", CYAN)

print(f"Total Events:            {BOLD}{len(events)}{RESET}")
print(f"Completed Events:        {GREEN}{BOLD}{len(completed)}{RESET}")
print(f"Upcoming Events:         {YELLOW}{BOLD}{len(upcoming)}{RESET}")
print(f"Total Participants:      {BOLD}{np.sum(events['Participants'])}{RESET}")
print(f"Total Event Budget:      {GREEN}{BOLD}₹ {np.sum(events['Budget']):,}{RESET}")
print(f"Average Event Rating:    {YELLOW}{BOLD}{round(np.mean(events['Rating']), 2)}{RESET}")
print(f"Most Participated Event: {CYAN}{BOLD}{most_participated}{RESET}")
print(f"Highest Rated Event:     {MAGENTA}{BOLD}{highest_rated}{RESET}")

print(f"\n{GREEN}{BOLD}✔ Event Management System Analysis Completed Successfully!{RESET}")
print(f"{CYAN}{BOLD}{'=' * 70}{RESET}")