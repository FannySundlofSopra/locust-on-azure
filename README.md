# Running Locust.io on Azure Container Instances

Running distributed Locust.io on Azure Container Instances

Article with details is here:

[Running Locust on Azure](https://dev.to/azure/running-locust-on-azure-2k40)

Or just run `azure-deploy.sh` and follow instructions. Is that easy :)

A VNet integrated deployment is available via `azure-vnet-deploy.sh`

![Locust on Azure](./images/locust-dotnet-sqlhs.png)

You can try it right away, even if you don't have any API you can call, using [JSONPlaceholder](https://jsonplaceholder.typicode.com). To avoid flooding JSONPlaceholder with tons of request, the default values are set to create 1 locust client that will simulate 1 user only. The user will send a GET or a POST request every 5 to 10 seconds.

# Editing .sh files in VS Code on Windows

In case you are editing .sh files in Windows, you might encounter error at runtime in  WSL because of the default CRLF line ending applied. 
You can fix existing files with command `sed -i.bak 's/\r$//' azure-deploy.sh` [see this discussion](https://askubuntu.com/questions/803162/how-to-change-windows-line-ending-to-unix-version) and if you are using VS Code you can [configure line ending](https://github.com/Microsoft/vscode/issues/2957)