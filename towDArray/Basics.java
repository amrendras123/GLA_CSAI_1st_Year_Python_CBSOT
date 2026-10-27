import java.util.Scanner;

class Basics{
    
    public static void main(String[] args) {
       Scanner sc=new Scanner(System.in);
    //     int[][] arr0={
    //     {1,2,3,4},
    //     {2,3,4,5,6},
    //     {10,20,30,40},
    //     {1},
    //     {12,13}
    // };

        // int[] ar={1,2,3,44,5,10,4,4,4,6,3,3,2};
        
        // int[][] arr2=new int[][4];
        // int[][] arr3=new int[][];
        // int[][] arr4=new int[4][];
        // arr4[0][0]=10;
        // System.out.println(arr4[0][0]);
        // int[][] arr5=new int[0][0];
       
        // arr[0][0]=20;
        // arr[6][4]=10;
        // row
        // System.out.println(arr.length);
        // // col
        // System.out.println(arr[0].length);

        // System.out.println(arr);
         int m=sc.nextInt(); //row
        int n=sc.nextInt(); //col
        int[][] arr=new int[m][n];

        for(int i=0;i<arr.length;i++){
            for(int j=0;j<arr[i].length;j++){
                arr[i][j]=sc.nextInt();
            }
            
        }
// two-d array print
        for(int i=0;i<arr.length;i++){
            for(int j=0;j<arr[i].length;j++){
                System.out.print(arr[i][j]+" ");
            }
            System.out.println();
        }
       
    }
}