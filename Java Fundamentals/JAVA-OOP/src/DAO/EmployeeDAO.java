package DAO;

import employee.Employee;

public class EmployeeDAO {
	
	public void saveEmployee(Employee emp)
	{
		System.out.println("Saving "+emp.getName()+" into database..");
	}
	
	public void deleteEmployee(Employee emp)
	{
		System.out.println("Deleting "+emp.getName()+" from database..");
	}

}
