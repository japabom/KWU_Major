import java.util.*;
import java.lang.*;
public class MenuSortingSystem {
    public static void main(String[] args) {
        Restaurant start=new Restaurant();
        start.play();
    }
}
class Restaurant{
    static int orderNumber=0;
    static final String[] menu={"steak","apple","pasta","pizza"};
    Kitchen kk=new Kitchen();

    Analysis history=new Analysis();

    private int tableNumber;
    private int selectM=0;
    private int numSteak=0;
    private int numApple=0;
    private int numPasta=0;
    private int numPizza=0;
    private int steakTotal=0;
    private int appleTotal=0;
    private int pastaTotal=0;
    private int pizzaTotal=0;
    private int selectm=0;

    void play(){
        Scanner sc=new Scanner(System.in);
        int selectOp;

        System.out.println("Order System Start!!");
        while(true){
            System.out.println("Select option");
            System.out.print("1. Order, 2. Pay 3. Order list 4. Order History 5. FindMenuRanking 6. Terminate");
            selectOp=sc.nextInt();

            if(selectOp==1){
                System.out.print("Select your table number: ");
                tableNumber=sc.nextInt();
                order(tableNumber);
            }
            else if(selectOp==2){
                System.out.print("Select your table number: ");
                tableNumber=sc.nextInt();
                pay(tableNumber);
            }
            else if (selectOp == 3) {
                System.out.print("Select your table number: ");
                tableNumber=sc.nextInt();
                printOrderList(tableNumber);

            }
            else if (selectOp == 4) {
                printHistory();

            }
            else if(selectOp==5){
                findRanking(numSteak,numApple,numPasta,numPizza);
            }
            else if (selectOp == 6) {
                System.out.println("System terminate.....");
                break;
            }
            else {
                System.out.println("Wrong Input, check please");
                continue;
            }

        }

    }
    void order(int tableN){

        Scanner s=new Scanner(System.in);

        selectM=0;
        while(selectM!=5) {

            System.out.println("\nmenu: 1. steak, 2. apple, 3. pasta, 4. pizza, 5. Exit");
            System.out.print("Select menu: ");
            selectM = s.nextInt();

            if(selectM==1) {
                System.out.print("Select number of menu: ");
                int menuNum = s.nextInt();
                numSteak+=menuNum;
                steakTotal+=menuNum;
                System.out.print("1. Add more food, 2. Finish");
                selectm=s.nextInt();
                if(selectm==1)
                    continue;
                else if(selectm==2) {
                    orderNumber+=1;
                    if(tableN==1) {
                        kk.table1.set(numSteak, numApple, numPasta, numPizza);
                        if(kk.table1.totalPrice()!=0) {

                            history.table[orderNumber - 1] = new OrderInfo(kk.table1);
                        }
                    }
                    else if(tableN==2) {
                        kk.table2.set(numSteak, numApple, numPasta, numPizza);
                        if(kk.table2.totalPrice()!=0) {

                            history.table[orderNumber - 1] = new OrderInfo(kk.table2);
                        }
                    }
                    else if(tableN==3) {
                        kk.table3.set(numSteak, numApple, numPasta, numPizza);
                        if(kk.table3.totalPrice()!=0) {

                            history.table[orderNumber - 1] = new OrderInfo(kk.table3);
                        }
                    }
                    return;
                }
            }
            else if(selectM==2) {
                System.out.print("Select number of menu: ");
                int menuNum = s.nextInt();
                numApple+=menuNum;
                appleTotal+=menuNum;
                System.out.print("1. Add more food, 2. Finish");
                selectm=s.nextInt();
                if(selectm==1)
                    continue;
                else if(selectm==2) {
                    orderNumber+=1;
                    if(tableN==1) {
                        kk.table1.set(numSteak, numApple, numPasta, numPizza);
                        if(kk.table1.totalPrice()!=0) {

                            history.table[orderNumber - 1] = new OrderInfo(kk.table1);
                        }
                    }
                    else if(tableN==2) {
                        kk.table2.set(numSteak, numApple, numPasta, numPizza);
                        if(kk.table2.totalPrice()!=0) {

                            history.table[orderNumber - 1] = new OrderInfo(kk.table2);
                        }
                    }
                    else if(tableN==3) {
                        kk.table3.set(numSteak, numApple, numPasta, numPizza);
                        if(kk.table3.totalPrice()!=0) {

                            history.table[orderNumber - 1] = new OrderInfo(kk.table3);
                        }
                    }
                    return;
                }
            }

            else if(selectM==3) {
                System.out.print("Select number of menu: ");
                int menuNum = s.nextInt();
                numPasta+=menuNum;
                pastaTotal+=menuNum;
                System.out.print("1. Add more food, 2. Finish");
                selectm=s.nextInt();
                if(selectm==1)
                    continue;
                else if(selectm==2) {
                    orderNumber+=1;
                    if(tableN==1) {
                        kk.table1.set(numSteak, numApple, numPasta, numPizza);
                        if(kk.table1.totalPrice()!=0) {

                            history.table[orderNumber - 1] = new OrderInfo(kk.table1);
                        }
                    }
                    else if(tableN==2) {
                        kk.table2.set(numSteak, numApple, numPasta, numPizza);
                        if(kk.table2.totalPrice()!=0) {

                            history.table[orderNumber - 1] = new OrderInfo(kk.table2);
                        }
                    }
                    else if(tableN==3) {
                        kk.table3.set(numSteak, numApple, numPasta, numPizza);
                        if(kk.table3.totalPrice()!=0) {

                            history.table[orderNumber - 1] = new OrderInfo(kk.table3);
                        }
                    }
                    return;
                }
            }
            else if(selectM==4) {
                System.out.print("Select number of menu: ");
                int menuNum = s.nextInt();
                numPizza+=menuNum;
                pizzaTotal+=menuNum;
                System.out.print("1. Add more food, 2. Finish");
                selectm=s.nextInt();
                if(selectm==1)
                    continue;
                else if(selectm==2) {
                    orderNumber+=1;
                    if(tableN==1) {
                        kk.table1.set(numSteak, numApple, numPasta, numPizza);
                        if(kk.table1.totalPrice()!=0) {

                            history.table[orderNumber - 1] = new OrderInfo(kk.table1);
                        }
                    }
                    else if(tableN==2) {
                        kk.table2.set(numSteak, numApple, numPasta, numPizza);
                        if(kk.table2.totalPrice()!=0) {

                            history.table[orderNumber - 1] = new OrderInfo(kk.table2);
                        }
                    }
                    else if(tableN==3) {
                        kk.table3.set(numSteak, numApple, numPasta, numPizza);
                        if(kk.table3.totalPrice()!=0) {

                            history.table[orderNumber - 1] = new OrderInfo(kk.table3);
                        }
                    }
                    return;
                }
            }
            else if(selectM==5) {
                return;
            }
        }
    }
    void pay(int tableN){
        clearTable(tableN);
    }

