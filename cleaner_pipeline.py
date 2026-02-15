import pandas as pd

def run_cleaning_pipeline():
    print("🔄 Pipeline Started: Cleaning raw hospital data...")
    
    # 1. Load the messy data
    df = pd.read_csv('raw_hospital_data.csv')
    
    # 2. Fix Ages: Replace missing or impossible ages with the average
    avg_age = df.loc[df['age'] <= 110, 'age'].mean()
    df['age'] = df['age'].apply(lambda x: avg_age if pd.isna(x) or x > 110 else x)
    
    # 3. Fix Weights: Remove negative values (impossible)
    df['weight_kg'] = df['weight_kg'].apply(lambda x: abs(x) if x < 0 else x)
    
    # 4. Filter Blood Types: Keep only valid ones
    valid_types = ['A', 'B', 'AB', 'O']
    df = df[df['blood_type'].isin(valid_types)]
    
    # 5. Save the 'Golden' dataset
    df.to_csv('cleaned_research_data.csv', index=False)
    print("✨ Success! Clean data saved to 'cleaned_research_data.csv'")
    print(df)

if __name__ == "__main__":
    run_cleaning_pipeline()