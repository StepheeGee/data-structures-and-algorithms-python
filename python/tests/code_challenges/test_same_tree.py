import pytest
from code_challenges.same_tree import Solution, TreeNode  

@pytest.fixture
def solution():
    return Solution()

def test_same_tree(solution):
    # Two empty trees should be considered the same
    assert solution.isSameTree(None, None) == True

    # One empty tree and one non-empty tree should not be considered the same
    assert solution.isSameTree(None, TreeNode(1)) == False

    # Two non-empty trees with different values should not be considered the same
    assert solution.isSameTree(TreeNode(1), TreeNode(2)) == False

    # Two non-empty trees with the same values and structure should be considered the same
    assert solution.isSameTree(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3))) == True

    # Two non-empty trees with the same values but different structure should not be considered the same
    assert solution.isSameTree(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), None)) == False

    # Two non-empty trees with the same structure but different values should not be considered the same
    assert solution.isSameTree(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(4))) == False

    # Two non-empty trees with different values and different structure should not be considered the same
    assert solution.isSameTree(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(4, TreeNode(5), TreeNode(6))) == False
