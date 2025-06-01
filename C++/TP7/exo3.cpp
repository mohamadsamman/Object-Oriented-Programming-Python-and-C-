#include<iostream>
#include <stdlib.h>
#include <time.h> 

using namespace std;

double* create_array(int n)
{
    double d[n];
    return d;
}

double get_kbd_number()
{
    double k;
    cout<<"entrez une val reelle"<< endl;
    cin >> k;
    return k;
}

double get_rand_number()
{
    srand (time(NULL));
    double num = rand() % 10000000+1 ;
    double v;
    v = num/10000000.0;
    return v;
}

void init_array_kbd(double* t,int n)
{
    for (int i=0 ; i<n; i++)
    {
        t[i]=get_kbd_number();
    }
}

void affiche(double* t, int n)
{
    for (int i=0 ; i<n; i++)
    {
        cout<< t[i] << endl;
    }
}

void init_array_rand(double *t,int n)
{
    for (int i=0 ; i<n; i++)
    {
        t[i]=get_rand_number();
    }
}

void apply(double* t[],int n,double(*f(void)))
{
    for (int i=0;i<n;i++)
    {
        t[i]=f();
    }
}

int main()

{
    double* tablrau= create_array(5);
    cout<<get_kbd_number() <<endl;
    cout<<get_rand_number()<<endl;
    int n = 6;
    double* tab = create_array(n);
    init_array_kbd(tab,n);
    affiche(tab,n);
    double * tt = create_array(n);
    init_array_rand(tt,n);
    affiche(tt,n);
    return 0;
}
