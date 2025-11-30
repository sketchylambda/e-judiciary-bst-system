# ==============================
# Hearing Record (Data Object)
# ==============================
class HearingRecord:
    def __init__(self, case_id, hearing_date, hearing_time, judge_name, courtroom, status):
        self.case_id = case_id
        self.date = hearing_date
        self.time = hearing_time
        self.judge = judge_name
        self.courtroom = courtroom
        self.status = status

    def __str__(self):
        return f"{self.case_id} | {self.date} | {self.time} | {self.judge} | {self.courtroom} | {self.status}"


# ==============================
# BST Node (ADT Internal Node)
# ==============================
class BSTNode:
    def __init__(self, key, record):
        self.key = key                # Case ID
        self.record = record          # HearingRecord object
        self.left = None
        self.right = None


# ==============================
# Hearing BST (Main ADT)
# ==============================
class HearingBST:

    # ----------------
    # INSERT
    # ----------------
    def insert(self, root, key, record):
        """Insert a new hearing record into BST."""
        if root is None:
            return BSTNode(key, record)

        # Sequential comparison:
        if key < root.key:
            if root.left is None:
                root.left = BSTNode(key, record)
            else:
                root.left = self.insert(root.left, key, record)

        elif key > root.key:
            if root.right is None:
                root.right = BSTNode(key, record)
            else:
                root.right = self.insert(root.right, key, record)

        else:
            print(f"[Duplicate] Case ID {key} already exists. Insert skipped.")

        return root

    # ----------------
    # SEARCH
    # ----------------
    def search(self, root, key):
        """Search for a specific case ID."""
        if root is None:
            return None

        if key == root.key:
            return root.record
        elif key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    # ----------------
    # UPDATE
    # ----------------
    def update(self, root, key, new_record):
        """Update an existing hearing record."""
        node = self.search_node(root, key)
        if node:
            node.record = new_record
            print(f"[Updated] Case ID {key} updated successfully.")
        else:
            print(f"[Not found] Cannot update Case ID {key}.")

    def search_node(self, root, key):
        """Helper: return node object (not only record)."""
        if root is None:
            return None
        if key == root.key:
            return root
        elif key < root.key:
            return self.search_node(root.left, key)
        else:
            return self.search_node(root.right, key)

    # ----------------
    # DISPLAY / INORDER TRAVERSAL
    # ----------------
    def inorder(self, root):
        """Traverse and print hearing records in sorted order."""
        if root:
            self.inorder(root.left)
            print(root.record)
            self.inorder(root.right)
