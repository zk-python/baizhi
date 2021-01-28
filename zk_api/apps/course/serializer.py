from rest_framework.serializers import ModelSerializer

from course.models import CourseCategory, Course, Teacher, CourseChapter, CourseLesson


class CourseCategoryModelSerializer(ModelSerializer):
    """分类"""

    class Meta:
        model = CourseCategory
        fields = ['id', "name"]


class TeacherModelSerializer(ModelSerializer):
    """老师的序列化器"""
    class Meta:
        model = Teacher
        fields = ['id', "name", "title",'image',"signature"]


class CourseModelSerializer(ModelSerializer):
    """课程列表"""

    # 返回课程列表所需的老师的信息
    teacher = TeacherModelSerializer()

    class Meta:
        model = Course
        fields = ["id", "name", "course_img", "brief_html","students", "lessons", "pub_lessons", "price", "teacher", 'lesson_list']


class ListModelSerializer(ModelSerializer):
    """课程详情展示界面"""

    # 返回课程列表所需的老师的信息
    teacher = TeacherModelSerializer()

    class Meta:
        model = Course
        fields = ["id", "name", "course_img", "students","brief_html", "lessons", "pub_lessons", "price", "teacher", "course_video",'lesson_list',"level_1"]

class CourseLessonModelSerializer(ModelSerializer):
    """课时的序列化器"""
    class Meta:
        model = CourseLesson
        fields = ['id', "name", "free_trail","duration"]
class CourseChapterModelSerializer(ModelSerializer):
    """章节
    章节对应的课时"""

    coursesections=CourseLessonModelSerializer(many=True)

    class Meta:
        model = CourseChapter
        fields = ["id", "name","chapter","coursesections"]
