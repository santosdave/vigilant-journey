from django.contrib import admin
from .models import edAuditTrace, edStaff, edCollege, edFaculty, edDepartment, edCourse, edUnit, edStaffAcademic, edStudent, edStudentSuspended, edSemester, edAcademicYear, AppraiQuestion, LecEvalQuestion, xamScore, xamAbsents, xamScoreSsp, xamRegSsp, AppraiScore, LecEvalScore, edStudyMode, edUnitClass, studentIntake, studentGraduate, studentGdtProgress, UnitDeptLecturer, StudentUnitReg
 

# initial view for admin panel
admin.site.register(edAuditTrace)
# admin.site.register(edStaff)
@admin.register(edStaff)
class edStaffAdmin(admin.ModelAdmin):
    list_display = ('stf_fname', 'stf_lname', 'stf_idnumber', 'stf_email')


admin.site.register(edCollege)
admin.site.register(edFaculty)
admin.site.register(edDepartment)
admin.site.register(edCourse)
admin.site.register(edUnit)
admin.site.register(edStaffAcademic)
admin.site.register(edStudent)
admin.site.register(edStudentSuspended)
admin.site.register(edSemester)
admin.site.register(edAcademicYear)
admin.site.register(AppraiQuestion)
admin.site.register(LecEvalQuestion)
admin.site.register(xamScore)
admin.site.register(xamAbsents)
admin.site.register(xamScoreSsp)
admin.site.register(xamRegSsp)
admin.site.register(AppraiScore)
admin.site.register(LecEvalScore)
admin.site.register(edStudyMode)
admin.site.register(edUnitClass)
admin.site.register(studentIntake)
admin.site.register(studentGraduate)
admin.site.register(studentGdtProgress)
admin.site.register(UnitDeptLecturer)
admin.site.register(StudentUnitReg)
# admin.site.register()
