
public class IterativeApproach{
   public static void main(String[] args){
      
      int n = 10;
      int b = 5;
      int k = 4;
     
      System.out.printf("The possible number of ways we can place %d robots in %d stacks with a max number of %d robots in a stack is %d.", b, n, k, ComboCompute(n, k, b));
   }
   
   public static int ComboCompute(int n, int k, int b){
      
      int bcs[][] = new int[b + 1][n + 1];
      
      int LCV = 0;
      int LCV2 = 0;
      
      for(LCV = 0; LCV <= b; LCV++){
         for(LCV2 = 0; LCV2 <= n; LCV2++){
            bcs[LCV][LCV2] = -1;
         }
      }
      
      
      return robotCompute(b, k, n, bcs);
   }
   
   public static int robotCompute(int n, int k, int b, int[][] bcs){
      
      int i = 0;
      int j = 0;
      int m = 0;
      
      for(i = 0; i <= n; i++){
         for(j = 0; j <= b; j++){
            
            if(j == 0 || j == k * i){
               bcs[i][j] = 1;
            }
            else if(j > i * k){
               bcs[i][j] = 0;
            }
            else if(k == j){
               bcs[i][j] = bcs[i - 1][j] + bcs[i][j - 1];
            }
            else{
                           
               for(m = 0; m <= Math.min(k, b); m++){
                  
                  if(bcs[i][j] == -1){
                     bcs[i][j] = 0;
                  }
                  
                  if(n - 1 >= 0 && j - m >= 0){
                     bcs[i][j] += bcs[i - 1][j - m];
                  }
               }
            }
         }
      }
      
      for(j = 0; j < bcs.length; j++){
         for(i = 0; i < bcs[j].length; i++){
            System.out.printf("%7d ", bcs[j][i]);
         }
         System.out.printf("\n");
      }
      
      return bcs[n][b];
   }
}