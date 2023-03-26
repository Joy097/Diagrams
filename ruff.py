from diagrams import Cluster, Diagram, Edge
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
            

    ex_clnt >> lb >>Edge(label="IDM(Keycloak)")>> idm


