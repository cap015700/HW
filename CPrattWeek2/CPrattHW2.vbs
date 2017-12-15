Sub WallStreet()
   
    Dim Ticker As String
    Dim Summary_Table_Row As Integer
    Summary_Table_Row = 2
    Dim TotalValue As Double
    TotalValue = 0
    Dim i As Double
    Dim lastRow As Long
    lastRow = Cells(Rows.Count, "G").End(xlUp).Row
    
    Dim Closing_Price As Double
    Dim Opening_Price As Double
    Dim change As Double
    Opening_Price = Cells(2, 3).Value
    
    
    
    
    Dim Perc_Change As Double
    Perc_Change = (change / Opening_Price)
    
    For i = 2 To lastRow
        If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
        Closing_Price = Cells(i, 6).Value
        change = (Closing_Price - Opening_Price)
        Range("H" & Summary_Table_Row).Value = change
        Opening_Price = Cells(i + 1, 3).Value
        Ticker = Cells(i, 1).Value
        TotalValue = TotalValue + Cells(i, 7).Value
        Range("I" & Summary_Table_Row).Value = Ticker
        Range("J" & Summary_Table_Row).Value = TotalValue
        Summary_Table_Row = Summary_Table_Row + 1
        TotalValue = 0
        
        
        
        Else
        TotalValue = TotalValue + Cells(i, 7).Value
        
        End If
        
        Next i
        
End Sub
