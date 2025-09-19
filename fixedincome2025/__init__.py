import pandas as pd
from IPython.display import HTML

def table(filename):
    df = pd.read_csv(f'tables/{filename}.csv')
    
    # Convert to HTML and wrap in a div with centered styling
    html = f"""
    <div style="display: flex; justify-content: center;">
        {df.to_html(index=False)}
    </div>
    """
    return HTML(html)