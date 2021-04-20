from django.contrib import admin

# Register your models here.
from Teacher.models import Quiz, Question, Answer, Student, TakenQuiz, StudentAnswer

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Student)
admin.site.register(TakenQuiz)
admin.site.register(StudentAnswer)
