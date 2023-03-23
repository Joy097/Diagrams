from diagrams import Diagram, Cluster
from diagrams.utils import save
from diagrams.aws.compute import EC2


with Diagram("Example Diagram"):
    with Cluster("Example Cluster", graph_attr={"pos": "10,10!"}):
        ec2 = EC2("Example EC2 Instance")
    save("example-diagram.svg")
