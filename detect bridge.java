class Solution
{
   static int isBridge(int V, ArrayList<ArrayList<Integer>> adj,int c,int d)
   {
       // code here
       adj.get(c).remove(new Integer(d));
       adj.get(d).remove(new Integer(c));
       boolean vis[]=new boolean[V];
       dfs(adj,vis,c); 
       if(vis[d]==true) 
       return 0;
       return 1;
   }
   static void dfs(ArrayList<ArrayList<Integer>> adj,boolean[] vis,int curr){
       vis[curr]=true;
       for(int it:adj.get(curr)){
           if(vis[it]==false)
            dfs(adj,vis,it);
       }
   }
}
