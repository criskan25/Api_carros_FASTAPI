from pydantic import BaseModel
from fastapi import FastAPI, HTTPException


app = FastAPI()
class Carro(BaseModel):
    id: int
    marca: str
    modelo: str
    año: int

class CarroUpdate(BaseModel):
    marca: str
    modelo: str
    año: int

CARROS = [
    {"id": 1, "marca": "Toyota", "modelo": "Corolla", "año": 2020},
    {"id": 2, "marca": "Honda", "modelo": "Civic", "año": 2019},
    {"id": 3, "marca": "Ford", "modelo": "Mustang", "año": 2021},
]

# Este endpoint te trae la lista de carros
@app.get("/carros")
def get_carros():
    return CARROS


# trae un carro segun el id
@app.get("/carros/{carro_id}")
def get_carro(carro_id):
    for carro in CARROS: 

        if int(carro_id) == int(carro["id"]):
            print("coincide")
            return carro 

    return {"error": "Carro no encontrado"}
#enpoint para agregar un carro
@app.post("/carros")
def crear_carro(carro: Carro):
    nuevo_carro = carro.model_dump()
    CARROS.append(nuevo_carro)
    return {"carro": nuevo_carro, "message": "Carro agregado exitosamente"}

#enpoint para reeplazar los datos de un carro
@app.put("/carros/{carro_id}")
def actualizar_carro(carro_id: int, carro: Carro):
    for i, c in enumerate(CARROS):
        if int(carro_id) == int(c["id"]):
            CARROS[i] = carro.model_dump()
            return {"carro": CARROS[i], "message": "Carro actualizado exitosamente"}
    return {"error": "Carro no encontrado"}


#endpoint para actualizar parcialmente los datos de un carro
@app.patch("/carros/{carro_id}") 
def modificar_carro(carro_id: int, carro: CarroUpdate):
    for i, c in enumerate(CARROS):
        if int(carro_id) == int(c["id"]):
            CARROS[i].update(carro.model_dump(exclude_unset=True))
            
            return {"carro": CARROS[i], "message": "Carro modificado exitosamente"}
    return {"error": "Carro no encontrado"}


#endpoint para eliminar un carro
@app.delete("/carros/{carro_id}")
def eliminar_carro(carro_id: int):
    for i, c in enumerate(CARROS):
        if int(carro_id) == int(c["id"]):
            del CARROS[i]
            return {"message": "Carro eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Carro no encontrado")




# Run the application using Uvicorn
if __name__ == "__main__":
    import uvicorn
    print("Empezando el servidor putacation...")
    uvicorn.run("main:app", host="127.0.0.1", port=8900, reload=True)

