# content_structure.py

class ContentStructure:
    def __init__(self, title):
        self.title = title

    def generate_review_template(self):
        return {
            "title": self.title,
            "sections": [
                "Visão geral",
                "Prós e contras",
                "Preços",
                "Experiência do usuário",
                "Segurança",
                "Conclusão"
            ]
        }

    def generate_comparison_template(self):
        return {
            "title": self.title,
            "sections": [
                "Resumo",
                "Tabela comparativa",
                "Diferenças principais",
                "Qual escolher",
                "Conclusão"
            ]
        }


if __name__ == "__main__":
    content = ContentStructure("Comparativo de Plataformas")
    print(content.generate_comparison_template())
