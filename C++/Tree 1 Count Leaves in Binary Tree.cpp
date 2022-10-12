//User function Template for C++

/* A binary tree node has data, pointer to left child
   and a pointer to right child  
struct Node
{
    int data;
    Node* left;
    Node* right;
}; */

/* Should return count of leaves. For example, return
    value should be 2 for following tree.
         10
      /      \ 
   20       30 */
void count(Node* root, int &c)
{
    if(root == NULL)
    {
        return ;
    }
    
    count(root->left, c);
    
    if(root->left == NULL && root->right == NULL)
    {
        c++;
    }
    
    count(root->right, c);
}
int countLeaves(Node* root)
{
    int c = 0;
    count(root, c);
    return c;
}