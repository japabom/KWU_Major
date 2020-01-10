/*
	Advanced Programming - Assignment #2 Class_Calculator_integrated

	Affiliation : Department of Computer Software
	Student ID : 2017203053
	Student Name : Hyoung Seok Kim

	Submission date : 2019.5.11
*/

#include "std_lib_facilities.h"

double pi=3.14159;
double e=2.71828;

const char let = 'L';
const char quit = 'Q';
const char print = ';';
const char number = '8';
const char name = 'a';

class Calculator{
public:
    void calculate();

private:
    struct Variable{
        string name;
        double value;
        Variable(string n, double v) :name(n), value(v){ }
    };
    vector<Variable> names;
    double get_value(string s);
    void set_value(string s, double d);
    bool is_declared(string s);
    double expression();
    double primary();
    double pri_primary();
    double term();
    double declaration();
    double statement();
    void clean_up_mess();
    struct Token{
        char kind;
        double value;
        string name;
        Token(char ch) :kind(ch), value(0) { }
        Token(char ch, double val) :kind(ch), value(val) { }
        Token(char ch, string s) :kind(ch), name(s) { }
    };
    class Token_stream{
        bool full;
        Token buffer;
    public:
        Token_stream() :full(false), buffer(0) { }

        Token get();
        void putback(Token t) { buffer=t; full=true; }

        void ignore(char);
    };
    Token_stream ts;

    const string prompt = "> ";
    const string result = "= ";

};

int main()
try{
    Calculator c;
    c.calculate();
    return 0;
}
catch (exception& e) {
    cerr << "exception: " << e.what() << endl;
    keep_window_open();
    return 1;
} catch (...) {
    cerr << "exception\n";
    keep_window_open();
    return 2;
}

void Calculator::calculate(){
    set_value("pi",pi);
    set_value("e",e);
    while(true) try {
            cout << prompt;
            Token t = ts.get();
            while (t.kind == print) t=ts.get();
            if (t.kind == quit) return;
            ts.putback(t);
            cout << result << statement() << endl;
        }
        catch(runtime_error& e) {
            cerr << e.what() << endl;
            clean_up_mess();
        }
}
Calculator::Token Calculator::Token_stream::get(){
    if (full) { full=false; return buffer; }
    char ch;
    cin >> ch;
    switch (ch) {
        case '(':
        case ')':
        case '+':
        case '-':
        case '*':
        case '/':
        case '%':
        case ';':
        case '=':
        case '^':
            return Token(ch);
        case '.':
        case '0':
        case '1':
        case '2':
        case '3':
        case '4':
        case '5':
        case '6':
        case '7':
        case '8':
        case '9':
        {
            cin.putback(ch);
            double val;
            cin >> val;
            return Token(number,val);
        }
        default:
            if (isalpha(ch)) {
                string s;
                s += ch;
                while(cin.get(ch) && (isalpha(ch) || isdigit(ch))) s += ch;
                cin.putback(ch);
                if (s == "let") return Token(let);
                if (s == "quit") return Token(quit);
                return Token(name,s);
            }
            error("Bad token");
    }
}

double Calculator::get_value(string s){
    for (int i = 0; i<names.size(); ++i)
        if (names[i].name == s) return names[i].value;
    error("get: undefined name ",s);

}
void Calculator::set_value(string s, double d){
    names.push_back(Variable(s,d));
    for (int i = 0; i<=names.size(); ++i)
        if (names[i].name == s) {
            names[i].value = d;
            return;
        }
    error("set: undefined name ",s);
}
bool Calculator::is_declared(string s){
    for (int i = 0; i<names.size(); ++i)
        if (names[i].name == s) return true;
    return false;
}
double Calculator::expression(){
    double left = term();
    while(true) {
        Token t = ts.get();
        switch(t.kind) {

            case '+':
                left += term();
                break;
            case '-':
                left -= term();
                break;
            default:
                ts.putback(t);
                return left;
        }
    }
}
double Calculator::primary(){
    Token t = ts.get();

    switch (t.kind) {
        case '(': {
            double d = expression();
            t = ts.get();
            if (t.kind != ')') error("'(' expected");
            return d;
        }
        case '-':
            return -primary();
        case '+':
            return primary();
        case number:
            return t.value;
        case name:
            if (is_declared(t.name))
                t.value = get_value(t.name);
            return t.value;
        default:
            error("primary expected");
    }

}
double Calculator::pri_primary(){
    vector<double> values;
    values.push_back(primary());

    while (true) {
        Token t = ts.get();

        switch (t.kind) {
            case '^':
                values.push_back(primary());
                break;
            default:
                ts.putback(t);
                int lastidx=values.size()-1;
                double right = values[lastidx];
                lastidx--;
                while (lastidx>=0) {
                    right = pow(values[lastidx], right);

                    lastidx--;
                }
                return right;
        }
    }
}
double Calculator::term(){
    double left = pri_primary();
    while(true) {
        Token t = ts.get();
        switch(t.kind) {
            case '*':
                left *= pri_primary();
                break;
            case '/':
            {	double d = pri_primary();
                if (d == 0) error("divide by zero");
                left /= d;
                break;
            }
            default:
                ts.putback(t);
                return left;
        }
    }
}
double Calculator::declaration(){
    Token t = ts.get();
    if (t.kind != name) error ("name expected in declaration");
    string name = t.name;
    if (is_declared(name)) error(name, " declared twice");
    Token t2 = ts.get();
    if (t2.kind != '=') error("= missing in declaration of " ,name);
    double d = expression();


    names.push_back(Variable(name,d));
    return d;
}
double Calculator::statement(){
    Token t = ts.get();
    switch(t.kind) {
        case let:
            return declaration();
        default:
            ts.putback(t);
            return expression();
    }
}
void Calculator::Token_stream::ignore(char c)
{
    if (full && c==buffer.kind) {
        full = false;
        return;
    }
    full = false;

    char ch;
    while (cin>>ch)
        if (ch==c) return;
}

void Calculator::clean_up_mess(){
    ts.ignore(print);
}

