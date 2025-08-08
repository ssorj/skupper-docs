# Installing Skupper on Kubernetes

Before you can create a site on Kubernetes, you must install the
Skupper controller and CRDs.  You can use any of the following
methods:

* Directly using YAML
* Helm charts
* Operator

After installation, you can create sites using the CLI or YAML:

* [Creating a site using the CLI][cli-site]
* [Creating a site using YAML][yaml-site]

[cli-site]: ../kube-cli/site-configuration.html
[yaml-site]: ../kube-yaml/site-configuration.html

## Installing Skupper using YAML

**Prerequisites**

* cluster-admin access to cluster

**Procedure**

To install the latest Skupper release, use `kubectl apply` with the
[installation YAML](https://skupper.io/install.yaml):

~~~ shell
kubectl apply -f https://skupper.io/install.yaml
~~~

To install a particular version of Skupper, use the GitHub release URL:

**Procedure**

~~~ shell
kubectl apply -f https://github.com/skupperproject/skupper/releases/download/{{skupper_version}}/skupper-cluster-scope.yaml
~~~

There is also an option to install the controller at namespace scope:

~~~ shell
kubectl apply -f https://github.com/skupperproject/skupper/releases/download/{{skupper_version}}/skupper-namespace-scope.yaml
~~~

**NOTE**: If you install the controller at cluster scope, you can
create sites in any namespace.  If you install the controller at
namespace scope, you can create sites only in that namespace.

## Installing Skupper using Helm

**Prerequisites**

* cluster-admin access to cluster
* Helm (see [Installing Helm](https://helm.sh/docs/intro/install/))

**Procedure**

Run the following command to install the controller at cluster scope:

~~~ shell
helm install skupper oci://quay.io/skupper/helm/skupper --version {{skupper_version}}
~~~

To install a controller at namespace scope, add the `--set
scope=namespace` option.

**NOTE**: If you install the controller at cluster scope, you can
create sites in any namespace.  If you install the controller at
namespace scope, you can create sites only in that namespace.

<!-- ## Installing the Skupper controller using the Skupper Operator -->

<!-- **Prerequisites** -->

<!-- * cluster-admin access to cluster -->
<!-- * OpenShift -->

<!-- **Procedure** -->

<!-- 1. Navigate to the **OperatorHub** in the **Administrator** view. -->
<!-- 2. Search for `Skupper`, provided by `Skupper project`. -->
<!-- 3. Select **stable-2.0** from **Channel**. -->
<!-- 4. Select the latest **Version**. -->
<!-- 5. Click **Install**. -->
