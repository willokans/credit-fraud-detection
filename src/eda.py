from itertools import count

from src.data_loader import load_data;


def main():
    df = load_data()

    counts = df["Class"].value_counts()
    percentages = df["Class"].value_counts(normalize=True) * 100

    print("\nClass counts:")
    print(counts)
    print("\nClass percentages:")
    print(percentages.round(4))

    print("\nAmount by class (summary stats):")
    print(df.groupby("Class")["Amount"].describe())

if __name__ == "__main__":
    main()