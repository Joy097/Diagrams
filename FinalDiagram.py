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
            
        with Cluster("API Gateway"):
            with Group("APG"):
                apiG = ECS("172.16.254.122\n(veonapi)")
                apiG1 = ECS("172.16.254.25\n(gzvldopenapi01)")
                apiG2 = ECS("172.16.254.52\n(gzvlam01)")

        with Cluster("LAN"):
            lan1 = Lambda("172.16.7.90(gzvlapihdev02)")
            lan2 = Lambda("172.16.7.90(gzvllopenapi01)")
            lan3 = Lambda("172.16.7.90(gzvllopenapi02)")
            lan4 = Lambda("172.16.7.90(gzvlapihub15)")

            

        
    

    ex_clnt >> lb >> idm
    lb >> apiG