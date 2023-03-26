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
    "fontsize":"40",
    "fontweight":"bold"
}
graph_in={
    "fontsize":"45"
}
graph_font={
    "fontsize":"20"
}


with Diagram("Neir and Open-api Architecture", show=True,graph_attr=graph_attr):
    
    with Cluster("External Network",graph_attr={"fontsize":"30", "align": "center"}):
        ex_clnt = [Custom("BTRC",external,fontsize="18px"),
                   Custom("SSL-COMMERZ",external,fontsize="18px")]
        
    

    with Cluster("Internal Network",graph_attr=graph_in):
        
        with Cluster("Load balancer",graph_attr=graph_font):
            lb = Custom("172.16.254.26\n(gzvldopenapi02)",loadBalancer,fontsize="18px")
        
        with Cluster("IDM",graph_attr={"fontsize":"20","height":"500"}):
            with Cluster('gzvldopenapi01',graph_attr=graph_font):
                idm1 = Custom("\n172.16.254.25\n:8080",IDM,fontsize="18px")
            with Cluster('gzvlam01',graph_attr=graph_font):
                idm2 = Custom("\n172.16.254.52\n:8080",IDM,fontsize="18px")
            
            
        with Cluster("API Gateway",graph_attr=graph_font):
            with Cluster('veonapi',graph_attr=graph_font):
                apiG = Custom("\n172.16.254.122",apiGateway,fontsize="18px")
            with Cluster('gzvldopenapi01',graph_attr=graph_font):
                apiG1 = Custom("\n172.16.254.25",apiGateway,fontsize="18px")
            with Cluster('gzvlam01',graph_attr=graph_font):
                apiG2 = Custom("\n172.16.254.52",apiGateway,fontsize="18px")


        with Cluster("LAN",graph_attr=graph_font):
            with Cluster('gzvlapihdev02',graph_attr=graph_font):
                lan1 = Custom("\n172.16.7.90",LAN,fontsize="18px")
            with Cluster('gzvllopenapi01',graph_attr=graph_font):
                lan2 = Custom("\n172.16.7.90",LAN,fontsize="18px")
            with Cluster('gzvllopenapi02',graph_attr=graph_font):
                lan3 = Custom("\n172.16.7.90",LAN,fontsize="18px")
            with Cluster('gzvlapihub15',graph_attr=graph_font):
                lan4 = Custom("\n172.16.7.90",LAN,fontsize="18px")
           
            
        with Cluster("Business Layer",graph_attr=graph_font):
            with Cluster('Identity-Register(N)',graph_attr=graph_font):
                bl1 = Custom("",srvc,fontsize="18px")
            with Cluster('CMS(OA)',graph_attr=graph_font):
                bl2 = Custom("",srvc,fontsize="18px")
            with Cluster('LMS(OA)',graph_attr=graph_font):
                bl3 = Custom("",srvc,fontsize="18px")
            with Cluster('IRIS(OA)',graph_attr=graph_font):
                bl4 = Custom("",srvc,fontsize="18px")
                
        
        
        with Cluster("Integration Layer(AH & BTRC)",graph_attr=graph_font):
            with Cluster('BTRC',graph_attr=graph_font):
                ew1 = Custom("",srvc)
            with Cluster('EIR',graph_attr=graph_font):
                ew2 = Custom("",srvc)
            with Cluster('Customer-Information',graph_attr=graph_font):
                ew3 = Custom("",srvc)
            with Cluster('IRIS',graph_attr=graph_font):
                ew4 = Custom("",srvc)
            with Cluster('CMS2',graph_attr=graph_font):
                ew5 = Custom("",srvc)
            with Cluster('LMS2',graph_attr=graph_font):
                ew6 = Custom("",srvc)
                
            


                

    #ex_clnt >> lb >>Edge(label="IDM(Keycloak)",fontsize="18px")>> idm
    ex_clnt >> lb >>Edge(label="IDM(Keycloak)",fontsize="18px")>> idm1
    lb >>Edge(label="IDM(Keycloak)",fontsize="18px")>>idm2
    lb >> Edge(fontsize="18px")>> apiG >> lan1
    lb >> Edge(fontsize="18px")>> apiG1
    lb >> Edge(fontsize="18px")>> apiG2 >> lan4
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
    
    #to bring IDM in front
    
   
    idm2 - Edge(color="transparent") - apiG1