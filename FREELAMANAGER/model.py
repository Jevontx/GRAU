from datetime import datetime, timedelta
import json, os

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "freelancers.json")

class Freelancer:
    def __init__(self, id, nome, idade, categoria, cargo, valor_hora, disponibilidade=True, fornecedor=None):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.categoria = categoria
        self.cargo = cargo
        self.valor_hora = float(valor_hora)
        self.disponibilidade = disponibilidade
        self.fornecedor = fornecedor  # field kept for compatibility with original prompt

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "categoria": self.categoria,
            "cargo": self.cargo,
            "valor_hora": self.valor_hora,
            "disponibilidade": self.disponibilidade,
            "fornecedor": self.fornecedor
        }

    @staticmethod
    def from_dict(d):
        return Freelancer(
            id=d["id"],
            nome=d["nome"],
            idade=d.get("idade"),
            categoria=d.get("categoria"),
            cargo=d.get("cargo"),
            valor_hora=d.get("valor_hora", 0),
            disponibilidade=d.get("disponibilidade", True),
            fornecedor=d.get("fornecedor")
        )

class GerenciadorFreelancers:
    def __init__(self, data_file=DATA_FILE):
        self.data_file = data_file
        self.freelancers = []
        self._load()

    def _load(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r", encoding="utf-8") as f:
                    arr = json.load(f)
                    self.freelancers = [Freelancer.from_dict(x) for x in arr]
            except Exception:
                self.freelancers = []
        else:
            self.freelancers = []
            self._save()

    def _save(self):
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump([f_.to_dict() for f_ in self.freelancers], f, indent=2, ensure_ascii=False)

    def add(self, freelancer: Freelancer):
        # ensure unique id
        if any(f_.id == freelancer.id for f_ in self.freelancers):
            raise ValueError("ID já existe")
        self.freelancers.append(freelancer)
        self._save()

    def remove(self, id):
        self.freelancers = [f for f in self.freelancers if f.id != id]
        self._save()

    def list_all(self):
        return list(self.freelancers)

    def find_by_id(self, id):
        for f in self.freelancers:
            if f.id == id:
                return f
        return None

    def search(self, term):
        term_low = term.lower()
        return [f for f in self.freelancers if term_low in f.nome.lower() or term_low in f.categoria.lower()]

    def set_availability(self, id, disponibilidade: bool):
        f = self.find_by_id(id)
        if f:
            f.disponibilidade = disponibilidade
            self._save()
            return True
        return False
