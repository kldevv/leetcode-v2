//235. Lowest Common Ancestor of a Binary Search Tree

#include "235.h"

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    explicit TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (root == nullptr || p == nullptr || q == nullptr) {
            return root;
        }

        if (p->val > q->val) {
            return lowestCommonAncestor(root, q, p);
        }

        while (root != nullptr) {
            int rootV = root->val;
            int pV = p->val;
            int qV = q->val;

            if (rootV >= pV && rootV <= qV) {
                return root;
            } else if (rootV < pV) {
                root = root->right;
            } else if (rootV > qV) {
                root = root->left;
            }
        }

        return nullptr;
    }
};