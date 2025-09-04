# Skupper performance

- The router scales up to millions of connections

- It also scales down to small devices, suitable for resource-constrained edge environments

- The router is proﬁcient at low latency, asynchronous communication

- Horizontal scale property

- Skupper’s per-app deployment model means it can scale horizontally
  and avoid bottlenecking at a cluster-wide entrypoint.

- 10 Gbps with one CPU core

- Performance Considerations Skupper's performance is significantly
  influenced by router CPU allocation, which is the primary scaling
  factor. Two CPU cores (2,000 millicores) per router is a recommended
  starting point for most workloads. Router memory scales with the
  number of open connections, with 4GB recommended for up to 65,536
  concurrent connections. While an L7 approach cannot match L3
  performance, Skupper has shown competitive throughput and latency
  results in multi-cluster benchmarking.

- Optimized TCP Adaptor: A new, faster TCP adaptor with improved
  buffer handling and reduced threading overhead is included, aiming
  for lower application latency and decreased router CPU utilization.
