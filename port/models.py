from django.db import models

#ポートフォリオに登録される銘柄の基本情報
class Security(models.Model):
    des = models.CharField(max_length=200)
    asset = models.CharField(max_length=200,null=True)
    price = models.CharField(max_length=200,null=True)
    position = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.des


#Securityクラスと関係する、企業の詳細情報.ForeignKeyはnameとし、SecurityのidとDescriptionのname_idが対応する
class Description(models.Model):
    name = models.ForeignKey(Security,on_delete=models.CASCADE,null=True)
    sector = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=225, null=True)
    business = models.CharField(max_length=225, null=True)

    def __str__(self):
        return str(self.name)