    void printOrderList(int tableN){
        System.out.printf("table %d Order List: \n",tableN);
        if(tableN==1) {
            System.out.printf("%10s: %d\n", menu[0], kk.table1.getSteak());
            System.out.printf("%10s: %d\n", menu[1], kk.table1.getApple());
            System.out.printf("%10s: %d\n", menu[2], kk.table1.getPasta());
            System.out.printf("%10s: %d\n", menu[3], kk.table1.getPizza());
        }
        else if(tableN==2) {
            System.out.printf("%10s: %d\n", menu[0], kk.table2.getSteak());
            System.out.printf("%10s: %d\n", menu[1], kk.table2.getApple());
            System.out.printf("%10s: %d\n", menu[2], kk.table2.getPasta());
            System.out.printf("%10s: %d\n", menu[3], kk.table2.getPizza());
        }
        else if(tableN==3) {
            System.out.printf("%10s: %d\n", menu[0], kk.table3.getSteak());
            System.out.printf("%10s: %d\n", menu[1], kk.table3.getApple());
            System.out.printf("%10s: %d\n", menu[2], kk.table3.getPasta());
            System.out.printf("%10s: %d\n", menu[3], kk.table3.getPizza());
        }
    }
    void clearTable(int tableN){
        if(tableN==1){
            kk.table1.set(0,0,0,0);
        }
        else if(tableN==2){
            kk.table2.set(0,0,0,0);
        }
        else if(tableN==3){
            kk.table3.set(0,0,0,0);
        }
    }
    void printHistory(){
        for(int i=0;i<orderNumber;i++){
            System.out.printf("#%d. steak: %-5d, apple: %-5d, pasta: %-5d, pizza: %-5d\n",i+1,history.table[i].getSteak(),history.table[i].getApple(),history.table[i].getPasta(),history.table[i].getPizza());
        }


    }
    void findRanking(int a,int b,int c, int d){ // using Arrays.sort and Arrays.binarySearch to find each menu's Ranking, and using Arrays.copyOf for safety.
        int[] totalArr =new int[]{a,b,c,d};
        Scanner sc=new Scanner(System.in);

        System.out.print("Select Menu: ");
        String searchMenu=sc.nextLine();
        int index=5;
        int[] copyTotalArr=Arrays.copyOf(totalArr,4);
        Arrays.sort(copyTotalArr);
        if("steak".equals(searchMenu) || "Steak".equals(searchMenu))
            index=Arrays.binarySearch(copyTotalArr,numSteak);
        else if("apple".equals(searchMenu) || "Apple".equals(searchMenu))
            index=Arrays.binarySearch(copyTotalArr,numApple);
        else if("pasta".equals(searchMenu) || "Pasta".equals(searchMenu))
            index=Arrays.binarySearch(copyTotalArr,numPasta);
        else if("pizza".equals(searchMenu) || "Pizza".equals(searchMenu))
            index=Arrays.binarySearch(copyTotalArr,numPizza);
        else {
            System.out.println("error");
            return;
        }

        System.out.printf("The menu's Ranking is %d \n",(3-index)+1);





    }
}

class OrderInfo{

    static final int priceA=7000;
    static final int priceB=8000;
    static final int priceC=6000;
    static final int priceD=9000;


    private int numSteak=0;
    private int numApple=0;
    private int numPasta=0;
    private int numPizza=0;
    private int total_Price=0;
    private int totalNum=0;

    OrderInfo(){};
    OrderInfo(OrderInfo x){
        this.numSteak=x.getSteak();
        this.numApple=x.getApple();
        this.numPasta=x.getPasta();
        this.numPizza=x.getPizza();
    }
    void set(int a,int b,int c,int d){
        numSteak=a;
        numApple=b;
        numPasta=c;
        numPizza=d;

    }
    int getSteak(){
        return numSteak;
    }
    int getApple(){
        return numApple;
    }
    int getPasta(){
        return numPasta;
    }
    int getPizza(){
        return numPizza;
    }
    int totalPrice(){
        total_Price=priceA*getSteak()+priceB*getApple()+priceC*getPasta()+priceD*getPizza();
        return total_Price;
    }
    int totalNum(int a,int b){
        totalNum=getSteak()+getApple()+getPasta()+getPizza();
        return totalNum;
    }
}

class Kitchen{
    OrderInfo table1=new OrderInfo();
    OrderInfo table2=new OrderInfo();
    OrderInfo table3=new OrderInfo();
}

class Analysis{
    OrderInfo[] table=new OrderInfo[100];
}
