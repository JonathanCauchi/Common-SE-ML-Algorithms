import java.util.Hashtable;
import java.util.Set;

public class hashtable1
{
    
    
    
    public static void main(String[] args)
    {
       
        
        Hashtable<String, String> hash = new Hashtable<String, String>();
        hash.put("1", "one");
        hash.put("2",  "two");
        hash.put("3",  "three");
        hash.put("4",  "four");
        
        System.out.println(hash);
        
        Set<String> keys = hash.keySet();
        for(String key: keys)
        {
            System.out.println(key + ':' + hash.get(key));
        }
        
    
    }
   
}
