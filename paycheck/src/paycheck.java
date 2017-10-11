import java.net.SocketImpl;

public class paycheck extends employee
{
    // instance variables

    private double hourlyWage;
    private double overtimeWage;
    private double netPay;
    private double federalTax;
    private double stateTax;
    private double socialSecTax;
    private double grossPay;
    private double unionDues;



    public paycheck()
    {
        // initialise paycheck instance variables
        hourlyWage = 16.78;
        socialSecTax = .06;
        federalTax = .14;
        stateTax = .05;
        netPay = 0;
        grossPay = 0;
        overtimeWage = hourlyWage *1.5;
        unionDues = 10;
    }

    // calculate overall Pay
    public double getGrossPay(double hoursWorked, double getDependants) {

        grossPay = hourlyWage * hoursWorked;
        if (hoursWorked > 40){

            double overtimeHours = hoursWorked - 40;
            System.out.println("over time hours = " + overtimeHours);

            double overTimePay = overtimeHours * overtimeWage;
            System.out.println("Overtime pay = " + overTimePay);

            //calculate grossPay  with overtim and Union Dues
            double grossPay = (overTimePay + (hoursWorked - overtimeHours) * hourlyWage) - unionDues;
            System.out.println("subtracting $ 10 for Union Dues");
            return grossPay;

        }else if (hoursWorked > 0 && hoursWorked <= 40){

            // calculate Gross pay for regular time
            double grossPay = (hoursWorked * hourlyWage) - unionDues;
            System.out.println("subtracting $ 10 for Union Dues");
            return grossPay;

        }else

            System.out.println("System error, does not compute");

        //return TOTAL pay value
        return grossPay;
    }

    // calculate amount of tax taken from gross pay
    public double getTax(double grossPay){

        System.out.println("federal tax = " + federalTax + "%");
        System.out.println("state tax = " + stateTax + "%");
        System.out.println("Social security Tax = " + socialSecTax + "%");
        double getTax = grossPay * (federalTax + stateTax + socialSecTax);
        return getTax;
    }

    // gets final pay amount
    public double netPay(double grossPay, double getTax, double getDependants){


        // check if employee has 3 or more dependants
        if (getDependants >= 3) {

            //yes they do, take 35 more dollars
            netPay = (grossPay - getTax) - 35;
            System.out.println("number of dependants is " + getDependants + " so subtract another $35 ");
            return netPay;

        }else
            // no they don't, print out
            System.out.println("number of dependants = " + getDependants);
            netPay = (grossPay - getTax);
            return netPay;
    }

}
