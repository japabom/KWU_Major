#ifndef TREE_BINARY_TREE_NODE_H
#define TREE_BINARY_TREE_NODE_H

#include <algorithm>
#include <iostream>
#include <iomanip>

using namespace std;

template <typename Item>
class binary_tree_node{
private:
    Item data_field;
    binary_tree_node *left_field;
    binary_tree_node *right_field;
public:
    binary_tree_node(const Item& init_data=Item(),binary_tree_node* init_left=NULL,binary_tree_node* init_right=NULL);

    Item& data();
    const Item& data() const;

    binary_tree_node*& left();
    const binary_tree_node* left() const;

    binary_tree_node*& right();
    const binary_tree_node* right() const;

    void set_data(const Item& new_data);
    void set_left(binary_tree_node* new_left);
    void set_right(binary_tree_node* new_right);

    bool is_leaf() const;

    void tree_clear(binary_tree_node<Item>*& root_ptr);
    binary_tree_node<Item>* tree_copy(binary_tree_node<Item>* root_ptr);
};

#endif //TREE_BINARY_TREE_NODE_H
