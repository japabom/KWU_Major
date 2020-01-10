#ifndef __TREE_H__
#define __TREE_H__
#include "TreeNode.hpp"
class Tree {
public:
    Tree();
    Tree(int data);
    void insert(int data);
    void display();
    bool search(int data);
    void remove(int data);
    void remove(TreeNode* root_ptr,int target);
    int remove_max(TreeNode* curNode,TreeNode* parent, int removed_Item);


private:
    void display(TreeNode *curNode);
    TreeNode *rootnode;
};
#endif