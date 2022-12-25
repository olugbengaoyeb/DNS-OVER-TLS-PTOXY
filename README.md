# DNS-OVER-TLS-PTOXY

# SOURCE CODE
    - This is a simple DNS-over-TLS proxy written in Python. It listens for incoming DNS queries on a specified port and     forwards them to a DNS-over-TLS server. It then receives the response from the server and sends it back to the client.
    - The main entry point for the proxy is the main function, which creates a socket to listen for incoming DNS queries and    enters an infinite loop to handle each incoming query. When a query is received, the proxy calls the handle_query function, which does the following:

      1. Receives the query from the client.
      2. Creates a new socket and wraps it in a Secure Sockets Layer (SSL) context using the ssl module. This establishes an encrypted connection to the DNS-over-TLS server.
      3. Sends the query to the DNS-over-TLS server and receives the response.
      4. Sends the response back to the client.
      5. Closes the connection to the server and the connection to the client.

    - To use this proxy, you will need to set the DNS_SERVER variable to the address of a DNS-over-TLS server and the DNS_PORT variable to the port that the server is listening on. You can also change the LISTEN_PORT variable to specify the port that the proxy should listen for incoming queries on.
    
      -----PREREQUISITES------
      To start the DNS proxy, follow these steps:

      1. Make sure you have Python 3 installed on your machine. You can check the version of Python you have installed by running the command python3 --version.

      2. Install the required libraries by running the command pip3 install -r requirements.txt. This will install the dnslib and ssl modules, which are required for the DNS proxy to function.

      3. Start the DNS proxy by running the command python3 dns_proxy.py. This will start the proxy, which will listen for incoming DNS queries on port 53 and forward them to a DoT server using an encrypted TLS connection.

      4. To test the proxy, you can use a tool such as dig or nslookup to send a DNS query to the proxy. For example, you can run the command dig @localhost -p 53 google.com to query the proxy for the IP address of the domain google.com.

      To run this code, you will need to install the dnspython library using pip:
      "pip install dnspython"

      # Then, you can run the proxy using Python:
      "python proxy.py"

      To stop the proxy, press CTRL+C in the terminal window where the proxy is running.
 


# DOCKERFILE
     This Dockerfile uses the Python 3.9 base image and installs the tls and dnslib libraries using pip. It then copies the proxy.py file (which should contain the code for the DNS proxy as shown above) to the /app directory and exposes the DNS proxy port (53). The CMD specifies the command to run when the container is started, which is to run the proxy.py script.

     -----PREREQUISITES------
     You must have Docker installed on your machine to build and run the proxy using the provided Dockerfile. You can follow the instructions for installing Docker on the Docker website.
     
     # BUILDING THE PROXY
     To build the DNS to DNS-over-TLS proxy, follow these steps:

     1. Change to the directory containing the Dockerfile and the proxy.py

     2. To build the Docker image, run the following command in the same    
        directory as the Dockerfile:
        "docker build -t dns-proxy ."
        This will build the Docker image and tag it as dns-proxy.

     3. To run the Docker container, use the following command:
         "docker run -d -p 53:53 dns-proxy"
        This will start the Docker container and map the host's port 53 to the container's port 53, allowing the DNS proxy to listen for queries on the host's port 53.

        You can also pass additional options to the docker run command, such as --name to specify a name for the container or -d to run the container in detached mode. Use the following command:
         "docker run -d --name dns-proxy-1 -p 53:53/tcp dns-proxy"

        You can modify the Dockerfile and run command to customize the behavior of the proxy. For example, you can pass command-line arguments to the proxy.py script to specify the DNS-over-TLS server address and port, or you can mount a configuration file to the container to allow the proxy to read its configuration from a file.
     
     4. To stop the Docker container, run the following command:
         "docker stop dns-proxy"

# Testing the Proxy
To test the DNS to DNS-over-TLS proxy, you can use a tool such as dig to send DNS queries to the proxy and verify that the correct responses are returned.

For example, to send a DNS query for the domain example.com to the proxy, you can use the following command:
"dig @localhost example.com"

This will send the DNS query to the proxy running on the localhost (@localhost) and display the response. You can also specify the -t option to specify the DNS record type (e.g., A, NS, MX) or the -p option to specify the port (e.g., -p 53).

# Stopping the Proxy
To stop the DNS to DNS-over-TLS proxy, you can use the docker stop command to stop the running container.

For example, if the container is running with the name dns-proxy-1, you can use the following command to stop it:

"docker stop dns-proxy-1"












# Security Concerns
   When deploying this proxy in an infrastructure, there are several security concerns to consider:

   1. Confidentiality: It is important to ensure that the DNS queries and responses are not intercepted or tampered with while in transit. To address this concern, the proxy uses TLS encryption to secure the communication between the client and the DNS-over-TLS server.

   2. Authentication: It is important to ensure that the DNS-over-TLS server being used is trusted and authentic. To address this concern, you can use certificate pinning or certificate transparency to verify the authenticity of the server's certificate.

   3. Access control: It is important to ensure that only authorized clients can access the proxy. To address this concern, you can use authentication or IP-based access control to limit access to the proxy.

   4. DoS protection: It is important to protect the proxy from DoS attacks, which could prevent it from functioning properly or cause it to crash. To address this concern, you can implement rate limiting or use a WAF (Web Application Firewall) to block malicious traffic.

# Integration in a Microservices Architecture
   One way to integrate this proxy in a distributed, microservices-oriented and containerized architecture would be to deploy it as a standalone service in its own container. The proxy could then be accessed by other services in the infrastructure using DNS requests sent to the proxy's IP address and port.

   To integrate the DNS to DNS-over-TLS proxy into a microservices-oriented and containerized architecture, you can follow these steps:

   1. Build a Docker image for the proxy using the provided Dockerfile.

   2. Deploy the proxy as a standalone service using a container orchestration platform such as Kubernetes.

   3. Set the proxy as the DNS server for the other microservices in the architecture. This can be done by specifying the proxy's address and port as the nameserver in the /etc/resolv.conf file of each microservice container.

# Potential Improvements
  Some potential improvements that could be made to the project include:

  1. Caching: To improve performance and reduce the number of queries sent to the DNS-over-TLS server, you can add a cache to the proxy. This can store the results of previous queries and return them to clients without sending a new query to the server.

  2. Error handling: To improve reliability, you can add error handling to the proxy to handle cases where the DNS-over-TLS server is not reachable or returns an error.

  3. Load balancing: To improve scalability, you can add load balancing to the proxy to distribute the queries across multiple DNS-over-TLS servers.

  4. Metrics and logging: To improve monitoring and debugging, you can add metrics and logging to the proxy to track the number of queries received and the responses returned.
