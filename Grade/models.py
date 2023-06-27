from django.db import models


class Grade(models.Model):
    id_grade = models.AutoField(primary_key=True)
    ano = models.IntegerField(null=False)
    versao = models.CharField(max_length=12)
    codigo = models.CharField(max_length=6)

    @staticmethod
    def cadastrarGrade(ano, versao, codigo):
        try:
            grade = Grade(ano=ano, versao=versao, codigo=codigo)
            grade.save()
            return True
        except Exception:
            return False

    @staticmethod
    def excluirGrade(id_grade):
        try:
            grade = Grade.objects.get(id_grade=id_grade)
            grade.delete()
            return True
        except Grade.DoesNotExist:
            return False
        except:
            return False

    @staticmethod
    def alterarGrade(id_grade, ano, versao, codigo):
        try:
            grade = Grade.objects.get(id_grade=id_grade)
            grade.ano = ano
            grade.versao = versao
            grade.codigo = codigo
            grade.save()
            return True
        except Grade.DoesNotExist:
            return False
        except Exception:
            return False

    @staticmethod
    def consultarGrade(id_grade):
        try:
            grade = Grade.objects.get(id_grade=id_grade)
            return True, grade
        except Grade.DoesNotExist:
            return False
