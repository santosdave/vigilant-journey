from django.db import models

class edAuditTrace(models.Model):
	action_id  = models.IntegerField(unique=True)
	act_user = models.CharField(max_length=10) 
	act_staffid = models.CharField(max_length=10) 
	act_descr  = models.CharField(max_length=100) 
	act_datetime = models.DateField() 
	act_other  = models.CharField(max_length=30) 

	def __str__(self):
		return self.act_user

class edStaff(models.Model):
	staff_id  = models.CharField(max_length=30, primary_key=True)		
	stf_fname  = models.CharField(max_length=30)	
	stf_lname  = models.CharField(max_length=30)	
	stf_userid  = models.CharField(max_length=10)		
	stf_idnumber  = models.CharField(max_length=30)		
	stf_dob  = models.DateField()		
	stf_phone  = models.CharField(max_length=30)		
	stf_email  = models.CharField(max_length=30)		
	stf_dept_id  = models.CharField(max_length=30) #Changed version 2
	stf_addr1  = models.CharField(max_length=30)		
	stf_addr2  = models.CharField(max_length=30)		
	std_other1  = models.CharField(max_length=30)		
	std_other2  = models.CharField(max_length=30)		

	def __str__(self):
		return self.stf_fname + ' ' +self.stf_lname

	class Meta:
		verbose_name_plural = 'STAFF'

class edCollege(models.Model):
	clg_code  = models.CharField(max_length=10, primary_key=True)	
	clg_name  = models.CharField(max_length=30)	
	clg_campus  = models.IntegerField()
	clg_head  = models.ForeignKey(edStaff, on_delete=models.CASCADE)
	clg_other1 = models.IntegerField()
	clg_other2  = models.CharField(max_length=30) 
	clg_other3  = models.CharField(max_length=30) 

	def __str__(self):
		return self.clg_code
	
	class Meta:
		verbose_name_plural = 'College'

class edFaculty(models.Model):
	fty_code = models.CharField(max_length=10, primary_key=True) 
	fty_name  = models.CharField(max_length=30) 
	fty_college  = models.ForeignKey(edCollege, on_delete=models.CASCADE)	
	fty_clg_namecc  = models.CharField(max_length=30)
	fty_head  = models.ForeignKey(edStaff, on_delete=models.CASCADE)	
	fty_other2  = models.CharField(max_length=30)		
	fty_other3  = models.CharField(max_length=30)		
	fty_other4  = models.CharField(max_length=30)
	
	def __str__(self):
		return self.fty_code

	class Meta:
		verbose_name_plural = 'Faculty'

class edDepartment(models.Model):
	dept_code  = models.CharField(max_length=30, primary_key=True)
	faculty_id  = models.ForeignKey(edFaculty, on_delete=models.CASCADE)		
	fty_codecc  = models.CharField(max_length=10)		
	dept_name  = models.CharField(max_length=30)		
	dept_hod  = models.ForeignKey(edStaff, on_delete=models.CASCADE)		
	dept_other1  = models.CharField(max_length=30)		
	dept_other2  = models.CharField(max_length=30)		
	dept_other3  = models.CharField(max_length=30)		
	dept_other4  = models.CharField(max_length=30)
	
	def __str__(self):
		return self.dept_code

	class Meta:
		verbose_name_plural = 'Departments'

class edCourse(models.Model):
	crs_code  = models.CharField(max_length=10, primary_key=True)		
	crs_name  = models.CharField(max_length=30)		
	crs_dept  = models.ForeignKey(edDepartment, on_delete=models.CASCADE)		
	crs_dept_codecc  = models.CharField(max_length=30)
	crs_coord  = models.ForeignKey(edStaff, on_delete=models.CASCADE)
	crs_numunits  = models.IntegerField()
	crs_mode  = models.CharField(max_length=10)
	crs_other1  = models.CharField(max_length=30)		
	crs_other2  = models.CharField(max_length=30)		
	crs_other3  = models.IntegerField()	
	crs_other4  = models.IntegerField()

	def __str__(self):
		return self.crs_code

	class Meta:
		verbose_name_plural = 'Courses'

