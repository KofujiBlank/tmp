VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} Userform1 
   Caption         =   "問題"
   ClientHeight    =   4395
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   6345
   OleObjectBlob   =   "Userform1.frx":0000
   StartUpPosition =   1  'オーナー フォームの中央
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
'正解のとき
    MsgBox ("Collect!")
    flag = "collect"
    f0 = Worksheets(2).Cells(x, 7).Value
    f1 = Worksheets(2).Cells(x, 8).Value
    Worksheets(2).Cells(x, 7) = f1 'F0をF1に移動
    Worksheets(2).Cells(x, 8) = f1 + f0  'F1に元のF0とF1を足したF数を入力
    Worksheets(2).Cells(x, 10) = Date  '最終学習日に今日の日付を入力
    '記録
    y = Worksheets(3).Cells(Rows.Count, 1).End(xlUp).Row
    Worksheets(3).Cells(y + 1, 1) = Date
    Worksheets(3).Cells(y + 1, 2) = x - 1 '問題NO
    Worksheets(3).Cells(y + 1, 3) = flag
    
    x = x + 1
    For x = x To 100
    d = Worksheets(2).Cells(x, 9).Value
    
        If d <= Date Then
            Label1 = Worksheets(2).Cells(x, 2).Value '問題文
            Label2 = Worksheets(2).Cells(x, 4).Value '科目
            ans = Worksheets(2).Cells(x, 3).Value
            TextBox1 = ""
            Exit For
        Else 'If d > Date Then
        End If
    Next
Else
'不正解の時
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
    Worksheets(3).Cells(y + 1, 2) = x - 1 '問題NO
    Worksheets(3).Cells(y + 1, 3) = flag
    
    x = x + 1
    For x = x To 100
    d = Worksheets(2).Cells(x, 9).Value
    
        If d <= Date Then
            Label1 = Worksheets(2).Cells(x, 2).Value '問題文
            Label2 = Worksheets(2).Cells(x, 4).Value '科目
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
    d = Worksheets(2).Cells(x, 9).Value '復習目安日付格納場所
        If d <= Date Then
            Label1 = Worksheets(2).Cells(x, 2).Value '問題文
            Label2 = Worksheets(2).Cells(x, 4).Value '科目
            ans = Worksheets(2).Cells(x, 3).Value
    Exit For
        Else
        End If
    Next
End Sub

Private Sub UserForm_Activate()
x = 2 '問題No

For x = x To 100
d = Worksheets(2).Cells(x, 9).Value
    
    If d <= Date Then
        Label1 = Worksheets(2).Cells(x, 2).Value '問題文
        Label2 = Worksheets(2).Cells(x, 4).Value '科目
        ans = Worksheets(2).Cells(x, 3).Value
        TextBox1 = ""
        Exit For
    Else 'If d > Date Then
    End If
    Next
End Sub
