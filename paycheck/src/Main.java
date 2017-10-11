import java.util.Scanner;
// MAIN --  [JESUS TAKE THE WHEEL]
public class Main {

    public static void main(String[] args) {

    	// initialise cool variables
    	double getDependants;
    	double hoursWorked;
		double grossPay;
		double getTax;
		double netPay;
		double stateTax;
		double federalTax;
		double socialSecTax;
		Scanner in = new Scanner(System.in);
		paycheck pay = new paycheck();
		employee employee = new employee();
		hoursWorked = employee.getHoursWorked();

		//create objects

		employee.setHoursWorked();
		employee.setDependants();

		// call accessors
		getDependants = employee.getDependants();
		hoursWorked = employee.getHoursWorked();


		grossPay = pay.getGrossPay(hoursWorked, getDependants);
		System.out.println("Gross Pay = $" + grossPay);
		getTax = pay.getTax(grossPay);
		System.out.println("Tax  = $" + getTax);
		netPay = pay.netPay(grossPay, getTax, getDependants);
		System.out.println("Your Net Pay = $" + netPay);
		}








}
