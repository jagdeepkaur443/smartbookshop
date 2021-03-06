import matplotlib.pyplot as plt
import  base64
from io import BytesIO

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def plot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize = (10,5))
    plt.title('total copies of the particular book')
    plt.plot(x,y)
    plt.xticks(rotation=90)
    plt.xlabel('Book Name')
    plt.ylabel('No. of Copies')
    plt.grid(True)
    plt.tight_layout()
    graph = get_graph()
    return graph


def plot2(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize = (10,5))
    plt.title('Order for Books and Quantity')
    plt.plot(x,y)
    plt.xticks(rotation=90)
    plt.xlabel('Quantity')
    plt.ylabel('Order_Id')
    plt.grid(True)
    plt.tight_layout()
    graph = get_graph()
    return graph

def plot3(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize = (10,5))
    plt.title('Year of Publishing')
    plt.plot(x,y)
    plt.xticks(rotation=90)
    plt.xlabel('book_name')
    plt.ylabel('Published year of book')
    plt.grid(True)
    plt.tight_layout()
    graph = get_graph()
    return graph