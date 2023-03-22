from diagrams import Cluster, Diagram

with Diagram("My Diagram") as diag:
    with Cluster("My Cluster", shape="box", bgcolor="gray"):
        # Define the interface
        interface = diag.add("Interface", shape="cylinder", style="dashed")
        
        # Add other objects inside the cluster
        object1 = diag.add("Object 1")
        object2 = diag.add("Object 2")

        # Link the interface to other objects
        interface >> object1
        interface >> object2
