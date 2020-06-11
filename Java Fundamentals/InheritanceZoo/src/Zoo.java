public class Zoo {
	
	public static void main(String[] args)
	{		
		Animal no1 = new Animal(12,'M');
		no1.eating();
		no1.sleeping();
		
		Bird bird = new Bird(12,'M');
		bird.eating();
		bird.fly();
		bird.sleeping();
	}

}
