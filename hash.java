
import java.util.HashMap;

public class hash
{

    public static void main(String[] args)
    {
        int a =10;
        int b= 15;
        int c = 20;
        
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        map.put("Jon",a);
        map.put("Jonathan",b);
        map.put("Jonny",c);
        
        System.out.println(map);
        System.out.println(map.containsKey("Jon"));
        
    }
}
