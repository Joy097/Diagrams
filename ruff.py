from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import VPC

with Diagram("Example Diagram", show=False):
    with Cluster("VPC"):
        with Cluster("Private Subnet", label="Database Servers"):
            rds = RDS("Example RDS Instance")

        with Cluster("Public Subnet"):
            # ... add resources to public subnet cluster ...

        VPC("Example VPC") >> Cluster("Database Servers", group="databases") >> rds
