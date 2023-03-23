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


graph_attr={
    "margin-up": "600px",
    "fontsize":"40",
    "fontweight":"bold"
}
graph_in={
    "pos":"150,10!",
    "fontsize":"25"
}
graph_ex={
    "fontsize":"30",
    "width":"450px",
    }
graph_font={
    "pos":"10,10!",
    "fontsize":"20",
}
graph_font1={
    "fontsize":"15"
}

with Diagram("Neir and Open-api Architecture", show=True,graph_attr=graph_attr):
    
    with Cluster("External Network",graph_attr=graph_ex,graph_attr={"pos":"10,10!"}):
        ex_clnt = [Custom("BTRC",external,fontsize="18px"),
                   Custom("SSL-COMMERZ",external,fontsize="18px")]
        
    

    with Cluster("Internal Network",graph_attr=graph_in):
        
        with Cluster("Load balancer",graph_attr=graph_font):
            lb = Custom("172.16.254.26\n(gzvldopenapi02)",loadBalancer,fontsize="18px")
        
        with Cluster("IDM",graph_attr=graph_font):
            idm = [ Custom("172.16.254.25:8080\n(gzvldopenapi01)",IDM,fontsize="18px"),
                    Custom("172.16.254.52:8080\n(gzvlam01)",IDM,fontsize="18px")]
            
        with Cluster("API Gateway",graph_attr=graph_font):
            apiG = Custom("172.16.254.122\n(veonapi)",apiGateway,fontsize="18px")
            apiG1 = Custom("172.16.254.25\n(gzvldopenapi01)",apiGateway,fontsize="18px")
            apiG2 = Custom("172.16.254.52\n(gzvlam01)",apiGateway,fontsize="18px")

        with Cluster("LAN",graph_attr=graph_font):
            lan1 = Custom("172.16.7.90\n(gzvlapihdev02)",LAN,fontsize="18px")
            lan2 = Custom("172.16.7.90\n(gzvllopenapi01)",LAN,fontsize="18px")
            lan3 = Custom("172.16.7.90\n(gzvllopenapi02)",LAN,fontsize="18px")
            lan4 = Custom("172.16.7.90\n(gzvlapihub15)",LAN,fontsize="18px")
            
        with Cluster("Business Layer",graph_attr=graph_font):
            bl1 =  Custom("Identity-Register(N)",srvc,fontsize="18px")
            bl2 =  Custom("CMS(OA)",srvc,fontsize="18px")
            bl3 =  Custom("LMS(OA)",srvc,fontsize="18px")
            bl4 =  Custom("IRIS(OA)",srvc,fontsize="18px")
            
        
        with Cluster("Integration Layer(AH & BTRC)",graph_attr=graph_font):
            ew1 =   Custom("BTRC",srvc,fontsize="18px")
            ew2 =   Custom("EIR",srvc,fontsize="18px")
            ew3 =   Custom("Customer-Information",srvc,fontsize="18px")
            ew4 =   Custom("IRIS",srvc,fontsize="18px")
            ew5 =   Custom("CMS2",srvc,fontsize="18px")
            ew6 =   Custom("LMS2",srvc,fontsize="18px")


                

    ex_clnt >> lb >>Edge(label="IDM(Keycloak)",fontsize="18px")>> idm
    lb >> Edge(label="test",fontsize="18px")>> apiG >> lan1
    lb >> Edge(label="prod",fontsize="18px")>> apiG1
    lb >> Edge(label="pre-prod",fontsize="18px")>> apiG2 >> lan4
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