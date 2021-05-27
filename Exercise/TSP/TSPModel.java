package TSP;

public class TSPModel {
    int[] X;
    boolean[] marked; // Danh dau vi tri duyet
    double f;
    double best_f;
    int[] best_X;
    double[][] c;

    int n;
    double min_c;

    boolean check(int k, int v) {
        return f + c[X[k - 1]][v] + min_c * (n - k + 1) < best_f;
    }

    void tryValue(int k) {
        if (k == n + 1) {
            updateBest();
            return;
        }
        for (int i = 1; i <= n; i++) {
            if (!marked[i]) {
                if (check(k, i)) {
                    marked[i] = true;
                    f += c[X[k - 1]][i];
                    X[k] = i;
                    tryValue(k + 1);
                    f -= c[X[k - 1]][i];
                    marked[i] = false;
                }
            }
        }
    }

    void updateBest() {
        if (f + c[X[n]][0] < best_f)
            best_f = f + c[X[n]][0];
    }

    void printSolution() {
        System.out.println("Best solution is " + best_f);
        for (int i = 0; i <= n; i++) {
            System.out.print(X[i] + "->");
        }
        System.out.print(0);
    }

    void setInput(double[][] c) {
        this.c = c;

        // Constructor
        n = c.length - 1;
        X = new int[n + 1];
        marked = new boolean[n + 1];
        f = 0;
        best_f = Double.MAX_VALUE;
    }
}
