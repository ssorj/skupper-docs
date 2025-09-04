# Skupper architecture

## Principles

- Application-Layer Networking (Over-the-Top): Skupper operates at
  Layer 7, on top of existing IP networks. This means services connect
  across network boundaries without the need for VPNs or special
  firewall rules. It can function even over complex L3 network
  topologies.
- Protocol Layering: Communication involves Layer 3 TCP connections
  between routers (Skupper "site links") and Layer 7 AMQP
  messages. TCP and HTTP adaptors convert virtual TCP connections and
  HTTP requests into AMQP messages for routing across the network.
- Global Addressing: The Skupper router uses a global addressing
  system based on logical string addresses. This enables
  location-independent distributed applications.
- Isolation: Skupper creates isolated, application-focused
  networks. Each network is private to its application and uses its
  own dedicated router mesh. This strong isolation prevents broad
  exposure of internal infrastructure.
- Namespace Segmentation: When deployed in a Kubernetes namespace, the
  Skupper router provides namespace segmentation within the cluster,
  meaning only sites of a particular network can communicate with
  services on that network. For non-Kubernetes environments like
  Docker and Podman, a system user account can act as a namespace for
  micro-segmentation.
- No Elevated Privileges: Skupper and its routers run without elevated
  privileges, operating with the same permissions as your application.

## Components

The Skupper router, Skupper controller, and Skupper Network Observer
are indeed **key components** within the Skupper architecture, each
playing a distinct role in establishing and managing the Virtual
Application Network (VAN).

Here's an overview of these components:

### The Skupper router

Skupper Router (Data Plane): The heart of Skupper, the router, is a
distributed message router that uses AMQP messaging between routers to
form a fault-tolerant backbone. It is written in C, runs purely in
memory, and is a message router, not a broker. The router handles
application-layer addressing and routing based on logical string
addresses rather than IP numbers. It supports arbitrary topologies,
multipath routing, and routing based on cost and capacity. The router
makes services available on each namespace in the Skupper network by
creating proxy endpoints when a service is exposed.

The Skupper router provides the data plane of an application network.

The router is responsible for routing application connections and
requests between sites.  All inter-site communication is secured using
mutual TLS (mTLS), and the router operates without elevated
privileges, enhancing security.

The router employs a global addressing system, sharing
information about named destinations with peer routers to efficiently
determine the next nearest router for a given service.

The router also provides dynamic load balancing based on service
capacity and supports cost- and locality-aware traffic forwarding.  It
supports redundant network paths for high availability.

#### Protocol Layering and TCP/HTTP Encapsulation:

    - Skupper operates by creating an AMQP routing network. It works "over-the-top" of existing IP networks.
    - It uses TCP and HTTP adaptors to encapsulate and elaborate TCP data and HTTP requests into and out of AMQP messages.
    - This allows the AMQP protocol to route the TCP/HTTP data over the least-cost path, with automatic failover in case of an outage. The underlying interconnect network is hidden from the applications' virtual network.
    - Each TCP connection maps to two AMQP messages (one outgoing, one incoming), and virtual TCP connections are load-balanced on a per-connection basis. Similarly, each HTTP request maps to two AMQP messages (request and response) and is load-balanced on a per-request basis.


#### Listeners and connectors

#### Global addresssing

#### High availability

### The Skupper controller

*   **Skupper Controller** (often referred to as the Kubernetes control plane or operator for non-Kubernetes sites):
    *   The Skupper controller is responsible for **managing Kubernetes resources** such as Services, Deployments, Secrets, and ConfigMaps. In Skupper v2, this is achieved through a **declarative API using Custom Resource Definitions (CRDs)** for sites, links, listeners, and connectors.
    *   The **Skupper Operator** manages the Skupper infrastructure, simplifying deployment and updates of Skupper components within a Kubernetes or OpenShift cluster.
    *   In Skupper v2, there is a **unified controller** designed to combine the functionalities of the previous site and service controllers, and the "service-sync" mechanism of v1 is replaced with explicit listeners and connectors.
    *   The controller also handles aspects like **policy control**, allowing cluster administrators to restrict Skupper usage.
    * The API!
    * Configuring the data plane (the router)

Skupper Site Controller (Control Plane): This component configures the
Skupper router for a specific site and manages Kubernetes resources
such as Services, Deployments, Secrets, and ConfigMaps. In Skupper v2,
the site and service controllers are combined into a unified
Kubernetes controller, simplifying operations and allowing site
configuration changes without re-creating the site.

#### Declarative API

### The Skupper CLI

The Skupper Command Line Interface (CLI) is a **primary tool for interacting with and administering Skupper deployments**, allowing users to manage various aspects of the Virtual Application Network (VAN). It is designed to provide a consistent experience across different platforms, including Kubernetes, container engines like Podman and Docker, and bare-metal hosts.

