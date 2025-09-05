# Skupper use cases

XXX

- Skupper helps you overcome networking obstacles. See how you can
  securely connect services in sites behind firewalls or NAT without
  changing your existing networking.

- When your data sources are running in a mix of legacy environments,
  and you can’t move them
- When you can’t access your data sources by changing the networking
  at layer 3
- When you need to span administrative domains you don’t control

- Skupper's versatility makes it suitable for a wide range of
  scenarios, primarily aimed at bridging connectivity gaps in hybrid
  and multi-cloud environments.

## Remote resource access

A core function of Skupper is to enable secure access to resources located in "other" clusters or on-premises data centers from applications in public clouds, and vice versa.

- **Accessing On-Premises Data** - This is crucial for maintaining data privacy and leveraging cloud compute without migrating sensitive data. Data sources include databases (e.g., PostgreSQL, MySQL, MongoDB), message brokers, and API endpoints.
- **Accessing Cloud Resources** - Allows private data centers or on-prem applications to securely access cloud-based resources, such as cloud GPU instances for processing.
- **Firewall and NAT Traversal** - Skupper operates over existing L3 connectivity, eliminating the need to modify NAT configurations or open new firewall holes to establish cross-site networks.
- **Developer Access** - Simplifies developer access to applications deployed in the cloud without requiring administrative control of the clusters or network.

- **Unreachable Networks** - It makes "unreachable" networks routable, connecting diverse environments with complex firewalls, NAT, VPNs, and CIDR conflicts.
- **IPv4/IPv6 Interoperability** - Skupper supports networks with a mix of IPv4 and IPv6 sites, enabling IPv4 applications to work transparently over IPv6 networks.
- **DMZ Scenarios** - Can be used to establish secure links into a DMZ, allowing control over outbound connections.

Messaging Use Cases:

Skupper can be used to connect message brokers and clients, enabling communication across different departments or environments.

- **Single Connection Point** - Clients can have a single connection point to multiple AMQ brokers owned by different departments.
- **Service Telemetry Framework (STF)** - The STF team utilizes Skupper for multi-site event transport, extending beyond traditional AMQP protocols, allowing distribution of applications across clusters without modification.
- **Examples** - Dedicated examples exist for ActiveMQ, RabbitMQ, and Kafka.

Messaging-related Use Cases and Examples:

- Skupper is used in scenarios involving message brokers, such as
  multi-site access to message brokers.
- Examples include basic AMQP examples, federation examples with Apache
  ActiveMQ Artemis, and Kafka examples. A Kafka example connects a
  private cluster (Minikube) with a public one (OpenShift).
- Skupper can be used where clients need a single connection point to
  multiple AMQP brokers owned by different departments.
- Messaging (qbench) benchmarks show Skupper's performance for
  latency-tolerant, asynchronous operations

## Application modernization

Skupper simplifies the migration and modernization of applications by allowing components to be moved incrementally without disrupting overall service.

- **Incremental platform migration** **Incremental Service Migration** - Components can be moved one at a time, with traffic balanced across both old and new environments, allowing for verification at each step and the option to roll back if needed. This avoids "big bang" migrations.
- **Legacy to Podman Migration** - Skupper supports migrating legacy services to Podman environments.
- **Connecting Legacy to Cloud-Native** - It creates a frictionless path for legacy applications, including those on mainframes or other platforms, to integrate with or migrate to microservices and the cloud, even if they cannot be containerized or economically moved.
- **Example** - The "Patient Portal" and "Trade Zoo" examples demonstrate connecting application components across different cloud and on-prem environments during migration.
- Breaking up a monolithic application

## Application resiliency

Skupper enhances application resilience by providing mechanisms for high availability, disaster recovery, and intelligent load balancing across sites.

