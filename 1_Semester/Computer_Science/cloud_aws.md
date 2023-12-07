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

Here's the information formatted in Markdown:

```markdown
### CloudFormation:
- **Purpose:** AWS CloudFormation is a service that allows you to create and manage AWS infrastructure as code using templates.
- **Functionality:** Enables automated provisioning of resources, defining infrastructure in JSON or YAML templates.
- **Benefits:** Facilitates consistent, repeatable deployments, simplifies resource management, and supports infrastructure versioning.

### AWS Cloud9:
- **Purpose:** AWS Cloud9 is an integrated development environment (IDE) in the cloud for writing, running, and debugging code.
- **Functionality:** Offers a collaborative environment with pre-configured development environments for various programming languages.
- **Benefits:** Supports real-time collaboration, code sharing, and access to AWS resources directly from the IDE.

### AWS CLI (Command Line Interface):
- **Purpose:** AWS CLI is a unified tool to manage AWS services from the command line.
- **Functionality:** Allows users to interact with AWS services, automate tasks, and configure AWS resources using commands.
- **Benefits:** Provides scriptable access to AWS services, enabling automation and scripting for various tasks and workflows.

### Auto Scaling:
- **Purpose:** AWS Auto Scaling helps automatically adjust the number of EC2 instances or other resources based on demand or predefined conditions.
- **Functionality:** Scales resources up or down to maintain performance, cost efficiency, and availability.
- **Benefits:** Ensures applications can handle varying workloads, improves fault tolerance, and optimizes resource usage.

### Load Balancing:
- **Purpose:** AWS Elastic Load Balancing (ELB) distributes incoming application traffic across multiple targets, such as EC2 instances, containers, etc.
- **Functionality:** Ensures even distribution of traffic, increases fault tolerance, and scales applications seamlessly.
- **Benefits:** Enhances application availability, prevents overloading of individual resources, and facilitates easier management of traffic flow.

### AWS Polly:
- **Purpose:** Amazon Polly is a service for text-to-speech conversion, allowing applications to generate human-like speech.
- **Functionality:** Converts text into lifelike speech in various languages and voices.
- **Benefits:** Enables the creation of applications with speech-enabled capabilities, such as accessibility features or automated voice responses.
```
### Amazon S3 (Simple Storage Service):

- **Use Cases:**
  1. **Data Backup and Archiving:** S3 is commonly used for backup and long-term archiving of data due to its durability and scalability.
  2. **Static Website Hosting:** Ideal for hosting static websites, storing HTML, CSS, images, and other assets.
  3. **Media Storage and Distribution:** Serves as a repository for storing and delivering media files, such as images, videos, and audio files.
  4. **Data Lakes and Analytics:** Utilized as a data lake for storing and analyzing vast amounts of unstructured data in conjunction with analytics services like AWS Athena, Redshift, etc.
  5. **Disaster Recovery and Backup:** Organizations leverage S3 as part of their disaster recovery strategies due to its durability and availability across multiple regions.

### Amazon EBS (Elastic Block Store):

- **Use Cases:**
  1. **Block-Level Storage for EC2 Instances:** EBS volumes are used as block-level storage for EC2 instances, providing persistent storage.
  2. **Database Storage:** Commonly used for hosting databases requiring persistent and high-performance storage, ensuring data durability and consistency.
  3. **Development and Testing:** EBS volumes serve as reliable storage for development, testing, and staging environments, allowing for easy snapshot backups.
  4. **High-Performance Computing:** Utilized in applications requiring low-latency access to data and high-throughput performance, such as computational simulations and analytics.

### Amazon EFS (Elastic File System):

- **Use Cases:**
  1. **Shared File Storage:** EFS is suitable for shared file storage among multiple EC2 instances within a VPC, enabling multiple instances to access the same data concurrently.
  2. **Content Management and Collaboration:** Used for storing and sharing files in applications that require multiple users to collaborate and access the same set of files simultaneously.
  3. **Web Serving and CMS:** EFS can serve as a backend storage for web servers, content management systems (CMS), and applications that require a centralized file system accessible by multiple instances.
  4. **Big Data and Analytics:** Deployed in big data and analytics workflows where multiple compute instances need shared access to the same dataset.
Certainly! Here's the information about Amazon RDS presented in Markdown format:

```markdown
## Amazon RDS (Relational Database Service)

Amazon RDS is a managed service provided by Amazon Web Services (AWS) that simplifies the setup, operation, and scaling of relational databases in the cloud. It offers various relational database engines such as MySQL, PostgreSQL, Oracle, SQL Server, and Amazon Aurora.

### Key Features:

- **Managed Service:** AWS handles routine database tasks like backups, patching, and scaling, allowing users to focus on their applications.
- **Multiple Database Engines:** Supports various popular relational database engines, providing compatibility and flexibility for different applications.
- **Automated Backups and Restore:** Enables automated backups and point-in-time recovery, ensuring data durability and offering recovery options.
- **Scalability:** Allows for easy scaling of compute and storage resources, accommodating changing workloads without downtime.
- **Security Features:** Offers security features like encryption at rest and in transit, network isolation using Amazon VPC, and IAM integration for access control.
- **High Availability:** Provides Multi-AZ deployments for automatic failover in case of an infrastructure failure, ensuring high availability.
- **Monitoring and Metrics:** Integrates with AWS CloudWatch for monitoring database instances, performance metrics, and setting alarms.
- **Read Replicas:** Supports creating read replicas to offload read traffic from the primary database, improving read scalability and performance.

### Use Cases:

- **Web Applications:** Suitable for hosting databases powering web applications, content management systems, and e-commerce platforms.
- **Business Applications:** Ideal for various business applications requiring a relational database backend, such as CRM, ERP, and HR management systems.
- **Development and Testing:** Provides a managed environment for development, testing, and staging databases without the hassle of managing infrastructure.
- **Data Warehousing:** Supports storing and managing data for analytical purposes in data warehousing and reporting systems.

Amazon RDS simplifies the process of setting up, operating, and scaling relational databases, making it an attractive solution for businesses and developers looking for a managed database service in the cloud.
```
