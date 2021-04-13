package formatting;

import employee.Employee;

public class ReportFormatter {

	String outputformat;
	
	public ReportFormatter(Employee emp, FormatType type)
	{
		switch(type)
		{
		case XML:
			outputformat = convertObjectToXML(emp);
			break;
		case CSV:
			outputformat = convertObjectToCSV(emp);
			break;
		}
	}
	
	private String convertObjectToXML(Employee emp)
	{
		return "<title>"+emp.toString()+"</title>";
	}
	
	private String convertObjectToCSV(Employee emp)
	{
		return ",,,,"+emp.toString()+",,,,";
	}
	
	protected String getFormattedvalue()
	{
		return outputformat;
	}
	

}
