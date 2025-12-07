import unittest
import random
from b_tree import BTree

def inorder_traversal(node):
    result = []
    if node.is_leaf:
        result.extend(node.node_values)
    else:
        for i in range(len(node.node_values)):
            result.extend(inorder_traversal(node.children[i]))
            result.append(node.node_values[i])
        result.extend(inorder_traversal(node.children[-1]))
    return result

class TestBTreeInsertDeleteMany(unittest.TestCase):
    def test_insert_and_delete_1000_times(self):
        t = 5
        for trial in range(1000):
            with self.subTest(trial=trial):
                # Generate 1000 unique random integers
                values = random.sample(range(1, 1000000), 1000)
                btree = BTree(t)
                for v in values:
                    btree.insert(v)
                expected_inserted = sorted(values)
                self.assertEqual(inorder_traversal(btree.root), expected_inserted)
                # Randomly choose 400 to delete
                to_delete = random.sample(expected_inserted, 400)
                for v in to_delete:
                    btree.delete(v)
                expected_remaining = [x for x in expected_inserted if x not in to_delete]
                self.assertEqual(inorder_traversal(btree.root), expected_remaining)

if __name__ == "__main__":
    unittest.main()
