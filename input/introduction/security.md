# Skupper security

<!-- Skupper securely connects your services with TLS authentication and -->
<!-- encryption.  See how Skupper enables you to deploy your application -->
<!-- securely across Kubernetes clusters. -->

Skupper is designed to address the security challenges inherent to
distributed applications in hybrid environments.

## Security challenges

Moving an application to the cloud raises security risks.

Increasing the challenge, layer 3 network controls do not extend
easily to multiple clusters.  These network controls must be
duplicated for each cluster.

<!-- Either your -->
<!-- services must be exposed to the public internet, or you must adopt -->
<!-- complex layer 3 network controls like VPNs, firewall rules, and access -->
<!-- policies. -->

- Exposure of Services to the Public Internet and Layer 3 Networking
  Complexities: Traditional networking often requires exposing
  services directly to the internet or implementing complex Layer 3
  (L3) controls like VPNs and extensive firewall rules, which can be
  difficult to manage, especially across multiple clusters.

- Unauthorized Access and Data Interception: In distributed systems,
  ensuring data privacy and authenticating all communication partners
  can be a significant challenge, leading to risks of unauthorized
  access and data exfiltration.

- Broad Network Access and Lack of Application-Level
  Compartmentalization: Traditional network configurations often grant
  broad access to internal infrastructure, making it difficult to
  isolate applications from each other and increasing the attack
  surface.

- Privilege Escalation and System Compromise: Running network services
  with elevated privileges increases the risk of system compromise if
  a vulnerability is exploited.

- Lack of Visibility and Control for Administrators: Administrators
  need tools to monitor and control network usage to enforce
  organizational policies.

Many networking tools are confined to the scope of their platform.

Skupper changes the security picture in some important ways.

IP addresses and network locations used by traditional networks, vpns
and dmz architectures to establish access are often conﬁgured to allow
excessive implicit trust and unpatched vulnerabilities Leave
enterprises at risk for attack.

## Mutual TLS authentication and encryption

- Inter-router
- Service-to-router and router-to-service
- Cert rotation

- **Mutual TLS** - All inter-site communication within a Skupper
  application network is secured using mutual TLS, where both sides of
  a router-to-router link are authenticated, and all router-to-router
  traffic is encrypted.  Skupper also provides the option of mutual
  TLS for service-to-router and router-to-service communication within
  each site.

- Mutual TLS for inter-router communication.  Optional mutual TLS for
  service-to-router and router-to-service communication.

- **User-Provided TLS Certificates** - Skupper supports using
  user-provided TLS certificates for both linking sites and
  pod-to-router communication.

- **Site-Specific Certificate Authorities (CAs)** - By default, each
  Skupper site has its own Certificate Authority (CA). `skupper init`
  creates a CA for the site without elevated privileges.

- OpenSSL

## Built-in network isolation

Skupper provides default, built-in security that scales across
clusters and clouds.  In a Skupper network, the connections between
Skupper routers are secured with mutual TLS using a private, dedicated
certificate authority (CA).  Each router is uniquely identified by its
own certificate.

This means that the Skupper network is isolated from external access,
preventing security risks such as lateral attacks, malware
infestations, and data exfiltration.

- **Strong isolation** - Each application network is dedicated to the
  components of one distributed application, using its own set of
  routers.  Skupper exposes specific network interfaces (socket
  listeners) rather than creating layer 3 connections between IP
  networks, preventing broad exposure of internal infrastructure.

- **No elevated privileges** - The Skupper router runs without
  elevated privileges, limiting your exposure if there is a
  vulnerability.

- Skupper exposes service listeners, not IP networks.
- The Skupper router runs without elevated privileges.

Skupper prioritizes security by establishing **application-layer
networks** that offer secure, compartmentalized communication across
diverse environments.

- **No Direct Exposure of Internal Applications** - Skupper links
  originate from the private site to the public site, and once
  established, application connections can traverse them securely in
  either direction, eliminating the need to open ports on private data
  centers. This aligns with a **Zero Trust Network Architecture
  (ZTNA)** where IP addresses are not exposed.

