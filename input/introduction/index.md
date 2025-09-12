---
title: Introduction
---

# Introducing Skupper

Skupper is an over-the-top, multi-platform service interconnect.  Its
core purpose is to provide secure communication between application
components in disparate environments where general network
connectivity is difficult or undesirable.

## Application networks

Skupper solves communication challenges with something called an
application network (also known as a virtual application network or
VAN).  To understand the value of Skupper, it is helpful to understand
what an application network is.

An application network is made up of sites.  These are places where
you have workloads running.  They can be on different platforms and in
different parts of the world.

The sites are securely linked to form a network.  Each site has an
application router that is responsible for forwarding service traffic
across the network.

<img src="../images/overview-clouds.png" style="width: 80%;"/>

<!-- XXX An application network connects the services in your hybrid cloud into -->
<!-- a virtual network so that they can communicate with each other as if -->
<!-- they were all running in the same site.  In this diagram, an -->
<!-- application network connects three services, each of which is running -->
<!-- in a different cloud: -->

<!-- - XXX What the application sees. -->
<!-- - XXX How it is isolated. -->
<!-- - XXX The routers are in user space. -->

<!-- A Skupper network is composed of sites, where application components -->
<!-- run. These sites are linked together to form a dedicated network for -->
<!-- your applications.  -->

The application network is an isolated, distributed set of connected
software components where addressing and routing occur at the service
level (application layer), independent of the underlying IP
network. This approach abstracts away the complexities of underlying
network configurations.

<!-- ## Skupper connectivity -->

<!-- Skupper represents a new approach to connecting services across multiple Kubernetes clusters. -->
<!-- See how Skupper can give you the flexibility to deploy your services where you need them. -->

<!-- **One cluster** -->

<!-- Kubernetes **services** provide a virtual network address for each element of your distributed application. -->
<!-- Service "A" can contact service "B", "B" can contact "C", and so on. -->

<!-- ![one-cluster](../images/one-cluster.svg) -->

<!-- But if you want to deploy your application across multiple clusters, your options are limited. -->
<!-- You have to either expose your services to the public internet or set up a VPN. -->

<!-- Skupper offers a third way. -->
<!-- It connects clusters to a secure layer 7 network. -->
<!-- It uses that network to forward local service traffic to remote clusters. -->

<!-- **Secure hybrid cloud communication** -->

<!-- Deploy your application across public and private clusters. -->

<!-- ![two-clusters](../images/two-clusters.svg) -->

<!-- You can host your database on a private cluster and retain full connectivity with services running on the public cloud. -->
<!-- All communication is secured by mutual TLS authentication and encryption. -->

<!-- **Edge-to-edge connectivity** -->

<!-- Distribute application services across geographic regions. -->

<!-- ![five-clusters](../images/five-clusters.svg) -->

<!-- You can connect multiple retail sites to a central office. -->
<!-- Once connected, each edge location can contact any other edge. -->
<!-- You can add and remove sites on demand. -->

<!-- **Scale up and out** -->

<!-- Build large, robust networks of connected clusters. -->

<!-- ![many-clusters](../images/many-clusters.svg) -->

## Comparing Skupper to other solutions

**VPNs** - Unlike VPNs, Skupper does not expose IP networks.  Instead,
Skupper exposes only the specific network interfaces (socket
listeners) of application components.

**Service meshes** - Unlike service meshes, Skupper does not attempt
to manage all aspects of service communication.  Instead, Skupper
focuses on flexible connectivity.  Many service meshes focus on one
particular platform.  Skupper is designed to work across platforms.

Compared to other solutions, Skupper is notably very easy to set up.
Because it operates over-the-top, it does not require any changes to
your existing networking.

## Zooming out

In essence, Skupper leverages the robust, multipath, and secure
routing capabilities of its AMQP 1.0-based data plane to
provide application-layer connectivity for a wide range of protocols,
primarily TCP and HTTP, abstracting the complexities of underlying
Layer 3 networks for distributed applications.

<!-- To learn more: -->

<!-- * [Use cases](use-cases.html) -->
<!-- * [Security](security.html) -->
<!-- * [Observability](observability.html) -->
<!-- * [Architecture](architecture.html) -->
<!-- * [Routing](routing.html) -->
<!-- * [Performance](performance.html) -->
<!-- * [History](history.html) -->

<!-- ## Unfiled -->

<!-- - Skupper, also known as Red Hat Service Interconnect (RHSI), is a -->
<!--   service interconnect platform designed to facilitate **secure -->
<!--   communication between application components** across various -->
<!--   environments such as Kubernetes clusters, virtual machines (VMs), -->
<!--   container engines (like Podman and Docker), and bare-metal -->
<!--   hosts. Its core purpose is to simplify complex network topologies by -->
<!--   operating at the application layer, "over the top" of existing Layer -->
<!--   3 (L3) networking, without requiring VPNs or special firewall -->
<!--   rules. Skupper creates **isolated, application-focused virtual -->
<!--   networks** with logical service addresses, enabling application -->
<!--   portability and secure communication through mutual TLS (mTLS) -->
<!--   authentication and encryption. -->
