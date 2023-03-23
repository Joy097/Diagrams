from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2


with Diagram("Example Diagram"):
    with Cluster("Example Cluster"):
        ec2 = EC2("Example EC2 Instance",node_attr="pos=\"100,10!\"")
    


