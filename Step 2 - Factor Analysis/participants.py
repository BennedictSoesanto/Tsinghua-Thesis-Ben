import matplotlib.pyplot as plt
import pandas as pd

# Load the CSV file
df = pd.read_csv("final_cleaned.csv")

### Subplot 1: Age Distribution (BAC1) ###
bins = [18, 30, 40, 50, 60, 70, 80, 90]  # Age groups

# Create figure and subplots
fig, axes = plt.subplots(4, 1, figsize=(8, 15))  # 3 rows, 1 column

# Histogram for BAC1 (Age Distribution)
counts, edges, patches = axes[0].hist(df['BAC1'], bins=bins, edgecolor='black', alpha=0.7, rwidth=0.9)
axes[0].set_xlabel('Age Group')
axes[0].set_ylabel('Frequency')
axes[0].set_title('Distribution of Participant Ages')
axes[0].set_xticks(bins)
axes[0].tick_params(axis='x', labelsize=8)
axes[0].grid(axis='y', linestyle='--', alpha=0.7)

# Add frequency labels on top of bars (centered)
for count, left_edge, right_edge in zip(counts, edges[:-1], edges[1:]):
    center = (left_edge + right_edge) / 2
    axes[0].text(center, count + 1, str(int(count)), ha='center', va='bottom', fontsize=8)

### Subplot 2: Education Level Distribution (BAC4) ###
edu_translation = {
    1: "No Schooling",
    2: "Elementary School",
    3: "Middle School",
    4: "High School/Vocational",
    5: "Diploma/Bachelor’s"
}

# Translate BAC4 values to English
df['BAC4_Translated'] = df['BAC4'].map(edu_translation)

edu_order = ["No Schooling", "Elementary School", "Middle School", "High School/Vocational", "Diploma/Bachelor’s"]

# Count occurrences of each education level
edu_counts = df['BAC4_Translated'].value_counts()[edu_order]

# Bar chart for BAC4 (Education Level)
bars = axes[2].bar(edu_counts.index, edu_counts.values, color='skyblue', edgecolor='black', alpha=0.7)
axes[2].set_xlabel('Education Level')
axes[2].set_ylabel('Frequency')
axes[2].set_title('Distribution of Education Levels')
axes[2].tick_params(axis='x', labelsize=7)
axes[2].grid(axis='y', linestyle='--', alpha=0.7)

# Add frequency labels on top of bars (centered)
for bar in bars:
    axes[2].text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, 
                 str(bar.get_height()), ha='center', va='bottom', fontsize=8)

### Subplot 3: Income Distribution (BAC3) ###

# Income levels dictionary and map to the "BAC3" column
income_translation = {
    1: "< Rp2 million",
    2: "Rp2-5 million",
    3: "Rp5-10 million",
    4: "Rp10-15 million",
    5: "> Rp15 million"
}

# Translate BAC3 values to numeric using the dictionary
df['BAC3_Translated'] = df['BAC3'].map(income_translation)

# Count occurrences of each income level
income_counts = df['BAC3_Translated'].value_counts().sort_index()

# Bar chart for BAC3 (Income Level)
income_labels = ["< Rp2 million", "Rp2-5 million", "Rp5-10 million", "Rp10-15 million", "> Rp15 million"]
bars_income = axes[1].bar(income_labels, income_counts.values, color='lightgreen', edgecolor='black', alpha=0.7)
axes[1].set_xlabel('Income Level')
axes[1].set_ylabel('Frequency')
axes[1].set_title('Distribution of Estimated Monthly Income from Farming')
axes[1].tick_params(axis='x', labelsize=8)

# Add frequency labels on top of bars (centered)
for bar in bars_income:
    axes[1].text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, 
                 str(bar.get_height()), ha='center', va='bottom', fontsize=8)

axes[1].grid(axis='y', linestyle='--', alpha=0.7)

### Subplot 4: Region Distribution (BAC8) ###

# Region translation dictionary
region_translation = {
    1: 'Central Java',
    2: 'North Sumatra',
    3: 'West Java',
    4: 'Lampung'
}

# Translate BAC8 values to region names
df['BAC8_Translated'] = df['BAC8'].map(region_translation)

# Count occurrences of each region
region_counts = df['BAC8_Translated'].value_counts()

# Bar chart for BAC8 (Region Distribution)
bars_region = axes[3].bar(region_counts.index, region_counts.values, color='lightcoral', edgecolor='black', alpha=0.7)
axes[3].set_xlabel('Region')
axes[3].set_ylabel('Frequency')
axes[3].set_title('Distribution of Regions')
axes[3].tick_params(axis='x', labelsize=8)

# Add frequency labels on top of bars (centered)
for bar in bars_region:
    axes[3].text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, 
                 str(bar.get_height()), ha='center', va='bottom', fontsize=8)

axes[3].grid(axis='y', linestyle='--', alpha=0.7)

axes[0].set_ylim(0, 400)
axes[1].set_ylim(0, 500)
axes[2].set_ylim(0, 400)
axes[3].set_ylim(0, 400)

# Adjust layout and show figure
plt.subplots_adjust(hspace=0.5)
plt.savefig("figure.png", dpi=1000, bbox_inches="tight", pad_inches=0.1)
# plt.show()

percentage_ones = (df['BAC5'].sum() / len(df['BAC5'])) * 100
print(f"Percentage of 1s in BAC5: {percentage_ones:.2f}%")

percentage_bac6_1 = (df['BAC6'] == 1).mean() * 100
print(f"Percentage of BAC6 that is 1: {percentage_bac6_1:.2f}%")

df['BAC7'] = pd.to_numeric(df['BAC7'], errors='coerce')
percentage_ones = (df['BAC7'].sum() / len(df['BAC7'])) * 100
print(f"Percentage of 1s in BAC7: {percentage_ones:.2f}%")
