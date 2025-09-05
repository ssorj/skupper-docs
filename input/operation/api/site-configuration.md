# Configuring sites

XXX

- Declarative model of config
- See the [Site API]({{skupper_api_ref}}/site.html)
- Using YAML allows you to create and manage sites from the context of the current namespace.
- You can use YAML to create and manage Skupper sites.
- There are many options to consider when creating sites using YAML, see... .
- Prerequisite: The Skupper controller is running on the Kubernetes
  cluster you are running or you are running on a platform.

## Creating a site

Procedure:

1. Create a file with a name of your choice.  Include the YAML for a
   `Site` resource:

   <div class="file-label">site-1.yaml:</div>

   ~~~ yaml
   apiVersion: skupper.io/v2alpha1
   kind: Site
   metadata:
     name: site-1
     namespace: namespace-1
   ~~~

   This YAML defines a site named `site-1` in the `namespace-1`
   namespace.  If you don't set the namespace, the one from the
   current context is used.

1. Use your platform's `apply` to create the site.

   Kubernetes:

   ~~~ shell
   kubectl apply -f site-1.yaml
   ~~~

   Linux:

   ~~~ shell
   skupper system apply -f site-1.yaml
   ~~~

1. Use `kubectl get` or the Skupper CLI to check the status of your
   site.

   Kubectl:

   ~~~ shell
   kubectl get site
   ~~~

   Skupper CLI:

   ~~~ shell
   skupper site status
   ~~~

## Updating a site

Updating a site uses the same procedure as creating a site.  Change
the values in your local file and apply it again.

## Deleting a site

To delete a site defined in a YAML file, use the platform's `delete`
command.

Kubernetes:

~~~ shell
kubectl delete -f site-1.yaml
~~~

Linux:

~~~ shell
skupper system delete -f site-1.yaml
~~~
