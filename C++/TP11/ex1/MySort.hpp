#include<iostream>

using namespace std;

template < typename T >

void MySwap( T &a , T &b){
    T tmp = a;
    T tmp2 = b;
    a=tmp2;
    b=tmp;
}

void MySort(T *t, int n){

    for (unsigned int i=n-1; i>0 ; i--){

    
        for (unsigned int j=0;j<i;j++)
        {
            if (t[j+1]<t[j]){
                T tmp = t[j+1];
                T tmp2 = t[j];
                t[j+1] = tmp2;
                t[j] = tmp;
            }

}}}