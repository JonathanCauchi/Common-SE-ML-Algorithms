
public class Human {
	
	int age;
	String name;
	int height;
	
	public void displayinfo()
	{
		System.out.println("Name is: "+name);
		System.out.println("Age is: "+age);
		System.out.println("Height is: "+height);
	}
 
    
	public Human(int age, String name, int height) {
		super();
		this.age = age;
		this.name = name;
		this.height = height;
	}
	
	public void setAge(int age)
	{
		this.age = age;
	}
	
	public void setName(String name)
	{
		this.name = name;
	}
	
	public void setHeight(int height)
	{
		this.height = height;
	}
	
	public int getAge()
	{
		return age;
	}
	
	public int getHeight()
	{
		return height;
	}
	
	public String getName()
	{
		return name;
	}

	
}