Here's a detailed look at the Skupper CLI:

*   **Core Functionality for Site Management and Connectivity:**
    *   **Site Configuration:** Commands like `skupper init` are used to **create a Skupper site** and establish a Certificate Authority (CA) without requiring elevated privileges. In Skupper v2, configuration parameters are moving to standard Kubernetes resources.
    *   **Site Linking:** The CLI facilitates linking Skupper sites. `skupper token create` generates **credentials (tokens)**, which are then used with `skupper link create` to establish a secure connection between sites. These tokens are typically single-use and time-limited, though options exist for unlimited use.
    *   **Service Exposure:** `skupper expose` makes services available across the Skupper network. It **does not create an L3 connection** between namespaces but rather translates service protocols (TCP, HTTP1, HTTP2) into AMQP for secure inter-site communication. For more complex scenarios, `skupper service create` defines a service, and `skupper service bind` links that service to a cluster service (e.g., deployment, statefulset).
    *   **Load Balancing:** The CLI supports configuring load balancing. For instance, `skupper service create` with `--mapping tcp` can enable **connection-level load balancing** instead of HTTP load balancing. Multiple `skupper service bind` commands for a single service can also be used for load balancing.
    *   **Network Status and Monitoring:** Administrator-level network monitoring is available through the CLI. Commands like `skupper network status` provide an overview of the Skupper network.

*   **Troubleshooting and Debugging:**
    *   The CLI offers several commands for **diagnosing issues**. These include `skupper status` (for site status), `skupper service status -v` (for exposed services), and `skupper debug events` (for Skupper events).
    *   The `skupper debug dump` command is crucial, creating a tarball that includes logs, configuration, and Kubernetes resource YAML for Skupper-related components, aiding in issue reporting.

*   **Evolution with Skupper v2 and Non-Kubernetes Platforms:**
    *   **Revamped and CRD-based:** Skupper v2 introduces a **revamped CLI that is CRD-based and blocking**, replacing the previous "service-sync" mechanism with explicit listeners and connectors.
    *   **Non-Kubernetes Support:** For non-Kubernetes environments like Podman and Linux (using systemd), new commands such as `skupper system install`, `skupper system apply`, `skupper system start`, and `skupper system reload` are being developed to manage Skupper infrastructure. The `localhost` is often the default host value for `skupper connector create` on non-Kube platforms.
    *   **YAML Integration:** The CLI is designed to **generate and apply YAML configurations** for resources like sites, links, listeners, and connectors.
    *   **Improvements in v2:** Skupper v2 aims for a simplified CLI using the new model, with an OpenShift console plugin offering similar capabilities. There have been efforts to improve CLI usability, including a "big CLI redesign" in 2024.

*   **Usability and Development Considerations:**
    *   The CLI integrates with Kubernetes contexts, and understanding `kubectl` or `oc` contexts is important when working with multiple clusters.
    *   Discussions around CLI design emphasize consistency, conventional naming, and avoiding arbitrary differences. For example, the utility of a `skupper token status` command in v2 has been debated, focusing on whether it should indicate if a token is valid and redeemable.
    *   There is an ongoing effort to improve documentation for CLI commands, including overviews of concepts, resources, and command usage.

### The Skupper Network Observer

*   **Skupper Network Observer** (previously known as vFlow or Vanflow/flow-collector):
    *   This component is responsible for **publishing and collecting events and metrics** within the Skupper network. It plays a crucial role in **observability**.
    *   It **ingests events** from protocol observers within the Skupper router (e.g., HTTP/1 and HTTP/2 observers) and **exposes them as Prometheus metrics**. These metrics are then used in the Skupper console for network monitoring.
    *   In Skupper v2, observability components are designed to be **deployed separately from site components**, offering more flexibility.

## More

1. Origins in Apache Qpid Dispatch and AMQP 1.0:
    - The underlying technology for Skupper's data plane is Apache Qpid Dispatch, an AMQP 1.0 message router developed by Red Hat and the Apache Qpid community starting around 2013-2014.
    - AMQP 1.0 is highlighted as an efficient, binary wire protocol that excels at highly general application-layer communication. Key features include concurrent sessions, message streaming, message- and byte-level flow control, message-level acknowledgement, and anycast or multicast message distribution.
    - Qpid Dispatch is a message router, not a broker; it runs purely in memory, is lightweight, low latency, and capable of building reliable, multipath networks that scale from small devices to large wide-area networks.
2. Skupper's Role as Control Plane for Interconnect Routers:
    - While Qpid Dispatch (referred to as Interconnect Router) handles the data plane, Skupper acts as its control plane, automating and integrating the Interconnect Router across various environments like Kubernetes, Docker, Podman, VMs, and bare metal.
    - Skupper connects router nodes in a multipath network for reliability and uses mTLS for secure, bidirectional communication through firewalls.
