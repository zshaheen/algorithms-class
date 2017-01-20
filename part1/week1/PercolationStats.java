import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;

public class PercolationStats {
  private double[] threasholdValues;

  public PercolationStats(int n, int trials) {
    // perform trials independent experiments on an n-by-n grid
    if (n <= 0 || trials <= 0)
      throw new java.lang.IllegalArgumentException();

    threasholdValues = new double[trials];
    for (int i = 0; i < trials; i++) {
      threasholdValues[i] = calculateThreashold(n);
    }
  }

  private double calculateThreashold(int n) {
    Percolation p = new Percolation(n);
    // continue until percolates
    int row, col;
    double count = 0;

    while (!p.percolates()) {
      row = StdRandom.uniform(n) + 1;
      col = StdRandom.uniform(n) + 1;
      if (!p.isOpen(row, col)) {
        p.open(row, col);
        count++;
      }
    }
    return count/(n*n);
  }

  public double mean() {
    // sample mean of percolation threshold
    return StdStats.mean(threasholdValues);
  }

  public double stddev() {
    // sample standard deviation of percolation threshold
    return StdStats.stddev(threasholdValues);
  }

  public double confidenceLo() {
    // low  endpoint of 95% confidence interval
    return mean() - (1.96*stddev())/(Math.sqrt(threasholdValues.length));
  }

  public double confidenceHi() {
    // high endpoint of 95% confidence interval
    return mean() + (1.96*stddev())/(Math.sqrt(threasholdValues.length));
  }

  public static void main(String[] args) {
    // test client (described below)
    int n = Integer.parseInt(args[0]);
    int t = Integer.parseInt(args[1]);
    PercolationStats ps = new PercolationStats(n, t);

    System.out.println("mean                    = " + ps.mean());
    System.out.println("stddev                  = " + ps.stddev());
    System.out.println("95% confidence interval = " + ps.confidenceLo() + ", " + ps.confidenceHi());
  }
}
