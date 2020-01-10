/*
 * Student ID: 2017203053
 * Name: 김 형 석
 */
#include <iostream>
#include <stack>
#include <string>
#include <algorithm>
#include <sstream>
using namespace std;

const char DECIMAL='.';

string read_and_convert_to_postfix(string& ins);
int operatorPriority(char op);
int priority(char op1,char op2);

int main(){
    string a;
    while(true) {
        cout<<"Input exp(input 'q' to terminate): ";
        cin >> a;
        if(a=="q")
            break;
        try {

            cout<<fixed;
            cout.precision(3);
            cout<<"Postfix notation : ";
            cout << read_and_convert_to_postfix(a)<<endl;
        }catch(runtime_error& e){
            cout<<e.what()<<endl;
        }
    }
    cout<<">> Terminate input."<<endl;

    return 0;
}
int operatorPriority(char op){
    switch(op){
        case '*':
        case '/':
            return 5;
        case '+':
        case '-':
            return 3;
        case '(':
        case '{':
        case '[':
            return 2;
        default:
            return 1;
    }
}

int priority(char op1,char op2){
    int op1pre=operatorPriority(op1);
    int op2pre=operatorPriority(op2);
    if (op1pre > op2pre)
        return 1;
    else if (op1pre < op2pre)
        return -1;
    else
        return 0;
}

string read_and_convert_to_postfix(string& ins){
    string post;
    string num;
    string::iterator iter;
    stack<char> operations;

    stack<int> lastbracket;
    for(iter=ins.begin();iter!=ins.end();++iter){

        if(isdigit(*iter)||*iter==DECIMAL) {
            post+=*iter;
            continue;
        }
        else {
            switch (*iter) {
                case '(':
                    operations.push('(');
                    lastbracket.push(4);
                    break;
                case ')':
                    if(lastbracket.top()!=4)
                        throw runtime_error("Error!:unbalanced parentheses");
                    while (!operations.empty()) {
                        if (operations.top() == '(') {
                            operations.pop();
                            break;
                        }
                        post += operations.top();
                        operations.pop();
                    }
                    lastbracket.pop();
                    break;
                case '*':
                case '/':
                case '+':
                case '-':
                    while (!operations.empty() && priority(operations.top(), *iter) >= 0) {
                        post += operations.top();
                        operations.pop();
                    }
                    operations.push(*iter);
                    break;
                case ' ':
                    break;
                default:
                    post+=*iter;
                    break;
            }
        }
    }
    while(!operations.empty()){
        post += operations.top();
        operations.pop();
    }
    return post;
}

