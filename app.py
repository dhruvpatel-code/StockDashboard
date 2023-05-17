from layout import get_layout
from server import app, cache

app.layout = get_layout()

# Import callbacks after defining app.layout, no need to call anything
import callbacks 

if __name__ == '__main__':
    app.run_server(debug=True)






