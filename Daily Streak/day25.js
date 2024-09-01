// //...................do it again........
// 1038. Binary Search Tree to Greater Sum Tree
// Medium
// Topics
// Companies
// Hint
// Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

// As a reminder, a binary search tree is a tree that satisfies these constraints:

// The left subtree of a node contains only nodes with keys less than the node's key.
// The right subtree of a node contains only nodes with keys greater than the node's key.
// Both the left and right subtrees must also be binary search trees.
 

// Example 1:


// Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
// Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
// Example 2:

// Input: root = [0,null,1]
// Output: [1,null,1]
 

// Constraints:

// The number of nodes in the tree is in the range [1, 100].
// 0 <= Node.val <= 100
// All the values in the tree are unique.
 

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var bstToGst = function(root) {
    let sum = 0;

 function traverse(node) {
   if (!node) return;

   // Traverse the right subtree first
   traverse(node.right);

   // Update the sum and the node's value
   sum += node.val;
   node.val = sum;

   // Traverse the left subtree
   traverse(node.left);
 }

 traverse(root);
 return root;
}

// Helper function to insert a node into the BST
function insertIntoBST(root, val) {
 if (!root) return new TreeNode(val);
 if (val < root.val) {
   root.left = insertIntoBST(root.left, val);
 } else {
   root.right = insertIntoBST(root.right, val);
 }
 return root; 
};