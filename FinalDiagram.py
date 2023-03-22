from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS, EKS, Lambda
from diagrams.aws.database import Redshift
from diagrams.aws.integration import SQS
from diagrams.aws.storage import S3
from diagrams.custom import Custom


loadBalancer = "logos/lb.png" 
external = 



    



with Diagram("Neir and Open-api Architecture", show=True):
    
    with Cluster("External Network"):
        ex_clnt = [ECS("BTRC"),
                   ECS("SSL-COMMERZ")]
        
    

    with Cluster("Internal Network"):
        
        with Cluster("Load balancer"):
            lb = Custom("172.16.254.26\n(gzvldopenapi02)",loadBalancer)
        
        with Cluster("IDM"):
            idm = [ ECS("172.16.254.25:8080\n(gzvldopenapi01)"),
                    ECS("172.16.254.52:8080\n(gzvlam01)")]
            
        with Cluster("API Gateway"):
            apiG = ECS("172.16.254.122\n(veonapi)")
            apiG1 = ECS("172.16.254.25\n(gzvldopenapi01)")
            apiG2 = ECS("172.16.254.52\n(gzvlam01)")

        with Cluster("LAN"):
            lan1 = Lambda("172.16.7.90\n(gzvlapihdev02)")
            lan2 = Lambda("172.16.7.90\n(gzvllopenapi01)")
            lan3 = Lambda("172.16.7.90\n(gzvllopenapi02)")
            lan4 = Lambda("172.16.7.90\n(gzvlapihub15)")
            
        with Cluster("Business Layer"):
            bl1 =  ECS("Identity-Register(N)")
            bl2 =  ECS("CMS(OA)")
            bl3 =  ECS("LMS(OA)")
            bl4 =  ECS("IRIS(OA)")
            
        
        with Cluster("Integration Layer(AH & BTRC)"):
            ew1 =   ECS("BTRC")
            ew2 =   ECS("EIR")
            ew3 =   ECS("Customer-Information")
            ew4 =   ECS("IRIS")
            ew5 =   ECS("CMS2")
            ew6 =   ECS("LMS2")


                

    ex_clnt >> lb >> idm
    lb >> apiG >> lan1
    lb >> apiG1
    lb >> apiG2 >> lan4
    apiG1 >> lan2
    apiG1 >> lan3
    lan1 >> bl1
    lan2 >> bl2
    lan3 >> bl3
    lan4 >> bl4
    bl1 >> ew1
    bl2 >> ew3
    bl3 >> ew5
    bl4 >> ew6