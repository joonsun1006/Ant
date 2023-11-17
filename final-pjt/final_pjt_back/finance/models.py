from django.db import models

# Create your models here.
class DepositAndSavings(models.Model):
    # 공시제출월
    dcls_month = models.CharField(max_length=30)
    # 금융 회사명
    kor_co_nm = models.CharField(max_length=50)
    # 상품명
    fin_prdt_nm = models.CharField(max_length=100)
    # 금융상품 코드
    fin_prdt_cd = models.TextField()
    # 가입 제한
    join_member = models.TextField()
    # 가입 방법
    join_way = models.TextField(null=True)
    # 우대 조건
    spcl_cnd = models.TextField()
    # 기타 유의사항
    etc_note = models.TextField()
    # 금리
    intr_rate_6 = models.FloatField(null=True)
    intr_rate_12 = models.FloatField(null=True)
    intr_rate_24 = models.FloatField(null=True)
    intr_rate_36 = models.FloatField(null=True)
    # 우대 금리
    intr_rate2_6 = models.FloatField(null=True)
    intr_rate2_12 = models.FloatField(null=True)
    intr_rate2_24 = models.FloatField(null=True)
    intr_rate2_36 = models.FloatField(null=True)
    # 저축 금리 유형
    intr_rate_type_nm = models.CharField(max_length=10, null=True)
    # 적금 최고 한도
    max_limit = models.IntegerField(null=True)
    # 예적금 타입 1 == 예금, 2 == 적금
    type = models.IntegerField()