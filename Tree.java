public class Tree
{
    
    public static void main(String[] args)
    {
        BST tree = new BST();
        Node root = null;
        root= tree.insert(root, 5);
        root= tree.insert(root, 9);
        root= tree.insert(root, 12);
        root= tree.insert(root, 7);
        root= tree.insert(root, 16);
        root= tree.insert(root, 10);
        root= tree.insert(root, 22);
    }
}

class Node
{
    int key;
    Node left;
    Node right;
} 
  
class BST{
    
    public Node createNode(int key)
    {
        Node a = new Node();
        a.key = key;
        a.left = null;
        a.right = null;
        return a;
        
    }
    
    public Node insert(Node node, int key)
    {
        if(node == null)
        {
            return createNode(key);
        }
        else if(key > node.key)
        {
            node.right = insert(node.right,key);
        }
        else{
            node.left = insert(node.left,key);
        }
        
        return node;
    }
    
    
    
 
 

}
