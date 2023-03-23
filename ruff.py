from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB

with Diagram("Example Diagram"):

    with Cluster("Cluster 1"):
        ec2_1 = EC2("EC2 1")
        ec2_2 = EC2("EC2 2")

    with Cluster("Cluster 2"):
        elb = ELB("ELB")

    # Set color attribute of the edge to transparent
    ec2_1 >> elb >> ec2_2 << elb << ec2_1
    elb.color = "transparent"