- **Dynamic Load Balancing** - Skupper dynamically balances requests across clusters based on service capacity, favoring the closest available and least congested service instance rather than simple round-robin.
- **Failover** - By assigning different "costs" to inter-cluster links, Skupper can configure the network for failover, directing traffic to a specific location until failure, then rerouting to a backup location.
- **Data Replication** - Supports replicating data across sites using application-specific clustering technologies (e.g., RabbitMQ, Redis) for data consistency and high availability.
- **"Faux Stretch Cluster"** - As an alternative to a traditional stretch cluster, Skupper can connect redundantly deployed applications across two different clusters, making microservices available across both.
- **Kafka and 3scale Resiliency** - Skupper has been successfully used to provide resiliency for Kafka and 3scale deployments across multiple sites.

## Edge applications

Skupper is well-suited for applications spread across numerous geographical locations and diverse computing environments, common in edge scenarios.

- **Multi-Geo Retail and Logistics** - Provides connectivity for applications across multiple field offices or retail branches.
- **Centralized Edge Management** - Enables centralized configuration management of edge sites and the deployment/update of AI models at the edge.
- **Edge Failover and Telemetry** - Connects nearby edge environments for failover purposes and facilitates collecting telemetry from edge sites.
- **Intermittent Connectivity** - Its bidirectional network and automatic reconnection capabilities are valuable in edge environments with unreliable connectivity.
- **Non-Kubernetes Edge** - Edge sites often run on container engines like Podman or bare metal rather than Kubernetes, which Skupper fully supports.

## Others

#### 5. AI/ML Workloads

Skupper can facilitate various AI/ML use cases, particularly those involving distributed data and computational resources.

- **Federated Learning** - Creates isolated networks for federated learning, allowing models to be trained locally at remote data locations while maintaining data privacy.
- **Remote GPU Access** - Enables secure access to remote GPUs for model training, connecting on-prem applications to cloud-based high-performance computing resources.
- **Edge Model Deployment** - Supports deploying and updating AI models at the edge.

#### 8. Developer-Centric Networking and Security

Skupper empowers application owners with direct control over their application's networking and security, providing guardrails for centralized policy.

- **On-Demand Network Creation** - Application teams can create and tear down application networks on demand, matching the application lifecycle, without requiring coordination with a separate infrastructure team.
- **Per-Application Isolation** - Each application gets its own dedicated, isolated network ("Virtual Application Network"), limiting exposure and preventing lateral attacks. If one Skupper application is compromised, others are not affected.
- **Zero Trust Network Architecture (ZTNA)** - By connecting specific application listeners and connectors rather than entire IP networks, Skupper aligns with ZTNA principles, reducing the attack surface and providing identity-aware access control.
- **No Elevated Privileges** - Skupper and its routers run without elevated privileges, further limiting the potential reach of attackers.

---

## Skupper "Anti-Use Cases"

While Skupper is highly flexible, there are scenarios where other tools might be a better fit:

- **Cluster-Level Interconnect** - Skupper is not designed to be a "one giant network" cluster-level interconnect for all services without application isolation. For universal L3 access across OpenShift clusters, **Submariner** is generally recommended.
- **Service Mesh Features** - Skupper is a connectivity solution, not a replacement for a full service mesh like Istio. It does not natively provide features like service access authorization, advanced traffic shaping, or policy enforcement beyond connectivity controls. However, Skupper can be used *with* a service mesh to import remote services into a local mesh or expose a service from a mesh to a Skupper network.
- **Replicated Data Stores Needing Node/Service-Level Identity** - For replicated data stores like MongoDB, CockroachDB, Redis, or RabbitMQ that require node- and service-level identity and lower latencies with fewer router hops, **Submariner** might be a better fit than Skupper.
- **Specific Protocol Limitations** - Like Azure App Service Hybrid Connections, Skupper cannot directly mount a drive, use UDP, access TCP-based services that use dynamic ports (like FTP Passive Mode or Extended Passive Mode), or support LDAP due to its reliance on UDP.
