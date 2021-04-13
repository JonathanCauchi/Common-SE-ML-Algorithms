package client;

import DAO.EmployeeDAO;
import employee.Employee;
import formatting.EmployeeReportFormatter;
import formatting.FormatType;

public class ClientModule {
	
	public static void main(String[] args)
	{	
		Employee Susan = new Employee(1,"Susan","IT",true);
		EmployeeDAO EmpDAO = new EmployeeDAO();	
		hireNewEmployee(Susan, EmpDAO);
		printEmployeeReport(Susan);
		terminateEmployee(Susan, EmpDAO);
	}
	
	public static void hireNewEmployee(Employee emp, EmployeeDAO EmpDAO)
	{
		EmpDAO.saveEmployee(emp);
	}
	
	public static void terminateEmployee(Employee emp, EmployeeDAO EmpDAO)
	{
		EmpDAO.deleteEmployee(emp);
	}

	public static void printEmployeeReport(Employee emp)
	{
		EmployeeReportFormatter Formatter = new EmployeeReportFormatter(emp, FormatType.CSV);
		String output = Formatter.getFormattedEmployee();
		System.out.println(output);
	}


}