class edUnit(models.Model):
	unt_code  = models.CharField(max_length=10, primary_key=True)		
	unt_name  = models.CharField(max_length=100)		
	unt_course  = models.ForeignKey(edCourse, on_delete=models.CASCADE)		
	unt_crs_codecc  = models.CharField(max_length=10)		
	unt_hours  = models.IntegerField()		
	unt_mode  = models.CharField(max_length=10)		
	unt_iscore  = models.CharField(max_length=10)		
	unt_isactive  = models.IntegerField()		
	unt_other1  = models.IntegerField()		
	unt_other2  = models.CharField(max_length=30)		
	unt_other3  = models.CharField(max_length=30)		
	unt_other4  = models.IntegerField()

	def __str__(self):
		return self.unt_code

	class Meta:
		verbose_name_plural = 'Units'

class edStaffAcademic(models.Model):
	staffid = models.OneToOneField(edStaff, on_delete=models.CASCADE, primary_key=True)
	dept = models.ForeignKey(edDepartment, on_delete=models.CASCADE)
	qualifs = models.CharField(max_length=100)
	qualifdetails = models.CharField(max_length=300)
	other1 = models.DateField()
	other2 = models.CharField(max_length=30)
	other3 = models.CharField(max_length=30)
	other4 = models.CharField(max_length=10)

	def __str__(self):
		return self.staffid
	
	class Meta:
		verbose_name_plural = 'Academic Staff'

class edStudent(models.Model):
	student_id   = models.CharField(max_length=30, primary_key=True)
	std_fname  = models.CharField(max_length=30)		
	std_lname  = models.CharField(max_length=30)		
	std_dob  = models.DateField()
	std_doreg  = models.DateField()
	std_course  = models.ForeignKey(edCourse, on_delete=models.CASCADE)		
	std_crs_codecc  = models.CharField(max_length=10)		
	std_idnumber  = models.CharField(max_length=30)	
	std_email  = models.EmailField(max_length=30)		
	std_phone  = models.CharField(max_length=10)
	std_addr1  = models.CharField(max_length=30)		
	std_addr2  = models.CharField(max_length=30)		
	std_suspended  = models.IntegerField()		
	std_isactive  = models.IntegerField()		
	std_other1  = models.CharField(max_length=30)		
	std_other2  = models.CharField(max_length=30)		

	def __str__(self):
		return self.student_id

	class Meta:
		verbose_name_plural = 'students'

class edStudentSuspended(models.Model):
	student_id   = models.ForeignKey(edCourse, on_delete=models.CASCADE)		
	std_studentidcc  = models.CharField(max_length=30)
	std_dosuspension  = models.DateField()
	std_doreg  = models.DateField()
	std_casenumber  = models.CharField(max_length=30)
	std_reason  = models.CharField(max_length=100)		
	std_adminremarks  = models.CharField(max_length=300)		
	std_other2  = models.CharField(max_length=30)		
	std_other3  = models.IntegerField()

	def __str__(self):
		return self.student_id

	class Meta:
		verbose_name_plural = 'Students suspended'

class edSemester(models.Model):
	semester_code  = models.CharField(max_length=30, primary_key=True)	
	sem_year  = models.CharField(max_length=30)		
	sem_startdate  = models.DateField()		
	sem_enddate  = models.DateField()	
	sem_other1  = models.CharField(max_length=30)		
	sem_other2  = models.CharField(max_length=30)		
	sem_other3  = models.IntegerField()

	def __str__(self):
		return self.semester_code

	class Meta:
		verbose_name_plural = 'Semesters'

