//
// Created by apple on 2019-11-07.
//
#include "binary_tree_node.h"

template <typename Item>
binary_tree_node<Item>::binary_tree_node(const Item& init_data, binary_tree_node* init_left, binary_tree_node* init_right){
    data_field=init_data;
    left_field=init_left;
    right_field=init_right;
}

template <typename Item>
Item& binary_tree_node<Item>::data(){
    return data_field;
}

template <typename Item>
const Item& binary_tree_node<Item>::data() const{
    return data_field;
}

template <typename Item>
binary_tree_node<Item>*& binary_tree_node<Item>::left(){
    return left_field;
}

template <typename Item>
const binary_tree_node<Item>* binary_tree_node<Item>::left() const{
    return left_field;
}

template <typename Item>
binary_tree_node<Item>*& binary_tree_node<Item>::right(){
    return right_field;
}

template <typename Item>
const binary_tree_node<Item>* binary_tree_node<Item>::right() const{
    return right_field;
}

template <typename Item>
void binary_tree_node<Item>::set_data(const Item& new_data){
    data_field=new_data;
}

template <typename Item>
void binary_tree_node<Item>::set_left(binary_tree_node* new_left){
    left_field=new_left;
}

template <typename Item>
void binary_tree_node<Item>::set_right(binary_tree_node* new_right){
    right_field=new_right;
}

template <typename Item>
bool binary_tree_node<Item>::is_leaf() const{
    return (left_field==NULL && right_field==NULL);
}

template <typename Item>
void binary_tree_node<Item>::tree_clear(binary_tree_node<Item>*& root_ptr){
    if(root_ptr != NULL){
        tree_clear(root_ptr->left());
        tree_clear(root_ptr->right());
        delete root_ptr;
        root_ptr=NULL;
    }
}

template <typename Item>
binary_tree_node<Item>* binary_tree_node<Item>::tree_copy(binary_tree_node<Item>* root_ptr){
    binary_tree_node<Item>* l_ptr;
    binary_tree_node<Item>* r_ptr;

    if(root_ptr==NULL)
        return NULL;
    else{
        l_ptr=tree_copy(root_ptr->left());
        r_ptr=tree_copy(root_ptr->right());
        return new binary_tree_node<Item>(root_ptr->data(),l_ptr,r_ptr);
    }
}



