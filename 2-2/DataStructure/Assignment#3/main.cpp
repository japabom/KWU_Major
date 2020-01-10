/*
	Data Structure - Assignment #3 Tree

	Affiliation : Department of Computer Software
	Student ID : 2017203053
	Student Name : Hyoung Seok Kim

	Submission date : 2019. 11. 28
*/
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <cstring>
#include <queue>
#include <cmath>
#include <vector>
#include <stddef.h>

#include "binary_tree_node.h"
#include "binary_tree_node.cpp"
using namespace std;

queue<char> q;
vector<char> leaf;
vector<char> characters;
int n;
int V[4][2]={{-1,0},{1,0},{0,1},{0,-1}}; // L,R,U,D
char H_tree[100][100];

template <typename Item, typename SizeType>
void printRotated(const binary_tree_node<Item>* root_ptr, SizeType depth);

template <typename Item>
void printLevel(const binary_tree_node<Item>* root_ptr);

template <typename Item>
void insertQueueLevel(const binary_tree_node<Item>* root_ptr,int level,int depth);

template <typename Item>
int height(const binary_tree_node<Item>* root_ptr);

void init();
void printHtree(int depth);
void H(int node,int i, int j, int d, int U, int D, int R, int L);
int center(int n);
int depth(int n);

int main() {
    string command;
    char character;
    int d;
    do{
        cin>>command;
        if(command=="INS") {
            cin >> character;
            if((character>='0' && character<='9')|| character=='?' || (character>='A' && character<='Z') || (character>='a' && character<='z')) {
                characters.push_back(character);
                push_heap(characters.begin(), characters.end());
            } else{
                perror("input scope error!");
                exit(-1);
            }
        }
        else if(command=="DEL") {
            pop_heap(characters.begin(), characters.end());
            characters.pop_back();
        }

    }while(command!="EOI");

    if(characters.size()<1 || characters.size()>200) {
        perror("size error!");
        return 0;
    }

    binary_tree_node<char> treeNode[characters.size()+1];
    for(int i=1;i<=characters.size();i++){
        treeNode[i].set_data(characters[i-1]);
    }
    for(int i=2;i<=characters.size();i++){
        if(i%2==0)
            treeNode[i/2].set_left(&treeNode[i]);
        else
            treeNode[i/2].set_right(&treeNode[i]);
    }

    if(characters.size()<2)
        n=0;
    else if(characters.size()<8)
        n=1;
    else if(characters.size()<32)
        n=2;
    else if(characters.size()<128)
        n=3;
    else
        n=4;
    d=pow(n,2)+n+3;

    init();
    printRotated(&treeNode[1],0);
    cout<<endl;
    printLevel(&treeNode[1]);
    cout<<endl;
    printHtree(d);
    return 0;
}

template <typename Item, typename SizeType>
void printRotated(const binary_tree_node<Item>* root_ptr, SizeType depth){
    if(root_ptr!=NULL){
        printRotated(root_ptr->right(),depth+1);
        cout<<setw(2*depth)<<""<<root_ptr->data()<<endl;
        printRotated(root_ptr->left(),depth+1);
    }
}

template <typename Item>
void printLevel(const binary_tree_node<Item>* root_ptr) {
    int h= height(root_ptr);

    for(int i=1;i<=h;i++) {
        insertQueueLevel(root_ptr, i, 0);
    }
    int size=q.size();
    int l=1;
    int depth=1;
    int count=0;
    int width=2*size-1;
    for(int i=0;i<size;i++) {
        if(pow(2,depth)==size+1)
            cout<<" ";
        cout<<setw(width/2)<<"";
        count=0;

        for(int j=0;j<pow(2,depth-1);j++){
            if(q.empty())
                return;
            else {
                if(count%2==0 && leaf[l-1]==-1) {
                    cout << q.front() << setw(width) << "";

                }
                else if(count%2==0&&leaf[l-1]!=-1) {
                    cout << q.front() << setw(1) << "";

                }
                else if(leaf[l-1]!=-1) { // leaf
                    if(size>=32)
                        cout << q.front() << setw(2*width-1) << "";
                    else if(size>=16)
                        cout<<q.front()<<setw(2*(width))<<"";
                    else if(size>=8)
                        cout<<q.front()<<setw(2*width-1)<<"";
                    else
                        cout<<q.front()<<setw(2*width)<<"";
                }
                else {
                    if(size>=32)
                        cout << q.front() << setw(width) << "";
                    else if(size>=16)
                        cout<<q.front()<<setw(width)<<"";
                    else if(size>=8)
                        cout<<q.front()<<setw(width+1)<<"";
                    else
                        cout<<q.front()<<setw(2*width)<<"";
                }
                count += 1;

                q.pop();

                l+=1;
            }
        }
        width=width/2;
        cout<<endl;
        depth+=1;
    }
}

template <typename Item>
void insertQueueLevel(const binary_tree_node<Item>* root_ptr,int level,int depth){
    if(root_ptr!=NULL){
        if(level == 1) {
            q.push(root_ptr->data());
            if(root_ptr->is_leaf()==true)
                leaf.push_back(root_ptr->data());
            else
                leaf.push_back(-1);
        }
        else if(level > 1){
            insertQueueLevel(root_ptr->left(),level-1,depth+1);
            insertQueueLevel(root_ptr->right(),level-1,depth+1);
        }
    }
}

template <typename Item>
int height(const binary_tree_node<Item>* root_ptr){
    if (root_ptr == NULL)
        return 0;
    else{

        int lheight = height(root_ptr->left());
        int rheight = height(root_ptr->right());

        if (lheight > rheight)
            return(lheight + 1);
        else
            return(rheight + 1);
    }
}



void init(){
    for(int i=0;i<100;i++) {
        for (int j = 0; j < 100; j++)
            H_tree[i][j]=' ';
    }
}
void printHtree(int dep){

    H(1,center(characters.size()),center(characters.size()),depth(characters.size()),2,3,1,0);
    for(int i=0;i<dep;i++) {
        for (int j = 0; j < dep; j++)
            cout << H_tree[j][i];
        cout<<endl;
    }

}
void H(int node,int i, int j, int d, int U, int D, int R, int L) { // 노드=노드갯수, n=child 갯수,
    if(node>characters.size())
        return;
    H_tree[i][j]=characters[node-1];
    if(2*node<=characters.size()){
        H_tree[i + d*V[L][0]][j + d*V[L][1]] = characters[2*node-1];
        H(4*node, i + d*(V[L][0]+V[D][0]),j + d*(V[L][1]+V[D][1]), d/2, D, U, L, R);
        H(4*node+1, i + d*(V[L][0]+V[U][0]),j + d*(V[L][1]+V[U][1]), d/2, U, D, R, L);
    }
    if(2*node+1 <= characters.size()) {
        H_tree[i + d*V[R][0]][j + d*V[R][1]] = characters[2*node];
        H(4*node+2, i + d*(V[R][0]+V[U][0]),j + d*(V[R][1]+V[U][1]), d/2, U, D, R, L);
        H(4*node+3, i + d*(V[R][0]+V[D][0]),j + d*(V[R][1]+V[D][1]), d/2, D, U, L, R);
    }

}

int center(int n){
    return n<=1 ? 0 : 2*center(n/4)+1;
}
int depth(int n){
    return n<=7 ? 1 : 2*depth(n/4);
}