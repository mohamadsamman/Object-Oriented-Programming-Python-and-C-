#include<iostream>

using namespace std;

int main ()
{
    string s;
    cout<<"entrez une chaine de char"<<endl;
    cin>>s;
    cout << "la chaine " <<s << " contient " << s.size() <<" caracteres."<< endl;
    string ss = s+s;
    cout << ss << endl;
    return 0;
}
