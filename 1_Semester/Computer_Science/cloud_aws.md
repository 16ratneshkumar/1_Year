# AWS-Computing-

## Cloud Computing

- **Overview:**
  - Cloud computing delivers various services over the internet.
  - AWS (Amazon Web Services) is a comprehensive cloud platform.

- **Cloud Computing Benefits:**
  - Faster time to market
  - Cost savings
  - Better collaboration
  - Advanced security
  - Data loss prevention
  - Scalability and flexibility

- **Cloud Computing Disadvantages:**
  - Risk of vendor lock-in
  - Less control over infrastructure
  - Security concerns
  - Integration complexity
  - Unforeseen costs

## AWS Services

- **Amazon S3 (Simple Storage Service):**
  - Object storage with 99.999999999% durability.
  - Infinitely scalable storage.
  - Global service with region-specific buckets.
  - Security features: IAM policies, bucket policies, ACLs.
  - Storage classes: Standard, IA, One Zone-IA, Glacier, Intelligent-Tiering.

- **EC2 (Elastic Compute Cloud):**
  - Popular AWS offering for virtual machines.
  - Infrastructure as code.
  - Uses EBS and instance store for data.
  - Types: General, CPU, RAM, Compute, Memory, Accelerated, Storage.
### [type of ec2  instances](https://aws.amazon.com/ec2/instance-types/)
  - **General Purpose**
      -General purpose instances provide a balance of compute, memory and networking resources, and can be used for a variety of diverse workloads. These instances are ideal for applications that use these resources in equal proportions such as web servers and code repositories. 
  - **Compute Optimized**
    - Compute Optimized instances are ideal for compute bound applications that benefit from high performance processors. Instances belonging to this category are well suited for batch processing workloads, media transcoding, high performance web servers, high performance computing (HPC), scientific modeling, dedicated gaming servers and ad server engines, machine learning inference and other compute intensive applications.
  - **Memory Optimized**
    - Memory optimized instances are designed to deliver fast performance for workloads that process large data sets in memory.
  - **Accelerated Computing**
    - Accelerated computing instances use hardware accelerators, or co-processors, to perform functions, such as floating point number calculations, graphics processing, or data pattern matching, more efficiently than is possible in software running on CPUs.
    - **Storage Optimized**
      - Storage optimized instances are designed for workloads that require high, sequential read and write access to very large data sets on local storage. They are optimized to deliver tens of thousands of low-latency, random I/O operations per second (IOPS) to applications.
    - **HPC Optimized**
      - High performance computing (HPC) instances are purpose built to offer the best price performance for running HPC workloads at scale on AWS. HPC instances are ideal for applications that benefit from high-performance processors such as large, complex simulations and deep learning workloads.
- **ELB (Elastic Load Balancer):**
  - Horizontal scaling implementation.
  - Types: Classic, Application (Layer 7), Network (Layer 4).

- **IAM (Identity and Access Management):**
  - Manages access to AWS services.

- **Other AWS Services:**
  - Lambda, CloudWatch, RDS, Route 53, etc.

## Cloud Models

- **Public Cloud:**
  - Offered by third-party providers.
  - Available over the public internet.
  - Scales quickly and conveniently.

- **Private Cloud:**
  - Offered to select users over the internet or a private network.
  - Greater security controls.
  - Requires traditional datacenter staffing.

- **Hybrid Cloud:**
  - Combination of public and private clouds.
  - Shared security responsibility.

## AWS Gov Cloud and China Regions

# Serverless

## Compute Service
- Fargate: Serverless compute engine for containers.
- Lambda: Serverless computing service.

## Database
- Aurora Serverless: On-demand, autoscaling configuration for Amazon Aurora.

## Storage
- EFS (Elastic File System): Shared file system without pre-defined size increase.
- DRBD: Distributed Replicated Block Device.

## Block Storage
- Object Storage
- RAID (Redundant Array of Independent Disks)
- SAN (Storage Area Network)

## Network
- VPC (Virtual Private Cloud)
- Direct Connect: Connect your on-premises database with AWS databases directly.

## AWS Services
- SQS (Simple Queue Service): Queue service.
- CodeBuild: Build tool, compiler.
- CloudTrail: Records AWS API calls.
- CodeDeploy: Automates code deployments.
- CodePipelines: Continuous delivery service.
- CodeCommit: Version control service.
- CodePipeline + CodeCommit: Service control system (SCS).
- Amazon Polly: Text-to-speech service.
- Amazon Lex: Conversational interfaces
- AWS Comprehend: Natural language processing.
- SNS (Simple Notification Service): Publish-subscribe messaging.
- Braket: Quantum computing service.
- RabbitMQ: Message broker with a pub-sub model.

# Auto Scaling

## AWS Auto Scaling

- **Auto Scaling Adjusts Resources:**
  - To match desired capacity, ensuring:
    - **Availability:** Maintains application availability.
    - **Dynamic Scaling:** Scales Amazon EC2 capacity based on demand.
    - **Optimization:** Automatically adjusts resources for efficient performance.
    - **Management:** Simplifies resource scaling and management.

## Load Balancer

