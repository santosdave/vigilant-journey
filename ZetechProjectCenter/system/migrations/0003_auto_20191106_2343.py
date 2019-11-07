# Generated by Django 2.2.7 on 2019-11-06 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_edstaff'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppraiQuestion',
            fields=[
                ('qnf_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('qnf_section', models.CharField(max_length=5)),
                ('qnf_number', models.IntegerField()),
                ('qnf_descr', models.CharField(max_length=300)),
                ('qnf_maxscore', models.IntegerField()),
                ('qnf_other1', models.IntegerField()),
                ('qnf_other2', models.IntegerField()),
                ('qnf_other3', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='edAcademicYear',
            fields=[
                ('acyr_code', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('acyr_description', models.CharField(max_length=30)),
                ('acyr_startyear', models.IntegerField()),
                ('acyr_endyear', models.IntegerField()),
                ('acyr_startdate', models.DateField()),
                ('acyr_enddate', models.DateField()),
                ('acyr_other1', models.CharField(max_length=30)),
                ('acyr_other2', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='edCollege',
            fields=[
                ('clg_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('clg_name', models.CharField(max_length=30)),
                ('clg_campus', models.IntegerField()),
                ('clg_other1', models.IntegerField()),
                ('clg_other2', models.CharField(max_length=30)),
                ('clg_other3', models.CharField(max_length=30)),
                ('clg_head', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.edStaff')),
            ],
        ),
        migrations.CreateModel(
            name='edCourse',
            fields=[
                ('crs_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('crs_name', models.CharField(max_length=30)),
                ('crs_dept_codecc', models.CharField(max_length=30)),
                ('crs_numunits', models.IntegerField()),
                ('crs_mode', models.CharField(max_length=10)),
                ('crs_other1', models.CharField(max_length=30)),
                ('crs_other2', models.CharField(max_length=30)),
                ('crs_other3', models.IntegerField()),
                ('crs_other4', models.IntegerField()),
                ('crs_coord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.edStaff')),
            ],
        ),
        migrations.CreateModel(
            name='edDepartment',
            fields=[
                ('dept_code', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('fty_codecc', models.CharField(max_length=10)),
                ('dept_name', models.CharField(max_length=30)),
                ('dept_other1', models.CharField(max_length=30)),
                ('dept_other2', models.CharField(max_length=30)),
                ('dept_other3', models.CharField(max_length=30)),
                ('dept_other4', models.CharField(max_length=30)),
                ('dept_hod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.edStaff')),
            ],
        ),
        migrations.CreateModel(
            name='edSemester',
            fields=[
                ('semester_code', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('sem_year', models.CharField(max_length=30)),
                ('sem_startdate', models.DateField()),
                ('sem_enddate', models.DateField()),
                ('sem_other1', models.CharField(max_length=30)),
                ('sem_other2', models.CharField(max_length=30)),
                ('sem_other3', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='edStudent',
            fields=[
                ('student_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('std_fname', models.CharField(max_length=30)),
                ('std_lname', models.CharField(max_length=30)),
                ('std_dob', models.DateField()),
                ('std_doreg', models.DateField()),
                ('std_crs_codecc', models.CharField(max_length=10)),
                ('std_idnumber', models.CharField(max_length=30)),
                ('std_email', models.EmailField(max_length=30)),
                ('std_phone', models.CharField(max_length=10)),
                ('std_addr1', models.CharField(max_length=30)),
                ('std_addr2', models.CharField(max_length=30)),
                ('std_suspended', models.IntegerField()),
                ('std_isactive', models.IntegerField()),
                ('std_other1', models.CharField(max_length=30)),
                ('std_other2', models.CharField(max_length=30)),
                ('std_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.edCourse')),
            ],
        ),
        migrations.CreateModel(
            name='edStudyMode',
            fields=[
                ('mod_code', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('mod_description', models.CharField(max_length=100)),
                ('mod_isactive', models.CharField(max_length=1)),
                ('mod_other1', models.CharField(max_length=30)),
                ('mod_other2', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='edUnit',
            fields=[
                ('unt_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('unt_name', models.CharField(max_length=100)),
                ('unt_crs_codecc', models.CharField(max_length=10)),
                ('unt_hours', models.IntegerField()),
                ('unt_mode', models.CharField(max_length=10)),
                ('unt_iscore', models.CharField(max_length=10)),
                ('unt_isactive', models.IntegerField()),
                ('unt_other1', models.IntegerField()),
                ('unt_other2', models.CharField(max_length=30)),
                ('unt_other3', models.CharField(max_length=30)),
                ('unt_other4', models.IntegerField()),
                ('unt_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.edCourse')),
            ],
        ),
        migrations.CreateModel(
            name='LecEvalQuestion',
            fields=[
                ('qnl_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('qnl_descr', models.CharField(max_length=300)),
                ('qnl_lot', models.CharField(max_length=10)),
                ('qnl_other1', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='xamAbsents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xab_absencecode', models.IntegerField(unique=True)),
                ('xab_descr', models.CharField(max_length=50)),
                ('xab_other1', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='xamRegSsp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xss_studentid', models.CharField(max_length=30)),
                ('xss_semester', models.CharField(max_length=10)),
                ('xss_unit', models.CharField(max_length=10)),
                ('xss_type', models.CharField(max_length=5)),
                ('xss_reason', models.CharField(max_length=100)),
                ('xss_other1', models.IntegerField()),
                ('xss_other2', models.CharField(max_length=30)),
                ('xss_other3', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='xamScoreSsp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xss_studentid', models.CharField(max_length=30)),
                ('xss_semester', models.CharField(max_length=10)),
                ('xss_unit', models.CharField(max_length=10)),
                ('xss_type', models.CharField(max_length=5)),
                ('xss_mainxam', models.IntegerField()),
                ('xss_entrydate', models.DateField()),
                ('xam_entrydate', models.DateField()),
                ('xam_reviewdate', models.DateField()),
                ('xam_reviewstaff', models.CharField(max_length=30)),
                ('xam_other1', models.IntegerField()),
                ('xam_other2', models.IntegerField()),
                ('xam_entrystaff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.edStaff')),
            ],
        ),
        migrations.CreateModel(
            name='xamScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xam_studentid', models.CharField(max_length=30)),
                ('xam_semester', models.CharField(max_length=30)),
                ('xam_unit', models.CharField(max_length=10)),
                ('xam_assgn1', models.IntegerField()),
                ('xam_assgn2', models.IntegerField()),
                ('xam_cat1', models.IntegerField()),
                ('xam_cat2', models.IntegerField()),
                ('xam_mainxam', models.IntegerField()),
                ('xam_take', models.IntegerField()),
                ('xam_absent', models.IntegerField()),
                ('xam_total', models.IntegerField()),
                ('xam_grade', models.CharField(max_length=5)),
                ('xam_entrydate', models.DateField()),
                ('xam_reviewdate', models.DateField()),
                ('xam_reviewstaff', models.CharField(max_length=30)),
                ('xam_other1', models.IntegerField()),
                ('xam_other2', models.IntegerField()),
                ('xam_entrystaff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.edStaff')),
            ],
        ),
        migrations.CreateModel(
            name='UnitDeptLecturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staffidcc', models.CharField(max_length=30)),
                ('active', models.IntegerField()),
                ('lastactivedate', models.DateField()),
                ('deacitadedate', models.DateField()),
                ('activatedby', models.CharField(max_length=30)),
                ('deactivatedby', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=70)),
                ('deptid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.edDepartment')),
                ('staffid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.edStaff')),
            ],
        ),
        migrations.CreateModel(
            name='StudentUnitReg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentidcc', models.CharField(max_length=30)),
                ('unt_codecc', models.CharField(max_length=30)),
                ('reg_date', models.DateField()),
                ('reg_other1', models.CharField(max_length=30)),
                ('reg_other2', models.CharField(max_length=30)),
                ('crs_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.edCourse')),
                ('reg_semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.edSemester')),
                ('studentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.edStudent')),
                ('unt_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.edUnit')),
            ],
        ),
        migrations.CreateModel(
            name='studentIntake',
            fields=[
                ('itk_code', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('itk_year', models.CharField(max_length=30)),
                ('itk_month', models.CharField(max_length=30)),
                ('itk_description', models.CharField(max_length=30)),
                ('itk_other1', models.CharField(max_length=30)),
                ('itk_other2', models.CharField(max_length=30)),
                ('itk_semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.edSemester')),
            ],
        ),
        migrations.CreateModel(
            name='studentGraduate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cls_crs_codecc', models.CharField(max_length=30)),
                ('studylevel', models.CharField(max_length=30)),
                ('profidcc', models.CharField(max_length=30)),
                ('professor2', models.CharField(max_length=30)),
                ('project', models.CharField(max_length=100)),
                ('thesis', models.CharField(max_length=100)),
                ('startacadyear', models.CharField(max_length=30)),
                ('other2', models.CharField(max_length=30)),
                ('other3', models.CharField(max_length=30)),
                ('crs_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.edCourse')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.edStaff')),
                ('studentid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='system.edStudent')),
            ],
        ),
        migrations.CreateModel(
            name='studentGdtProgress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentidcc', models.CharField(max_length=30)),
                ('remarks', models.CharField(max_length=100)),
                ('remarksdate', models.DateField()),
                ('remarksmaker', models.CharField(max_length=30)),
                ('comments', models.CharField(max_length=30)),
                ('commentsdate', models.CharField(max_length=30)),
                ('commentsmaker', models.CharField(max_length=30)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.edCourse')),
                ('studentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.edStudent')),
            ],
        ),
        migrations.CreateModel(
            name='LecEvalScore',
            fields=[
                ('evl_uniqeval', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('evl_semester', models.CharField(max_length=30)),
                ('evl_unit', models.CharField(max_length=10)),
                ('evl_qno', models.CharField(max_length=10, null=True)),
                ('evl_studentid', models.CharField(max_length=30, null=True)),
                ('evl_score', models.IntegerField()),
                ('evl_entrydate', models.DateField(null=True)),
                ('evl_revstatus', models.IntegerField(blank=True, null=True)),
                ('evl_revstaff', models.CharField(blank=True, max_length=30, null=True)),
                ('evl_other2', models.IntegerField()),
                ('evl_staffid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.edStaff')),
            ],
        ),
        migrations.CreateModel(
            name='ExamUnitPassed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.edStudent')),
            ],
        ),
        migrations.CreateModel(
            name='edUnitClass',
            fields=[
                ('unt_classid', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('cls_location', models.CharField(max_length=30)),
                ('cls_class', models.CharField(max_length=30)),
                ('cls_description', models.CharField(max_length=300)),
                ('cls_timeofday', models.CharField(default='', max_length=30)),
                ('cls_stdcount', models.IntegerField(default=0)),
                ('cls_lecturer2', models.CharField(blank=True, max_length=30, null=True)),
                ('cls_lec_allocdate', models.DateField(null=True)),
                ('cls_marks_done', models.IntegerField(default=0)),
                ('cls_other1', models.CharField(max_length=30)),
                ('cls_other2', models.DateField()),
                ('cls_academicyear', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.edAcademicYear')),
                ('cls_coursecode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.edCourse')),
                ('cls_lecturer1', models.ForeignKey(default='ZU/011', on_delete=django.db.models.deletion.CASCADE, to='system.edStaff')),
                ('cls_mode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.edStudyMode')),
                ('cls_semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.edSemester')),
                ('cls_unt_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.edUnit')),
            ],
        ),
        migrations.CreateModel(
            name='edStudentSuspended',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_studentidcc', models.CharField(max_length=30)),
                ('std_dosuspension', models.DateField()),
                ('std_doreg', models.DateField()),
                ('std_casenumber', models.CharField(max_length=30)),
                ('std_reason', models.CharField(max_length=100)),
                ('std_adminremarks', models.CharField(max_length=300)),
                ('std_other2', models.CharField(max_length=30)),
                ('std_other3', models.IntegerField()),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.edCourse')),
            ],
        ),
        migrations.CreateModel(
            name='edStaffAcademic',
            fields=[
                ('staffid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='system.edStaff')),
                ('qualifs', models.CharField(max_length=100)),
                ('qualifdetails', models.CharField(max_length=300)),
                ('other1', models.DateField()),
                ('other2', models.CharField(max_length=30)),
                ('other3', models.CharField(max_length=30)),
                ('other4', models.CharField(max_length=10)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.edDepartment')),
            ],
        ),
        migrations.CreateModel(
            name='edFaculty',
            fields=[
                ('fty_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('fty_name', models.CharField(max_length=30)),
                ('fty_clg_namecc', models.CharField(max_length=30)),
                ('fty_other2', models.CharField(max_length=30)),
                ('fty_other3', models.CharField(max_length=30)),
                ('fty_other4', models.CharField(max_length=30)),
                ('fty_college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.edCollege')),
                ('fty_head', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.edStaff')),
            ],
        ),
        migrations.AddField(
            model_name='eddepartment',
            name='faculty_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.edFaculty'),
        ),
        migrations.AddField(
            model_name='edcourse',
            name='crs_dept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.edDepartment'),
        ),
        migrations.CreateModel(
            name='AppraiScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stp_semester', models.CharField(max_length=30)),
                ('stp_unit', models.IntegerField()),
                ('stp_qn', models.IntegerField()),
                ('stp_score', models.IntegerField()),
                ('stp_entrydate', models.DateField()),
                ('stp_other1', models.CharField(max_length=50)),
                ('stp_other2', models.IntegerField()),
                ('stp_staffid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.edStaff')),
            ],
        ),
    ]