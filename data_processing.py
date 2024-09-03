import pandas as pd

# Load data
def load_data():
    # Example data: Replace with actual data or load from a CSV file
    data = {
        'Year': [2020, 2021, 2022, 2023],
        'Wins': [6, 10, 13, 12],
        'Losses': [10, 7, 4, 5],
        'Points For': [376, 427, 450, 460],
        'Points Against': [390, 365, 320, 330]
    }
    df = pd.DataFrame(data)
    return df

# Data processing
def process_data(df):
    df['Win Percentage'] = df['Wins'] / (df['Wins'] + df['Losses'])
    return df

if __name__ == "__main__":
    df = load_data()
    df = process_data(df)
    df.to_csv('49ers_performance.csv', index=False)
    print("Data processed and saved to '49ers_performance.csv'")
