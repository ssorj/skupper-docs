## Skupper history

Skupper has a history rooted in application-layer networking, evolving from an open-source project ...

Messaging!

Skupper has a rich messaging heritage, primarily stemming from its foundational reliance on Apache Qpid Dispatch, an AMQP 1.0 message router. This heritage significantly shapes Skupper's architecture and capabilities, even though Skupper itself primarily routes TCP connections rather than messages directly.
Here's a breakdown of Skupper's messaging heritage:
1. Origins in Apache Qpid Dispatch and AMQP 1.0:
    ◦ The underlying technology for Skupper's data plane is Apache Qpid Dispatch, an AMQP 1.0 message router developed by Red Hat and the Apache Qpid community starting around 2013-2014.

Here's a timeline and overview of Skupper's history:

**1. Foundations and Inception (2013-2019)**
*   **Apache Qpid Dispatch**: The underlying technology, an AMQP 1.0 message router, was developed by Red Hat and the Apache Qpid community, starting around **2013-2014**. Qpid Dispatch serves as Skupper's data plane, designed to be lightweight, low latency, and capable of building reliable, multipath networks. It's a message router, not a broker, running purely in memory and scaling from small devices to large wide-area networks.
*   **Skupper Project Launch**: The Skupper open-source project officially began in **June 2019**. Its initial focus was on automating the Interconnect Router and integrating it across various environments, including Kubernetes, Docker, Podman, VMs, and bare metal.

**4. The Era of Skupper v2.0 (2024-2025)**
*   **Skupper v2.0** represents a significant architectural shift, designed for improved usability, extensibility, and maintainability.