class edAcademicYear(models.Model):
	acyr_code  = models.CharField(max_length=30, primary_key=True)	
	acyr_description = models.CharField(max_length=30)	
	acyr_startyear  = models.IntegerField()
	acyr_endyear  = models.IntegerField()
	acyr_startdate = models.DateField()
	acyr_enddate = models.DateField()
	acyr_other1  = models.CharField(max_length=30)		
	acyr_other2  = models.CharField(max_length=30)		

	def __str__(self):
		return self.acyr_code

	class Meta:
		verbose_name_plural = 'Academic Year'

class AppraiQuestion(models.Model):
	qnf_id  = models.CharField(max_length=10, primary_key=True)		
	qnf_section  = models.CharField(max_length=5)		
	qnf_number  = models.IntegerField()		
	qnf_descr  = models.CharField(max_length=300)		
	qnf_maxscore  = models.IntegerField()
	qnf_other1  = models.IntegerField()
	qnf_other2  = models.IntegerField()
	qnf_other3  = models.IntegerField()

	def __str__(self):
		return self.qnf_identifier

	class Meta:
		verbose_name_plural = 'Apprai-Questions'

class LecEvalQuestion(models.Model):
	qnl_id = models.CharField(max_length=30, primary_key=True)		
	qnl_descr = models.CharField(max_length=300)		
	qnl_lot = models.CharField(max_length=10)		
	qnl_other1 = models.IntegerField()
	qnl_other1 = models.IntegerField()

class xamScore(models.Model):
	unique_together = (('xam_studentid', 'xam_unit'),)
	xam_studentid = models.CharField(max_length=30)		
	xam_semester = models.CharField(max_length=30)		#Changed version 2
	xam_unit = models.CharField(max_length=10)
	xam_assgn1 = models.IntegerField()
	xam_assgn2 = models.IntegerField()
	xam_cat1 = models.IntegerField()
	xam_cat2 = models.IntegerField()
	xam_mainxam = models.IntegerField()
	xam_take = models.IntegerField()
	xam_absent = models.IntegerField()
	xam_total = models.IntegerField()
	xam_grade = models.CharField(max_length=5)	
	xam_entrydate = models.DateField()
	xam_entrystaff = models.ForeignKey(edStaff, on_delete=models.CASCADE)
	xam_reviewdate = models.DateField()
	xam_reviewstaff = models.CharField(max_length=30)
	xam_other1 = models.IntegerField()
	xam_other2 = models.IntegerField()

	def __str__(self):
		return self.xam_studentid

	class Meta:
		verbose_name_plural = 'Exams Score'

class xamAbsents(models.Model):
	xab_absencecode = models.IntegerField(unique = True)
	xab_descr = models.CharField(max_length=50)	
	xab_other1 = models.CharField(max_length=30)

	class Meta:
		verbose_name_plural = 'Exam-Absent'

class xamScoreSsp(models.Model):
	unique_together = (('xss_studentid', 'xss_unit'),)

	xss_studentid = models.CharField(max_length=30)		
	xss_semester = models.CharField(max_length=10)		
	xss_unit = models.CharField(max_length=10)
	xss_type = models.CharField(max_length=5)	
	xss_mainxam = models.IntegerField()
	xss_entrydate = models.DateField()
	xam_entrydate = models.DateField()
	xam_entrystaff = models.ForeignKey(edStaff, on_delete=models.CASCADE)
	xam_reviewdate = models.DateField()
	xam_reviewstaff = models.CharField(max_length=30)
	xam_other1 = models.IntegerField()
	xam_other2 = models.IntegerField()

class xamRegSsp(models.Model):
	unique_together = (('xss_studentid', 'xss_unit'),)

	xss_studentid = models.CharField(max_length=30)		
	xss_semester = models.CharField(max_length=10)		
	xss_unit = models.CharField(max_length=10)
	xss_type = models.CharField(max_length=5)	
	xss_reason = models.CharField(max_length=100)
	xss_other1= models.IntegerField()
	xss_other2 = models.CharField(max_length=30)	
	xss_other3 = models.CharField(max_length=30)	

	def __str__(self):
		return self.xss_studentid

	class Meta:
		verbose_name_plural = 'Exam Registration'

