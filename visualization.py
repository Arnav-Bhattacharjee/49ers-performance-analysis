import pandas as pd
import matplotlib.pyplot as plt

# Load the processed data
def load_processed_data():
    df = pd.read_csv('49ers_performance.csv')
    return df

# Generate visualizations
def visualize_data(df):
    plt.figure(figsize=(10, 6))

    # Plot win percentage over time
    plt.plot(df['Year'], df['Win Percentage'], marker='o', linestyle='-', color='r', label='Win Percentage')
    plt.title('San Francisco 49ers Win Percentage Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Win Percentage')
    plt.ylim(0, 1)
    plt.grid(True)
    plt.legend()
    plt.savefig('win_percentage.png')
    plt.show()

    # Plot points for and against over time
    plt.figure(figsize=(10, 6))
    plt.plot(df['Year'], df['Points For'], marker='o', linestyle='-', color='g', label='Points For')
    plt.plot(df['Year'], df['Points Against'], marker='o', linestyle='-', color='b', label='Points Against')
    plt.title('San Francisco 49ers Points For and Against Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Points')
    plt.grid(True)
    plt.legend()
    plt.savefig('points_comparison.png')
    plt.show()

if __name__ == "__main__":
    df = load_processed_data()
    visualize_data(df)
