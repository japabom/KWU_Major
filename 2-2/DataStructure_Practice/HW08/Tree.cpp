#include "Tree.hpp"
#include "TreeNode.hpp"
#include <iostream>
#include <stddef.h>

using namespace std;

Tree::Tree() { this->rootnode = NULL; }
Tree::Tree(int data) {
    TreeNode *node = new TreeNode(data);
    this->rootnode = node;
}
void Tree::insert(int data) {
    TreeNode *node = new TreeNode(data);
    TreeNode *cursor = this->rootnode;
    if (cursor == NULL) {
        this->rootnode = node;
        return;
    }
    while (1) {
        int value = cursor->getData();
        if (value < data) {
            if (cursor->getRight() == NULL) {
                cursor->setRight(node);
                break;
            } else {
                cursor = cursor->getRight();
            }
        } else {
            if (cursor->getLeft() == NULL) {
                cursor->setLeft(node);
                break;
            } else {
                cursor = cursor->getLeft();
            }
        }
    }
    return;
}
void Tree::display() {
    display(this->rootnode);
    return;
}
void Tree::display(TreeNode *curNode) {
    if (curNode == NULL)
        return;
    display(curNode->getLeft());
    std::cout << " ";
    std::cout << curNode->getData();
    display(curNode->getRight());
    return;
}
bool Tree::search(int data){
    static TreeNode* current=rootnode;
    if(current==NULL) {
        cout<<endl;
        cout<<data<<" search failed"<<endl;
        current=rootnode;
        return false;
    }
    if(data==current->getData()){
        cout<<data<<" ";
        cout<<endl;
        cout<<data<<" search success!"<<endl;
        current=rootnode;
        return true;
    }
    else if(data < current->getData()){
        cout<<current->getData()<<" ";
        current=current->getLeft();
        return search(data);
    }
    else{
        cout<<current->getData()<<" ";
        current=current->getRight();
        return search(data);
    }
}
void Tree::remove(int data){
    remove(rootnode,data);
}
void Tree::remove(TreeNode* root_ptr,int target){
    static TreeNode* oldroot=root_ptr;

    if(root_ptr==NULL) {
        cout<<target<<" remove failed"<<endl;
        return;
    }
    if(target < root_ptr->getData()) {
        remove(root_ptr->getLeft(), target);
    }
    else if(target > root_ptr->getData()) {
        remove(root_ptr->getRight(), target);
    }
    else {
        if(root_ptr->getLeft()==NULL){
            if(rootnode==root_ptr){
                TreeNode* temp=root_ptr;
                root_ptr=root_ptr->getRight();
                delete temp;
                rootnode=root_ptr;
            }
            else if(oldroot->getRight()==root_ptr){
                oldroot->setRight(root_ptr->getRight());
                delete root_ptr;
            }
            else if(oldroot->getLeft()==root_ptr){
                oldroot->setLeft(root_ptr->getRight());
                delete root_ptr;
            }
        }
        else{
            root_ptr->setData(remove_max(root_ptr->getLeft(),root_ptr,target));
        }
        cout<<target<<" remove success"<<endl;
        return;
    }
}

int Tree::remove_max(TreeNode* root_ptr,TreeNode* parent, int removed_Item) {
    if(root_ptr->getRight()==NULL){
        if(parent->getRight()==root_ptr) {
            removed_Item = root_ptr->getData();
            parent->setRight(root_ptr->getLeft());
            delete root_ptr;
            return removed_Item;
        }
        if(parent->getLeft()==root_ptr) {
            removed_Item = root_ptr->getData();
            parent->setLeft(root_ptr->getLeft());
            delete root_ptr;
            return removed_Item;
        } else
            return 1;

    } else {
        return remove_max(root_ptr->getRight(),root_ptr, removed_Item);
    }

}
