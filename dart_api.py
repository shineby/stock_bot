import dart_fss as dart

# Open DART API KEY 설정
api_key='???'
dart.set_api_key(api_key=api_key)

# DART 에 공시된 회사 리스트 불러오기
corp_list = dart.get_corp_list()

# 삼성전자 검색
samsung = corp_list.find_by_corp_name('삼성전자', exactly=True)[0]
print(samsung)

# 2012년부터 연간 연결재무제표 불러오기
# fs = samsung.extract_fs(bgn_de='20160101')
#fs.save()