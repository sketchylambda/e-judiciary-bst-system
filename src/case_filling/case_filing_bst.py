class CaseRecord:
    def __init__(self, caseID, title, plaintiff, defendant, date):
        self.caseID = caseID   # now stored as string (e.g., C0001)
        self.title = title
        self.plaintiff = plaintiff
        self.defendant = defendant
        self.date = date

    def get_case_id(self):
        return self.caseID

    def get_details(self):
        return {
            "Case ID": self.caseID,
            "Title": self.title,
            "Plaintiff": self.plaintiff,
            "Defendant": self.defendant,
            "Date Filed": self.date
        }


class BSTNode:
    def __init__(self, caseRecord):
        self.data = caseRecord
        self.left = None
        self.right = None


class CaseIndexBST:
    def __init__(self):
        self.root = None

    # Import cases from a csv file
    def import_from_file(self, filename):
      try:
         with open(filename, "r") as file:
               lines = file.readlines()

               if not lines:
                  return False

               # Read header row
               header = lines[0].strip().split(",")

               # Convert to lowercase for flexible matching
               header = [h.strip().lower() for h in header]

               # Required fields
               required_fields = ["case_id", "case_title", "plaintiff", "defendant", "date_filed"]

               # Find column indices for required fields
               column_index = {}
               for field in required_fields:
                  if field in header:
                     column_index[field] = header.index(field)
                  else:
                     print(f"❌ Missing required column in CSV: {field}")
                     return False

               # Process data rows
               for line in lines[1:]:
                  parts = line.strip().split(",")
                  if len(parts) < len(header):
                     continue  # skip invalid row

                  # Extract required data
                  caseID = parts[column_index["case_id"]].strip()
                  title = parts[column_index["case_title"]].strip()
                  plaintiff = parts[column_index["plaintiff"]].strip()
                  defendant = parts[column_index["defendant"]].strip()
                  date = parts[column_index["date_filed"]].strip()

                  # Create Case Record
                  case = CaseRecord(caseID, title, plaintiff, defendant, date)
                  self.insert(case)

         return True

      except FileNotFoundError:
         return False

    def insert(self, caseRecord):
        self.root = self._insert(self.root, caseRecord)

    # Insert a new case
    def _insert(self, node, caseRecord):
        if node is None:
            return BSTNode(caseRecord)

        if caseRecord.caseID < node.data.caseID:
            node.left = self._insert(node.left, caseRecord)
        else:
            node.right = self._insert(node.right, caseRecord)
        return node

    def search(self, caseID):
        return self._search(self.root, caseID)

    # Search a specific case
    def _search(self, node, caseID):
        if node is None:
            return None
        if caseID == node.data.caseID:
            return node.data
        elif caseID < node.data.caseID:
            return self._search(node.left, caseID)
        else:
            return self._search(node.right, caseID)

    def delete(self, caseID):
        self.root = self._delete(self.root, caseID)

    # Delete unwanted case
    def _delete(self, node, caseID):
        if node is None:
            return None

        if caseID < node.data.caseID:
            node.left = self._delete(node.left, caseID)
        elif caseID > node.data.caseID:
            node.right = self._delete(node.right, caseID)
        else:

            if node.left is None and node.right is None:
                return None

            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            successor = self._min_value_node(node.right)
            node.data = successor.data
            node.right = self._delete(node.right, successor.data.caseID)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        records = []
        self._inorder(self.root, records)
        return records

    def _inorder(self, node, records):
        if node:
            self._inorder(node.left, records)
            records.append(node.data)
            self._inorder(node.right, records)

def validate_case_id(caseID):
    if not caseID.startswith("C"):
        return False
    if not caseID[1:].isdigit():
        return False
    return True

# Console-based main memu of the software
def main():
    bst = CaseIndexBST()

    while True:
        print("\n--- E-Judiciary Case Filing System ---")
        print("1. Import Case Database")
        print("2. File New Case")
        print("3. Search Case by ID")
        print("4. List All Cases")
        print("5. Delete Case")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            filename = input("Enter file name to import (e.g., cases.txt): ")
            success = bst.import_from_file(filename)
            if success:
                print("Case database imported successfully.")
            else:
                print("File not found. Import failed.")

        elif choice == "2":
            caseID = input("Case ID (format Cxxxx): ")

            # Validate prefix C
            if not validate_case_id(caseID):
                print("❌ Invalid Case ID! Must start with 'C' followed by digits (e.g., C0001).")
                continue

            # Check if exists
            if bst.search(caseID):
                print("❌ Case already exists in the system!")
                continue

            title = input("Case Title: ")
            plaintiff = input("Plaintiff: ")
            defendant = input("Defendant: ")
            date = input("Date Filed: ")

            case = CaseRecord(caseID, title, plaintiff, defendant, date)
            bst.insert(case)
            print("✔️ Case filed successfully!")

        elif choice == "3":
            caseID = input("Enter Case ID: ")
            result = bst.search(caseID)
            if result:
                print("\nCase Found:")
                for k, v in result.get_details().items():
                    print(f"{k}: {v}")
            else:
                print("Case Not Found!")

        elif choice == "4":
            print("\n--- All Cases (Sorted by Case ID) ---")
            for case in bst.inorder():
                print(case.get_details())

        elif choice == "5":
            caseID = input("Enter Case ID to delete: ")
            if bst.search(caseID):
                bst.delete(caseID)
                print("Case deleted successfully.")
            else:
                print("Case not found. Cannot delete.")

        elif choice == "6":
            print("Exiting system...")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
