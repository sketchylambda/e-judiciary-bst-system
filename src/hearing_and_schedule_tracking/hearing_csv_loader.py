import csv
import os
from hearing_bst_adt import HearingRecord



def load_csv_to_bst(filename, bst):
    root = None
    print("Current working directory:", os.getcwd())
    print("Does CSV exist?", os.path.exists(filename))
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                record = HearingRecord(
                    row["case_id"],
                    row["hearing_date"],
                    row["hearing_time"],
                    row["judge_name"],
                    row["courtroom"],
                    row["status"]
                )
                root = bst.insert(root, record.case_id, record)

        print("[Success] CSV loaded into BST.")

    except:
        print("[Error] Could not read CSV file.")
        print("Details:", e)

    return root
