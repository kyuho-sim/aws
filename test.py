import pyupbit

access = "FxYOyqm73xRtnGu1DCPcSOtoQZQNsV8hahtkyRau"          # 본인 값으로 변경
secret = "ejxJKXyIs8Cg0ERigxQStwlwdSh8jUK2dxkjE945"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-ETH"))     # KRW-XRP 조회
print(upbit.get_balance("KRW-LTC"))     # KRW-LTC 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
