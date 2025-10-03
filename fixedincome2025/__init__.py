import pandas as pd
from IPython.display import HTML

def table(filename):
    df = pd.read_csv(f'tables/{filename}.csv', index_col=0)

    return df

# def table(filename):    
#     ### Dilemma: If convert to HTML and wrap in a div with centered styling, 
#     ### the table is centered on slides, but will not show in pdf. 

#     df = pd.read_csv(f'tables/{filename}.csv')
#     html = f"""
#     <div style="display: flex; justify-content: center;">
#         {df.to_html(index=False)}
#     </div>
#     """
#     return HTML(html)

