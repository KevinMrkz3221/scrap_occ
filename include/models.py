class Vacante:
    def __init__(self, url, titulo,descripcion, categoria, subcategoria, educacion, company) -> None:
        self.url = url
        self.titulo = titulo
        self.descripcion = descripcion
        self.categoria = categoria
        self.subcategoria = subcategoria
        self.educacion = educacion
        self.company = company
        

    def to_record(self):
        return {
            'url': self.url,
            'titulo': self.titulo,
            'compañia': self.company,
            'descripcion': self.descripcion,
            'categoria': self.categoria,
            'sub-categoria': self.subcategoria,
            'educacion': self.educacion
        }