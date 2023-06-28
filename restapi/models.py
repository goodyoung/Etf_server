# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BokInflation(models.Model):
    index = models.DateTimeField(blank=True, null=True)
    소비자물가 = models.FloatField(blank=True, null=True)
    농축수산물 = models.FloatField(blank=True, null=True)
    공업제품 = models.FloatField(blank=True, null=True)
    집세 = models.FloatField(blank=True, null=True)
    공공서비스 = models.FloatField(blank=True, null=True)
    개인서비스 = models.FloatField(blank=True, null=True)
    근원물가 = models.FloatField(blank=True, null=True)
    생활물가 = models.FloatField(blank=True, null=True)
    생산자물가 = models.FloatField(blank=True, null=True)
    농림수산품 = models.FloatField(blank=True, null=True)
    공산품 = models.FloatField(blank=True, null=True)
    전력가스및수도 = models.FloatField(blank=True, null=True)
    서비스 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bok_inflation'


class CompanyBase(models.Model):
    회사명 = models.TextField(blank=True, null=True)
    symbol = models.TextField(db_column='Symbol', blank=True, null=True)  # Field name made lowercase.
    업종 = models.TextField(blank=True, null=True)
    주요제품 = models.TextField(blank=True, null=True)
    상장일 = models.TextField(blank=True, null=True)
    결산월 = models.TextField(blank=True, null=True)
    대표자명 = models.TextField(blank=True, null=True)
    홈페이지 = models.TextField(blank=True, null=True)
    지역 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_base'


class CompanyStock(models.Model):
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    표준코드 = models.TextField(blank=True, null=True)
    symbol = models.TextField(db_column='Symbol', blank=True, null=True)  # Field name made lowercase.
    한글종목명 = models.TextField(blank=True, null=True)
    한글종목약명 = models.TextField(blank=True, null=True)
    영문종목명 = models.TextField(blank=True, null=True)
    상장일 = models.TextField(blank=True, null=True)
    시장구분 = models.TextField(blank=True, null=True)
    증권구분 = models.TextField(blank=True, null=True)
    소속부 = models.TextField(blank=True, null=True)
    주식종류 = models.TextField(blank=True, null=True)
    액면가 = models.TextField(blank=True, null=True)
    상장주식수 = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_stock'
        db_table_comment = '20230614: stock_base -> company_stock 변경\r\n202305    : 현재: 한국 주식 종목의 주식 기본 정보'


