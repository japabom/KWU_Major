/*
	Data Structure - Assignment #2 Stack_Calculator

	Affiliation : Department of Computer Software
	Student ID : 2017203053
	Student Name : Hyoung Seok Kim

	Submission date : 2019. 10. 29
*/
#include <iostream>
#include <stack>
#include <cstring>
#include <algorithm>
#include <sstream>
using namespace std;

const char DECIMAL='.';

string read_and_convert_to_postfix(string& ins);
double read_postfix_and_evaluate(string ins);
void evaluate_stack(stack<double>& numbers,stack<char>& operations);
int operatorPriority(char op);
int priority(char op1,char op2);
int main(){
    string a;
    do {
        cin >> a;

        try {
            cout<<fixed;
            cout.precision(3);
            //cout << read_and_convert_to_postfix(a)<<endl;
            cout << read_postfix_and_evaluate(read_and_convert_to_postfix(a));
        }catch(runtime_error& e){
            cout<<e.what()<<endl;
        }
    }while(a!="EOI");


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
            post += " ";
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
                case '{':
                    operations.push('{');
                    lastbracket.push(2);
                    break;
                case '}':
                    if(lastbracket.top()!=2)
                        throw runtime_error("Error!:unbalanced curly");
                    while (!operations.empty()) {
                        if (operations.top() == '{') {
                            operations.pop();
                            break;
                        }
                        post += operations.top();
                        operations.pop();
                    }
                    lastbracket.pop();
                    break;
                case '[':
                    operations.push('[');
                    lastbracket.push(3);
                    break;
                case ']':
                    if(lastbracket.top()!=3)
                        throw runtime_error("Error!:unbalanced square bracket");
                    while (!operations.empty()) {
                        if (operations.top() == '[') {
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
                        post+=" ";
                        operations.pop();
                    }
                    operations.push(*iter);
                    break;

                case ' ':
                    break;
                default:
                    break;
            }
        }
    }
    while(!operations.empty()){
        post += " ";
        post += operations.top();
        operations.pop();
    }
    return post;
}
void evaluate_stack(stack<double>& numbers,stack<char>& operations){
    double operand1,operand2;
    operand2=numbers.top();
    numbers.pop();
    operand1=numbers.top();
    numbers.pop();

    switch(operations.top()){
        case '+':numbers.push(operand1 + operand2);break;
        case '-':numbers.push(operand1 - operand2);break;
        case '*':numbers.push(operand1 * operand2);break;
        case '/':
            if(operand2==0.0) {
                throw runtime_error("Error!:divide by zero");

            }
            else {
                numbers.push(operand1 / operand2);

            }
            break;
    }

    operations.pop();
}

double read_postfix_and_evaluate(string ins){
    stack<double> numbers;
    stack<char> operations;
    double number;
    char symbol;
    stringstream ss(ins);

    while(ss && ss.peek() !='\n'){
        if(isdigit(ss.peek())|| ss.peek()==DECIMAL) {
            ss>>number;
            numbers.push(number);
        }
        else if(strchr("+-*/",ss.peek())!=NULL){
            ss>>symbol;
            operations.push(symbol);
            evaluate_stack(numbers,operations);
        }
        else ss.ignore();
    }

    return numbers.top();
}
//{10.1+8.4*4.8}/2.2
//(19.2-8.6)/[12.4-3.1*4.0]
//(10.1*(8.4+4.8)}/2.9
//[5.3/2.5+{7.7-3.9*2.6}]*(0.8+30.9)
//{5.4/2.4+(7.9-3.2*2.4)}*([2.5+30.1]-{10.6+8.0*4.1}/2.5)
//(5+6)*(7+8)/(4+3)
//{5+6}*{7+8}/(4+3)
//((3–2)*(5/7))/(8*9*12)
//[({5+4)}]