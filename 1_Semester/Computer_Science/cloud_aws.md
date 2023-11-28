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
