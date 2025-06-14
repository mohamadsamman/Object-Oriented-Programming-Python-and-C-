#include "MySort.hpp"
#include<iostream>
using namespace std;

int main(void){

  int i1 = 3;
  int i2 = 4;  
  cout << "i1 = " <<  i1 << ", i2 = " << i2 << endl;
  MySwap(i1, i2);
  cout << "Après MySwap, i1 = " <<  i1 << ", i2 = " << i2 << endl;

  double d1 = 7.3;
  double d2 = 7.4;  
  cout << "d1 = " <<  d1 << ", d2 = " << d2 << endl;
  MySwap(d1, d2);
  cout << "Après MySwap, d1 = " <<  d1 << ", d2 = " << d2 << endl;

  string s1 = "AB";
  string s2 = "DE";  
  cout << "s1 = " <<  s1 << ", s2 = " << s2 << endl;  
  MySwap(s1, s2);
  cout << "Après MySwap, s1 = " <<  s1 << ", s2 = " << s2 << endl;  

  int* tabi = new int[5] {3, 1, 7, 2, 3};
  //
  cout << "tabi avant tri " <<  endl;  
  affiche(tabi, 5);
  //
  MySort(tabi, 5);
  //
  cout << "tabi après tri " <<  endl;  
  affiche(tabi, 5);
  
  string* tabs = new string[4] {"didier", "Andre", "robert", "martine"};
  //
  cout << "tabs avant tri " <<  endl;  
  affiche(tabs, 4);
  //
  MySort(tabs, 4);
  //
  cout << "tabs après tri " <<  endl;  
  affiche(tabs, 4);

  delete [] tabi;
  delete [] tabs;  
}
