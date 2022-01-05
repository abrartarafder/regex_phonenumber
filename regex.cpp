#include <iostream> 
#include <regex> 
#include<string.h> 
using namespace std; 

   
int main() 
{ 
    //string
    string phone_number; 
   
    // regex expression for pattern to be searched 
    regex regexp("[+0-9]*(-)*[(]*[0-9]{3}[)]*(-)*[0-9]{3}(-)*[0-9]{4}"); 
   
    // matching variable (finds match within string)
     smatch m; 


    // prompt user
    cout << "ENTER A PHONE NUMBER TO SEE IF ITS VALID: ";
    cin >> phone_number;

   
    // regex_search that searches pattern regexp in the string mystr  
    if (regex_search(phone_number, m, regexp) == true){
  
    cout<< "VALID PHONE NUMBER" << endl;

    }
    else{
        cout<< "INVALID PHONE NUMBER" << endl;
    }
    return 0; 
}
