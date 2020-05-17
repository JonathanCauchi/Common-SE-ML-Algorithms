
import java.util.*;

public class hashtable2
{
    public static void main(String[] args)
    {
        Hashtable hash = new Hashtable();
        hash.put("1","one");
        hash.put("2","two");    
        hash.put("3","three");
        
        Enumeration e = hash.keys();
        while(e.hasMoreElements())
        {
            String key = (String) e.nextElement();
            System.out.println(key + ":" + hash.get(key));
        }
    }
}
