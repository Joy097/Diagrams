from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS, EKS, Lambda
from diagrams.aws.database import Redshift
from diagrams.aws.integration import SQS
from diagrams.aws.storage import S3

with Diagram("Neir and Open-api Architecture", show=True):
    
    with Cluster("External Network"):
        ex_clnt = [ECS("BTRC"),
                   ECS("SSL-COMMERZ")]
        
    

    with Cluster("Internal Network"):
        
        with Cluster("Load balancer"):
            lb = EKS("172.16.254.26\n(gzvldopenapi02)")
        
        with Cluster("IDM"):
            idm = [ ECS("172.16.254.25:8080\n(gzvldopenapi01)"),
                    ECS("172.16.254.52:8080\n(gzvlam01)")]

        
    

    ex_clnt >> lb >> idm