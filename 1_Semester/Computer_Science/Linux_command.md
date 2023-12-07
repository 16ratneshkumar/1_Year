<h1>Linux command</h1>
<table>
<tr>
<th>S.No.</th>
<th>COMMAND
</th>
<th>WHY WE USE??
</th>
</tr>

<tr>
<td>1.
</td>
<td>
ls
</td>
<td>
directory listing (list all files/folders on current dir)
</td>
</tr>

<tr>
<td>2.
</td>
<td>ls -l</td>
<td>
formatted listing</td>
</tr>

<tr>
<td>3.
</td>
<td>
ls -la</td>
<td>
formatted listing including hidden files</td>
</tr>

<tr>
<td>4.
</td>
<td>
cd dir</td>
<td>
change directory to dir <b>(dir will be directory name)</b></td>
</tr>

<tr>
<td>5.
</td>
<td>
cd...</td>
<td>
change to parent directory directory</td>
</tr>

<tr>
<td>6.
</td>
<td>
cd../dir</td>
<td>
change to dir in parent</td>
</tr>


<tr>
<td>7.
</td>
<td>
cd</td>
<td>
change to home directory</td>
</tr>

<tr>
<td>8.
</td>
<td>
pwd</td>
<td>
show current directory</td>
</tr>

<tr>
<td>9.
</td>
<td>
mkdir dir</td>
<td>
create a directory dir</td>
</tr>

<tr>
<td>10.
</td>
<td>
rm file</td>
<td>
delete file</td>
</tr>

<tr>
<td>11.
</td>
<td>
rm -f dir</td>
<td>
force remove file</td>
</tr>

<tr>
<td>12.
</td>
<td>
rm -r dir</td>
<td>
delete directory dir</td>
</tr>

<tr>
<td>13.
</td>
<td>
rm-rf dir</td>
<td>
remove directory dir</td>
</tr>

<tr>
<td>14.
</td>
<td>
cp filel file2</td>
<td>
copy fill to filo2</td>
</tr>

<tr>
<td>15.
</td>
<td>
my filel file2</td>
<td>
rename filel to file2</td>
</tr>

<tr>
<td>16.
</td>
<td>
my filel dir/file2</td>
<td>
move filel to dir as file2</td>
</tr>

<tr>
<td>17.
</td>
<td>
touch file</td>
<td>
creato or updato filo</td>
</tr>

<tr>
<td>18.
</td>
<td>
cat file</td>
<td>
output contents of file</td>
</tr>

<tr>
<td>19.
</td>
<td>
cat > file</td>
<td>
write standard input into file</td>
</tr>

<tr>
<td>20.
</td>
<td>
cat >> file</td>
<td>
append standard input into file</td>
</tr>

<tr>
<td>21.
</td>
<td>
tail-f file</td>
<td>
output contents of file as it grows</td>
</tr>

</table>







Certainly! Below is the previously provided CloudFormation template for creating an EC2 instance, S3 bucket, Elastic Load Balancer, and Auto Scaling Group formatted as Markdown code blocks.

### YAML (YML) CloudFormation Template in Markdown:

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: Create an EC2 instance, S3 bucket, ELB, and Auto Scaling Group

Resources:
  MyS3Bucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: my-unique-bucket-name  # Replace with your bucket name

  MyLaunchConfiguration:
    Type: AWS::AutoScaling::LaunchConfiguration
    Properties:
      ImageId: ami-xxxxxxxxxxxxx  # Replace with your AMI ID
      InstanceType: t2.micro
      KeyName: my-keypair         # Replace with your Key Pair name
      UserData: |
        #!/bin/bash
        echo "Hello from UserData!"
      SecurityGroups:
        - sg-xxxxxxxx              # Replace with your Security Group ID
      IamInstanceProfile: your-instance-profile  # Replace with your IAM instance profile ARN

  MyAutoScalingGroup:
    Type: AWS::AutoScaling::AutoScalingGroup
    Properties:
      LaunchConfigurationName: !Ref MyLaunchConfiguration
      MinSize: 1
      MaxSize: 3
      DesiredCapacity: 2
      AvailabilityZones:
        - us-east-1a  # Replace with your desired availability zones
      LoadBalancerNames:
        - !Ref MyElasticLoadBalancer
      HealthCheckType: ELB
      HealthCheckGracePeriod: 300

  MyElasticLoadBalancer:
    Type: AWS::ElasticLoadBalancing::LoadBalancer
    Properties:
      AvailabilityZones:
        - us-east-1a  # Replace with your desired availability zones
      Listeners:
        - LoadBalancerPort: '80'
          InstancePort: '80'
          Protocol: HTTP
      HealthCheck:
        Target: 'HTTP:80/'
        HealthyThreshold: '3'
        UnhealthyThreshold: '5'
        Interval: '30'
        Timeout: '5'
```

### JSON CloudFormation Template in Markdown:

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "Create an EC2 instance, S3 bucket, ELB, and Auto Scaling Group",
  "Resources": {
    "MyS3Bucket": {
      "Type": "AWS::S3::Bucket",
      "Properties": {
        "BucketName": "my-unique-bucket-name"  // Replace with your bucket name
      }
    },
    "MyLaunchConfiguration": {
      "Type": "AWS::AutoScaling::LaunchConfiguration",
      "Properties": {
        "ImageId": "ami-xxxxxxxxxxxxx",  // Replace with your AMI ID
        "InstanceType": "t2.micro",
        "KeyName": "my-keypair",         // Replace with your Key Pair name
        "UserData": "#!/bin/bash\n\necho \"Hello from UserData!\"",
        "SecurityGroups": ["sg-xxxxxxxx"],  // Replace with your Security Group ID
        "IamInstanceProfile": "your-instance-profile"  // Replace with your IAM instance profile ARN
      }
    },
    "MyAutoScalingGroup": {
      "Type": "AWS::AutoScaling::AutoScalingGroup",
      "Properties": {
        "LaunchConfigurationName": { "Ref": "MyLaunchConfiguration" },
        "MinSize": 1,
        "MaxSize": 3,
        "DesiredCapacity": 2,
        "AvailabilityZones": ["us-east-1a"],  // Replace with your desired availability zones
        "LoadBalancerNames": [{ "Ref": "MyElasticLoadBalancer" }],
        "HealthCheckType": "ELB",
        "HealthCheckGracePeriod": 300
      }
    },
    "MyElasticLoadBalancer": {
      "Type": "AWS::ElasticLoadBalancing::LoadBalancer",
      "Properties": {
        "AvailabilityZones": ["us-east-1a"],  // Replace with your desired availability zones
        "Listeners": [
          {
            "LoadBalancerPort": "80",
            "InstancePort": "80",
            "Protocol": "HTTP"
          }
        ],
        "HealthCheck": {
          "Target": "HTTP:80/",
          "HealthyThreshold": "3",
          "UnhealthyThreshold": "5",
          "Interval": "30",
          "Timeout": "5"
        }
      }
    }
  }
}
```

Please replace the placeholder values with your actual details before deploying the CloudFormation templates.
