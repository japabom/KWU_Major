#include "MyDoubleVector.h"

MyDoubleVector::MyDoubleVector(size_type init_capacity):capa(init_capacity),used(0){
    // precondition:
    // postcondition: initialize member variables.
    data=new double[capa];
} // constructor

MyDoubleVector::MyDoubleVector(const MyDoubleVector& v){
    // precondition: const MyDoubleVector& object
    // postcondition: deep copy
    data=new double[v.capacity()];
    capa=v.capacity();
    used=v.size();
    copy(v.data,v.data+v.size(),data);
} // copy constructor

MyDoubleVector::~MyDoubleVector(){
    // precondition:
    // postcondition: delete dynamic array.
    used=0;
    delete[] data;
} // Destructor

// Binary operator overloading

MyDoubleVector& MyDoubleVector::operator+=(const MyDoubleVector& v){
    // precondition: const MyDoubleVector& object
    // postcondition: Add RHS to LHS
    assert(size()+v.size()<=capacity());

    copy(v.data,v.data+v.size(),data+used);
    used+=v.size();
    return *this;
}

const MyDoubleVector MyDoubleVector::operator+(const MyDoubleVector& v){
    // precondition: const MyDoubleVector& which size is equal with this.
    // postcondition: plus each element.
    assert(size()==v.size());
    MyDoubleVector larger_vector(size());
    for(int i=0;i<size();i++){
        larger_vector.push_back(data[i]+v.data[i]);
    }
    return larger_vector;
}

MyDoubleVector& MyDoubleVector::operator=(const MyDoubleVector& v){
    // precondition: const MyDoubleVector& object
    // postcondition: deep copy
    if(this==&v)
        return *this;
    if(capacity() != v.capacity()){
        delete[] data;
        data=new double[v.capacity()];
        capa=v.capacity();
    }
    used=v.size();
    copy(v.data,v.data+size(),data);
    return *this;
}


const MyDoubleVector MyDoubleVector::operator-(const MyDoubleVector& v){
    // precondition: const MyDoubleVector& which size is equal with this.
    // postcondition: minus each element.
    assert(size()==v.size());
    MyDoubleVector larger_vector(size());
    for(int i=0;i<size();i++){
        larger_vector.push_back(data[i]-v.data[i]);
    }
    return larger_vector;
}

const double MyDoubleVector::operator*(const MyDoubleVector& v){
    // precondition: const MyDoubleVector& which size is equal with this.
    // postcondition: dot product
    assert(size()==v.size());
    double sum=0;
    double mul;
    for(int i=0;i<size();i++){
        mul=data[i]*v.data[i];
        sum+=mul;
    }

    return sum;
}

bool MyDoubleVector::operator==(const MyDoubleVector& v) const{
    // precondition: const MyDoubleVector& object
    // postcondition: if each object's size and all elements are equal, return true, or return false
    if(size()==v.size())
        for(int i=0;i<size();i++){
            if(data[i]!=v.data[i])
                return false;
        }
    else
        return false;
    return true;
}
// Unary operator overloading

MyDoubleVector& MyDoubleVector::operator-(){
    // precondition:
    // postcondition: transform all positive elements to negative and all negative elements to positive
    for(int i=0;i<size();i++)
        data[i]=-data[i];
    return *this;

}


MyDoubleVector& MyDoubleVector::operator()(double x) {
    // precondition: real-typed value
    // postcondition: all elements transform to x
    for(int i=0;i<size();i++){
        data[i]=x;
    }

    return *this;
}

double MyDoubleVector::operator[](size_t idx) const {
    // precondition: positive integer, index < used
    // postcondition: return value
    assert(idx<=size() && idx >= 0);
    return data[idx];
}

double& MyDoubleVector::operator[](size_t idx){
    // precondition: positive integer, index < used
    // postcondition: return value
    assert(idx<=size() && idx >= 0);
    return data[idx];
} // vector element

void MyDoubleVector::pop_back(){
    // precondition:
    // postcondition:
    if(!empty())
        --used;
    else
        return;
}

void MyDoubleVector::push_back(double x){
    // precondition: real-typed value
    // postcondition: add x to last space
    if(size()==capacity()){
        this->reserve(used+1);
    }
    data[used++]=x;
}

size_type MyDoubleVector::capacity() const{
    // precondition:
    // postcondition: return capacity
    return capa;
}

size_type MyDoubleVector::size() const{
    // precondition:
    // postcondition: return size
    return used;
}

void MyDoubleVector::reserve(size_type new_capacity){
    // precondition: size which reserve
    // postcondition: return capacity to new_capacity
    double * larger_vector;
    if(new_capacity==capacity())
        return;
    if(new_capacity < size())
        new_capacity=size();
    larger_vector = new double[new_capacity];
    copy(data, data + size(), larger_vector);
    delete[] data;
    data = larger_vector;
    capa = new_capacity;

}

bool MyDoubleVector::empty() const{
    // precondition:
    // postcondition: if list is empty, return true, or false
    if(size()==0)
        return true;
    else
        return false;
}

void MyDoubleVector::clear(){
    // precondition:
    // postcondition: delete dynamic array and initialize all data
    delete[] data;
    used=0;
    data=new double[capacity()];
}
