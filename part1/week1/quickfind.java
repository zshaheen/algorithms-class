public class QuickFindUF {
  private int[] id;

  public QuickFindUF(int N) {
    id = new int[N];
    for (int i=0; i<N; i++) {
      id[i] = i;
    }
  }

  public boolean connected(int p, int j) {
    return id[p] == id[q];
  }

  public void union(int p, int q) {
    int pid = id[p];
    int qid = id[q];
    // Has at most 2N + 2 array accesses
    for (int i=0; i<id.length; i++) {
      // Change all of the values of q to p
      if(id[i] == qid) {
        id[i] = pid
      }
    }
  }

}
