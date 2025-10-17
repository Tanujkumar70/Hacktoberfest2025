import java.util.*;

public class DijkstraAlgorithm {

    // Define a class to represent a node in the priority queue
    static class Node implements Comparable<Node> {
        int target;  // The destination city
        long price;  // The price/weight to reach this city

        public Node(int target, long price) {
            this.target = target;
            this.price = price;
        }

        // Comparison based on price (for the Min-Heap behavior of PriorityQueue)
        @Override
        public int compareTo(Node other) {
            return Long.compare(this.price, other.price);
        }
    }

    // Define a constant for infinity (a very large number)
    private static final long INF = Long.MAX_VALUE;

    /**
     * Finds the shortest path from a source city to all other cities in the graph.
     * @param V The number of cities (vertices).
     * @param adj The adjacency list: adj[u] contains a list of Node objects {v, price}
     * representing an edge from u to v with the given price.
     * @param src The starting city (source node).
     * @return An array containing the minimum price to reach each city from the source.
     */
    public static long[] dijkstra(int V, List<List<Node>> adj, int src) {
        // 1. Initialize distance array. dist[i] stores the minimum price from src to i.
        long[] dist = new long[V + 1]; // Using 1-based indexing
        Arrays.fill(dist, INF);

        // 2. Priority Queue (Min Heap) to store nodes to visit, prioritized by price.
        PriorityQueue<Node> pq = new PriorityQueue<>();

        // 3. Set the distance of the source node to 0 and push it to the priority queue.
        dist[src] = 0;
        pq.add(new Node(src, 0));

        while (!pq.isEmpty()) {
            // Extract the city 'u' with the minimum distance 'd'
            Node current = pq.poll();
            long d = current.price;
            int u = current.target;

            // Check if the extracted distance is obsolete (we found a shorter path already)
            if (d > dist[u]) {
                continue;
            }

            // Iterate over all neighbors 'v' of 'u'
            for (Node edge : adj.get(u)) {
                int v = edge.target;
                long price = edge.price;
                long newPrice = d + price;

                // Relaxation Step: If a shorter path to v is found through u
                if (newPrice < dist[v]) {
                    // Update the distance of v
                    dist[v] = newPrice;
                    // Push the new minimum distance to the priority queue
                    pq.add(new Node(v, newPrice));
                }
            }
        }
        return dist;
    }

    public static void main(String[] args) {
        // Example Graph (4 cities, 5 flights):
        // 1 --(4)--> 2
        // | \      / |
        // (5) (2) (5) (3)
        // |   \ /   /  |
        // 4     3 <----
        
        int V = 4; // Number of cities
        int src = 1; // Source city (Syrjälä)

        // Initialize adjacency list for 1-based indexing (V+1 size)
        List<List<Node>> adj = new ArrayList<>(V + 1);
        for (int i = 0; i <= V; i++) {
            adj.add(new ArrayList<>());
        }

        // Add flights (u, v, price)
        adj.get(1).add(new Node(4, 5));
        adj.get(1).add(new Node(2, 4));
        adj.get(2).add(new Node(4, 5));
        adj.get(1).add(new Node(3, 2));
        adj.get(3).add(new Node(4, 3));

        long[] shortestPrices = dijkstra(V, adj, src);

        System.out.println("Shortest prices from City " + src + " (Syrjälä):");
        for (int i = 1; i <= V; i++) {
            if (shortestPrices[i] == INF) {
                System.out.println("City " + i + ": Unreachable");
            } else {
                System.out.println("City " + i + ": " + shortestPrices[i]);
            }
        }
        
        // Output for Lehmälä (City 4)
        System.out.println("\nMinimum price to Lehmälä (City " + V + "): " + shortestPrices[V]);
        
        /*
        The output for the example graph will be:
        City 1: 0
        City 2: 4
        City 3: 2
        City 4: 5  (Path 1->3->4 with cost 2+3=5, or 1->4 with cost 5)
        */
    }
}
