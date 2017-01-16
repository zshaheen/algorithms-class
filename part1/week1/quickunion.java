public class QuickUnionUF() {
  private int[] id;

  public QuickUnionUF(int N) {
    id = new int[N];
    for (int i=0; i<N; i++) {
      id[i] = i;
    }
  }

  public int root(int p) {
    current = p;
    while(id[current] != current) {
      current = id[current];
    }
    return current;
  }

  public boolean connected(int p, int q) {
    return root(p) == root(q)
  }

  public void union(int p, int q) {
    id[root(p)] = root(q);
  }
}
