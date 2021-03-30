from django.http import HttpResponse

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Student
from api.serializer import StuSerializer, StuDeSerializer


class StudentView(APIView):
    def get(self, request, *args, **kwargs):
        username = kwargs.get('username')
        if username:
            # 查询单个
            stu_obj = Student.objects.get(username=username)
            print(stu_obj, type(stu_obj))
            # 查询出的单个用户无法直接序列化，需要使用序列化器去完成序列化
            # .data 将序列化后的数据打包成字典
            serializer = StuSerializer(stu_obj).data

            return Response({
                "status": 200,
                "message": "查询单个用户成功",
                "results": serializer
            })
        else:
            # 查询所有
            student_objects_all = Student.objects.all()

            data = StuSerializer(student_objects_all, many=True).data
            return Response({
                "status": 200,
                "message": "查询单个用户成功",
                "results": data,
            })

    def post(self, request, *args, **kwargs):

        # 获取前端传递的参数
        user_data = request.data

        if not isinstance(user_data, dict) or user_data == {}:
            return Response({
                "status": 400,
                "message": "请求参数有误"
            })

        # 使用序列化器对前台提交的数据进行反序列化
        # 在反序列化时需要指定关键字参数 data
        serializer = StuDeSerializer(data=user_data)

        # 校验失败的错误信息
        # 对反序列化数据的进行校验  通过is_valid进行校验  如果校验通过，该方法返回True
        if serializer.is_valid():
            # 校验通过，则调用save()方法去保存对象 创建成功会返回对象
            # 底层调用的是create(）方法完成的对象的创建
            stu_obj = serializer.save()
            if stu_obj:
                # 有员工对象代表创建成功 返回到前端
                return Response({
                    "status": 201,
                    "message": "创建单个对象成功",
                    # 将创建成功后的对象返回到前端时需要序列化
                    "results": StuSerializer(stu_obj).data
                })

        return Response({
            "status": 400,
            "message": "创建失败",
            "errors": serializer.errors
        })