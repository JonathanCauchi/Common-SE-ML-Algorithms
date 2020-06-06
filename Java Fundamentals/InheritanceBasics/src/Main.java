
public class Main {
	
	public static void main(String args[])
	{		
		Human human2 = new Human(23, "Jonathan", 180);
		human2.displayinfo();
		System.out.println(human2.getAge());
		human2.setAge(45);
		human2.displayinfo();
	}

}