class AppraiScore(models.Model):
	unique_together = (('stfv_staffid', 'stfv_semester'),)

	stp_staffid = models.ForeignKey(edStaff, on_delete=models.CASCADE)	
	#stp_staffidcc = models.CharField(max_length=30)	#Changed version 2	
	stp_semester = models.CharField(max_length=30)		
	stp_unit = models.IntegerField()
	stp_qn = models.IntegerField()
	stp_score = models.IntegerField()
	stp_entrydate = models.DateField()
	stp_other1 = models.CharField(max_length=50)	
	stp_other2 = models.CharField(max_length=50)	
	stp_other2 = models.IntegerField()

	def __str__(self):
		return self.stp_staffid
	
	class Meta:
		verbose_name_plural = 'Apprai-Score'

class LecEvalScore(models.Model):
	evl_uniqeval = models.CharField(max_length=30, primary_key=True)	
	evl_staffid = models.ForeignKey(edStaff, on_delete=models.CASCADE)	
	evl_semester = models.CharField(max_length=30)		
	evl_unit = models.CharField(max_length=10)	#Changed version 2
	evl_qno = models.CharField(max_length=10, null=True)	#Changed version 2
	evl_studentid = models.CharField(max_length=30, null=True)		#Changed version 2
	evl_score = models.IntegerField()
	evl_entrydate = models.DateField(null=True)	#Changed version 2
	evl_revstatus = models.IntegerField(blank=True, null=True)	#Changed version 2
	evl_revstaff = models.CharField(max_length=30, blank=True, null=True)	#Changed version 2
	evl_other2 = models.IntegerField()

	def __str__(self):
		return self.evl_uniqeval

	class Meta:
		verbose_name_plural = 'Lecturer Evaluation Forms'

class edStudyMode(models.Model):
	mod_code = models.CharField(max_length=30, primary_key=True)
	mod_description = models.CharField(max_length=100)
	mod_isactive = models.CharField(max_length=1)
	mod_other1 = models.CharField(max_length=30)
	mod_other2 = models.CharField(max_length=30)

	def __str__(self):
		return self.modecode

	class Meta:
		verbose_name_plural = 'Mode of Study'

class edUnitClass(models.Model):
	unt_classid = models.CharField(max_length=30, primary_key=True)
	cls_academicyear = models.ForeignKey(edAcademicYear, on_delete=models.CASCADE)
	cls_semester = models.ForeignKey(edSemester, on_delete=models.CASCADE)
	#cls_semestercc = models.CharField(max_length=30)	#Changed version 2
	cls_unt_code  = models.ForeignKey(edUnit, on_delete=models.CASCADE)
	#unt_codecc = models.CharField(max_length=30)  	#Changed version 2
	cls_mode = models.ForeignKey(edStudyMode, on_delete=models.CASCADE) 
	cls_coursecode = models.ForeignKey(edCourse, on_delete=models.CASCADE)
	#cls_crs_codecc = models.CharField(max_length=30) 	#Changed version 2
	#cls_crs_codecc = models.CharField(max_length=30) 	#Changed version 2
	cls_location = models.CharField(max_length=30)
	cls_class = models.CharField(max_length=30)
	cls_description = models.CharField(max_length=300)
	cls_timeofday = models.CharField(max_length=30, default = "")
	cls_stdcount = models.IntegerField(default=0) 
	cls_lecturer1 = models.ForeignKey(edStaff, on_delete=models.CASCADE, default="ZU/011")	 	#Changed version 2  # Plz check
	cls_lecturer2 = models.CharField(max_length=30, blank = True, null = True)	 	#Changed version 2
	cls_lec_allocdate = models.DateField(null = True)	 	#Changed version 2
	cls_marks_done = models.IntegerField(default=0) 	 	#Changed version 2
	cls_other1 = models.CharField(max_length=30)
	cls_other2 = models.DateField()

	def __str__(self):
		return self.unt_classid

	class Meta:
		verbose_name_plural = 'Unit Class/Room'
	
