# ============================================
# menu_demo.py
# CLI Menu for G15 E-Judiciary Hearing Module
# BST Version
# ============================================

from hearing_bst_adt import HearingBST, HearingRecord
from hearing_csv_loader import load_csv_to_bst

bst = HearingBST()
root = None

# ------------------------------
# Helper: Insert new record
# ------------------------------
def insert_record():
    global root
    print("\n=== Add New Hearing Record ===")
    case_id = input("Case ID: ")
    date = input("Date (YYYY-MM-DD): ")
    time = input("Time (HH:MM): ")
    judge = input("Judge Name: ")
    courtroom = input("Courtroom: ")
    status = input("Status: ")

    record = HearingRecord(case_id, date, time, judge, courtroom, status)
    root = bst.insert(root, case_id, record)
    print("[Success] Hearing added.\n")


# ------------------------------
# Helper: Search record
# ------------------------------
def search_record():
    print("\n=== Search Hearing Record ===")
    key = input("Enter Case ID to search: ")

    result = bst.search(root, key)
    if result:
        print("[FOUND]")
        print(result)
    else:
        print("[NOT FOUND] No hearing with Case ID", key)
    print()


# ------------------------------
# Helper: Update record
# ------------------------------
def update_record():
    print("\n=== Update Hearing ===")
    key = input("Enter Case ID to update: ")

    existing = bst.search(root, key)
    if not existing:
        print("[NOT FOUND] Cannot update.")
        return

    print("Current Record:", existing)
    print("Enter NEW values (press ENTER to keep old value):")

    date = input(f"New Date [{existing.date}]: ") or existing.date
    time = input(f"New Time [{existing.time}]: ") or existing.time
    judge = input(f"New Judge [{existing.judge}]: ") or existing.judge
    courtroom = input(f"New Courtroom [{existing.courtroom}]: ") or existing.courtroom
    status = input(f"New Status [{existing.status}]: ") or existing.status

    updated = HearingRecord(key, date, time, judge, courtroom, status)
    bst.update(root, key, updated)
    print()


# ------------------------------
# Helper: Display all hearings in sorted order
# ------------------------------
def display_all():
    print("\n=== All Hearing Records (Inorder Traversal) ===")
    if root is None:
        print("[Empty] No records loaded.")
    else:
        bst.inorder(root)
    print()


# ------------------------------
# MAIN MENU LOOP
# ------------------------------
def main_menu():
    global root

    while True:
        print("======================================")
        print(" G15 E-Judiciary Hearing BST System")
        print("======================================")
        print("1. Load hearing_cases.csv")
        print("2. Add New Hearing Record")
        print("3. Search Hearing")
        print("4. Update Hearing")
        print("5. Display All Hearings")
        print("6. Exit")
        print("======================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            root = load_csv_to_bst("hearing_cases.csv", bst)

        elif choice == "2":
            insert_record()

        elif choice == "3":
            search_record()

        elif choice == "4":
            update_record()

        elif choice == "5":
            display_all()

        elif choice == "6":
            print("Exiting system. Goodbye.")
            break

        else:
            print("Invalid choice. Try again.\n")


# Run program
if __name__ == "__main__":
    main_menu()
