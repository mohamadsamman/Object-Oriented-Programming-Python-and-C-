#include<iostream>
#include "MySort.hpp"
#include<string>

using namespace std;

int main(void)

{

    // test de la fonction myswap avec double
    double r = 3;
    double t = 2;

    MySwap(r,t);

    cout <<"r "<< r<< " t "<<t<<endl;

    // test de la fonction myswap avec int
    int c = 5;
    int d = 6;

    MySwap(c,d);
    
    cout<< "c "<< c<< " d "<< d <<endl;

    // test de la fonction myswap avec float
    float e = 5.2;
    float f = 6.3;

    MySwap(e,f);
    
    cout<< "e "<< e<< " f "<< f <<endl;

    // test de la fonction mysort avec double
    double tab[5]={66.0,6.2,3,8.5,7};
    double* ptr=tab;
    for (unsigned int i=0;i<5;i++){
        cout<< "unsorted" <<"tab[" << i <<"] "<<tab[i]<<endl;
    }
    MySort(ptr,5);
    for (unsigned int i=0;i<5;i++){
        cout<< "sorted" <<"tab[" << i <<"] "<<tab[i]<<endl;
    }


    // test de la fonction mysort avec int
    int tab2[5]={65,62,3,85,7};
    int* ptr2=tab2;
    for (unsigned int i=0;i<5;i++){
        cout<< "unsorted" <<"tab[" << i <<"] "<<tab[i]<<endl;
    }
    MySort(ptr2,5);
    for (unsigned int i=0;i<5;i++){
        cout<< "sorted" <<"tab[" << i <<"] "<<tab[i]<<endl;
    }


    // test de la fonction mysort avec string
    string tab3[5]={"banana","Carte","tarte","table","Razoir"};
    string* ptr3=tab3;
    for (unsigned int i=0;i<5;i++){
        cout<< "unsorted" <<"tab[" << i <<"] "<<tab[i]<<endl;
    }
    MySort(ptr3,5);
    for (unsigned int i=0;i<5;i++){
        cout<< "sorted" <<"tab[" << i <<"] "<<tab[i]<<endl;
    }

    return 0;
}