class studentIntake(models.Model):
	itk_code = models.CharField(max_length=30, primary_key=True)
	itk_year  = models.CharField(max_length=30)
	itk_month  = models.CharField(max_length=30)
	itk_semester = models.ForeignKey(edSemester, on_delete=models.CASCADE)
	itk_description = models.CharField(max_length=30)
	itk_other1 = models.CharField(max_length=30)
	itk_other2 = models.CharField(max_length=30)

	def __str__(self):
		return self.intakecode

	class Meta:
		verbose_name_plural = 'Intake'

class studentGraduate(models.Model):
	studentid  = models.OneToOneField(edStudent, on_delete=models.CASCADE)
	crs_code = models.ForeignKey(edCourse, on_delete=models.CASCADE)
	cls_crs_codecc = models.CharField(max_length=30)
	studylevel = models.CharField(max_length=30)
	professor = models.ForeignKey(edStaff, on_delete=models.CASCADE)
	profidcc = models.CharField(max_length=30)
	professor2 = models.CharField(max_length=30)
	project = models.CharField(max_length=100)
	thesis = models.CharField(max_length=100)
	startacadyear = models.CharField(max_length=30)
	other2 = models.CharField(max_length=30)
	other3 = models.CharField(max_length=30)

	def __str__(self):
		return self.studentid

	class Meta:
		verbose_name_plural = 'Graduate-Student'

class studentGdtProgress(models.Model):
	studentid = models.ForeignKey(edStudent, on_delete=models.CASCADE)
	studentidcc = models.CharField(max_length=30)
	course = models.ForeignKey(edCourse, on_delete=models.CASCADE)
	remarks = models.CharField(max_length=100)
	remarksdate = models.DateField()
	remarksmaker = models.CharField(max_length=30)
	comments = models.CharField(max_length=30)
	commentsdate = models.CharField(max_length=30)
	commentsmaker = models.CharField(max_length=30)

	def __str__(self):
		return self.studentid

	class Meta:
		verbose_name_plural = 'Graduate Progress'

class UnitDeptLecturer(models.Model):
	deptid = models.ForeignKey(edDepartment, on_delete=models.CASCADE)
	staffid = models.ForeignKey(edStaff, on_delete=models.CASCADE)
	staffidcc = models.CharField(max_length=30)
	active = models.IntegerField()
	lastactivedate = models.DateField()
	deacitadedate = models.DateField()
	activatedby = models.CharField(max_length=30)
	deactivatedby = models.CharField(max_length=30)
	description = models.CharField(max_length=70)

	def __str__(self):
		return self.staffId
	
	class Meta:
		verbose_name_plural = 'Unit Dept Lecurer'

class StudentUnitReg(models.Model):		# RENAME to UnitRegisterStudents  // PUT UNIQUE Field
	studentid = models.ForeignKey(edStudent, on_delete=models.CASCADE)
	studentidcc = models.CharField(max_length=30)
	unt_code = models.ForeignKey(edUnit, on_delete=models.CASCADE)
	unt_codecc = models.CharField(max_length=30)
	crs_code = models.ForeignKey(edCourse, on_delete=models.CASCADE)
	reg_semester = models.ForeignKey(edSemester, on_delete=models.CASCADE)
	reg_date = models.DateField()
	reg_other1 = models.CharField(max_length=30)
	reg_other2 = models.CharField(max_length=30)

	def __str__(self):
		return self.studentid

	class Meta:
		verbose_name_plural = 'Unit Registration'

class ExamUnitPassed(models.Model):
	studentid = models.ForeignKey(edStudent, on_delete=models.CASCADE)
