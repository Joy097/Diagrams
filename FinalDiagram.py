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
        
        source = EKS("k8s source")
        
        with Cluster("Event Workers"):
            workers = [ECS("worker1"),
                       ECS("worker2"),
                       ECS("worker3")]

        with Cluster("Event Workers"):
            workers = [ECS("worker1"),
                       ECS("worker2"),
                       ECS("worker3")]

        with Cluster("Processing"):
            handlers = [Lambda("proc1"),
                        Lambda("proc2"),
                        Lambda("proc3")]
            
        with Cluster("Event Workers"):
            workers = [ECS("worker1"),
                    ECS("worker2"),
                    ECS("worker3")]
            
        with Cluster("Event Workers"):
            workers = [ECS("worker1"),
                       ECS("worker2"),
                       ECS("worker3")]

    

    ex_clnt >> source >> workers >> handlers