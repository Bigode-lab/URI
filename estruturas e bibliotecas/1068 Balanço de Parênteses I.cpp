#include <bits/stdc++.h>

using namespace std;

int main()
{
    int m;

    string s ;
    while (cin >> s){
        stack<char> pilha;
        int flag = 0;
        for (int i = 0; i < s.size(); i++){
            if (s[i] == '(') pilha.push('(');
            else if (s[i] == ')'){
                if (pilha.empty()) flag = 1;
                else pilha.pop();
            }
        }

        if (pilha.empty() and flag == 0) cout <<"correct\n";
        else cout << "incorrect\n";
    }
    
    return 0;
}