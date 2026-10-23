import os
import pandas
import typing
import time
import openpyxl
import openpyxl.styles as st
import colorsys

# 1.Introduction Message :
# - 1.1.Code Explaination :
def introduction_message():
    print("=== Excel Sheet of Powers Creation (Python) ===\nCreate a sheet with all powers of a number until certain range")

# 2.Determinating Path :
# - 2.1.Receiveng User Input :
def user_path():
    print('Please insert save path :')
    path = []
    while True:
        current = input('Folder : ')
        if current in ['', ' '] and len(path) > 0:
            break
        else :
            path.append(str(current))
            if not os.path.exists(os.path.join(*path)):
                path.clear()            

    path.append(f'powers_{str(time.time()).replace('.','')}.xlsx')
    file = os.path.join(*path)
    return file

# 3.Generation Process :
# - 3.1.Selecting Powers and Range :
def parameters():
    while True:
        try:
            powers = int(input('Powers : '))
            rangeof = int(input('Range : '))
            break
        except:
            continue
    return powers, rangeof

# - 3.2.Styling Chooser :
def styling():
    modes = {0:'Rainbow', 1:'Monochrome'}
    while True:
        try:
            mode = input(', '.join([f'{d[0]} for "{d[1]}"' for d in modes.items()]))
            modes.get(mode)
            break
        except:
            continue
    return int(mode)

# - 3.3.Construction and Segregation :
def construction(number:int, power:int) :
    frame = {}
    for n in range(2, number):
        frame[n] = [n ** p for p in range(1, power + 1)]

    df = pandas.DataFrame(frame)
    df.rename({p:p + 1 for p in range(power)}, inplace=True)
    df.rename(columns=dict.fromkeys(df.columns, ''), inplace=True)
    return df
    

# 4.Saving File :
# - 4.1.File Creation and Storing Contents :
def save(file, df, style_mode):
    with pandas.ExcelWriter(file, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Powers')
        ws = writer.sheets['Powers']
        
        max_row = ws.max_row
        max_col = ws.max_column
        
        # Row-column Headers : 
        header_fill = st.PatternFill(start_color="202020", end_color="202020", fill_type="solid")
        header_font = st.Font(name="Segoe UI", size=11, bold=True, color="FFFFFF")
        center_align = st.Alignment(horizontal="center", vertical="center")
        
        # Column headers (Row 1)
        for col in range(1, max_col + 1):
            cell = ws.cell(row=1, column=col)
            cell.fill = header_fill
            cell.font = header_font
            cell.alignment = center_align

        # Row headers (Column 1)
        for row in range(2, max_row + 1):
            cell = ws.cell(row=row, column=1)
            cell.fill = header_fill
            cell.font = header_font
            cell.alignment = center_align

        # --- Gradient / Monochrome ---
        # Total cells to calc :
        total_data_cells = (max_row - 1) * (max_col - 1)
        
        if total_data_cells > 1:
            cell_counter = 0
            for row in range(2, max_row + 1):
                for col in range(2, max_col + 1):
                    cell = ws.cell(row=row, column=col)
                    
                    # Ride :
                    factor = cell_counter / (total_data_cells - 1)
                    
                    if style_mode == 0:
                        # Rainbow : 0.0 to 0.85
                        hue = factor * 0.85 
                        # HSV to RGB (S : 65%, V : 95%, readable cake tones)
                        rgb = colorsys.hsv_to_rgb(hue, 0.65, 0.95)
                    else:
                        # Monochrome : Only change light
                        rgb = colorsys.hsv_to_rgb(0.6, 0.2, 0.4 + (factor * 0.5))
                    
                    # Float to Hex :
                    hex_color = "".join(f"{int(c * 255):02X}" for c in rgb)
                    
                    # Format and color :
                    cell.fill = st.PatternFill(start_color=hex_color, end_color=hex_color, fill_type="solid")
                    cell.font = st.Font(name="Segoe UI", size=10, bold=True, color="000000")
                    cell.number_format = '#,##0'
                    cell.alignment = center_align
                    
                    cell_counter += 1

        # Adjust column width :
        for col in ws.columns:
            max_len = max(len(str(cell.value or '')) for cell in col)
            col_letter = openpyxl.utils.get_column_letter(col[0].column)
            ws.column_dimensions[col_letter].width = max(max_len + 4, 12)


# 5.Conclusion Message :
# - 5.1.Goodbye and File Stats :
def conclusion_message():
    print('=== Goodbye, file ready, check now! ===')

# 6.Execute Code :
if __name__ == "__main__" :
    introduction_message()
    file = user_path()
    number, power = parameters()
    style = styling()
    df = construction(number, power)
    save(file, df, style)
    conclusion_message()