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
            source = EKS("172.16.254.26(gzvldopenapi02)")
        
        with Cluster("IDM"):
            workers = [ECS("worker1"),
                       ECS("worker2"),
                       ECS("worker3")]

        with Cluster("API Gateway"):
            workers = [ECS("worker1"),
                       ECS("worker2"),
                       ECS("worker3")]

        with Cluster("LAN"):
            handlers = [Lambda("proc1"),
                        Lambda("proc2"),
                        Lambda("proc3")]
            
        with Cluster("Business Layer"):
            workers = [ECS("worker1"),
                    ECS("worker2"),
                    ECS("worker3")]
            
        with Cluster("Event Workers"):
            workers = [ECS("worker1"),
                       ECS("worker2"),
                       ECS("worker3")]

    

    ex_clnt >> source >> workers >> handlers