class CompanyUs(models.Model):
    idx = models.AutoField(primary_key=True)
    symbol = models.CharField(db_column='Symbol', max_length=10, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sector = models.CharField(db_column='Sector', max_length=200, blank=True, null=True)  # Field name made lowercase.
    industry = models.TextField(db_column='Industry', blank=True, null=True)  # Field name made lowercase.
    market = models.CharField(db_column='Market', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'company_us'


class Config(models.Model):
    corpinfo_fetch = models.DateField(blank=True, null=True)
    krxohlc_fetch = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'config'


class DbUpdates(models.Model):
    idx = models.AutoField(primary_key=True)
    table_name = models.CharField(max_length=45)
    current_update = models.DateTimeField(db_comment='테이블에 업데이트한 최종일')
    last_update = models.DateTimeField(blank=True, null=True)
    memo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'db_updates'
        db_table_comment = 'finance_db 에 업데이트한 이력'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EnergyPrices(models.Model):
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    brent = models.FloatField(db_column='Brent', blank=True, null=True)  # Field name made lowercase.
    wti = models.FloatField(db_column='WTI', blank=True, null=True)  # Field name made lowercase.
    gas = models.FloatField(db_column='GAS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'energy_prices'


class EtfDetails(models.Model):
    종목 = models.TextField(blank=True, null=True)
    종목명 = models.TextField(blank=True, null=True)
    영문명 = models.TextField(blank=True, null=True)
    표준코드 = models.TextField(blank=True, null=True)
    종목코드 = models.TextField(blank=True, null=True)
    상장일 = models.TextField(blank=True, null=True)
    펀드형태 = models.TextField(blank=True, null=True)
    기초지수명 = models.TextField(blank=True, null=True)
    추적배수 = models.TextField(blank=True, null=True)
    자산운용사 = models.TextField(blank=True, null=True)
    ap = models.TextField(db_column='AP', blank=True, null=True)  # Field name made lowercase.
    총보수 = models.TextField(blank=True, null=True)
    회계기간 = models.TextField(blank=True, null=True)
    과세유형 = models.TextField(blank=True, null=True)
    분배금지급 = models.TextField(blank=True, null=True)
    홈페이지 = models.TextField(blank=True, null=True)
    기본정보 = models.TextField(blank=True, null=True)
    투자유의사항 = models.TextField(blank=True, null=True)
    pay_class = models.TextField(db_column='PAY_CLASS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'etf_details'
        db_table_comment = 'kind.krx.co.kr / 상장종목현황 상세정보 파일. 2023/05/10 초기화'


class EtfProfitPayout(models.Model):
    month = models.TextField(db_column='MONTH', primary_key=True)  # Field name made lowercase. The composite primary key (MONTH, 종목코드) found, that is not supported. The first column is selected.
    종목코드 = models.CharField(max_length=8)
    yf코드 = models.CharField(max_length=10, blank=True, null=True)
    종목이름 = models.TextField(blank=True, null=True)
    지급기준일 = models.TextField(blank=True, null=True)
    지급예정일 = models.TextField(blank=True, null=True)
    분배금_원_field = models.SmallIntegerField(db_column='분배금(원)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    close = models.IntegerField(db_column='Close', blank=True, null=True)  # Field name made lowercase.
    mode = models.CharField(db_column='MODE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    dc_r = models.FloatField(db_column='DC_R', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'etf_profit_payout'
        unique_together = (('month', '종목코드'),)


class FinStatement(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    종목코드 = models.TextField(blank=True, null=True)
    매출액 = models.TextField(blank=True, null=True)
    영업이익 = models.TextField(blank=True, null=True)
    영업이익_발표기준_field = models.TextField(db_column='영업이익(발표기준)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    세전계속사업이익 = models.TextField(blank=True, null=True)
    당기순이익 = models.TextField(blank=True, null=True)
    당기순이익_지배_field = models.TextField(db_column='당기순이익(지배)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    당기순이익_비지배_field = models.TextField(db_column='당기순이익(비지배)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    자산총계 = models.TextField(blank=True, null=True)
    부채총계 = models.TextField(blank=True, null=True)
    자본총계 = models.TextField(blank=True, null=True)
    자본총계_지배_field = models.TextField(db_column='자본총계(지배)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    자본총계_비지배_field = models.TextField(db_column='자본총계(비지배)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    자본금 = models.TextField(blank=True, null=True)
    영업활동현금흐름 = models.TextField(blank=True, null=True)
    투자활동현금흐름 = models.TextField(blank=True, null=True)
    재무활동현금흐름 = models.TextField(blank=True, null=True)
    capex = models.TextField(db_column='CAPEX', blank=True, null=True)  # Field name made lowercase.
    fcf = models.TextField(db_column='FCF', blank=True, null=True)  # Field name made lowercase.
    이자발생부채 = models.TextField(blank=True, null=True)
    영업이익률 = models.TextField(blank=True, null=True)
    순이익률 = models.TextField(blank=True, null=True)
    roe_field = models.TextField(db_column='ROE(%)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    roa_field = models.TextField(db_column='ROA(%)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    부채비율 = models.TextField(blank=True, null=True)
    자본유보율 = models.TextField(blank=True, null=True)
    eps_원_field = models.TextField(db_column='EPS(원)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    per_배_field = models.TextField(db_column='PER(배)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    bps_원_field = models.TextField(db_column='BPS(원)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    pbr_배_field = models.TextField(db_column='PBR(배)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    현금dps_원_field = models.TextField(db_column='현금DPS(원)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    현금배당수익률 = models.TextField(blank=True, null=True)
    현금배당성향_field = models.TextField(db_column='현금배당성향(%)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    발행주식수_보통주_field = models.TextField(db_column='발행주식수(보통주)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    기준일 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_statement'


class ForeignKrw(models.Model):
    date = models.DateTimeField(db_column='Date', primary_key=True)  # Field name made lowercase.
    jpykrw_x = models.FloatField(db_column='JPYKRW=X', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    usdkrw_x = models.FloatField(db_column='USDKRW=X', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'foreign_krw'


class Kospi(models.Model):
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    open = models.FloatField(db_column='Open', blank=True, null=True)  # Field name made lowercase.
    high = models.FloatField(db_column='High', blank=True, null=True)  # Field name made lowercase.
    low = models.FloatField(db_column='Low', blank=True, null=True)  # Field name made lowercase.
    close = models.FloatField(db_column='Close', blank=True, null=True)  # Field name made lowercase.
    adj_close = models.FloatField(db_column='Adj Close', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    volume = models.FloatField(db_column='Volume', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kospi'


class KrWords(models.Model):
    idx = models.AutoField(primary_key=True)
    kind = models.CharField(max_length=25, db_comment='단어의 종류')
    words = models.TextField(db_comment='단어의 종류')
    current_update = models.DateTimeField(db_comment='테이블에 업데이트한 최종일')

    class Meta:
        managed = False
        db_table = 'kr_words'
        db_table_comment = '한글 단어 관련 데이터를 수집'


class KrxIndexStocks(models.Model):
    지수 = models.TextField(blank=True, null=True)
    기준일 = models.TextField(blank=True, null=True)
    종목코드 = models.TextField(blank=True, null=True)
    종목명 = models.TextField(blank=True, null=True)
    종가 = models.TextField(blank=True, null=True)
    대비 = models.TextField(blank=True, null=True)
    등락률 = models.TextField(blank=True, null=True)
    시가총액 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'krx_index_stocks'


class PricesEtfKr(models.Model):
    date = models.DateTimeField(db_column='Date', primary_key=True)  # Field name made lowercase. The composite primary key (Date, Symbol) found, that is not supported. The first column is selected.
    symbol = models.TextField(db_column='Symbol')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    close = models.BigIntegerField(db_column='Close', blank=True, null=True)  # Field name made lowercase.
    changes = models.BigIntegerField(db_column='Changes', blank=True, null=True)  # Field name made lowercase.
    changeratio = models.FloatField(db_column='ChangeRatio', blank=True, null=True)  # Field name made lowercase.
    nav = models.FloatField(db_column='Nav', blank=True, null=True)  # Field name made lowercase.
    open = models.BigIntegerField(db_column='Open', blank=True, null=True)  # Field name made lowercase.
    high = models.BigIntegerField(db_column='High', blank=True, null=True)  # Field name made lowercase.
    low = models.BigIntegerField(db_column='Low', blank=True, null=True)  # Field name made lowercase.
    volume = models.BigIntegerField(db_column='Volume', blank=True, null=True)  # Field name made lowercase.
    amount = models.BigIntegerField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    marcap = models.BigIntegerField(db_column='Marcap', blank=True, null=True)  # Field name made lowercase.
    navcap = models.BigIntegerField(db_column='NavCap', blank=True, null=True)  # Field name made lowercase.
    stocks = models.BigIntegerField(db_column='Stocks', blank=True, null=True)  # Field name made lowercase.
    indexname = models.TextField(db_column='IndexName', blank=True, null=True)  # Field name made lowercase.
    indexclose = models.TextField(db_column='IndexClose', blank=True, null=True)  # Field name made lowercase.
    indexchange = models.TextField(db_column='IndexChange', blank=True, null=True)  # Field name made lowercase.
    indexchangeratio = models.TextField(db_column='IndexChangeRatio', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prices_etf_kr'
        unique_together = (('date', 'symbol'),)


class PricesKr(models.Model):
    idx = models.AutoField(primary_key=True)
    symbol = models.CharField(db_column='Symbol', max_length=50, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    open = models.IntegerField(db_column='Open', blank=True, null=True)  # Field name made lowercase.
    high = models.IntegerField(db_column='High', blank=True, null=True)  # Field name made lowercase.
    low = models.IntegerField(db_column='Low', blank=True, null=True)  # Field name made lowercase.
    close = models.IntegerField(db_column='Close', blank=True, null=True)  # Field name made lowercase.
    adj_close = models.IntegerField(db_column='Adj Close', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    volume = models.BigIntegerField(db_column='Volume', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prices_kr'


class PricesUs(models.Model):
    idx = models.AutoField(primary_key=True)
    symbol = models.CharField(db_column='Symbol', max_length=50, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    open = models.FloatField(db_column='Open', blank=True, null=True)  # Field name made lowercase.
    high = models.FloatField(db_column='High', blank=True, null=True)  # Field name made lowercase.
    low = models.FloatField(db_column='Low', blank=True, null=True)  # Field name made lowercase.
    close = models.FloatField(db_column='Close', blank=True, null=True)  # Field name made lowercase.
    adj_close = models.FloatField(db_column='Adj Close', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    volume = models.BigIntegerField(db_column='Volume', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prices_us'


class TickersKr(models.Model):
    기준일 = models.DateTimeField(blank=True, null=True)
    종목코드 = models.TextField(blank=True, null=True)
    종목명 = models.TextField(blank=True, null=True)
    시장구분 = models.TextField(blank=True, null=True)
    종가 = models.BigIntegerField(blank=True, null=True)
    시가총액 = models.BigIntegerField(blank=True, null=True)
    eps = models.TextField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    선행eps = models.TextField(db_column='선행EPS', blank=True, null=True)  # Field name made lowercase.
    bps = models.TextField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    주당배당금 = models.TextField(blank=True, null=True)
    종목구분 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tickers_kr'
