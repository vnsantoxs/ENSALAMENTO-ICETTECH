from django.db import models
from django.contrib.auth.models import AbstractUser

class Administrador(models.Model):
    id_administrador = models.AutoField(primary_key=True)
    nome_administrador = models.CharField(max_length=60)
    email_administrador = models.EmailField()
    telefone_administrador = models.TextField(max_length=20)
    senha_administrador = models.CharField(max_length=20)
    siape_administrador = models.CharField(max_length=7)
    cargo_administrador = models.CharField(max_length=15)
    comorbidade_administrador = models.BooleanField()
    estado_administrador = models.BooleanField()

    @staticmethod
    def cadastrar_Administrador(nome_administrador, telefone_administrador, email_administrador,
                                senha_administrador, siape_administrador, cargo_administrador,
                                comorbidade_administrador, estado_administrador):
        try:
            Administrador.objects.get(nome_administrador=nome_administrador,
                                      telefone_administrador=telefone_administrador,
                                      email_administrador=email_administrador, senha_administrador=senha_administrador,
                                      siape_administrador=siape_administrador, cargo_administrador=cargo_administrador,
                                      comorbidade_administrador=comorbidade_administrador)
            return False
        except:
            administrador = Administrador(nome_administrador=nome_administrador,
                                          telefone_administrador=telefone_administrador,
                                          email_administrador=email_administrador,
                                          senha_administrador=senha_administrador,
                                          siape_administrador=siape_administrador,
                                          cargo_administrador=cargo_administrador,
                                          comorbidade_administrador=comorbidade_administrador,
                                          estado_administrador=estado_administrador)
            administrador.save()
            return True

    @staticmethod
    def excluir_Administrador(id_administrador):
        try:
            administrador = Administrador.objects.get(id_administrador=id_administrador)
            administrador.delete()
            return True
        except Administrador.DoesNotExist:
            return False
        except:
            return False

    @staticmethod
    def consultar_Administrador(id_administrador):
        try:
            administrador = Administrador.objects.get(id_administrador=id_administrador)
            return True, administrador
        except Administrador.DoesNotExist:
            return False

    @staticmethod
    def alterar_Administrador(id_administrador, nome_administrador, email_administrador, senha_administrador,
                              siape_administrador, cargo_administrador, comorbidade_administrador,
                              estado_administrador):
        try:
            administrador = Administrador.objects.get(id_administrador)
            administrador.nome_administrador = nome_administrador
            administrador.email_administrador = email_administrador
            administrador.senha_administrador = senha_administrador
            administrador.siape_administrador = siape_administrador
            administrador.cargo_administrador = cargo_administrador
            administrador.comorbidade_administrador = comorbidade_administrador
            administrador.estado_administrador = estado_administrador
            administrador.save()
            return True
        except Administrador.DoesNotExist:
            return False
        except:
            return False

    @staticmethod
    def coletar_id_Administrador(siape_administrador):
        try:
            administrador = Administrador.objects.get(siape_administrador)
            return administrador.id_administrador
        except Administrador.DoesNotExist:
            return False
        except:
            return False
        
    def loginadmin(siape, senha):
        try:
            administrador = Administrador.objects.get(siape_administrador = siape, senha_administrador = senha)
            if administrador:
                return True
        except:
            return False

