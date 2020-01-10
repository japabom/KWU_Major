//
// Created by apple on 2019-09-19.
//

#ifndef DATASTRUCTURE1_MYDOUBLEVECTOR_H
#define DATASTRUCTURE1_MYDOUBLEVECTOR_H

#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <cassert>
#define size_type int
using namespace std;

class MyDoubleVector{
private:
    double * data;
    size_type capa;
    size_type used;


public:
    static const int Default_Capacity=100;
    MyDoubleVector(size_type init_capacity=Default_Capacity); // constructor

    MyDoubleVector(const MyDoubleVector& v); // copy constructor

    ~MyDoubleVector(); // Destructor

    // Binary operator overloading
    MyDoubleVector& operator+=(const MyDoubleVector& v);
    const MyDoubleVector operator+(const MyDoubleVector& v);
    MyDoubleVector& operator=(const MyDoubleVector& v);
    const MyDoubleVector operator-(const MyDoubleVector& v);
    const double operator*(const MyDoubleVector& v);
    bool operator==(const MyDoubleVector& v) const;

    // Unary operator overloading
    MyDoubleVector& operator-();
    MyDoubleVector& operator()(double x);
    double operator[](size_t idx) const;
    double& operator[](size_t idx);

    void pop_back();
    void push_back(double x);
    size_type capacity() const;
    size_type size() const;
    void reserve(size_type new_capacity);

    bool empty() const;

    void clear();

};

#endif //DATASTRUCTURE1_MYDOUBLEVECTOR_H
