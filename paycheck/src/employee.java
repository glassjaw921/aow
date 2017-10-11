import java.util.Scanner;

import static java.lang.System.in;

public class employee {


    // create instance variables
    private double hoursWorked;
    private double dependants;
    private double hourlyWage;
    Scanner in = new Scanner(System.in);



    public employee(){

        // initialise employee instance variables
        hoursWorked = 0;
        dependants = 0;
    }

    // mutator
    public void setHoursWorked(){
        hoursWorked = hoursWorked;
        System.out.println("Enter number of hours worked : ");
        hoursWorked = in.nextInt();

    }

    // mutator
    public void setDependants(){
        System.out.println("Enter number of Dependants : ");
        dependants = in.nextInt();
    }

    // accessor
    public double getHoursWorked(){
        return hoursWorked;
    }

    // accessor
    public double getDependants() {
        return dependants;
    }
}
