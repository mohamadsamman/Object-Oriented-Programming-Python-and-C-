#include<iostream>
using namespace std;

int myMin(int a,int b, int c)
{
    int min = a;
    if (b<min)
    {
        min=b;
    }
    if (c<min)
    {
        min=c;
    }
    return min;
}

double myMin(double a, double b, double c)
{
    double min = a;
    if (b<min)
    {
        min=b;
    }
    if (c<min)
    {
        min=c;
    }
    return min ;
}

int myMin(int tab[3])
{
    int min = tab[0];
    if (tab[1]<min)
    {
        min=tab[1];
    }
    if (tab[2]<min)
    {
        min=tab[2];
    }
    return min ;
}

double myMin(double tab[3])
{
    double min = tab[0];
    if (tab[1]<min)
    {
        min=tab[1];
    }
    if (tab[2]<min)
    {
        min=tab[2];
    }
    return min ;
}

int main(void) 

{
    int a=myMin(1,2,3);
    cout << a << endl;
    cout << myMin(2.5,3.5,4.5) << endl;
    int t[] = {5, 6 ,7};
    cout << myMin(t) << endl;
    double tt[]={2.4,3.2,5.6};
    cout<<myMin(tt)<<endl;
    //faire une fonction en plus qui prends un tableau de double
    return 0;
}

