from django.db import models


# Create your models here.

class Professor(models.Model):
    id_professor = models.IntegerField(primary_key=True)
    nome_professor = models.CharField(max_length=60)
    email_professor = models.EmailField()
    senha_professor = models.CharField(max_length=20)
    siape_professor = models.CharField(max_length=8)
    area_atuacao_professor = models.CharField(max_length=15)
    comorbidade = models.BooleanField()
    estado_professor = models.BooleanField()

    @staticmethod
    def cadastrar_Professor(id_professor, nome_professor, email_professor, senha_professor, siape_professor,
                            area_atuacao_professor, comorbidade, estado_professor):
        try:
            Professor.objects.get(id_professor=id_professor, nome_professor=nome_professor,
                                  email_professor=email_professor, senha_professor=senha_professor,
                                  siape_professor=siape_professor, area_atuacao_professor=area_atuacao_professor,
                                  comorbidade=comorbidade, estado_professor=estado_professor)
            return False
        except Professor.DoesNotExist:
            professor = Professor(id_professor=id_professor, nome_professor=nome_professor,
                                  email_professor=email_professor, senha_professor=senha_professor,
                                  siape_professor=siape_professor, area_atuacao_professor=area_atuacao_professor,
                                  comorbidade=comorbidade, estado_professor=estado_professor)
            professor.save()
            return True
        except Exception:
            return False

    @staticmethod
    def excluir_professor(id_professor):
        try:
            professor = Professor.objects.get(id_professor=id_professor)
            professor.delete()
            return True
        except Professor.DoesNotExist:
            return False
        except:
            return False

    @staticmethod
    def consultar_professor(id_professor):
        try:
            professor = Professor.objects.get(id_professor=id_professor)
            return True, professor
        except Professor.DoesNotExist:
            return False

    @staticmethod
    def alterar_professor(id_professor, nome_professor, email_professor, senha_professor, siape_professor,
                          area_atuacao_professor, comorbidade, estado_professor):
        try:
            professor = Professor.objects.get(id_professor=id_professor, nome_professor=nome_professor,
                                              email_professor=email_professor, senha_professor=senha_professor,
                                              siape_professor=siape_professor,
                                              area_atuacao_professor=area_atuacao_professor, comorbidade=comorbidade,
                                              estado_professor=estado_professor)
            professor.nome_professor = nome_professor
            professor.email_professor = email_professor
            professor.senha_professor = senha_professor
            professor.siape_professor = siape_professor
            professor.area_atuacao_professor = area_atuacao_professor
            professor.comorbidade = comorbidade
            professor.estado_professor = estado_professor
            professor.save()
        except Professor.DoesNotExist:
            return False
        except:
            return False

    @staticmethod
    def coletar_id_professor(siape_professor):
        try:
            professor = Professor.objects.get(siape_professor)
            return professor.id_professor
        except Professor.DoesNotExist:
            return False
        except:
            return False
        
    def loginprofessor(siape, senha):
        try:
            professor = Professor.objects.get(siape_professor = siape, senha_professor = senha)
            if professor:
                return True
        except:
            return False
