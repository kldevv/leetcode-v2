// 236. Lowest Common Ancestor of a Binary Tree

#include "236.h"

 struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 };

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        TreeNode* result = nullptr;

        lowestCommonAncestor(root, p, q, result);

        return result;
    }

    bool lowestCommonAncestor(TreeNode* const root, const TreeNode* const p, const TreeNode* const q, TreeNode*& result) {
        if (root == nullptr) {
            return false;
        }

        int left = lowestCommonAncestor(root->left, p, q, result) ? 1 : 0;
        int right = lowestCommonAncestor(root->right, p, q, result) ? 1 : 0;
        int mid = (root == p) || (root == q);

        if (left + right + mid == 2) {
            result = root;
        }

        return left + right + mid == 1;
    }
};