
public class Animal {
	
	char gender;
	int weight;
    
	public Animal(int weight, char c)
	{
		this.gender = c;
		this.weight = weight;
	}
	
	public void eating()
	{
		System.out.println("Eating....");
	}
	
	public void sleeping()
	{
		System.out.println("Sleeping...");
	}
	
}
