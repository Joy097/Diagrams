from diagrams import Cluster, Diagram
from diagrams.aws.database import Redshift
from diagrams.aws.integration import SQS
from diagrams.aws.storage import S3
from diagrams.custom import Custom



loadBalancer = "logos/lb.png" 
external = "logos/external.png"
apiGateway = "logos/apiG.png"
IDM = "logos/IDM.png"
LAN = "logos/LAN.png"
srvc = "logos/services.png"






with Diagram("Neir and Open-api Architecture", show=True):
    
    with Cluster("External Network"):
        ex_clnt = [Custom("BTRC",external),
                   Custom("SSL-COMMERZ",external)]
        
    

    with Cluster("Internal Network"):
        
        with Cluster("Load balancer"):
            lb = Custom("172.16.254.26\n(gzvldopenapi02)",loadBalancer)
        
        with Cluster("IDM"):
            idm = [ Custom("172.16.254.25:8080\n(gzvldopenapi01)",IDM),
                    Custom("172.16.254.52:8080\n(gzvlam01)",IDM)]
            
        with Cluster("API Gateway"):
            apiG = Custom("172.16.254.122\n(veonapi)",apiGateway)
            apiG1 = Custom("172.16.254.25\n(gzvldopenapi01)",apiGateway)
            apiG2 = Custom("172.16.254.52\n(gzvlam01)",apiGateway)

        with Cluster("LAN"):
            lan1 = Custom("172.16.7.90\n(gzvlapihdev02)",LAN)
            lan2 = Custom("172.16.7.90\n(gzvllopenapi01)",LAN)
            lan3 = Custom("172.16.7.90\n(gzvllopenapi02)",LAN)
            lan4 = Custom("172.16.7.90\n(gzvlapihub15)",LAN)
            
        with Cluster("Business Layer"):
            bl1 =  Custom("Identity-Register(N)",srvc)
            bl2 =  Custom("CMS(OA)",srvc)
            bl3 =  Custom("LMS(OA)",srvc)
            bl4 =  Custom("IRIS(OA)",srvc)
            
        
        with Cluster("Integration Layer(AH & BTRC)"):
            ew1 =   Custom("BTRC",srvc)
            ew2 =   Custom("EIR",srvc)
            ew3 =   Custom("Customer-Information",srvc)
            ew4 =   Custom("IRIS",srvc)
            ew5 =   Custom("CMS2",srvc)
            ew6 =   Custom("LMS2",srvc)


                

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