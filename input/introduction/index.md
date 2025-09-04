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

XXX An application network connects the services in your hybrid cloud into
a virtual network so that they can communicate with each other as if
they were all running in the same site.  In this diagram, an
application network connects three services, each of which is running
in a different cloud:

- XXX What the application sees.
- XXX How it is isolated.
- XXX The routers are in user space.

A Skupper network is composed of sites, where application components
run. These sites are linked together to form a dedicated network for
your applications. The VAN is an isolated, distributed set of
connected software components where addressing and routing occur at
the service level (Layer 7), independent of the underlying
network. This approach abstracts away the complexities of underlying
network configurations.

## Skupper connectivity

Skupper represents a new approach to connecting services across multiple Kubernetes clusters.
See how Skupper can give you the flexibility to deploy your services where you need them.

**One cluster**

Kubernetes **services** provide a virtual network address for each element of your distributed application.
Service "A" can contact service "B", "B" can contact "C", and so on.

![one-cluster](../images/one-cluster.svg)

But if you want to deploy your application across multiple clusters, your options are limited.
You have to either expose your services to the public internet or set up a VPN.

Skupper offers a third way.
It connects clusters to a secure layer 7 network.
It uses that network to forward local service traffic to remote clusters.

**Secure hybrid cloud communication**

Deploy your application across public and private clusters.

![two-clusters](../images/two-clusters.svg)

You can host your database on a private cluster and retain full connectivity with services running on the public cloud.
All communication is secured by mutual TLS authentication and encryption.

**Edge-to-edge connectivity**

Distribute application services across geographic regions.

![five-clusters](../images/five-clusters.svg)

You can connect multiple retail sites to a central office.
Once connected, each edge location can contact any other edge.
You can add and remove sites on demand.

**Scale up and out**

Build large, robust networks of connected clusters.

![many-clusters](../images/many-clusters.svg)

## Comparing Skupper to other solutions

**VPNs** - Unlike VPNs, Skupper does not expose IP networks.  Instead,
Skupper exposes only the specific network interfaces (socket
listeners) of application components.

**Service meshes** - Unlike service meshes, Skupper does not attempt
to manage all aspects of service communication.  Instead, Skupper
focuses on flexible, multi-platform connectivity.

<!-- ^^ Confined to one platform XXX -->

<!-- **Tailscale and similar** XXX -->

Compared to other solutions, Skupper is notably very easy to set up.
Because it operates over-the-top, it does not require any changes to
your existing networking.

## Zooming out

In essence, Skupper leverages the robust, multipath, and secure
routing capabilities of its AMQP 1.0-based data plane to
provide application-layer connectivity for a wide range of protocols,
primarily TCP and HTTP, abstracting the complexities of underlying
Layer 3 networks for distributed applications.

## More resources

* [Use cases](introduction/use-cases.html)
* [Security](introduction/security.html)
* [Routing](introduction/routing.html)
* [Observability](introduction/observability.html)
* [Architecture](introduction/architecture.html)
* [Performance](introduction/performance.html)
* [History](introduction/history.html)
