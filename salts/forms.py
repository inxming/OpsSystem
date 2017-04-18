#-*- coding: utf-8 -*-
from django import forms
Choice=(('list','List'),('grain','Grain'),('pcre','Regex'),('nodegroup','NodeGroup'),('glob','Hostname'))
class CmdInputForm(forms.Form):
    target=forms.CharField(error_messages={'required':u'请输入目标主机！'},
	    label=u'Target',
	    max_length=100,
	    required=True,
	    widget=forms.TextInput(attrs={'class':'form-control'}))
    mapping=forms.ChoiceField(required=True,
	    choices=(('list','List'),('grain','Grain'),('pcre','Regex'),('nodegroup','NodeGroup'),('glob','Hostname')),
	    widget=forms.RadioSelect(attrs={'checked':None}))
    cmdline=forms.CharField(error_messages={'required':u'请输入命令！'},
	    label=u'Command',
	    max_length=1000,
	    required=True,
	    widget=forms.TextInput(attrs={'class':'form-control'}))
class DownloadFileForm(forms.Form):
    target=forms.CharField(error_messages={'required':u'请输入目标主机！'},
	    label=u'Target',
	    max_length=100,
	    required=True,
	    widget=forms.TextInput(attrs={'class':'form-control'}))
    file_path=forms.RegexField(regex=r'^/',
	    error_messages={'required':u'请输入文件绝对路径！','invalid':u'无效的路径，必须以/开头'},
	    label=u'FilePath',
	    max_length=1000,
	    required=True,
	    widget=forms.TextInput(attrs={'class':'form-control'}))

class ProjectRecord(forms.Form):
    type=forms.CharField(label=u'类型',max_length=100,required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'可选类型为: mps,appportal'}))
    version=forms.CharField(label=u'版本号',max_length=100,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    projects=forms.CharField(label=u'工程名',max_length=1000,required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'多个工程以空格相隔'}))
    sql=forms.CharField(label=u'Sql文件名',max_length=1000,required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'若无则不填'}))
    comment=forms.CharField(label=u'版本说明',max_length=2000,required=True,widget=forms.Textarea(attrs={'class':'form-control'}))
    #comment=forms.Textarea()

