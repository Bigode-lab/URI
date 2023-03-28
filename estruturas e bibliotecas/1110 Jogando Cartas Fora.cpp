#include<bits/stdc++.h>
using namespace std;
int main(){
    int n, aux;
    while (cin >> n){
        if (n == 0) return 0;
        queue<int> fila, descarte;
        for (int i = 1; i <= n; i++){
            fila.push(i);
        }
        while(fila.size() > 1){

            aux= fila.front();
            fila.pop();
            descarte.push(aux);

            aux= fila.front();
            fila.pop();
            fila.push(aux);
        }
        cout << "Discarded cards: ";
        int size = descarte.size();
        for (int i = 0; i < size; i++){
            cout << descarte.front() << (i == size-1 ?'\n' : ', ');
            descarte.pop();
        }
        cout << "Remaining card: " << fila.front() << endl;
        

    }

    
    return  0;
}