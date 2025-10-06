from model import GerenciadorFreelancers, Freelancer

manager = GerenciadorFreelancers()

def cadastrar_freelancer(data):
    # data: dict with fields id, nome, idade, categoria, cargo, valor_hora, disponibilidade, fornecedor
    f = Freelancer(
        id=str(data.get("id")),
        nome=data.get("nome"),
        idade=data.get("idade"),
        categoria=data.get("categoria"),
        cargo=data.get("cargo"),
        valor_hora=data.get("valor_hora", 0),
        disponibilidade=(data.get("disponibilidade") in [True, "True", "true", "on", "1"]),
        fornecedor=data.get("fornecedor")
    )
    manager.add(f)
    return f

def listar():
    return manager.list_all()

def buscar(term):
    return manager.search(term)

def remover(id):
    manager.remove(id)

def ocupar(id):
    return manager.set_availability(id, False)

def liberar(id):
    return manager.set_availability(id, True)
