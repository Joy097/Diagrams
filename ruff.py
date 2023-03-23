from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2

with Diagram("Example Diagram") as diag:
    with Cluster("Example Cluster", graph_attr={"pos": "10,10!"}, subgraph_attr={"pos": "5,5!"}):
        ec2 = EC2("Example EC2 Instance")