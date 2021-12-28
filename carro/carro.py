class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session

        carro = self.session.get("carro") # identifica el string con el carro

        if not carro: # si no hay carro, lo creamos
            carro = self.session["carro"]={}
        else: # si hay
            self.carro = carro

    # agregar productos al carro
    def agregar(self, producto):
        if(str(producto.id) not in self.carro.keys()) # si el producto no esta en el carro
            self.carro[producto.id]={
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio":str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url
            }
        else: # si ya esta, agregamos mas productos