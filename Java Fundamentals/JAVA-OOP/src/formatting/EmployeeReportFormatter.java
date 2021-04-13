package formatting;

import employee.Employee;

public class EmployeeReportFormatter extends ReportFormatter{

	public EmployeeReportFormatter(Employee emp, FormatType type) {
		super(emp, type);
	}
	
	public String getFormattedEmployee()
	{
		return getFormattedvalue();
	}
	
	

}
