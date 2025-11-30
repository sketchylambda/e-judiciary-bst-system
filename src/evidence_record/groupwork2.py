class Evidence:
    def __init__(self, evidence_id, case_id, evidence_type, date_submitted, description):
        self.evidence_id = evidence_id
        self.case_id = case_id
        self.evidence_type = evidence_type
        self.date_submitted = date_submitted
        self.description = description

    def __str__(self):
        return f"EvidenceID: {self.evidence_id}, Case: {self.case_id}, Type: {self.evidence_type}, Date: {self.date_submitted}, Desc: {self.description}"

class EvidenceNode:
    def __init__(self, evidence):
        self.data = evidence
        self.left = None
        self.right = None


class EvidenceBST:
    def __init__(self):
        self.root = None

    # ADT Operation: Insert
    def insert(self, evidence):
        self.root = self._insert_recursive(self.root, evidence)

    def _insert_recursive(self, node, evidence):
        if node is None:
            return EvidenceNode(evidence)
        if evidence.evidence_id < node.data.evidence_id:
            node.left = self._insert_(node.left, evidence)
        else:
            node.right = self._insert_recursive(node.right, evidence)
        return node

    # ADT Operation: Search
    def search(self, evidence_id):
        return self._search_recursive(self.root, evidence_id)

    def _search_recursive(self, node, evidence_id):
        if node is None:
            return None
        if evidence_id == node.data.evidence_id:
            return node.data
        elif evidence_id < node.data.evidence_id:
            return self._search_recursive(node.left, evidence_id)
        else:
            return self._search_recursive(node.right, evidence_id)

    # ADT Operation: In-order traversal
    def display_inorder(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        if node:
            self._inorder_recursive(node.left)
            print(node.data)
            self._inorder_recursive(node.right)

if __name__ == "__main__":
    import pandas as pd
    import os

    #current_dir = os.getcwd()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    #print(current_dir)
    full_path = os.path.join(current_dir, "Adv_csv.csv")
    #full_path = os.path.join(os.getcwd(), "Adv_data_struct/Adv_csv.csv")
    data = pd.read_csv(full_path)
    bst = EvidenceBST()
    for index, row in data.iterrows():
        bst.insert(Evidence(row[0], row[1], row[2], row[3], row[4]))
    # Insert sample evidence items
    #bst.insert(Evidence(101, "C001", "Document", "2024-01-05", "Signed confession"))
    #bst.insert(Evidence(203, "C002", "Photo", "2024-02-10", "Crime scene photo"))
    #bst.insert(Evidence(150, "C001", "Video", "2024-03-08", "Surveillance footage"))
    #bst.insert(Evidence(99, "C003", "Audio", "2024-01-15", "Witness recorded statement"))

    print("=== In-order Evidence Listing ===")
    bst.display_inorder()

    print("\n=== Search Evidence ===")
    result = bst.search(10)
    if result:
        print("Found ->", result)
    else:
        print("Evidence not found")

