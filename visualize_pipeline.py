import pandas as pd
import matplotlib.pyplot as plt
import os

def create_report():
    print("📊 Generating Data Quality Visualization...")
    
    # 1. Load both the messy and cleaned files
    if not os.path.exists('raw_hospital_data.csv') or not os.path.exists('cleaned_research_data.csv'):
        print("❌ Error: Missing CSV files. Please run dirty_data_gen.py and cleaner_pipeline.py first!")
        return

    dirty = pd.read_csv('raw_hospital_data.csv')
    clean = pd.read_csv('cleaned_research_data.csv')
    
    # 2. Prepare data for the chart
    labels = ['Raw Data (Messy)', 'Cleaned Data (Research-Ready)']
    counts = [len(dirty), len(clean)]
    
    # 3. Create the bar chart
    plt.figure(figsize=(10, 6))
    bars = plt.bar(labels, counts, color=['#e74c3c', '#2ecc71']) # Red for messy, Green for clean
    
    # Add the numbers on top of the bars
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, yval, ha='center', va='bottom', fontsize=12)

    plt.title('Automated Data Pipeline: Quality Control Report', fontsize=14)
    plt.ylabel('Number of Patient Records', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # 4. Save the chart as an image
    plt.savefig('data_quality_report.png')
    print("✅ Success! Your report has been saved as 'data_quality_report.png'")
    
    # Optional: This will try to open the image automatically
    plt.show()

if __name__ == "__main__":
    create_report()