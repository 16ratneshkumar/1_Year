
# What is aws ?
- Cloud computing is the delivery of computing services –including servers, storage, databases, networking, software, analytics, and intelligence-over the internet(“the cloud”)to offer faster innovation, flexible resources, and economies of scale.

Benefits of cloud
Faster time to market  :-
Cost savings
Better collaboration :-ios
Advanced security
Data loss prevention 
Scalability and flexibility  

Disadvantage of cloud
Risk of vendor lock-in
Less control over underlying cloud infrastructure
Concerns about security risks like data privacy and online threats
Integration complexity with existing systems
Unforeseen costs and unexpected expenses
Cloud computing 
on–demand delivery 
Pay –as-you-go model
Provision only the size you need (exactly right type and size
Access resources instantly

S3
Object storage with durability of 99.999999999%,11 9’s 
Infinitely scaling storage
Can keep files in buckets S3 is a global service but buckets are created in specific regions
Globally unique bucket names
S3 standard has 99.99% availability =not available 53 minutes a year
Security 
User based-iam policies
Resource based
Bucket policies
Bicke acls
object acls
Public vs private 
accessible buckets 
Object versioning
State-of-the-art- in-transit and at-rest encryption
Storage classes
Amazon s3 standard- general purpose
Amazon s3 standard-Infrequent access(ia)
Amazon s3 one zone- Infrequent access
Amazon s3 glacier instant retrievel
Amazon s3 glacier flexible retrieval
Amazon s3 glacier deep archive
Amazon s3 intelligent tiering
Ec2
Most Popular AWS offering
Infrastructure as a code service
Provides rented Virtual MachinesEC2 uses EBS and instance store to store dataEC2 uses ELB to distribute dataEC2 uses autoscaling for scaling purposeBootstrapping can be done using userdata scripts Intances type 	N genral	C  cpu intancive	R more ram	GeneralComputememory	Accelerated	StoragePort no(tcp)	Stp -21	Ssh-22	telnet-23	dns-53(udp )	http-80	https-443	rdp-3389	mysql-3306EC2 • On-Demand Instances - short workload, predictable pricing, pay by second• Reserved (1 & 3 years) • Reserved Instances - commitment to an amount of usage, long workload, 1& 3 years upfront commitment, can save up to 72% on billing.• Spot Instances -short workloads, cheap, can lose instances (less reliable)• Dedicated Hosts - book an entire physical server, control instance placement, most expensive EC2, use case - BYOL, compliance or regulations• Dedicated Instances - no other customers will share your hardwareElbImplementation of horizontal scalingRequired for high availabilityTypes of load balancerClassic load balancer-layer 4&7(old &first)Application load balancer-layer7Network load balancer-layer 4Virtual host:-multiple hosting through single apace server