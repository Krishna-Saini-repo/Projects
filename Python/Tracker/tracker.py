import json
import os

# File to store the data
FILE = "tracker_data.json"

# Load data from file
def load_data():
    if os.path.exists(FILE):
        with open(FILE, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []  # Return empty list if file is corrupted
    return []

# Save data to file
def save_data(data):
    with open(FILE, 'w') as file:
        json.dump(data, file, indent=4)

# Add new entry
def add_entry(data):
    title = input("Enter title:\t")
    category = input("Enter category (e.g., Movie, Book, Anime):\t")
    ratings = input("Enter rating (1–10):\t")
    status = input("Enter status (Watched/Read/Complete):\t")

    try:
        ratings = int(ratings)
        if not 1 <= ratings <= 10:
            print("Rating must be between 1 and 10.")
            return
    except ValueError:
        print("Invalid rating. Must be a number.")
        return

    entry = {
        "title": title.strip(),
        "category": category.strip().capitalize(),
        "ratings": ratings,
        "status": status.strip().capitalize()
    }

    data.append(entry)
    print(f"'{title}' added successfully!")

# View all entries
def view_entries(data):
    if not data:
        print("No entries found!")
        return
    print("\nYour Entries:")
    for idx, entry in enumerate(data, 1):
        print(f"{idx}. {entry['title']} ({entry['category']}) - {entry['ratings']}/10 [{entry['status']}]")

# Search by title
def search_entries(data):
    key = input("Enter title to search:\t").lower()
    results = [entry for entry in data if key in entry['title'].lower()]
    if results:
        print("\nSearch Results:")
        for entry in results:
            print(f"{entry['title']} ({entry['category']}) - {entry['ratings']}/10 [{entry['status']}]")
    else:
        print("No match found!")

# Delete entry by title
def delete_entry(data):
    title = input("Enter the title to delete:\t").lower()
    for entry in data:
        if entry['title'].lower() == title:
            data.remove(entry)
            print(f"'{entry['title']}' removed successfully!")
            return
    print("Title not found!")

# Main program loop
def main():
    data = load_data()
    while True:
        print("\n--- Personal Tracker ---")
        print("1 -> Add entry")
        print("2 -> View all entries")
        print("3 -> Search entry")
        print("4 -> Delete an entry")
        print("5 -> Exit")

        try:
            choice = int(input("Enter choice:\t"))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 5.")
            continue

        if choice == 1:
            add_entry(data)
            save_data(data)
        elif choice == 2:
            view_entries(data)
        elif choice == 3:
            search_entries(data)
        elif choice == 4:
            delete_entry(data)
            save_data(data)
        elif choice == 5:
            save_data(data)
            print("Goodbye! Your data has been saved.")
            break
        else:
            print("Invalid choice! Please choose between 1 and 5.")


if __name__ == "__main__":
    main()
