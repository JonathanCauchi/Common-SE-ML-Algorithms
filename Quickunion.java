public class Quickunion
{
    private int[] id;
    
    public Quickunion(int N)
    {
        id = new int[N];
        for(int i = 0; i < N; i++)
        {
            id[i] = i;
        }
    
    }    
    public int root(int i)
    {
        while(i!=id[i])
        {
            i = id[i];
        }
        return i;
    }   
    public boolean connected(int p, int q)
    {
        if(root(p)==root(q))
        {
            return true;
        }else
        {
            return false;
        }
        
    
    }  
    public void union(int p, int q)
    {
        int i = root(p);
        int j = root(q);
        id[i] = j;
    }
    
// worst case = O(n)


}
