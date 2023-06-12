from django.db import models


class EspacoFisico(models.Model):
    id_espaco_fisico = models.IntegerField(primary_key=True)
    tipo_espaco_fisico = models.CharField(max_length=15,)
    dimencoes = models.CharField(max_length=15)
    capacidade = models.IntegerField()
    bloco = models.CharField(max_length=15)
    andar = models.IntegerField()
    numero = models.IntegerField()

    @staticmethod
    def cadastrarEspacoFisico(tipo_espaco_fisico, dimensoes, capacidade, bloco, andar, numero):
        try:
            EspacoFisico.objects.get(tipo_espaco_fisico=tipo_espaco_fisico, dimensoes=dimensoes, capacidade=capacidade,
                                     bloco=bloco, andar=andar, numero=numero)
            return False
        except EspacoFisico.DoesNotExist:
            espaco_fisico = EspacoFisico(
                tipo_espaco_fisico=tipo_espaco_fisico,
                dimensoes=dimensoes,
                capacidade=capacidade,
                bloco=bloco,
                andar=andar,
                numero=numero
            )
            espaco_fisico.save()
            return True
        except Exception:
            return False

    @staticmethod
    def excluirEspacoFisico(id_espaco_fisico):
        try:
            espaco_fisico = EspacoFisico.objects.get(id_espaco_fisico=id_espaco_fisico)
            espaco_fisico.delete()
            return True
        except EspacoFisico.DoesNotExist:
            return False
        except:
            return False

    @staticmethod
    def alterarEspacoFisico(id_espaco_fisico, new_tipo, new_dimensoes, new_capacidade, new_bloco, new_andar, new_numero):
        try:
            espaco_fisico = EspacoFisico.objects.get(id_espaco_fisico=id_espaco_fisico)
            espaco_fisico.tipo_espaco_fisico = new_tipo
            espaco_fisico.dimensoes = new_dimensoes
            espaco_fisico.capacidade = new_capacidade
            espaco_fisico.bloco = new_bloco
            espaco_fisico.andar = new_andar
            espaco_fisico.numero = new_numero
            espaco_fisico.save()
            return True
        except EspacoFisico.DoesNotExist:
            return False
        except Exception:
            return False

    @staticmethod
    def consultarEspacoFisico(id_espaco_fisico):
        try:
            espaco_fisico = EspacoFisico.objects.get(id_espaco_fisico=id_espaco_fisico)
            return True, espaco_fisico
        except EspacoFisico.DoesNotExist:
            return False, None
