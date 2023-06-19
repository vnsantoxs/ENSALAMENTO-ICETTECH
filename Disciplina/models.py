from django.db import models

class Disciplina(models.Model):
    id_disciplina = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=6)
    nome_disciplina = models.CharField(max_length=20)
    periodo_disciplina = models.IntegerField()
    tipo_disciplina = models.PositiveBigIntegerField()

    @staticmethod
    def cadastrarDisciplina(codigo, nome_disciplina, periodo_disciplina):
        try:
            disciplina = Disciplina(
                codigo=codigo,
                nome_disciplina=nome_disciplina,
                periodo_disciplina=periodo_disciplina
            )
            disciplina.save()
            return True
        except Exception:
            return False

    @staticmethod
    def excluirDisciplina(id_disciplina):
        try:
            disciplina = Disciplina.objects.get(id_disciplina=id_disciplina)
            disciplina.delete()
            return True
        except Disciplina.DoesNotExist:
            return False
        except:
            return False

    @staticmethod
    def alterarDisciplina(id_disciplina, new_codigo, new_nome_disciplina, new_periodo_disciplina):
        try:
            disciplina = Disciplina.objects.get(id_disciplina=id_disciplina)
            disciplina.codigo = new_codigo
            disciplina.nome_disciplina = new_nome_disciplina
            disciplina.periodo_disciplina = new_periodo_disciplina
            disciplina.save()
            return True
        except Disciplina.DoesNotExist:
            return False
        except Exception:
            return False

    @staticmethod
    def consultarDisciplina(id_disciplina):
        try:
            disciplina = Disciplina.objects.get(id_disciplina=id_disciplina)
            return True, disciplina
        except Disciplina.DoesNotExist:
            return False, None

