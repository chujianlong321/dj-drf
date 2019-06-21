import re
from rest_framework import serializers
from test.models import Movie
# 在外部定义利用序列化器中对单个字段的校验
def v_age(value):
    reg = r'^[123]\d{1}$'
    v = str(value)
    if not re.match(reg,v):
        raise serializers.ValidationError("age 字段值必须在10-40之间")

class ActorSerializer(serializers.Serializer):
    """演员序列化器"""
    GENDER_ID = (
        ('0', '男'),
        ('1', '女')
    )
    aid = serializers.IntegerField(label='编号', read_only=True)
    aname = serializers.CharField(label='姓名', max_length=30)
    age = serializers.IntegerField(label='年龄', required=False)#,validators=[v_age]
    agender = serializers.ChoiceField(choices=GENDER_ID, label='性别', required=False)
    birth_date = serializers.DateField(label='出生年月', required=False)
    photo = serializers.ImageField(label='头像', required=False)
    #在类内部定义多个字段的校验方法
    def validate(self, attrs):
        aname = attrs['aname']
        age = attrs['age']

        if 'hello' in aname:
            raise serializers.ValidationError("aname 字段值不能包含hello")

        reg = r'^[123]\d{1}$'
        v = str(age)
        if not re.match(reg, v):
            raise serializers.ValidationError("age 字段值必须在10-40之间")

        return attrs

class MovieSerializer(serializers.Serializer):
    mid = serializers.IntegerField(label='影片编号', read_only=True)
    mname = serializers.CharField(label='影片名称', max_length=30)
    m_pub_date = serializers.DateField(label='上映日期', required=False)
    mread = serializers.IntegerField(label='阅读量')
    mcomment = serializers.CharField(label='评论', max_length=300, required=False, allow_null=True)
    mimage = serializers.ImageField(label='图片', required=False)
    actors = serializers.PrimaryKeyRelatedField(label='演员', read_only=True)
    #外键字段插入值 增加或修改 与数据库外键字段名匹配
    actors_id=serializers.IntegerField()
    # actors=serializers.StringRelatedField(label='演员') 返回的是model中 str方法返回值 
    # 填表单时将内容序列化 校验 并将其写入到validated_data
    def create(self, validated_data):
        print(validated_data)
        # ** valaidated_data 解包
        instance=Movie.objects.create(**validated_data)
        return instance