    # bild_profile()함수는 이름과 성을 받고, 이름-값 쌍으로 제한 없이 받는다.
    # **user_info의 별 두 개를 인식하고 이름-값 쌍 인수를 모두 user_info딕셔너리에 저장한다.
def build_profile(first, last, **user_info):
    """사용자에 대해 아는 정보를 전부 딕셔너리에 저장"""
    # 이름과 성을 user_info 딕셔너리에 추가
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info #->user_info 딕셔너리를 반환

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)