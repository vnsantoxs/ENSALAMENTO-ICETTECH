from django.db import models
from Professor.models import Professor
from Disciplina.models import Disciplina
from EspacoFisico.models import EspacoFisico


class Alocacao(models.Model):
    id_alocacao = models.AutoField(primary_key=True)
    dia_semana = models.CharField(max_length=15)
    horario_alocacao = models.IntegerField()
    disciplina = models.ForeignKey(Disciplina,on_delete=models.CASCADE)
    espaco_fisico = models.ForeignKey(EspacoFisico, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    @staticmethod
    def cadastrar_Alocacao(dia_semana, horario_alocacao, disciplina, professor):
        try:
            Alocacao.objects.get(dia_semana=dia_semana, horario_alocacao=horario_alocacao,
                                 disciplina=disciplina, professor=professor)
            return False
        except Alocacao.DoesNotExist:
            alocacao = Alocacao(dia_semana=dia_semana, horario_alocacao=horario_alocacao,
                                disciplina=disciplina, professor=professor)
            alocacao.save()
            return True
        except Exception:
            return False

    @staticmethod
    def excluir_Alocacao(id_alocacao):
        try:
            alocacao = Alocacao.objects.get(id_alocacao=id_alocacao)
            alocacao.delete()
            return True
        except Alocacao.DoesNotExist:
            return False
        except Exception:
            return False

    @staticmethod
    def alterar_Alocacao(id_alocacao, dia_semana, horario_alocacao, disciplina, professor, espaco_fisico):
        try:
            alocacao = Alocacao.objects.get(id_alocacao=id_alocacao)
            alocacao.dia_semana = dia_semana
            alocacao.horario_alocacao = horario_alocacao
            alocacao.disciplina = disciplina
            alocacao.professor = professor
            alocacao.espaco_fisico = espaco_fisico
            alocacao.save()
            return True
        except Exception:
            return False

    @staticmethod
    def consultar_Alocacao(id_alocacao):
        try:
            alocacao = Alocacao.objects.get(id_alocacao=id_alocacao)
            return True, alocacao
        except Alocacao.DoesNotExist:
            return False, None
        except Exception:
            return False, None

    @staticmethod
    def verificarTipoEspacoFisico(id_espaco_fisico):
        try:
            alocacao = Alocacao.objects.get(espaco_fisico=id_espaco_fisico)
            if(alocacao.espaco_fisico.tipo_espaco_fisico == "Laboratorio"):
                return True
            else:
                return False
        except Alocacao.DoesNotExist:
            return False
        except Exception:
            return False
        
    @staticmethod
    def estadoEspacoFisico(espaco_fisico, horario):
        try:
            Alocacao.objects.get(espaco_fisico=espaco_fisico, horario_alocacao=horario)
            return False
        except Alocacao.DoesNotExist:
            return True
        except Exception:
            return False

    @staticmethod
    def verificarComorbidade(id_professor):
        try:
            professor = Alocacao.objects.get(professor=id_professor)
            return True
        except Professor.DoesNotExist:
            return False
        except Exception:
            return False

    @staticmethod
    def verificarPeriodo(id_disciplina):
        try:
            disciplina = Alocacao.objects.get(disciplina=id_disciplina)
            if disciplina.disciplina.periodo_disciplina == 1:
                return True
            else:
                return False
        except Alocacao.DoesNotExist:
            return False
        except Exception:
            return False


    @staticmethod
    def alocacao_espacos_fisicos(Times):
        alocacoes = Alocacao.objects.all()
        espacos = EspacoFisico.objects.all()
        for time in Times:
            for alocacao in alocacoes:
                for espaco in espacos:
                    if (alocacao.verificarComorbidade(alocacao.professor)):
                        if ((alocacao.espaco_fisico.andar) == 1):
                            if not(alocacao.estadoEspacoFisico(espaco_fisico=espaco, horario=time)):
                                alocacao.espaco_fisico = espaco
                        elif ((alocacao.disciplina.periodo_disciplina) == 1):
                            if (alocacao.consultar_Alocacao(alocacao.id_alocacao)):
                                if not(alocacao.estadoEspacoFisico(espaco_fisico=espaco, horario=time)):
                                    alocacao.espaco_fisico = espaco
                        else:
                            if not(alocacao.estadoEspacoFisico(espaco_fisico=espaco, horario=time)):
                                alocacao.espaco_fisico = espaco
                alocacao.save()