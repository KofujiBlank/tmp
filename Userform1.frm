VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} Userform1 
   Caption         =   "���"
   ClientHeight    =   4395
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   6345
   OleObjectBlob   =   "Userform1.frx":0000
   StartUpPosition =   1  '�I�[�i�[ �t�H�[���̒���
End
Attribute VB_Name = "Userform1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Dim x As Integer
Dim d As Date

Private Sub AnsButton_Click()
    yourAns = TextBox1.Value
    ans = Worksheets(2).Cells(x, 3).Value
    question = Worksheets(2).Cells(x, 2).Value
If yourAns = ans Then
'�����̂Ƃ�
    MsgBox ("Collect!")
    flag = "collect"
    f0 = Worksheets(2).Cells(x, 7).Value
    f1 = Worksheets(2).Cells(x, 8).Value
    Worksheets(2).Cells(x, 7) = f1 'F0��F1�Ɉړ�
    Worksheets(2).Cells(x, 8) = f1 + f0  'F1�Ɍ���F0��F1�𑫂���F�������
    Worksheets(2).Cells(x, 10) = Date  '�ŏI�w�K���ɍ����̓��t�����
    '�L�^
    y = Worksheets(3).Cells(Rows.Count, 1).End(xlUp).Row
    Worksheets(3).Cells(y + 1, 1) = Date
    Worksheets(3).Cells(y + 1, 2) = x - 1 '���NO
    Worksheets(3).Cells(y + 1, 3) = flag
    
    x = x + 1
    For x = x To 100
    d = Worksheets(2).Cells(x, 9).Value
    
        If d <= Date Then
            Label1 = Worksheets(2).Cells(x, 2).Value '��蕶
            Label2 = Worksheets(2).Cells(x, 4).Value '�Ȗ�
            ans = Worksheets(2).Cells(x, 3).Value
            TextBox1 = ""
            Exit For
        Else 'If d > Date Then
        End If
    Next
Else
'�s�����̎�
    retry = MsgBox("NO:" + ans, vbOKOnly)
    flag = "wrong"
    TextBox1 = ""
    If retry = vbOK Then
        checkTest = Application.InputBox(question)
        If checkTest = ans Then
            MsgBox ("You passed the CheckTest!")
        Else
            MsgBox ("Please retry")
        End If
    End If
    y = Worksheets(3).Cells(Rows.Count, 1).End(xlUp).Row
    Worksheets(3).Cells(y + 1, 1) = Date
    Worksheets(3).Cells(y + 1, 2) = x - 1 '���NO
    Worksheets(3).Cells(y + 1, 3) = flag
    
    x = x + 1
    For x = x To 100
    d = Worksheets(2).Cells(x, 9).Value
    
        If d <= Date Then
            Label1 = Worksheets(2).Cells(x, 2).Value '��蕶
            Label2 = Worksheets(2).Cells(x, 4).Value '�Ȗ�
            ans = Worksheets(2).Cells(x, 3).Value
            TextBox1 = ""
            Exit For
        Else 'If d > Date Then
        End If
    Next


End If
End Sub

Private Sub SkipButton_Click()
    x = x + 1
    For x = x To 100
    d = Worksheets(2).Cells(x, 9).Value '���K�ڈ����t�i�[�ꏊ
        If d <= Date Then
            Label1 = Worksheets(2).Cells(x, 2).Value '��蕶
            Label2 = Worksheets(2).Cells(x, 4).Value '�Ȗ�
            ans = Worksheets(2).Cells(x, 3).Value
    Exit For
        Else
        End If
    Next
End Sub

Private Sub UserForm_Activate()
x = 2 '���No

For x = x To 100
d = Worksheets(2).Cells(x, 9).Value
    
    If d <= Date Then
        Label1 = Worksheets(2).Cells(x, 2).Value '��蕶
        Label2 = Worksheets(2).Cells(x, 4).Value '�Ȗ�
        ans = Worksheets(2).Cells(x, 3).Value
        TextBox1 = ""
        Exit For
    Else 'If d > Date Then
    End If
    Next
End Sub
