from django.db import models

# Create your models here.

class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=6)
    nome = models.CharField(max_length=30)

    @staticmethod
    def cadastrarCurso(codigo, nome):
        try:
            curso = Curso(codigo=codigo, nome=nome)
            curso.save()
            return True
        except Exception:
            return False

    @staticmethod
    def excluirCurso(id_curso):
        try:
            curso = Curso.objects.get(id_curso=id_curso)
            curso.delete()
            return True
        except Curso.DoesNotExist:
            return False
        except:
            return False

    @staticmethod
    def alterarCurso(id_curso, new_codigo, new_nome):
        try:
            curso = Curso.objects.get(id_curso=id_curso)
            curso.codigo = new_codigo
            curso.nome = new_nome
            curso.save()
            return True
        except Curso.DoesNotExist:
            return False
        except Exception:
            return False

    @staticmethod
    def consultarCurso(id_curso):
        try:
            curso = Curso.objects.get(id_curso=id_curso)
            return True, curso
        except Curso.DoesNotExist:
            return False, None
