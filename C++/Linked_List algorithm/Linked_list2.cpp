#include <iostream>
using namespace std;

class Node{
    public:
    Node(const int& data = 0,Node* next = NULL) : data(data),next(next){ }
    int data;
    Node* next;
};
 
class list{
    Node* root;
    public : 
        list() : root(NULL){   }
        Node* begin()const{ return root;   }
        Node* end()const{ return NULL;     }
        //bool isEmpty()const{ return root==NULL; }
        bool isEmpty()const{return begin() == end(); }
        void push_back(const int& value){
            if(isEmpty()){
                root = new Node(value);
            }
            else{
                Node* temp = begin();
                while(temp->next != end()){
                    temp = temp ->next;
                    temp ->next = new Node(value);
                }
            }
        }

};

int main(){
    list L;
    cout << L.isEmpty() << endl ; 
    L.push_back(5);
    cout << L.isEmpty() << endl ;
    L.push_back(10);

return 0;}