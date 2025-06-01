#include<iostream>
#include<cmath>
using namespace std;

double moyenne(double *x,int n)
{
    double m = 0;
    for (int i=0;i<n;i++)
    {
       m = m + x[i];
    }
    m=m/n;
    return m;
}

double moment(int k ,double *x ,int n )
{
    double mk = 0;
    double m=moyenne(x,n);
    for ( int i=0; i<n ;i++)
    {
        mk+= pow((x[i] - m),k);
    }
    return mk;
}

int main()
{
    double x[] = {6,-2.1,-0.5};
    cout <<moment(2,x,3)<<endl;
    double xx[] = {1.1, 2.1, -3.1, 6.1, -1.1};
    cout<< moment (5,xx,5)<<endl;
}
