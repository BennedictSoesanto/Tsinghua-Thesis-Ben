import pandas as pd

# Load dataset
df = pd.read_csv("final_cleaned.csv")

# Likert-scale questions (IMP1_1 includes 0 in its scale)
likert_scale = ["MAD1", "MAD3_1", "MAD3_2", "MAD3_3", "MAD3_4", "MAD3_5",
                "MAD4", "INO1_1", "INO1_2", "INO1_3", "INO1_4", "INO1_5",
                "COM2_1", "COM2_2", "COM2_3", "COM2_4", "OUT1_1", "OUT1_2",
                "OUT1_3", "ADO1", "ADO2", "ADO3", "SRI1", "SRI2", "IMP1_1",
                "IMP1_2", "IMP1_3", "ASI1_1", "ASI1_2", "ASI1_3"]

# Process Likert-scale responses
output = []
output.append("Likert Scale Analysis\n" + "="*40)

for col in likert_scale:
    if col not in df.columns:
        continue  # Skip if column is missing

    # Calculate frequency distribution (as percentages)
    freq_dist = df[col].value_counts(normalize=True) * 100
    freq_dist = freq_dist.sort_index()  # Ensure correct order (1-5 or 0-5)

    # Calculate mean and standard deviation
    mean_value = df[col].mean()
    std_dev = df[col].std()

    # Format output
    output.append(f"\nItem Code: {col}")
    output.append(f"Mean: {mean_value:.2f}, Standard Deviation: {std_dev:.2f}")
    output.append("Percentage Distribution:")
    
    # Print frequency percentages in order
    for i in range(0 if col == "IMP1_1" else 1, 6):
        output.append(f"  {i}: {freq_dist.get(i, 0):.2f}%")

# Print result to console
print("\n".join(output))

# Save to file
with open("likert_scale_analysis.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(output))

print("\nLikert scale analysis saved as 'likert_scale_analysis.txt'.")

ranking_questions = ["MAD2_1", "MAD2_2", "MAD2_3", "MAD2_4", "MAD2_5"]

# Process ranking questions separately
ranking_output = []
ranking_output.append("Ranking Question Analysis\n" + "="*40)

for col in ranking_questions:
    ranking_output.append(f"\nItem Code: {col}")
    
    # Percentage distribution
    value_counts = df[col].value_counts(normalize=True).sort_index() * 100
    distribution = ", ".join([f"Rank {int(val)}: {perc:.2f}%" for val, perc in value_counts.items()])
    
    ranking_output.append(f"Distribution: {distribution}")

# Save ranking question results to a separate text file
with open("ranking_analysis.txt", "w") as f:
    f.write("\n".join(ranking_output))

print("Ranking question analysis completed. Results saved to ranking_analysis.txt")

# Define the INO2 columns (multiple binary columns for single-choice questions)
ino2_columns = ["INO2_1", "INO2_2", "INO2_3", "INO2_4", "INO2_5"]

# Define the select-all-that-apply columns (COM1 and OUT2)
select_all_columns = {
    "COM1": ["COM1_1", "COM1_2", "COM1_3", "COM1_4", "COM1_5", "COM1_6", "COM1_7"],
    "OUT2": ["OUT2_1", "OUT2_2", "OUT2_3", "OUT2_4", "OUT2_5"]
}

# Open a file to write the results
output_file = "selection_distribution.txt"

with open(output_file, "w") as f:
    # Process INO2 (Single-choice frequency distribution)
    f.write("\n=== INO2 Single-Choice Distribution ===\n\n")
    
    # Get the index of the selected option for each respondent
    selected_ino2 = df[ino2_columns].idxmax(axis=1).apply(lambda x: x.replace('INO2_', ''))  # Get selected option as number (1, 2, 3, 4, or 5)

    # Calculate the frequency distribution of the selected options
    ino2_counts = selected_ino2.value_counts(normalize=True).mul(100).round(2)
    f.write(ino2_counts.to_string() + "\n")

    # Process COM1 and OUT2 (Select-all-that-apply)
    for category, cols in select_all_columns.items():
        f.write(f"\n=== {category} Selection Frequency ===\n\n")
        
        # Compute percentage of respondents selecting each option
        freq_percent = df[cols].mean().mul(100).round(2)

        # Count number of selections per respondent
        total_selections = df[cols].sum(axis=1)

        # Write the results to file
        results_df = pd.DataFrame({
            "Option": cols,
            "Selection %": freq_percent
        })
        
        f.write(results_df.to_string(index=False) + "\n")

        # Show distribution of how many options were selected
        f.write("\nSelections per respondent:\n")
        selection_dist = total_selections.value_counts(normalize=True).mul(100).round(2).astype(str) + '%'
        f.write(selection_dist.to_string() + "\n")
    
print(f"Results saved to {output_file}")

# Yes/No Questions
yes_no_questions = ["SRI3"]  # Add more if necessary

yes_no_output = ["Yes/No Question Analysis\n" + "="*40]

for col in yes_no_questions:
    if col in df.columns:
        yes_count = (df[col] == 1).sum()
        no_count = (df[col] == 0).sum()
        total_responses = yes_count + no_count

        yes_percentage = (yes_count / total_responses) * 100 if total_responses > 0 else 0
        no_percentage = (no_count / total_responses) * 100 if total_responses > 0 else 0

        yes_no_output.append(f"\nItem Code: {col}")
        yes_no_output.append(f"Yes: {yes_percentage:.2f}% ({yes_count} responses)")
        yes_no_output.append(f"No: {no_percentage:.2f}% ({no_count} responses)")

# Save Yes/No analysis
with open("yes_no_analysis.txt", "w") as file:
    file.write("\n".join(yes_no_output))

print("Yes/No analysis saved as 'yes_no_analysis.txt'.")

# Categorical (Single-Select) Questions
categorical_questions = ["IMP2"]  # Update if needed

categorical_output = ["Categorical Question Analysis\n" + "="*40]

for col in categorical_questions:
    if col in df.columns:
        category_counts = df[col].value_counts(normalize=True) * 100
        categorical_output.append(f"\nItem Code: {col}")
        categorical_output.append("Category Distribution:")
        
        for category, percentage in category_counts.items():
            categorical_output.append(f"  {category}: {percentage:.2f}%")

        most_selected = category_counts.idxmax()
        least_selected = category_counts.idxmin()

        categorical_output.append(f"Most Selected: {most_selected} ({category_counts[most_selected]:.2f}%)")
        categorical_output.append(f"Least Selected: {least_selected} ({category_counts[least_selected]:.2f}%)")

# Save categorical analysis
with open("categorical_analysis.txt", "w") as file:
    file.write("\n".join(categorical_output))

print("Categorical analysis saved as 'categorical_analysis.txt'.")