- **AWS Load Balancer:**
  - Horizontal Scaling: Distributes incoming application traffic.
  - High Availability: Ensures fault tolerance.
  - Types:
    - Classic Load Balancer: Layer 4 & 7.
    - Application Load Balancer: Layer 7, routing based on content.
    - Network Load Balancer: Layer 4, handles TCP/UDP traffic.
  - Implementation of Horizontal Scaling: Facilitates scaling applications horizontally.

## EKS Service on AWS

- **AWS EKS (Elastic Kubernetes Service):**
  - Managed Kubernetes: Fully managed Kubernetes service.
  - Easy Deployment: Simplifies deployment, management, and scaling of containerized applications.
  - Benefits:
    - Automates Kubernetes cluster provisioning and maintenance.
    - Integrated with AWS services and features.
    - Supports popular Kubernetes tools and applications.
  - Worker Nodes: Managed EC2 instances running in your account.
  - Control Plane: Managed by AWS, reducing operational overhead.

# ECS (Elastic Container Service)

- **AWS ECS is a service that provides:**
  - Container Orchestration: Manages deployment and scaling of containerized applications.
  - Compatibility: Works with Docker containers.
  - Key Features:
    - Task Definitions: Defines containers to be launched together.
    - Clusters: Logical grouping of container instances.
    - Services: Defines how tasks are deployed and maintained.
  - Integration: Integrates with other AWS services like ELB, ECR, IAM, etc.
  - Managed Service: Removes the need for you to install, operate, and scale your own cluster management infrastructure.
## Aws CLI
-The AWS Command Line Interface (CLI) is a unified tool provided by Amazon Web Services (AWS) that enables users to manage their AWS services via a command-line interface. It allows users to interact with various AWS services, such as EC2 (Elastic Compute Cloud), S3 (Simple Storage Service), Lambda, IAM (Identity and Access Management), and more, directly from the terminal. Users can perform tasks like creating instances, managing storage, configuring security settings, and automating workflows by issuing commands via the AWS CLI.
## Aws SDK
- The AWS SDK (Software Development Kit) provides developers with tools, libraries, and APIs to build applications that interact with various Amazon Web Services (AWS). It offers programming interfaces in various languages such as Python, Java, JavaScript/Node.js, Ruby, .NET, and more, enabling developers to integrate AWS services into their applications easily.The SDK abstracts the complexities of making direct HTTP requests to AWS APIs and provides a higher-level interface, making it easier to interact with services like S3, EC2, DynamoDB, SNS, SQS, and others. Developers can perform tasks such as creating, managing, and deleting resources, handling authentication, managing access control, and integrating AWS functionalities seamlessly within their applications using the SDK.
## cloudformation
- AWS CloudFormation is a service provided by Amazon Web Services (AWS) that allows users to define and manage their infrastructure as code (IaC). It enables the creation, management, and provisioning of AWS resources in a declarative manner using templates.With CloudFormation, users can define a template (typically written in YAML or JSON) that describes the desired AWS infrastructure configuration, including resources like EC2 instances, S3 buckets, databases, load balancers, security groups, IAM policies, and more. This template represents the complete architecture of an application or system.Once the template is defined, CloudFormation takes care of provisioning and managing the resources specified in the template, handling dependencies and ensuring the defined configuration is deployed consistently and predictably across different environments.CloudFormation templates can be version-controlled, reused, and shared, allowing for easy replication of infrastructure setups, simplifying deployments, and providing a streamlined approach to managing AWS resources. This service helps in automating the provisioning of infrastructure and promotes a consistent, repeatable, and efficient deployment process.
## aws fargate
- AWS Fargate is a serverless, pay-as-you-go compute engine that lets you focus on building applications without managing servers. Moving tasks such as server management, resource allocation, and scaling to AWS does not only improve your operational posture, but also accelerates the process of going from idea to production on the cloud, and lowers the total cost of ownership.
Certainly! Here's the summary of the information in Markdown format:

```markdown
### Types of AWS EC2 Instances:

1. **Compute Instances:**
   - Families like "t2", "t3", "m5", "c5", etc., emphasize balanced CPU, memory, and networking resources.
   - Check instance types such as "t2.micro", "m5.xlarge", "c5.large" for compute-focused capabilities.

2. **Memory-Optimized Instances:**
   - Families like "R6g", "R5", "X1e", "High Memory (u-* and z1d*)" cater to memory-intensive applications.
   - Look for instance types such as "r6g.large", "r5.large", "x1e.xlarge" for high memory-to-CPU ratios.

3. **Network-Optimized Instances:**
   - Families like "C5", "M5", "F1", "H1" offer good networking performance.
   - Smallest instances could be "c5.large", "m5.large", "f1.2xlarge", "h1.2xlarge".

4. **Storage-Optimized Instances:**
   - Families like "D2", "I3", "H1", "G3s" are designed for storage-intensive workloads.
   - Smallest instances might include "d2.xlarge", "i3.large", "h1.2xlarge", "g3s.xlarge".

These instance families vary in their resource allocations and are tailored for specific workload requirements. Always verify the latest instance types and their capabilities through the AWS documentation or Management Console.
```

This Markdown code creates formatted text suitable for use in various Markdown-supporting environments or platforms, allowing for better readability and organization of information.