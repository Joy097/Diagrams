from diagrams import Cluster, Diagram
from shapes import Shape

# Define a custom shape
class CustomShape(Shape):
    _shape = "custom_shape"
    _template = "<rect x='0' y='0' width='100' height='50' rx='10' ry='10' />"

# Create a diagram
with Diagram("My Diagram") as diag:
    # Create a cluster
    with Cluster("My Cluster", shape=CustomShape()):
        # Add objects inside the cluster
        object1 = diag.add("Object 1")
        object2 = diag.add("Object 2")