- Each network has a dedicated set of routers, providing full process
  isolation for application traffic.

- The app owner (or data owner) directly controls who can connect.

Skupper provides network isolation primarily through its **application-layer networking model** and **compartmentalization strategies**, distinguishing it from traditional Layer 3 (L3) networking solutions.

Here's how Skupper achieves network isolation:

*   **Application-Layer Network Compartmentalization**: Each Skupper network is specifically designed to fit the components of one distributed application and utilizes its own dedicated router mesh. This creates **strong network isolation** and **per-app network isolation**, ensuring that the routers of one network are fully process-isolated from others. This enforces application data isolation at the CPU level. Skupper exposes specific application components (their listeners and connectors) rather than entire IP networks, which helps avoid security pitfalls that can arise from L3 networking complexity.
*   **No L3 Connection Between Namespaces/IP Networks**: Unlike VPN-based solutions, Skupper does not create L3 connections between IP networks or namespaces. Instead, it routes from client connectors to server listeners using logical application addressing. This means services are not made available on a public ingress or listening on public IPs, significantly reducing their exposure.
*   **Namespace Segmentation in Kubernetes**: When the Skupper router is deployed in a Kubernetes namespace, it delivers **namespace segmentation within the cluster itself**. If standard Kubernetes network policy is in place, only the sites of a particular network can see and communicate with services on that network. Skupper can also be combined with Kubernetes NetworkPolicies for **microsegmentation** in multi-tenant clusters.
*   **Isolation for Non-Kubernetes Environments**: For container environments like Docker and Podman, Skupper can use **system user accounts as namespaces** to achieve micro-segmentation, mirroring the isolation provided by Kubernetes namespaces.
*   **Controlled Connectivity and Policy**: The application owner or data owner directly controls who can connect to the Skupper network. Skupper offers **policy controls**, such as `SkupperClusterPolicy`, which allow cluster administrators to restrict Skupper usage. **Incoming and outgoing link policies** protect a cluster from unauthorized sites, and **service and resource policies** prevent unauthorized service exposure. Skupper v2 further leverages standard Role-Based Access Control (RBAC) mechanisms with its Custom Resources (CRDs) for fine-grained control over Skupper resources.
*   **Mutual TLS (mTLS)**: All inter-site communication within a Skupper service network is secured using mutual TLS, where both client and server authenticate each other with certificates. This encryption and authentication prevent unauthorized access and data exfiltration.
*   **No Elevated Privileges**: Skupper and its router run without elevated privileges. They operate with the same privileges as the application, limiting the potential reach of an attacker if a vulnerability were exploited.
*   **Dynamic Network Lifecycle**: Skupper networks are easy to create and destroy. When an application network is no longer needed, it can be easily removed without coordinating with other teams, which helps prevent lingering security exposures. This aligns the network lifecycle with the application lifecycle.

## Observability angle

## Administration and lifecycle

- **Easy Network Management** - Skupper networks are easy to create
  and destroy, allowing for minimal distributed applications with
  minimal connectivity. When an application network is no longer
  needed, it can be easily removed without coordinating with other
  teams.

- No leaving firewall rules around because you can't tell what it will
  break if you remove it.

- **Lifecycle** - The lifecycle of an application network is the same
  as the application it serves.  No need to find and tear down
  app-specific IP network changes such as old firewall rules.

- **Policy Controls** - Skupper offers policy controls, such as
  `SkupperClusterPolicy`, which allow cluster administrators to
  restrict the use of Skupper on their cluster. **Incoming and
  outgoing link policies** protect a cluster from unauthorized sites,
  and **service and resource policies** prevent unauthorized service
  exposure.

- **Role-Based Access Control (RBAC)** - With the adoption of
  Kubernetes Custom Resources (CRDs) in Skupper v2, standard RBAC
  mechanisms can be leveraged for fine-grained control over Skupper
  resources.

- **Cluster admin controls**

- The lifecycle of an application network is the same as the
  application it serves.  No need to find and tear down app-specific
  IP network changes such as old firewall rules.

- Clean division of platform admin concerns and app owner concerns
